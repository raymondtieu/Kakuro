import sys
from cspbase import *
from propagators import *
import itertools
import traceback

##############
##MODEL TEST CASES (KAKURO)

##Checking that variables are initialized with correct domains in csp model.
def model_import(stu_models):
    return 0



##Checks that code is able to encode proper constraints over some problem.
def test_full_run(model, stu_orderings, name=""):
    score = 0
    try:
        # 4x4
        board = [[0,0,(7,0),(6,0)],
                 [0,(4,4),None,None],
                 [(0,7),None,None,None],
                 [(0,6),None,None,None]
                ]
        
        board = [[0,(17,0),(12,0),(10,0)],
                 [(0,23),None,None,None],
                 [(0,9),None,None,None],
                 [(0,7),None,None,None]
                ]
        
        board = [[0,0,(7,0),(6,0)],
                 [0,(4,4),None,None],
                 [(0,7),None,None,None],
                 [(0,6),None,None,None]
                ]

        # 2x2
        board = [[0,(14,0),(13,0)],
                 [(0,17), None, None],
                 [(0,10),None,None]]
        
        # 3x3
        board = [[0,(14,0),(9,0)],
                 [(0,16),None,None],
                 [(0,7),None,None]
                ]
        
        # 5x5
        board = [[0,(17,0),(7,0),0,0],
                 [(0,9),None,None,(24,0),0],
                 [(0,18),None,None,None,(16,0)],
                 [0,(0,21),None,None,None],
                 [0,0,(0,16),None,None]
                ]
        
        board = [[0,0,0,(7,0),(24,0)],
                 [0,(7,0),(23,10),None,None],
                 [(0,16),None,None,None,None],
                 [(0,23),None,None,None,None],
                 [(0,12),None,None,0,0]
                ]
        
        
        # 6x5
        board = [[0, 0, (23,0), (21,0), 0],
                 [0, (15,8), None, None, 0],
                 [0, None, None, None, 0],
                 [(0,27), None, None, None, None],
                 [(0,5), None, None, 0, 0],
                 [(0,14), None, None, 0, 0]
                ]

        # no solution
        board = [[0,0,(7,0),(6,0)],
                 [0,(4,4),None,None],
                 [(0,7),None,None,None],
                 [(0,10),None,None,None]]

        # 9x8
        board = [[0, 0, (22,0), (15,0), 0, 0, 0, 0],
                 [0, (3,7), None, None, (5,0), 0, 0, 0],
                 [(0,18), None, None, None, None, (13,0), 0, 0],
                 [(0,5), None, None, (11,10), None, None, (21, 0), 0],
                 [0, (0,3), None, None, (0,6), None, None, 0],
                 [0, (0,16), None, None, (14,5), None, None, (4,0)],
                 [0, 0, (0,11), None, None, (16,9), None, None],
                 [0, 0, 0, (0,20), None, None, None, None],
                 [0, 0, 0, 0, (0,14), None, None, 0]]
        
        board = [[0,(11,0),(5,0),0,0,(19,0),(14,0),0],
                 [(0,8),None,None,(8,0),(0,11),None,None,0],
                 [(0,10),None,None,None,(20,9),None,None,0],
                 [0,0,(0,12),None,None,None,0,0],
                 [0,0,0,(18,13),None,None,0,0],
                 [0,0,(0,11),None,None,(5,0),0,0],
                 [0,0,(17,18),None,None,None,(4,0),(11,0)],
                 [0,(0,13),None,None,(0,13),None,None,None],
                 [0,(0,9),None,None,0,(0,5),None,None]
                ]
        
        board = [[0,0,0,(13,0),(8,0),0,0,0],
                 [0,0,(0,16),None,None,(20,0),0,0],
                 [0,(5,0),(12,10),None,None,None,(22,0),0],
                 [(0,4),None,None,0,(11,17),None,None,0],
                 [(0,7),None,None,(18,15),None,None,None,(16,0)],
                 [0,(0,15),None,None,None,(0,17),None,None],
                 [0,(0,13),None,None,(13,0),(3,10),None,None],
                 [0,0,(0,7),None,None,None,0,0],
                 [0,0,0,(0,10),None,None,0,0]
                ]
        
        # 13x13
        board = [[0,0,0,(3,0),(10,0),0,(6,0),(16,0),(15,0),0,(16,0),(15,0),0],
                 [0,0,(0,4),None,None,(0,14),None,None,None,(3,8),None,None,0],
                 [0,0,(0,3),None,None,(3,26),None,None,None,None,None,None,(17,0)],
                 [0,(17,0),(4,0),(0,9),None,None,None,(30,6),None,None,(0,11),None,None],
                 [(0,10),None,None,(11,3),None,None,(0,8),None,None,0,(10,13),None,None],
                 [(0,12),None,None,None,(16,0),0,(29,11),None,None,(17,7),None,None,0],
                 [0,0,(0,11),None,None,(0,15),None,None,(0,11),None,None,0,0],
                 [0,0,(34,10),None,None,(34,14),None,None,(0,9),None,None,(4,0),(3,0)],
                 [0,(17,11),None,None,(0,17),None,None,0,(16,0),(11,8),None,None,None],
                 [(0,13),None,None,0,(3,11),None,None,(23,8),None,None,(0,3),None,None],
                 [(0,17),None,None,(17,8),None,None,(3,22),None,None,None,(17,0),0,0],
                 [0,(0,31),None,None,None,None,None,None,(0,12),None,None,0,0],
                 [0,(0,17),None,None,(0,17),None,None,None,(0,10),None,None,0,0]
                ]
        
        board = [[0,(4,0),(23,0),0,0,(17,0),(3,0),0,0,0,0,0,0],
                 [(0,12),None,None,(4,0),(28,9),None,None,0,0,0,0,0,0],
                 [(0,29),None,None,None,None,None,None,0,0,0,0,0,0],
                 [0,(0,9),None,None,None,(16,0),0,0,0,0,(16,0),(29,0),(7,0)],
                 [0,0,0,(3,8),None,None,(6,0),0,(17,0),(42,21),None,None,None],
                 [0,0,(30,17),None,None,None,None,(24,29),None,None,None,None,None],
                 [0,(24,16),None,None,None,(17,27),None,None,None,None,(4,8),None,None],
                 [(0,16),None,None,(3,23),None,None,None,None,(4,12),None,None,None,0],
                 [(0,25),None,None,None,None,None,(0,18),None,None,None,None,0,0],
                 [(0,19),None,None,None,0,0,0,(0,10),None,None,(3,0),(24,0),None],
                 [0,0,0,0,0,0,0,(4,0),(17,18),None,None,None,(16,0)],
                 [0,0,0,0,0,0,(0,34),None,None,None,None,None,None],
                 [0,0,0,0,0,0,(0,9),None,None,0,(0,16),None,None]
                ]

        # 15x30 
        # board = [[0, (4,0), (11,0), 0, (3,0), (24, 0), 0, 0, 0, (16,0), (23, 0), (7,0), 0, 0, (24,0), (3,0), 0, (11, 0), (4, 0), (16, 0), 0, (29, 0), (3, 0), 0, 0, 0, 0, (10,0), (23,0), 0],
        #          [(0,3), None, None, (24,10), None, None, 0, (35, 0), (17,19), None, None, None, 0, (0,10), None, None, (3,12), None, None, None, (0,11), None, None, 0, 0, (6,0), (30,16), None, None, 0],
        #          [(0,23), None, None, None, None, None, (3, 31), None, None, None, None, None, 0, (10,26), None, None, None, None, None, None, (40, 6), None, None, 0, (19,22), None, None, None, None, 0],
        #          [0, (0,13), None, None, (0,26), None, None, None, None, (0,11), None, None, (17,10), None, None, (0, 5), None, None, (16,0), (0,13), None, None, 0, (0,24), None, None, None, None, None, 0],
        #          [0, (0,10), None, None, 0, (0,9), None, None, (16,0), 0, (38,0), (3,11), None, None, 0, 0, (0,10), None, None, (16,11), None, None, 0, (6,17), None, None, None, (4,0), 0, 0],
        #          [0, 0, 0, 0, 0, 0, (4,12), None, None, (23,15), None, None, None, None, (16,0), (29,0), 0, (0,17), None, None, None, 0, (16,3), None, None, (8,7), None, None, (3,0), (4,0)],
        #          [0, 0, 0, 0, (4,0), (23,35), None, None, None, None, None, None, (0,15), None, None, None, 0, 0, (0,9), None, None, (23,15), None, None, None, None, (3,6), None, None, None],
        #          [0, (17,0), (16,0), (0,13), None, None, None, (23,0), (4,10), None, None, 0, 0, (0,16),None, None, (17,0), 0, 0, (0,21), None, None, None, None, (17,3), None, None, (0,4), None, None],
        #          [(0,16), None, None, (3,7),None, None, (13,25), None, None, None, None, (3,0), 0, 0, (0,15), None, None, (10,0), 0, (4,17), None, None, (3,0), (16,12), None, None, None, 0, 0, 0],
        #          [(0,19),None, None, None, (11,17), None, None, None, None, (0,4), None, None, (17,0), None, (0,18), None, None, None, (17,32), None, None, None, None, None, None, 0, 0, 0, 0, 0],
        #          [0, 0, (0,4), None, None, (24,11), None, None, 0, (29,17), None, None, None, (10,0), 0, 0, (0,20), None, None, None, None, (0,3), None, None, (3,0), 0, 0, (23,0), (11,0), 0],
        #          [0, 0, (6,0), (23,16), None, None, None, 0, (0,16), None, None, (0,10), None, None, (16,0), 0, (24,12), None, None, (6,0), (24,0), 0, (17,8), None, None, (24,0), (0,13), None, None, 0],
        #          [0, (0,26), None, None, None, None, None, 0, (4,9), None, None, (16,0), (3,10), None, None, (4,13),None, None, (0,9), None, None, (4,21), None, None, None, None, (3,8), None, None, (17,0)],
        #          [0, (0,19), None, None, None, None, 0, (0,12), None, None, (0,30), None, None, None, None, None, None, 0, (0,21), None, None, None, None, None, (0,27), None, None, None, None, None],
        #          [0, (0,8), None, None, 0, 0, 0, (0,9), None, None, (0,14), None, None, None, (0,8), None, None, 0, (0,14), None, None, None, 0, 0, (0, 10), None, None, (0,12), None, None]
        #         ]

        csp,var_array = model(board)
        solver = BT(csp)
        solver.bt_search(prop_BT, stu_orderings.ord_mrv, stu_orderings.val_arbitrary)

        print("===== FC ====")
        solver.bt_search(prop_FC, stu_orderings.ord_mrv, stu_orderings.val_arbitrary)


        if check_solution(var_array):
            score = 5
            details = ""
        else:
            details = "Solution found in full run with MRV heuristic on %s was not a valid Hitori solution." % name

    except Exception:

        details = "One or more runtime errors occurred while trying a full run on %s: %r" % (name, traceback.format_exc())

    if score < 5:
        try:
            board = [[2, 2, 2, 4, 2],
                     [5, 1, 4, 2, 3],
                     [5, 4, 2, 3, 5],
                     [4, 1, 1, 1, 2],
                     [2, 3, 5, 1, 2]]


            csp,var_array = model(board)
            solver = BT(csp)
            solver.bt_search(prop_BT, stu_orderings.ord_dh, stu_orderings.val_arbitrary)

            if check_solution(var_array):
                score = 5
                details = ""
            else:
                details = "Solution found in full run with DH heuristic on %s was not a valid Hitori solution." % name
        except Exception:
            details = "One or more runtime errors occurred while trying a full run on %s: %r" % (name, traceback.format_exc())

    if score < 5:
        try:
            board = [[2, 2, 2, 4, 2],
                     [5, 1, 4, 2, 3],
                     [5, 4, 2, 3, 5],
                     [4, 1, 1, 1, 2],
                     [2, 3, 5, 1, 2]]

            csp,var_array = model(board)
            solver = BT(csp)
            solver.bt_search(prop_BT, stu_orderings.ord_random, stu_orderings.val_lcv)

            if check_solution(var_array):
                score = 5
                details = ""
            else:
                details = "Solution found in full run with LCV heuristic on %s was not a valid Hitori solution." % name
        except Exception:
            details = "One or more runtime errors occurred while trying a full run on %s: %r" % (name, traceback.format_exc())

    return score,details

