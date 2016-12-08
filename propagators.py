'''
This file will contain different constraint propagators to be used within
bt_search.

propagator == a function with the following template
    propagator(csp, newly_instantiated_variable=None)
        ==> returns (True/False, [(Variable, Value), (Variable, Value) ...])

Consider implementing propagators for forward cehcking or GAC as a course project!        

'''

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
