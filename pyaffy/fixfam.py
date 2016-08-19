#!/usr/bin/env python
import sys
import pandas as pd
import numpy as np

columns = [
    'trash',
    'participant_id',
    'notused',
    'alsonotused',
    'gender',
    'alsotrash',
   ]

filename = sys.argv[1]

t_geno = pd.read_csv(filename, header=0, names=columns, index_col=False, delim_whitespace=True)
t_geno["participant_id"] = t_geno["participant_id"].map( lambda x: x[0:16] )

t_geno.to_csv(filename, sep=' ', header=False, index=False)

