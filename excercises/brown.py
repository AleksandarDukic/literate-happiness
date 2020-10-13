from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future


import os, fnmatch
import operator

with open('../large_files/brown/ca01', encoding='utf-8') as f:
  for line in f:
    print(line)
    print("+++++++++++")

list = fnmatch.filter(os.listdir('./large_files/brown'), 'c???') # 500