def test_ord_dh(model, stu_orderings):

        score = 0
        details = ""

        board = [[2, 2, 2, 4, 2],
                [5, 1, 4, 2, 3],
                [5, 4, 2, 3, 5],
                [4, 1, 1, 1, 2],
                [2, 3, 5, 1, 2]]

        assigned = [[0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0]]    


        try:
            csp,var_array = model(board)

            count = 0
            for i in range(0,len(board)):
                for j in range(0,len(board[0])):
                    if (assigned[i][j]):
                        csp.vars[count].assign(board[i][j])
                    count += 1

            var = stu_orderings.ord_dh(csp)

            if((var.name) == csp.vars[4].name):
                return 1, ""

            return 0, "Failed to locate the variable with the highest degree."

        except Exception:
            details = "One or more runtime errors occurred while trying to test ord_dh."

        return 0, details


def test_ord_mrv(model, stu_orderings):
    board = [[0,0,0],[0,0,0],[0,0,0]]
    score = 0
    details = ""

    try:
        csp,var_array = model(board)

        count = 0
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                csp.vars[count].add_domain_values(range(0, count))
                count += 1

        var = stu_orderings.ord_mrv(csp)

        if((var.name) == csp.vars[0].name):
            return 1, ""

    except Exception:
        details = "One or more runtime errors occurred while trying to test ord_mrv"

    return 0, details


