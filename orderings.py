#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

import random
import itertools

'''
This file will contain different variable ordering heuristics to be used within
bt_search.

var_ordering == a function with the following template
	ord_type(csp)
		==> returns Variable 

	csp is a CSP object---the heuristic can use this to get access to the
	variables and constraints of the problem. The assigned variables can be
	accessed via methods, the values assigned can also be accessed.

	ord_type returns the next Variable to be assigned, as per the definition
	of the heuristic it implements.

val_ordering == a function with the following template
	val_ordering(csp,var)
		==> returns [Value, Value, Value...]
	
	csp is a CSP object, var is a Variable object; the heuristic can use csp to access the constraints of the problem, and use var to access var's potential values. 

	val_ordering returns a list of all var's potential values, ordered from best value choice to worst value choice according to the heuristic.

'''


def ord_random(csp):
	'''
	ord_random(csp):
	A var_ordering function that takes a CSP object csp and returns a Variable object var at random.  var must be an unassigned variable.
	'''
	var = random.choice(csp.get_all_unasgn_vars())
	return var


def val_arbitrary(csp,var):
	'''
	val_arbitrary(csp,var):
	A val_ordering function that takes CSP object csp and Variable object var,
	and returns a value in var's current domain arbitrarily.
	'''
	return var.cur_domain()


def ord_mrv(csp):
	'''
	ord_mrv(csp):
	A var_ordering function that takes CSP object csp and returns Variable object var, 
	according to the Minimum Remaining Values (MRV) heuristic as covered in lecture.  
	MRV returns the variable with the most constrained current domain 
	(i.e., the variable with the fewest legal values).
	'''
#IMPLEMENT
	min = None
	for v in csp.get_all_unasgn_vars():
		if v.cur_domain_size() == 1:
			return v

		if not min or v.cur_domain_size() < min.cur_domain_size():
			min = v

	return min


def ord_dh(csp):
	'''
	ord_dh(csp):
	A var_ordering function that takes CSP object csp and returns Variable object var,
	according to the Degree Heuristic (DH), as covered in lecture.
	Given the constraint graph for the CSP, where each variable is a node, 
	and there exists an edge from two variable nodes v1, v2 iff there exists
	at least one constraint that includes both v1 and v2,
	DH returns the variable whose node has highest degree.
	'''    
#IMPLEMENT
	cons = csp.get_all_cons()
	degrees = {}
	for c in cons:
		unassigned_vars = c.get_unasgn_vars()
		for v in c.get_scope():
			# check if a variable is within a constraint's scope
			if unassigned_vars.count(v) > 0:
				# update degree for node v
				if v not in degrees:
					degrees[v] = 0

				degrees[v] = degrees[v] + len(unassigned_vars)

	var = max(degrees, key=degrees.get)
	return var
	
	
def val_lcv(csp,var):
	'''
	val_lcv(csp,var):
	A val_ordering function that takes CSP object csp and Variable object var,
	and returns a list of Values [val1,val2,val3,...]
	from var's current domain, ordered from best to worst, evaluated according to the 
	Least Constraining Value (LCV) heuristic.
	(In other words, the list will go from least constraining value in the 0th index, 
	to most constraining value in the $j-1$th index, if the variable has $j$ current domain values.) 
	The best value, according to LCV, is the one that rules out the fewest domain values in other 
	variables that share at least one constraint with var.
	'''    
#IMPLEMENT
	domain = var.cur_domain()
	cons = csp.get_cons_with_var(var)
	sums = {}
	
	# look at values in domain of var
	for value in domain:
		# assign value to variable
		var.assign(value)
		
		accounted_for = {}    # neighbours with values that have been ruled out

		total = 0
		# look at constraints with var
		for c in cons:

			# look at unassigned neighbours in each constraint
			for n in c.get_unasgn_vars():
				# look at the domains of each neighbour and count invalid values
				for val in n.cur_domain():
					if not c.has_support(n, val):
						# keep track of which neighbour has already been ruled out
						if n not in accounted_for:
							accounted_for[n] = [val]
						else:
							# avoid double counting
							if val not in accounted_for[n]:
								accounted_for[n].append(val)

		# count how many were ruled out
		for lst in accounted_for.values():
		 	total += len(lst)
		
		sums[value] = total
		
		var.unassign()
	
	return sorted(sums, key=sums.get)


def ord_custom(csp):
	'''
	ord_custom(csp):
	A var_ordering function that takes CSP object csp and returns Variable object var,
	according to a Heuristic of your design.  This can be a combination of the ordering heuristics 
	that you have defined above.
	'''    
#IMPLEMENT
	# run MRV and find min ties
	mins = []
	for v in csp.get_all_unasgn_vars():
		if len(mins) == 0:
			mins = [v]
		elif v.cur_domain_size() == mins[0].cur_domain_size():
			mins.append(v)
		elif v.cur_domain_size() < mins[0].cur_domain_size():
			mins = [v]

	if len(mins) == 1:
		return mins[0]
	else:
		# use DH as tiebreaker
		cons = csp.get_all_cons()
		degrees = {}

		for c in cons:
			unassigned_vars = c.get_unasgn_vars()

			# loop over minimum variables found instead of entire scope
			for v in mins:
				# check if a variable is within a constraint's scope
				if unassigned_vars.count(v) > 0:
					# update degree for node v
					if v not in degrees:
						degrees[v] = 0

					degrees[v] = degrees[v] + len(unassigned_vars)

		var = max(degrees, key=degrees.get)
		return var


