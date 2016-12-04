#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the hitori models.  

'''
Construct and return hitori CSP models.
'''

from cspbase import *
import itertools

def hitori_csp_model_1(initial_hitori_board):
	'''Return a CSP object representing a hitori CSP problem along 
	   with an array of variables for the problem. That is return

	   hitori_csp, variable_array

	   where hitori_csp is a csp representing hitori using model_1
	   and variable_array is a list of lists

	   [ [  ]
		 [  ]
		 .
		 .
		 .
		 [  ] ]

	   such that variable_array[i][j] is the Variable (object) that
	   you built to represent the value to be placed in cell i,j of
	   the hitori board (indexed from (0,0) to (8,8))

	   
	   
	   The input board is specified as a list of n lists. Each of the
	   n lists represents a row of the board. Each item in the list 
	   represents a cell, and will contain a number between 1--n.
	   E.g., the board
	
	   -------------------  
	   |1|3|4|1|
	   |3|1|2|4|
	   |2|4|2|3|
	   |1|2|3|2|
	   -------------------
	   would be represented by the list of lists
	   
	   [[1,3,4,1],
	   [3,1,2,4],
	   [2,4,2,3],
	   [1,2,3,2]]
	   
	   This routine returns Model_1 which consists of a variable for
	   each cell of the board, with domain equal to {0,i}, with i being
	   the initial value of the cell in the board. 
	   
	   Model_1 also contains BINARY CONSTRAINTS OF NOT-EQUAL between
	   all relevant variables (e.g., all pairs of variables in the
	   same row, etc.)
	   
	   All of the constraints of Model_1 MUST BE binary constraints 
	   (i.e., constraints whose scope includes exactly two variables).
	'''

##IMPLEMENT
	vars = init_variables(initial_hitori_board)
	cons = []

	# Add row constraints
	for i in range(len(initial_hitori_board)):
		for j in range(len(initial_hitori_board)):
			# current variable in row
			current = vars[i][j]

			# go across row and add constraints
			for k in range(j + 1, len(initial_hitori_board)):
				next = vars[i][k]

				con = Constraint('row-({}),({})'.format(current.name, next.name), [current, next])

				sat_tuples = []
				if (k == j + 1):
					sat_tuples = sat_tuples_model_1_adjacent(current.cur_domain(), next.cur_domain())
				else:
					sat_tuples = sat_tuples_model_1(current.cur_domain(), next.cur_domain())
				
				con.add_satisfying_tuples(sat_tuples)
				cons.append(con)		

	# Add column constraints
	for j in range(len(initial_hitori_board)):
		for i in range(len(initial_hitori_board)):
			# current variable in column
			current = vars[i][j]

			# go down column and add constraints
			for k in range(i + 1, len(initial_hitori_board)):
				next = vars[k][j]

				con = Constraint('col-({}),({})'.format(current.name, next.name), [current, next])

				sat_tuples = []
				if (k == i + 1):
					sat_tuples = sat_tuples_model_1_adjacent(current.cur_domain(), next.cur_domain())
				else:
					sat_tuples = sat_tuples_model_1(current.cur_domain(), next.cur_domain())
				
				con.add_satisfying_tuples(sat_tuples)
				cons.append(con)

	csp = CSP('hitori_csp_model_1', vars=list(itertools.chain.from_iterable(vars)))
	for c in cons:
		csp.add_constraint(c)
	return csp, vars


##############################

