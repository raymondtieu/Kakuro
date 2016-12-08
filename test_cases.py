import sys
from cspbase import *
from propagators import *
import itertools
import traceback

import orderings
from kakuro_csp import *

##############
##MODEL TEST CASES (KAKURO)

FC = "FC"
GAC = "FAC"
MRV = "MRV"
DH = "DH"
ARB = "ARB"
LCV = "LCV"

def test_5x5_boards(model, var_orderings=[MRV, DH], val_orderings=[ARB, LCV]):
    print("--------------------")
    print("Testing 5x5 board #1")
    print("--------------------")

    board = [[0,0,0,(23,0),(16,0)],
             [0,0,(24,16),None,None],
             [0,(4,24),None,None,None],
             [(0,17),None,None,None,0],
             [(0,10),None,None,0,0]]

    use_mode(model, var_orderings, val_orderings, board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

    print("--------------------")
    print("Testing 5x5 board #2")
    print("--------------------")

    board = [[0,0,(10,0),(30,0),0],
             [0,(16,10),None,None,(4,0)],
             [(0,16),None,None,None,None],
             [(0,21),None,None,None,None],
             [0,(0,13),None,None,0]]

    # DH hangs
    use_mode(model, [MRV], val_orderings, board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)


def test_9x8_boards(model, var_orderings=[MRV], val_orderings=[ARB, LCV]):
    
    print("--------------------")
    print("Testing 9x8 board #1")
    print("--------------------")

    board = [[0,0,0,(13,0),(6,0),0,(24,0),(17,0)],
             [0,0,(0,6),None,None,(13,9),None,None],
             [0,0,(23,26),None,None,None,None,None],
             [0,(14,4),None,None,(0,14),None,None,(15,0)],
             [(0,10),None,None,0,0,(0,10),None,None],
             [(0,11),None,None,(4,0),0,(13,17),None,None],
             [0,(17,9),None,None,(7,8),None,None,0],
             [(0,18),None,None,None,None,None,0,0],
             [(0,12),None,None,(0,12),None,None,0,0]]

    # LCV takes too long
    use_mode(model, var_orderings, [ARB], board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

    print("--------------------")
    print("Testing 9x8 board #2")
    print("--------------------")
    
    board = [[0,0,0,0,(4,0),(25,0),0,0],
             [0,0,(5,0),(14,7),None,None,(9,0),(11,0)],
             [0,(0,25),None,None,None,None,None,None],
             [0,(0,13),None,None,(4,19),None,None,None],
             [0,0,0,(23,5),None,None,0,0],
             [0,(13,0),(5,11),None,None,(10,0),(17,0),0],
             [(0,15),None,None,None,(17,17),None,None,0],
             [(0,28),None,None,None,None,None,None,0],
             [0,0,(0,17),None,None,0,0,0]]

    use_mode(model, var_orderings, [ARB], board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

    print("--------------------")
    print("Testing 9x8 board #3")
    print("--------------------")
    
    board = [[0, 0, (22,0), (15,0), 0, 0, 0, 0],
              [0, (3,7), None, None, (5,0), 0, 0, 0],
              [(0,18), None, None, None, None, (13,0), 0, 0],
              [(0,5), None, None, (11,10), None, None, (21, 0), 0],
              [0, (0,3), None, None, (0,6), None, None, 0],
              [0, (0,16), None, None, (14,5), None, None, (4,0)],
              [0, 0, (0,11), None, None, (16,9), None, None],
              [0, 0, 0, (0,20), None, None, None, None],
              [0, 0, 0, 0, (0,14), None, None, 0]
            ]

    use_mode(model, var_orderings, [ARB], board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

def test_13x13_boards(model, var_orderings=[MRV], val_orderings=[ARB]):
    
    print("----------------------")
    print("Testing 13x13 board #1")
    print("----------------------")

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

    # use_mode(model, orderings, board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

    print("----------------------")
    print("Testing 13x13 board #2")
    print("----------------------")
    
    board = [[0,(4,0),(23,0),0,0,(17,0),(3,0),0,0,0,0,0,0],
                [(0,12),None,None,(4,0),(28,9),None,None,0,0,0,0,0,0],
                [(0,29),None,None,None,None,None,None,0,0,0,0,0,0],
                [0,(0,9),None,None,None,(16,0),0,0,0,0,(16,0),(29,0),(7,0)],
                [0,0,0,(3,8),None,None,(6,0),0,(17,0),(42,21),None,None,None],
                [0,0,(30,17),None,None,None,None,(24,29),None,None,None,None,None],
                [0,(24,16),None,None,None,(17,27),None,None,None,None,(4,8),None,None],
                [(0,16),None,None,(3,23),None,None,None,None,(4,12),None,None,None,0],
                [(0,25),None,None,None,None,None,(0,18),None,None,None,None,0,0],
                [(0,19),None,None,None,0,0,0,(0,10),None,None,(3,0),(24,0),0],
                [0,0,0,0,0,0,0,(4,0),(17,18),None,None,None,(16,0)],
                [0,0,0,0,0,0,(0,34),None,None,None,None,None,None],
                [0,0,0,0,0,0,(0,9),None,None,0,(0,16),None,None]
            ]

    # use_mode(model, orderings, board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

def test_15x15_boards(model, var_orderings=[MRV], val_orderings=[ARB]):
    
    print("----------------------")
    print("Testing 15x15 board #1")
    print("----------------------")

    board = [[0,(3,0),(7,0),0,0,0,0,0,0,0,(4,0),(17,0),0,0,0],
             [(0,6),None,None,0,(13,0),(4,0),0,0,0,(23,12),None,None,(3,0),0,0],
             [(0,3),None,None,(11,4),None,None,0,0,(3,17),None,None,None,None,(28,0),0],
             [0,(0,14),None,None,None,None,0,(4,9),None,None,0,(0,8),None,None,(23,0)],
             [0,0,(0,3),None,None,(7,0),(19,12),None,None,None,(3,0),(16,0),(0,15),None,None],
             [0,(16,0),(29,17),None,None,None,None,None,(23,0),(25,10),None,None,(0,11),None,None],
             [(0,10),None,None,(3,0),(0,3),None,None,(7,20),None,None,None,None,(16,9),None,None],
             [(0,14),None,None,None,(0,26),None,None,None,None,None,(24,0),(0,9),None,None,(16,0)],
             [0,(6,3),None,None,(17,0),(4,28),None,None,None,None,None,(0,19),None,None,None],
             [(0,11),None,None,(0,21),None,None,None,None,(3,11),None,None,(29,0),(24,13),None,None,],
             [(0,5),None,None,(0,10),None,None,(7,0),(16,27),None,None,None,None,None,0,0],
             [(0,8),None,None,(16,0),0,(0,13),None,None,None,0,(4,17),None,None,(24,0),0],
             [0,(0,10),None,None,(16,0),(3,11),None,None,0,(0,23),None,None,None,None,(4,0)],
             [0,0,(0,19),None,None,None,None,0,0,(0,10),None,None,(0,8),None,None],
             [0,0,0,(0,10),None,None,0,0,0,0,0,0,(0,11),None,None]
            ]

    # use_mode(model, orderings, board, BT, name="")
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

    print("----------------------")
    print("Testing 15x15 board #2")
    print("----------------------")

    board = [[0,0,(39,0),(10,0),0,0,0,0,0,(16,0),(3,0),0,(22,0),(30,0),0],
             [0,(0,9),None,None,0,0,(17,0),(4,0),(0,11),None,None,(17,13),None,None,0],
             [0,(0,10),None,None,0,(0,10),None,None,(4,29),None,None,None,None,None,0],
             [0,(17,12),None,None,0,(0,12),None,None,None,(7,0),(17,19),None,None,None,0],
             [(0,13),None,None,None,0,0,0,(0,13),None,None,None,(11,8),None,None,0],
             [(0,15),None,None,(16,0),0,0,(17,0),(30,0),(10,23),None,None,None,None,(4,0),(17,0)],
             [0,(0,16),None,None,(29,0),(4,21),None,None,None,None,(3,14),None,None,None,None],
             [0,(4,0),(16,33),None,None,None,None,None,None,(16,3),None,None,(16,10),None,None],
             [(0,8),None,None,(21,11),None,None,(7,30),None,None,None,None,None,None,(22,0),0],
             [(0,23),None,None,None,None,(4,20),None,None,None,None,0,(0,8),None,None,(4,0)],
             [0,0,(11,17),None,None,None,None,(16,0),0,0,0,0,(10,7),None,None],
             [0,(0,5),None,None,(16,13),None,None,None,(4,0),(3,0),0,(0,12),None,None,None],
             [0,(0,12),None,None,None,(17,0),(3,10),None,None,None,0,(0,5),None,None,0],
             [0,(0,24),None,None,None,None,None,(0,4),None,None,0,(0,7),None,None,0],
             [0,(0,11),None,None,(0,9),None,None,0,0,0,0,(0,4),None,None,0]
            ]

    # use_mode(model, orderings, board, BT, name="")
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)

def test_15x30_board(model, var_orderings=[MRV], val_orderings=[ARB]):

    print("---------------------")
    print("Testing 15x30 board #1")
    print("---------------------")

    # 15x30 
    board = [[0, (4,0), (11,0), 0, (3,0), (24, 0), 0, 0, 0, (16,0), (23, 0), (7,0), 0, 0, (24,0), (3,0), 0, (11, 0), (4, 0), (16, 0), 0, (29, 0), (3, 0), 0, 0, 0, 0, (10,0), (23,0), 0],
             [(0,3), None, None, (24,10), None, None, 0, (35, 0), (17,19), None, None, None, 0, (0,10), None, None, (3,12), None, None, None, (0,11), None, None, 0, 0, (6,0), (30,16), None, None, 0],
             [(0,23), None, None, None, None, None, (3, 31), None, None, None, None, None, 0, (10,26), None, None, None, None, None, None, (40, 6), None, None, 0, (19,22), None, None, None, None, 0],
             [0, (0,13), None, None, (0,26), None, None, None, None, (0,11), None, None, (17,10), None, None, (0, 5), None, None, (16,0), (0,13), None, None, 0, (0,24), None, None, None, None, None, 0],
             [0, (0,10), None, None, 0, (0,9), None, None, (16,0), 0, (38,0), (3,11), None, None, 0, 0, (0,10), None, None, (16,11), None, None, 0, (6,17), None, None, None, (4,0), 0, 0],
             [0, 0, 0, 0, 0, 0, (4,12), None, None, (23,15), None, None, None, None, (16,0), (29,0), 0, (0,17), None, None, None, 0, (16,3), None, None, (8,7), None, None, (3,0), (4,0)],
             [0, 0, 0, 0, (4,0), (23,35), None, None, None, None, None, None, (0,15), None, None, None, 0, 0, (0,9), None, None, (23,15), None, None, None, None, (3,6), None, None, None],
             [0, (17,0), (16,0), (0,13), None, None, None, (23,0), (4,10), None, None, 0, 0, (0,16),None, None, (17,0), 0, 0, (0,21), None, None, None, None, (17,3), None, None, (0,4), None, None],
             [(0,16), None, None, (3,7),None, None, (13,25), None, None, None, None, (3,0), 0, 0, (0,15), None, None, (10,0), 0, (4,17), None, None, (3,0), (16,12), None, None, None, 0, 0, 0],
             [(0,19),None, None, None, (11,17), None, None, None, None, (0,4), None, None, (17,0), 0, (0,18), None, None, None, (17,32), None, None, None, None, None, None, 0, 0, 0, 0, 0],
             [0, 0, (0,4), None, None, (24,11), None, None, 0, (29,17), None, None, None, (10,0), 0, 0, (0,20), None, None, None, None, (0,3), None, None, (3,0), 0, 0, (23,0), (11,0), 0],
             [0, 0, (6,0), (23,16), None, None, None, 0, (0,16), None, None, (0,10), None, None, (16,0), 0, (24,12), None, None, (6,0), (24,0), 0, (17,8), None, None, (24,0), (0,13), None, None, 0],
             [0, (0,26), None, None, None, None, None, 0, (4,9), None, None, (16,0), (3,10), None, None, (4,13),None, None, (0,9), None, None, (4,21), None, None, None, None, (3,8), None, None, (17,0)],
             [0, (0,19), None, None, None, None, 0, (0,12), None, None, (0,30), None, None, None, None, None, None, 0, (0,21), None, None, None, None, None, (0,27), None, None, None, None, None],
             [0, (0,8), None, None, 0, 0, 0, (0,9), None, None, (0,14), None, None, None, (0,8), None, None, 0, (0,14), None, None, None, 0, 0, (0, 10), None, None, (0,12), None, None]
            ]

    # use_mode(model, orderings, board)
    use_mode(model, var_orderings, val_orderings, board, FC)
    use_mode(model, var_orderings, val_orderings, board, GAC)


def use_mode(model, var_orderings, val_orderings, board, propagator=None):
    for o in var_orderings:
        var_ordering = None

        if o == MRV:
            var_ordering = orderings.ord_mrv
        elif o == DH:
            var_ordering = orderings.ord_dh

        for v in val_orderings:
            val_ordering = None

            if v == ARB:
                val_ordering = orderings.val_arbitrary
            else:
                val_ordering = orderings.val_lcv

            try:
                csp,var_array = model(board)
                solver = BT(csp)

                if propagator is None:
                    print("--------------------------------------------")
                    print("==== Running BT with", o, "+", v, "ordering ====")
                    print("--------------------------------------------")
                    solver.bt_search(prop_BT, var_ordering, val_ordering)
                elif propagator == FC:
                    print("-----------------------------------------------------")
                    print("==== Running BT using FC with", o, "+", v, "ordering ====")
                    print("-----------------------------------------------------")
                    solver.bt_search(prop_FC, var_ordering, val_ordering)
                elif propagator == GAC:
                    print("------------------------------------------------------")
                    print("==== Running BT using GAC with", o, "+", v, "ordering ====")
                    print("------------------------------------------------------")
                    solver = BT(csp)
                    solver.bt_search(prop_GAC, var_ordering, val_ordering)

                if check_solution(board, csp.get_all_cons()):
                    print("Solution has been verified.")
                else:
                    print("This is not a valid Kakuro solution for the board.")

            except Exception:
                print("One or more runtime errors occurred while trying a full run on %s: %r" % (name, traceback.format_exc()))


def check_solution(kakuro_board, cons):
    '''
    Verify that a solution found by bt_search is a valid Kakuro solution to
    the given board.
    '''

    m = len(kakuro_board)
    n = len(kakuro_board[0])

    board = init_variables(kakuro_board, m, n)

    var_array_dict = {}

    for c in cons:
        vars = c.get_scope()
        soln = sum([v.get_assigned_value() for v in vars])
        var_array_dict[str(vars)] = soln

    # Check row solutions
    for i in range(m):
        entries = get_entries(board[i], True)
        for e in entries:
            scope = e['part']
            if len(scope) > 0:
                if str(scope) in var_array_dict:
                    if e['clue'] != var_array_dict[str(scope)]:
                        return False

    # Check column solutions
    for i in range(n):
        col = [board[j][i] for j in range(m)]
        entries = get_entries(col, False)
        for e in entries:
            scope = e['part']
            if len(scope) > 0:
                if str(scope) in var_array_dict:
                    if e['clue'] != var_array_dict[str(scope)]:
                        return False
    return True

##RUN TEST CASES     
if __name__=="__main__":
    test_5x5_boards(kakuro_csp_model)
    test_9x8_boards(kakuro_csp_model)
    # test_13x13_boards(kakuro_csp_model)
    # test_15x15_boards(kakuro_csp_model)
    # test_15x30_boards(kakuro_csp_model)
