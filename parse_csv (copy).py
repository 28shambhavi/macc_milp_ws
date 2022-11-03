import struct
import pandas
import numpy as np
import csv
import os

df = pandas.read_csv('makespan_obj.csv')
print(df)
# ['Name', 'Substructure','T', 'Solve_time', 'Total_Solve_Time','Cost', 'Num_agents']
Name = df['Structure']
substructure = df['Substructure']
T = df['Makespan']
obj = df['Obj']
# solve_time = df['Solve_time']
# total_solve_time = df['Total_Solve_Time']
num_agents = df['No_of_agents']
# print(T)
# print("T[0]: ", T[0])
structure = np.zeros(100)
makespan = np.zeros(100)
sum_of_costs = np.zeros(100)
max_agents = np.zeros(100)
# computation_time = np.zeros(100)
# total_computation_time = np.zeros(100)
l = 0


# create the csv writer


# write a row to the csv file

    
for n_idx,n in enumerate(Name):
	print(n_idx, n, "printing n and n idx")
	if isinstance(n, float):
		break
	# idx = int(n.split("_")[1])
	# print(n_idx, n)
	structure[n] = n
	makespan[n] += T[n_idx]
	sum_of_costs[n] += obj[n_idx]
	max_agents[n] = max(num_agents[n_idx], max_agents[n])
	# computation_time[n] += solve_time[n_idx]
	# total_computation_time[n] += total_solve_time[n_idx]
	
print("Read all files")
f = open('makespan_obj_cumulative.csv', 'w')
header = ['Name', 'Substructure','T', 'Cost', 'No_of_agents']
writer = csv.writer(f)
for i in range(len(makespan)):
    # mylist = [name[i],T[i],solve_time[i],obj[i]]
    writer.writerow([structure[i],makespan[i],sum_of_costs[i], max_agents[i]])

f.close()



