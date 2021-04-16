# KendellTau
Correlation tables for ordered lists of length 3, 4 or 5

Basic usage:  call with a "solution" permutation of ABC, ABCD, or ABCDE.
Returns  table indicating Kendall Tau correlation for each possible
permutation with the given solution.

with  -q Q   for Q positive integer, marks out put as "Question Q"
with  -d     returns values to 1 decimal place; 
              default is to return nearest half integer.
             This only makes a difference for lists of length 4.
