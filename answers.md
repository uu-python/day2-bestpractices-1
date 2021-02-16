# Answers

## Profiling

(a)

* operation `result[i][j] += X[i][k] * Y[k][j]` takes the most time to execute
* operation `result[i][j] += X[i][k] * Y[k][j]` also takes the most memory

(b)

* the `while` loop inside factorize takes the most time. Also the evaluation of `p > sqrt(n)` takes time.
* the function `factors` uses the most memory, since it is appending `n` to `factors` over several loops

(c)
Using the `line_profiler` package I get the following results:

* the original file takes: 24.4072 s
* the modified file take: Total time: 5.61298 s
