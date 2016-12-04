#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the hitori models.  

'''
Construct and return hitori CSP models.
'''

from cspbase import *
import itertools

def kakuro_csp_model(initial_kakuro_board):
	'''Return a CSP object representing a kakuro CSP problem along 
	   with an array of variables for the problem. That is return

	   kakuro_csp, variable_array

	   where kakuro_csp is a csp representing kakuro 
	   and variable_array is a list of lists

	   [ [  ]
		 [  ]
		 .
		 .
		 .
		 [  ] ]

	   such that variable_array[i][j] is the Variable (object) that
	   you built to represent the value to be placed in cell i,j of
	   the kakuro board (indexed from (0,0) to (n,n))

	   The input board is specified as a list of n lists. Each of the
	   n lists represents a row of the board. Each item in the list 
	   represents a cell where:
	   		0 is a black cell,
	   		(x, y) where x is the vertical sum/clue and y is the horizontal sum/clue
	   		None is an empty cell
	   E.g., the board
	
	   -------------------  
	   | 0 | 0 |7\ |6\ |
	   | 0 |4\4|   |   |
	   | \7|   |   |   |
	   | \6|   |   |   |
	   -------------------
	   would be represented by the list of lists
	   
	   [[0,0,(7,0),(6,0)],
	    [0,(4,4),None,None],
	    [(0,7),None,None,None],
	    [(0,6),None,None,None]]

	   An entry is defined by a continuous line of 'white' cells, horizontal or 
	   vertical. 
	'''

	return 0

### Helper Functions ###
def init_variables(board):
	all_vars = []

	return all_vars

def sat_tuples(domain):
	'''
	Return a list of all satisfying tuples given a domain for Kakuro.
	* Each entry must not have duplicate numbers
	* The sum of each entry matches the clue for the entry
	'''
	return []

def verify_satified_constraints(solution):
	'''
	Return True if the solution list satifies all constraints for Kakuro
	'''
	return False

