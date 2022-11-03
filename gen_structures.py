import numpy as np
import random
import pdb

from tupledict_ea_d import run_EA_d
from basins_of_attraction_2 import get_decompositions
from final_order import gen_order

random.seed(101)

structures = []
num_struct = 25

for i in range(num_struct*2):
	z_bar = np.zeros((10,10))
	for j in np.arange(2,8):
		for k in np.arange(2,8):
			z_bar[j][k] = random.randint(0,3)
	structures.append(z_bar)
	
for i in range(num_struct):
	z_bar = np.zeros((10,10))
	for j in np.arange(2,8):
		for k in np.arange(2,8):
			if random.randint(5,7)>5:
				z_bar[j][k] = random.randint(0,3)
	structures.append(z_bar)

for i in range(num_struct):
	z_bar = np.zeros((10,10))
	for j in np.arange(2,8):
		for k in np.arange(2,8):
			if random.randint(0,10)>0:
 				z_bar[j][k] = random.randint(1,3)
	#if i==24:
	structures.append(z_bar)
	 	

np.save("random_structures.npy",structures)

# f = open("random_structures.txt", "a")
# for s in structures:
# 	f.write(str(s))
# 	f.write("\n\n")
# f.close()
print(structures)
pdb.set_trace()



struct_decomp = get_decompositions(structures)
print(struct_decomp)
pdb.set_trace()

final_decomp=[]

for i,decomp in enumerate(struct_decomp):
    final_decomp.append(gen_order(structures[i], decomp))

print(struct_decomp)
print("Got decompositions!")


run_EA_d(final_decomp)


