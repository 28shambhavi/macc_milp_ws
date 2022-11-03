import pandas
import numpy as np

df = pandas.read_csv('/home/biorobotics/python_ws_macc/10x10x3_decom_data.csv')

s_idx = df['Structure']
sub_idx = df['Substructure']
T = df['Makespan']
obj = df['Obj']
total_solve = df['Total_Solve']
final_solve = df['Final_Solve']
Agents = df['Num']
obj = df['Obj']

print(s_idx[1], type(s_idx[1]))

makespan = np.zeros(85)
sum_of_costs = np.zeros(85)
computation_time = np.zeros(85)
last_computation_time = np.zeros(85)
max_agents = np.zeros(85)


for i in range(1,857):
	print(i)
	makespan[int(s_idx[i])]+=T[i]
	sum_of_costs[int(s_idx[i])]+=obj[i]
	computation_time[int(s_idx[i])]+=total_solve[i]
	last_computation_time[int(s_idx[i])]+=final_solve[i]
	max_agents[int(s_idx[i])]=max(max_agents[int(s_idx[i])], Agents[i])

# for n_idx,n in enumerate(Name):
# 	if isinstance(n, float):
# 		break
# 	idx = int(n.split("_")[1])
# 	print(idx)
# 	makespan[idx] += T[n_idx]
# 	sum_of_costs[idx] += obj[n_idx]
# 	computation_time[idx] += solve_time[n_idx]

print("Average makespan: ", sum(makespan)/84)
print("Average sum_of_costs: ", sum(sum_of_costs)/84)
print("Average computation_time: ", sum(computation_time)/84)
print("Average last_computation_time: ", sum(last_computation_time)/84)



