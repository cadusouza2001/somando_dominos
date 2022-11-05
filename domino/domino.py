import itertools


minhaentrada = [
    [272,46] , [16,66] , [302,803] , [824,880] , [767,995] , [53,808] , [462,268] , [63,441] , [546,852] , [94,847] ,
    [806,496] , [57,486] , [47,436] , [636,732] , [222,582] , [428,270] , [810,558] , [347,225] , [294,202] , [401,786] ,
    [880,55] , [657,390] , [120,333] , [201,772] , [744,788] , [655,457] , [680,640] , [339,447] , [846,23] , [663,717] ,
    [172,713] , [220,237] , [944,750] , [969,401] , [338,663] , [559,457] , [147,434]
]

def sum_side(set_, side):
    return sum([i[side] for i in set_])

def turn(domino):
    return [domino[1] , domino[0]]

def generate_keys(n):
    half = int((2**n)/2)
    return list(itertools.product([0, 1], repeat=n))[:half]

def arrange(set_, key):
    arranged = []
    set_order = [(set_[i],key[i]) for i in range(len(set_))]
    for i,j in set_order:
        if j == 1:
            arranged += [turn(i)]
        else:
            arranged += [i]
    return arranged

def equal_sums(set_):
    sum_up = sum_side(set_, 0)
    sum_dn = sum_side(set_, 1)
    if sum_up == sum_dn:
        return True
    else:
        return False

def remove(set_, index):
    new_set = [i for i in set_]
    new_set.pop(index)
    return new_set

def find_arrangement(set_):
    for key in generate_keys(len(set_)):
        arrangement = arrange(set_, key)
        if equal_sums(arrangement):
            return (sum_side(arrangement, 0) , None)
    return None

def find_with_removal(set_):
    biggest_sum = -1
    removed = None
    for i in range(len(set_)):
        arrangement = find_arrangement(remove(set_, i))
        if arrangement != None :
            actual_sum = arrangement[0]
            if actual_sum > biggest_sum:
                biggest_sum = arrangement[0]
                removed = [set_[i][0] , set_[i][1]]
    return (biggest_sum, removed)

def run(set_):
    result = find_arrangement(set_)
    if result != None:
        print("%d nenhuma peça deletada" %(result[0]))
    else:
        result = find_with_removal(set_)
        if result[0] == -1:
            print("Impossível")
        else:
            print("%d com remoção da peça %d|%d" %(result[0], result[1][0], result[1][1]))

run(minhaentrada)