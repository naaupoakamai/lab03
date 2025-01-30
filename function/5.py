from itertools import permutations

def print_permutations(a):
    perm_list=[' '.join(p) for p in permutations(a)]
    for perm in perm_list:
        print(perm)

user=input()
print_permutations(user)