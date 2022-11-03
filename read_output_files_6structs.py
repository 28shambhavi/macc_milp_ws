import numpy as np
import os
import glob

directory = "/home/biorobotics/decom_10x10_6"

# iterate over files in
# that directory
name = []
T = []
obj = []
solve_time = []
total_solve_time = []
agents = np.zeros(15) #25 timesteps
num_agents = []
for filename in glob.glob('/home/biorobotics/decom_10x10_6/random*.txt'):
    agents = np.zeros(15)
    print(filename)
    #if filename.endswith("random*txt"):
    name.append(filename)
    print(filename)
    f = os.path.join(directory, filename)
    with open(f) as f1:
        lines = f1.readlines()
    for idx,l in enumerate(lines):
        
        if l.startswith("Ri["):
            #print(idx,l)
            timestep = l.split(",")[0][3:]
            agents[int(timestep)]+=1
            #appends robots at each tiemstep
    print(max(agents))
    num_agents.append(max(agents))
    obj.append(lines[-3][5:])
    T.append(lines[-4].split(",")[0][3:])
    solve_time.append(lines[-2][12:])
    total_solve_time.append(lines[-1][17:])

print("Read all files")

import csv
# open the file in the write mode
f = open('output_decom_data_10x10.csv', 'w')
header = ['Name', 'T', 'Solve_time', 'Total Solve Time','Cost','No. of agents']

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for i in range(len(T)):
    # mylist = [name[i],T[i],solve_time[i],obj[i]]
    writer.writerow([name[i],T[i],solve_time[i], total_solve_time[i], obj[i], num_agents[i]])
        # {'Name' : name[i],
                     # 'T': T[i],
                     # 'Solve_time': solve_time[i],
                     # 'Cost': obj[i]})
# close the file
f.close()