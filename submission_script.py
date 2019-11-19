import os
import sys

steps = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

f_sum = open("README", "w")

os.mkdir("runs")
i = 0
for s in steps:
    job_str = """#!/bin/bash                                                             
#SBATCH -t 1:00:00
#SBATCH -o out.txt
cd $WORK/runs/""" + str(i)

    job_str += "\npython ../../test.py """ + str(s) + " > out"

    os.mkdir("runs/" + str(i))

    job_path = "runs/" + str(i) + "/" + str(i) + ".sh"
    f = open(job_path, "w")
    f.write(job_str)
    f.close()

    f_sum.write("sbatch " + job_path + "\n")

    i += 1

f_sum.close()