def hitori_csp_model_2(initial_hitori_board):
	'''Return a CSP object representing a hitori CSP problem along 
	   with an array of variables for the problem. That is return

	   hitori_csp, variable_array

	   where hitori_csp is a csp representing hitori using model_1
	   and variable_array is a list of lists

	   [ [  ]
		 [  ]
		 .
		 .
		 .
		 [  ] ]

	   such that variable_array[i][j] is the Variable (object) that
	   you built to represent the value to be placed in cell i,j of
	   the hitori board (indexed from (0,0) to (8,8))

	   
	   
	   The input board is specified as a list of n lists. Each of the
	   n lists represents a row of the board. Each item in the list 
	   represents a cell, and will contain a number between 1--n.
	   E.g., the board
	
	   -------------------  
	   |1|3|4|1|
	   |3|1|2|4|
	   |2|4|2|3|
	   |1|2|3|2|
	   -------------------
	   would be represented by the list of lists
	   
	   [[1,3,4,1],
	   [3,1,2,4],
	   [2,4,2,3],
	   [1,2,3,2]]

	   The input board takes the same input format (a list of n lists 
	   specifying the board as hitori_csp_model_1).
   
	   The variables of model_2 are the same as for model_1: a variable
	   for each cell of the board, with domain equal to {0,i}, where i is
	   the initial value of the cell.

	   However, model_2 has different constraints.  In particular, instead
	   of binary not-equals constraints, model_2 has 2n n-ary constraints
	   that resemble a modified all-different constraint.  Each constraint
	   is over n variables.  For any given row (resp. column), that 
	   constraint will incorporate both the adjacent black squares and 
	   no repeated numbers rules.
	   
	'''

###IMPLEMENT
	vars = init_variables(initial_hitori_board)
	cons = []

	# Add row constraints
	for i in range(len(initial_hitori_board)):
		scope = vars[i]
		con = Constraint('row-{}'.format(i), scope)
		domain = [var.cur_domain() for var in scope]
		con.add_satisfying_tuples(sat_tuples_model_2(domain))
		cons.append(con)

	# Add column constraints
	for j in range(len(initial_hitori_board)):
		# Get the column at j
		scope = [vars[i][j] for i in range(len(vars))]
		con = Constraint('col-{}'.format(i), scope)
		domain = [var.cur_domain() for var in scope]
		con.add_satisfying_tuples(sat_tuples_model_2(domain))
		cons.append(con)

	csp = CSP('hitori_csp_model_2', vars=list(itertools.chain.from_iterable(vars)))
	for c in cons:
		csp.add_constraint(c)
	return csp, vars
	

### Helper Functions ###
def init_variables(board):
	all_vars = []

	for i in range(len(board)):
		row_vars = []
		for j in range(len(board)):
			# add new Variable to row, with name Hi,j
			row_vars.append(Variable('H{},{}'.format(i,j), [0, board[i][j]]))
		all_vars.append(row_vars)

	return all_vars


def sat_tuples_model_1(dom1, dom2):
	'''
	Return a list of all satisfying tuples given two domains in the case that 
	the 2 variables are in the same row/column but not next to each other.
	Specifically, it is satisfiable if two variables in the same row/column
	are not the same, or they are black squares, denoted by 0
	'''
	return list(t for t in itertools.product(dom1, dom2) if (t[0] != t[1] or t[0] == 0 or t[1] == 0))


def sat_tuples_model_1_adjacent(dom1, dom2):
	'''
	Return a list of all satisfying tuples given two domains in the case that 
	the 2 variables are next to each other.
	Specifically, it is satisfiable if two variables next to each other are 
	not the same.
	'''
	return list(t for t in itertools.product(dom1, dom2) if t[0] != t[1])


def sat_tuples_model_2(domain):
	'''
	Return a list of all satisfying tuples given a domain for Hitori.
	* Each row must not have duplicate numbers
	* Each column must not have duplicate numbers
	* Black squares cannot be adjacent
	'''
	return [solution for solution in itertools.product(*domain) if verify_satified_constraints(solution)]

def verify_satified_constraints(solution):
	'''
	Return True if the solution list satifies all constraints for Hitori
	'''
	# if there are no black squares, there should be no duplicate values
	if 0 not in solution:
		if len(solution) == len(set(solution)):
			return True
	else:
		# check for adjacent black squares
		for i in range(len(solution) - 1):
			if solution[i] == 0 and solution[i + 1] == 0:
				return False

		# check for any duplicate values ignoring black squares
		# all constraints are satisfied if there are no duplicates
		solution_no_black = list(filter(lambda v: v != 0, solution))
		return len(solution_no_black) == len(set(solution_no_black))

