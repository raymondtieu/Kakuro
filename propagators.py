'''
This file will contain different constraint propagators to be used within
bt_search.

propagator == a function with the following template
    propagator(csp, newly_instantiated_variable=None)
        ==> returns (True/False, [(Variable, Value), (Variable, Value) ...])

Consider implementing propagators for forward cehcking or GAC as a course project!        

'''

from collections import deque

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []

    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''
    Do forward checking propogation. Algorithm is modeled after FCCheck(C, x)
    from class slide deck "CSP-Lecture.pdf" page 42.
    '''
    if not newVar:
        return True, []

    pruned = []

    for c in csp.get_cons_with_var(newVar):
        if not c.has_support(newVar, newVar.get_assigned_value()):
            return False, pruned

        # check all neighbours of newVar for consistency
        for v in c.get_scope():
            if v != newVar:
                # check all assignments of the neighbour v for consistency
                for x in v.cur_domain():
                    # prune all inconsistent values of v
                    if not c.has_support(v, x) and (v, x) not in pruned:
                        v.prune_value(x)
                        pruned.append((v, x))

            # if pruning inconsistent values results in a DWO, backtrack
            if (v.cur_domain_size() == 0):
                return False, pruned

    return True, pruned

def prop_GAC(csp, newVar=None):
    '''
    Do GAC propagation. Algorithm is modeled after GAC_Enforce from class 
    slide deck "CSP-Lecture.pdf" page 84.
    '''
    gac_queue = deque()
    pruned = []

    if not newVar:
        gac_queue.extend(csp.get_all_cons())
    else:
        gac_queue.extend(csp.get_cons_with_var(newVar))

    while len(gac_queue) > 0:
        c = gac_queue.popleft()

        for v in c.get_unasgn_vars():
            for d in v.cur_domain():
                
                # find all supporting values for the assignment of newVar
                if not c.has_support(v, d):
                    v.prune_value(d)
                    pruned.append((v, d))

                    # if pruning values results in a DWO, return
                    if v.cur_domain_size() == 0:
                        gac_queue.clear()
                        return False, pruned

                    # push all new constraints into queue
                    new_cons = [con for con in csp.get_cons_with_var(v) if con not in gac_queue]
                    gac_queue.extend(new_cons)

    return True, pruned
