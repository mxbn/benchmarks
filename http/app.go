package main

import (
    "io"
	"net/http"
)

func handle(rw http.ResponseWriter, rq *http.Request) {
    io.WriteString(rw, "hello from go  \nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
	return
}

func main() {
    http.HandleFunc("/", handle)
    http.ListenAndServe(":8080", nil)
}
