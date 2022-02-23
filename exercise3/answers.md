a. Investigate the performance of the matmult.py script
In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory?

ANS: Running the code for N=250 with line_profiler I find that most part of the time (over 97%) is spent inside the loop of line 22, mostly in **line 27**. That would be the best place to start optmizing for **speed**. With memory_profiler I find that the main sources of memory increment are the import at line 2, the very repeated **line 27** and the print statements at **line 30**. Since the import statement does not scale with matrix size that is not of big concern. The print statements should scale with matrix size, but if they are a requirement for the program not much could be done in that direction. The statement at **line 27**, on the other hand, could probably be refined, specially considered it is called so many times.

b. Investigate the performance of the euler72.py script
In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory? (This is one problem from the euler project: https://projecteuler.net/problem=72)

ANS: The gen_primes function is called only once and it executes rather quickly (4ms), so it is not a priority for speed optimization. The fast_phi function is called many times but in each call it spends most of the time (85%) waiting for the factorize function to return. That tells us that the factorize method is the one we should prioritize. Inside this method we see that its time is distributed mostly among three lines: **line 25**, **line 26** and **line 29**. Those lines would probably be the best place to start optimizing for speed. One improvement that I can already see is that the **sqrt(n) call in line 29** is unecessary and relatively costly: it could be improved by evaluating the square root outside the main loop, between lines 24 and 25, for example and storing the value. This would substitute the repeated calculation of a square root at line 29 for the repeated call of a value.
    As for memory I have found that **line 17** seems to be the one that creates most memory in the gen_primes method, while **line 26** is the one in the factorize method that creates the most memory.


c. Improve the performance of the matmult.py script
What is the best performance that you achieved with N=250?

ANS: Although I knew the line the nedded most improvement was line 27, I didn't really know how to improve it. I found this (https://stackoverflow.com/a/61583971/10172674) solution and tried to implement it. I saw a significant increase in perfornamce, with the run time going from 3.954 s to 2.716 s. This solution was used the python native sum() method. I then decided to see to try a solution closer to the original program, with only the only changes being the sum method instead of the most internal loop and the evaluation of the length of Y outside all loops. To my suprise this method performed the best, **with a runtime of 2.294 seconds**.

By suppressing the print statements at the end I got an even better result: **2.271 seconds**.