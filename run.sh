#!/bin/bash

rm -Rf ./build
mkdir build
mkdir build/bin

nsamples=100000
fname="./build/results.log"
port=8080
declare -a apps=("./build/bin/app-cpp" "./build/bin/app-go" "java -jar build/libs/httpbenchmark-1.0.0.jar" "./target/release/app-rust")
declare -a nthreads=(2 4 8 16 32 64 128 256 512)

[ ! -d "./crow" ] && git clone https://github.com/ipkn/crow

echo "building c++"
g++ app.cpp -o build/bin/app-cpp -I./crow/include -pthread -lboost_system -O3
echo "building go"
go build -o build/bin/app-go app.go
echo "building java"
gradle -q --console=plain build
echo "building rust"
cargo build --release -q

echo "" > $fname

for app in "${apps[@]}";
do
    echo "testing $app"
    ${app} 2>/dev/null &
    APP_PID=$!
    curl -s http://localhost:$port/ > /dev/null
    for nt in ${nthreads[@]};
    do
        sleep 1
        echo $'\t' $nt
        echo "results for $app called in $nt threads:\n\n" >> $fname
        ab -n $nsamples -c $nt -q http://localhost:$port/ >> $fname
        echo $'\n\n--------------------------------------------------------------------------------\n\n' >> $fname
    done
    kill -s 9 $APP_PID
    wait $! 2>/dev/null
done

echo "plotting results"
python3 plot.py
echo $'\tdone.'
