from wfpf_checker import *

tests = {
        'p':True,
        'q':True,
        '':False,
        'pq':False,
        '$':False,
        'p^q':True,
        'p_q':True,
        '((p^q) -> (p_q))':True,
        '((p^q)_~r)':True,
        '~->q':False,
        'p->qr':False,
        '->r':False,
        '~x':True,
        '~(~(~x))':True,
        'p -> q ^ r -> s _ ~q ^ ~s':True,
        '(p -> (q ^ r)) -> (s _ (~q ^ ~s))':True
        }


for expression, result in tests.items():
    evaluated = check_helper(expression)
    try :
        assert(evaluated == result)
    except AssertionError:
        print("Test failed for ", expression, "\nExpected result : ", result, "\nEvaluated result : ", evaluated, sep = '')
        quit()

print("All tests successful!")
