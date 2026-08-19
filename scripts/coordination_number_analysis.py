import numpy as np
import os
from ase.neighborlist import NeighborList
from ase.io import read
import matplotlib.pyplot as plt

tantala = read('44.xyz')
lattice = np.array([  # Example lattice parameters, replace with your specific values
    [12.77754, 0.0, 0.0],  # a, b, c vectors
    [0.0, 14.724618, 0.0],
    [0.0, 0.0, 19.21647]
])
tantala.set_cell(lattice, scale_atoms=False)
tantala.set_pbc(True)

cutoff = 2.36
nl = NeighborList([cutoff/2]*len(tantala),skin=0,self_interaction=False,bothways=True)
nl.update(tantala)

coordination_number=[]
species=[]

for i in range(len(tantala)):
    indices, offsets = nl.get_neighbors(i)
    coordination_number.append(len(indices))
    species.append(tantala.symbols[i])

data=[species,coordination_number]
#print(tantala.positions[i] + offset @ tantala.get_cell())
#nl.get_neighbors(2)

Ta=[]
O=[]

for i in range(len(data[0])):
    if data[0][i]=='Ta':
        Ta.append(data[1][i])
    elif data[0][i]=='O':
        O.append(data[1][i])

for i in range(0,10):
    print(i)
    print('---------------')
    #print(100*Ta.count(i)/len(Ta))
    print(100*O.count(i)/len(O))
    print()
    print()
    
plt.figure()
plt.title('Second Biggest Density')
for i in range(2,9):
    plt.bar(i,100*Ta.count(i)/len(Ta),width=0.6,color='b',label="Ta")
    plt.bar(i,100*O.count(i)/len(O),width=0.6,color='r',label="O")
plt.xlabel('Coordination Number')
plt.ylabel('% of Ta/O atoms')
plt.xticks(np.linspace(1,9,9))
plt.yticks(np.linspace(0,70,15))
plt.show()
