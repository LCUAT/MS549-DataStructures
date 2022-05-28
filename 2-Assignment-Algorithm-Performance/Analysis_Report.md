# Algorithm Analysis

- What computational resources does your algorithm/code use?

        The primary resources needed for this program are memory and cpu. 

- What computational resources impact the performance of your algorithm?

        This algorthim does not have good performance for higher numbers. Any number between 0 and 30 iterations of fibonachi the time and resources are negligable, anything above 30 the resources and time become exponenitally more expensive.

- In what cases, situations, or scenarios would your algorithms performance be enhanced or diminished?

        Any number 30 or less was when the algorithm was running effectively. 

- Show the lines or sections of code that would be affected and explain why.

        Lines 1-12 are affected if the number is adjusted because the number of iterations needed for the program to compute changes. 

- Determine and report the Big O of your algorithm. You may want to report the Big O for the best case, worst case, and average case.

        BigO value: O(2^n)
        Best Case: 1.600012183189392e-05s
        Worst Case: 104.42853229981847s

- Profiler - Use a profiler to analyze your code. Describe what you learned about the execution, resources, and efficiency of your code.

        The lower the iterations the less process time because of exponential nature of the algorithm and the number of iterations. 

- Runtime analysis (adding timers around sections of your code) - Conduct a runtime analysis of your code and report the results.

        The results are contained the the RunResults_#.md files. The program ran in a reasonable time for less than 30 iterations, anything above that took an exponentially long time. 
