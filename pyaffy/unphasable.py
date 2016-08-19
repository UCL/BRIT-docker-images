#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np

columns = [
    'chr',
    'pos',
    'snpid',
    'refal',
    'altal',
   ]

filename = sys.argv[1]

t_geno = pd.read_csv(filename, header=0, names=columns, usecols=[0, 1, 2, 3, 4], sep = '\t', index_col=False)
p_one = t_geno[t_geno['refal'] == '-']
p_two = t_geno[t_geno['refal'] == '.']
p_three = t_geno[t_geno['refal'] == '...']
p_four = t_geno[t_geno['refal'] == ' ']
p_five = t_geno[t_geno['altal'] == '-']
p_six = t_geno[t_geno['altal'] == '.']
p_seven = t_geno[t_geno['altal'] == '...']
p_eight = t_geno[t_geno['altal'] == ' ']

frames = [p_one, p_two, p_three, p_four, p_five, p_six, p_seven, p_eight]
t_exclude = pd.concat(frames)
del t_exclude["altal"]
del t_exclude["refal"]
del t_exclude["pos"]
del t_exclude["chr"]
#t_exclude = t_exclude.drop_duplicates()

t_exclude.to_csv("/app/exclude.csv", header=False, index=False)
