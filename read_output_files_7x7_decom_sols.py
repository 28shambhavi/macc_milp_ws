import numpy as np
import os
import glob

directory = "/media/storage/shambhavi/decom_10x10_6"

# iterate over files in
# that directory
name = []
T = []
makespan = []
solve_time = []
total_solve_time = []
obj = []
agents = np.zeros(10) #10 timesteps
num_agents = []
for filename in glob.glob('/media/storage/shambhavi/decom_10x10_6/random*.sol'):
    agents = np.zeros(10)
    print(filename)
    #if filename.endswith("random*txt"):
    name.append(filename)
    print(filename)
    f = os.path.join(directory, filename)
    with open(f) as f1:
        lines = f1.readlines()
    
    # for idx,l in enumerate(lines):
        
    #     if l.startswith("Ri["):
    #         #print(idx,l)
    #         agents[int(l[3])]+=1 
    #         #appends robots at each tiemstep
    # print(max(agents))
    # num_agents.append(max(agents))
    if len(lines)>0:
        obj.append(lines[1][20:22])
        makespan.append(lines[-2][3:5])
    else:
        makespan.append(0)
        obj.append(0)

print("Read all files")

import csv
# open the file in the write mode
f = open('macc_outputs/sol_files_6structs.csv', 'w')
header = ['Name', 'Makespan', 'Cost']

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for i in range(len(name)):
    # mylist = [name[i],T[i],solve_time[i],obj[i]]
    writer.writerow([name[i],makespan[i], obj[i]])
        # {'Name' : name[i],
                     # 'T': T[i],
                     # 'Solve_time': solve_time[i],
                     # 'Cost': obj[i]})
# close the file
f.close()