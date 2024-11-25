import random
import math
from copy import deepcopy

def generate_encoding(dim):
    encoding = []
    rows_added = []
    for _ in range(dim):
        row = random.randint(0, dim-1)
        while row in rows_added:
            row = random.randint(0, dim-1)
        encoding.append(row)
        rows_added.append(row)
    return encoding

def tweak(encoding):
    dim = len(encoding)
    new_encoding = deepcopy(encoding)
    column1 = random.randint(0,dim-1)
    column2 = random.randint(0,dim-1)
    while column2 == column1:
        column2 = random.randint(0,dim-1)
    new_encoding[column1],new_encoding[column2] = new_encoding[column2],new_encoding[column1]
    return new_encoding

def energy(encoding):
    dim = len(encoding)
    energy = 0
    for i in range(dim):
        for j in range(i+1,dim):
            if(abs(encoding[i]-encoding[j]) == abs(i-j)):
                energy += 1
    return energy

def print_chessboard(encoding):
    dim = len(encoding)
    chessboard = [['⬜️' if (i+j)%2==0 else '⬛️' for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        chessboard[i][encoding[i]] = '👑'
        print(" ".join(chessboard[i]))

def simulated_annealing(dim=8):
    current = generate_encoding(dim)
    current_energy = energy(current)
    best_energy = current_energy
    T = 20
    t = 0
    step_max = 100
    goal_test = lambda x: x==0
    while T>0.1:
        for _ in range(step_max):
            print(f"{t}){T}, {current}, Energia:{current_energy}")
            t +=1
            next = tweak(current)
            d_ev = current_energy - energy(next)
            if(d_ev>0):
                current = next
                current_energy = energy(next)
                if(current_energy<best_energy):
                    best_energy = current_energy
                    if(goal_test(best_energy)):
                        print("Soluzione trovata:")
                        print_chessboard(current)
                        return
            else:
                metropolis = math.exp(d_ev/T)
                test = random.random()
                if(test<metropolis):
                    current = next
                    current_energy = energy(current)
        T *= 0.9

simulated_annealing(20)