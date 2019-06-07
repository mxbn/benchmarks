import numpy as np
import regex as re
import matplotlib.pyplot as plt

nthreads = np.array([2,4,8,16,32,64,128,256,512])
n = len(nthreads)

time_mean_finder = re.compile(r'Time per request:\s+([0-9\.]+)\s+\[ms\]\s\(mean\)')
time_throughput_finder = re.compile(r'Time per request:\s+([0-9\.]+)\s+\[ms\]\s\(mean, across all concurrent requests\)')

times_mean = []
times_throughput = []

with open('./build/results.log', 'rt') as f:
    for l in f.readlines():
        m = time_mean_finder.match(l)
        if m is not None:
            times_mean.append(float(m.groups()[0]))
        m = time_throughput_finder.match(l)
        if m is not None:
            times_throughput.append(float(m.groups()[0]))

plt.figure(figsize=(8,6))

plt.subplot(211)
plt.title('mean response time for each call')
plt.plot(nthreads, times_mean[0:n], c='b', label='cpp')
plt.plot(nthreads, times_mean[n:2*n], c='g', label='go')
plt.plot(nthreads, times_mean[2*n:3*n], c='r', label='java')
plt.plot(nthreads, times_mean[3*n:4*n], c='m', label='rust')
plt.ylabel('ms per call')
plt.legend()

plt.subplot(212)
plt.title('mean throughput across all calls')
plt.plot(nthreads, times_throughput[0:n], c='b', label='cpp')
plt.plot(nthreads, times_throughput[n:2*n], c='g', label='go')
plt.plot(nthreads, times_throughput[2*n:3*n], c='r', label='java')
plt.plot(nthreads, times_throughput[3*n:4*n], c='m', label='rust')
plt.xlabel('n threads')
plt.ylabel('ms per call')
plt.legend()

plt.subplots_adjust(hspace=0.3)
plt.savefig('benchmark.png')
