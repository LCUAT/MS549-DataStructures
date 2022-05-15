# Asignment 1: Test Driven Developement

## Description: 
    This project shows a basic implementation of the test driven developement through the timiing of the pogram and it's functions as well as monitoring the cpu usage for the duration of the program.

## Results:
    Initial Runs:

    Best time: 0.006495199864730239s

    Best CPU usage: 25

    Best Pop time: 7.00121745467186e-07s
    
    Best Peek time: 1.8998980522155762e-06s

    Best Push time: 1.2800097465515137e-05s

    ================================================================
    Removed extra print statements

    Best time: 0.009197300067171454s

    Best CPU usage: 25
    
    Best pop time: 4.998873919248581e-07s

    Best Peek time: 4.699919372797012e-06s

    Best Push time: 7.899943739175797e-06s

## Resutls Analysis
    - Moving to a class slowed everything down, but keeping the variables global got the best results. 
    - Having less print statements, and less custom print statements also made a significant difference. 
    - CPU usage for this program was almost negligable reguardless.
    - There needs to be compromise between effeciency and functionalitly. Classes being a prime example of this. Classes are good for code re-use, yet from a speed perspective in this particular program (not all programs) they did not work well from an efficincy standpoint.
    - When all the print statements were changed the program still worked but it was nice to have the colors. And less print statemest is more efficient, but it was also harder to understand the results.      




