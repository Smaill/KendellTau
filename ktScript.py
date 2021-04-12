#!/usr/bin/env python3

## This version to work for linearly ordered sets of size 3 to 5
##
## to use:
## in linux or windows(?)  call with one argument, the solution:
##        eg: (size 5) ABECD; (size 3)  BCA   
##
##  (linux)  ./ktScript.py ABECD
##  (windows) py /path/to/ktFlexScript.py  ACEDB

import sys
import argparse
import numpy as np
from itertools import permutations
from tabulate import tabulate
from string import ascii_uppercase
from math import factorial
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument("soln",help="Give solution in form of permutation,\n\
  either of ABC, ABCD or ABCDE")
parser.add_argument("-q",help="Indicate question number Q",type=int,default=-1)
parser.add_argument("-d",help="Give mark to one decimal place;\n\
  by default return nearest half integer"
                        ,action='store_true')
args = parser.parse_args()

## turn strings into lists for next step,

if args.q == -1:
   question = ""
else:
   question = "Question " + str(args.q) + "  "


def score(str1, str2):
    n = len(str1)
    assert len(str2) == n, "strings have to be of equal length"
    i, j = np.meshgrid(np.arange(n), np.arange(n))
    a = np.argsort(list(str1))
    b = np.argsort(list(str2))
    ordered = np.logical_or(np.logical_and(a[i] < a[j], b[i] < b[j]),
                            np.logical_and(a[i] > a[j], b[i] > b[j])).sum()
    return ordered  / ( n - 1 )

def list_to_string ( intlist ):
    mlist = map( str, intlist )
    strlist = list( mlist )
    res = ''.join( strlist )
    return  res

## find nearest half-integer
def nearest( flt ):
    return( 0.5 * ( round (2 * flt) ))

def massage( flt, decimal ):
    if not decimal:
        return( nearest( flt ) )
##  in other case use one decimal place        
    if decimal:
        return( round( flt, 1 ) )
    
def mk_mark_info ( soln, decimal ):
    lst_soln = list( soln )
    l = len( lst_soln )
    poss = list(permutations(ascii_uppercase[0:l]))
    mrks = [ ( list_to_string( lst )+ ": "
                + str( massage( score( lst, soln ), decimal )))
            for lst in poss ]
    return mrks

## put into array;  use tabulate to get helpful dictionary-style format.
##  sneaky code here uses Fortran column major convention
##  decimal parameter to control approximations in case of length 4:
##  default gives nearest half integer,
##  with -d option round to 1 decimal place.

def mk_array( soln, decimal ):
    l = len( soln )
    arr = np.array(mk_mark_info( soln, decimal ))
    arr2d = arr.reshape( factorial( l - 1 ), l, order='F' )
    return tabulate( arr2d ) 
    ##    print( tabulate( arr2d, tablefmt = "latex" ))

def check_proposed_soln( soln ):
    size = len( soln )
##  print( "size is {}".format(size) )  ## for debugging
##      now input sanity checks:
    if size < 3 or size > 5:
        print( "solution must be of length 3, 4, or 5" )
        exit()
    if sorted(soln) != sorted( ascii_uppercase[0:size] ):
        print( "bad solution, must be permutation of ABC or ABCD or ABCDE" )
        exit()

def main ():
    soln = args.soln
    check_proposed_soln( soln )
    table = mk_array( soln, args.d )
    print( question + "Solution: " + soln ) 
    sys.stdout.write( table )
    sys.stdout.write( "\n" )

if __name__ == "__main__":
    main()