########################################
## Other helpers that may be of use
#Checks whether a solution given by BT is correct.
def check_solution(hitori_variable_array):
    for i in range(len(hitori_variable_array)):
        row_sol = []
        blacks = [False] * len(hitori_variable_array)
        for j in range(len(hitori_variable_array)):
            if hitori_variable_array[i][j].get_assigned_value() != 0:
                row_sol.append(hitori_variable_array[i][j].get_assigned_value())
                blacks[j] = False
            else:
                if blacks[j - 1] or blacks[j]:
                    print("1")
                    return False
                else:
                    blacks[j] = True
        if not check_list(row_sol):
            print("2")
            return False

    for i in range(len(hitori_variable_array)):
        row_sol = []
        blacks = [False] * len(hitori_variable_array)
        for j in range(len(hitori_variable_array)):
            if hitori_variable_array[j][i].get_assigned_value() != 0:
                row_sol.append(hitori_variable_array[j][i].get_assigned_value())
                blacks[j] = False
            else:
                if blacks[j - 1] or blacks[j]:
                    print("3")
                    return False
                else:
                    blacks[j] = True
        if not check_list(row_sol):
            print("4")
            return False

    return True

##Helper function that checks if a given list is valid
def check_list(solution_list):
    return len(solution_list) == len(set(solution_list))

##RUN TEST CASES 
def main(stu_propagators=None, stu_models=None):
    import orderings as stu_orderings
    import kakuro_csp as stu_models

    score, details = test_full_run(stu_models.kakuro_csp_model, stu_orderings)
    
if __name__=="__main__":
    main()
