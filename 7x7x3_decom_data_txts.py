import numpy as np
import os
import glob

directory = "/media/storage/shambhavi/final_experiments/macc_decom_test_7x7/output files/txt"

# iterate over files in
# that directory
structure = []
substructure =[]
T = []
obj = []
solve_time = []
total_solve_time = []
agents = np.zeros(10) #10 timesteps
num_agents = []
const_s =0

for filename in glob.glob('/media/storage/shambhavi/final_experiments/macc_decom_test_7x7/output files/txt/random*.txt'):
    agents = np.zeros(10)
    file_name_only, ext = os.path.splitext(os.path.basename(filename))
    ext, s1, subs1 = file_name_only.split("_")
    structure.append(s1)
    substructure.append(subs1)

    f = filename
    with open(f) as f1:
        lines = f1.readlines()
    for idx,l in enumerate(lines):
        if l.startswith("Ri["):
            #print(idx,l)
            agents[int(l[3])]+=1 
            #appends robots at each tiemstep
    num_agents.append(max(agents))
    obj.append(lines[-3][5:])
    T.append(lines[-4].split(",")[0][3:])
    solve_time.append(lines[-2][12:])
    total_solve_time.append(lines[-1][17:])
    const_s = structure

print("Read all files")

import csv
# open the file in the write mode
f = open('output_decom_data_7x7_computee.csv', 'w')

# create the csv writer
writer = csv.writer(f)
writer.writerow(['Name', 'Substructure','T', 'Solve_time', 'Total_Solve_Time','Cost', 'Num_agents'])
# write a row to the csv file
for i in range(len(T)):
    # mylist = [name[i],T[i],solve_time[i],obj[i]]
    writer.writerow([structure[i],substructure[i],T[i],solve_time[i], total_solve_time[i], obj[i], num_agents[i]])
        # {'Name' : name[i],
                     # 'T': T[i],
                     # 'Solve_time': solve_time[i],
                     # 'Cost': obj[i]})
# close the file
f.close()