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
	vars = init_variables(initial_kakuro_board)
	cons = []

	# Add row constraints
	for i in range(len(initial_kakuro_board)):
		scope = get_entries(vars[i], True)
		for entry in scope:
			print(entry['part'])
			if entry['part']:
				con = Constraint('row-{}'.format(i), entry['part'])
				domain = [var.cur_domain() for var in entry['part']]
				con.add_satisfying_tuples(sat_tuples(domain, entry['clue']))
				cons.append(con)
	print(cons)

	return 0

### Helper Functions ###
def init_variables(board):
	all_vars = []

	for i in range(len(board)):
		row_vars = []
		for j in range(len(board)):
			# add new Variable to row, with name Ki,j
			if board[i][j] == 0:
				row_vars.append(Variable('K{},{}'.format(i,j), [0]))
			elif isinstance(board[i][j], tuple):
				row_vars.append(Variable('K{},{}'.format(i,j), [board[i][j]]))
			elif board[i][j] == None:
				row_vars.append(Variable('K{},{}'.format(i,j), [1,2,3,4,5,6,7,8,9]))
			
		all_vars.append(row_vars)

	return all_vars

def get_entries(lst, is_row):
	all_entries = []
	part = []
	entry = {}

	for i in lst:
		e = i.cur_domain()[0] # first domain value

		if isinstance(e, tuple):
			# new partition
			if 'clue' in entry:
				part = []

			entry = {'clue': e[1] if is_row else e[0], 'part': part}
			all_entries.append(entry)
		elif e != 0:
			# add onto existing partition
			part.append(i)

	return all_entries

def get_entries_board(board):
	# convert rows to domains
	for row in board:
		print(get_entries(row, True))

	# Columns
	columns = []
	for i in range(len(board)):
		columns.append([row[i] for row in board])

	for column in columns:
		print(get_entries(column, False))

	return 0 

def sat_tuples(domain, clue):
	'''
	Return a list of all satisfying tuples given a domain for a Kakuro entry.
	* Each entry must not have duplicate numbers
	* The sum of all entries matches the clue for the entry
	'''
	return [solution for solution in itertools.product(*domain) if verify_satified_constraints(solution, clue)]

def verify_satified_constraints(solution, clue):
	'''
	Return True if the solution list satifies all constraints for Kakuro
	'''
	entries = [x for x in solution if not isinstance(x, tuple)]
	return sum(entries) == clue


if __name__ == '__main__':
	board = [[0,0,(7,0),(6,0)],
	    [0,(4,4),None,None],
	    [(0,7),None,None,None],
	    [(0,6),None,None,None]]

	row = [[0],[(4,4)],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
#	row = [[0],[(4,4)],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[(0,15)],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[0],[(0,9)],[1,2,3,4,5,6,7]]
	# [[Var-K0,0, Var-K0,1, Var-K0,2, Var-K0,3], [Var-K1,0, Var-K1,1, Var-K1,2, Var-K1,3], [Var-K2,0, Var-K2,1, Var-K2,2, Var-K2,3], [Var-K3,0, Var-K3,1, Var-K3,2, Var-K3,3]]
	#print(sat_tuples(row, 4))
	#print(get_entries(row, True))

	test = init_variables(board)

	#print(test)
	#print(test[1][2].cur_domain())

	get_entries_board(test)
	print('----------')
	kakuro_csp_model(board)
