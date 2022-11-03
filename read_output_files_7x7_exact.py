import numpy as np
import os
import glob

directory = "/home/biorobotics/exact_6r_7x7/"

# iterate over files in
# that directory
name = []
T = []
obj = []
solve_time = []
total_solve_time = []

for filename in glob.glob('/home/biorobotics/exact_6r_7x7/random*.txt'):
    name.append(filename)
    print(filename)
    f = os.path.join(directory, filename)
    with open(f) as f1:
        lines = f1.readlines()
        print(lines)
    # for idx,l in enumerate(lines):
        
    #     if l.startswith("Ri["):
    #         #print(idx,l)
    #         agents[int(l[3])]+=1 
    #         #appends robots at each tiemstep
    # print(max(agents))
        obj.append(lines[0][5:])
        solve_time.append(lines[1][12:])
        total_solve_time.append(lines[2][17:])

print("Read all files")

import csv
# open the file in the write mode
f = open('output_exact_7x7_data.csv', 'w')
header = ['Name', 'Solve_time', 'Total Solve Time','Cost']

# create the csv writer
writer = csv.writer(f)

# write a row to the csv fyile
for i in range(99):
    # mylist = [name[i],T[i],solve_time[i],obj[i]]
    writer.writerow([name[i],solve_time[i], total_solve_time[i], obj[i]])
        # {'Name' : name[i],
                     # 'T': T[i],
                     # 'Solve_time': solve_time[i],
                     # 'Cost': obj[i]})
# close the file
f.close() 