# Collatz
Code By Michael Sherif Naguib
## About the Collatz Conjecture
The *Collatz Conjecture* states that given a function
```
f(n) = n/2         (if n mod 2 =0),
       3*n +1       otherwise
```
And the sequence defined by:
```
a_i = n            for i=0,
      f(a_(i-1))   otherwise
```
The conjecture states that the sequence will always return to 1 for any starting value of x_0. This could be thought of as constructing
an iterated function system for the function ```f``` and determining if it always retunrs to  1: 
```f(...f(f(f(f(f(x_0)))))...) = 1 for x_0 in Positive Integers  given a finate number of calls will the IFS yeild a 1?``` (however this is only approximatly equivilant)...
The collatz conjecture has been called the problem that both mathematics and computer science is not prepared to solve. There are many intricate patterns that can come out of counting the length of the sequence for any given value of x_0

## About the Code: ```Collatz.ipynb```
* A repo for the purpose of exploring the *Collatz Conjecture* and plotting points graphically
* The code is optimized using memoization to compute different values concerning the collatz conjecture
including: sequence length, sequence values, collatz function values, etc. The calcualtions are quite fast however it uses recursion: (an iterative calculation method will need to be coded ... if a number with a large enough seqence length is calculated right off the start and can't terminate early because there are not values for the intermediate terms ... python's activation stack might reach its maximum recursive depth)
* The code plots a few  graphs and then I begin expiramenting with whatever comes into my head ...
* *Code includes a 3D plot* of the collatz sequence length ... inverting the points with respect to how many points were compued then switching the axis yeiled a curved rectangular prisim grouping of points for sufficienctly low point quantities; This is not meant to be rigorous but to show the innate patters
that emerge in the Collatz Conjecture
* **TWO FILES** The old code is in ```Collatz.py``` the new code is in ```Collatz.ipynb```
## Dependancies 
* Anaconda
* numpy,math,random,sys,bisect,tqdm,multiprocessing
* My Plotting Library etc *NumLib* (see my github repos ... this has its own deps...)