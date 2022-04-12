#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1GB


text_file = open("Output.txt", "w")
text_file.write("Hello World")
text_file.close()
