import csv
import sys
import numpy as np

csv.field_size_limit(sys.maxsize)

paths_dict = {}
start_end_values_dict = {}
line = 0
column = 0

with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	next(spamreader, None)  # skip the headers
	for row in spamreader:
		start = row[0]
		end = row[1]
		key = start + ' ' + end
		if key not in start_end_values_dict:
			start_end_values_dict[key] = line
			line = line + 1
		path = row[2][1:-1]
		if path not in paths_dict:
			paths_dict[path] = column
			column = column + 1

# print(len(start_end_values_dict))
# print(len(paths_dict))

for key, value in start_end_values_dict.iteritems() :
	print key

for key, value in paths_dict.iteritems() :
	print key

matrix = np.zeros([len(start_end_values_dict), len(paths_dict)])

with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	next(spamreader, None)  # skip the headers
	for row in spamreader:
		start = row[0]
		end = row[1]
		key = start + ' ' + end
		path = row[2][1:-1]
		matrix[start_end_values_dict.get(key)][paths_dict.get(path)] = 1

np.savetxt(sys.argv[1][:-4] + '_matrix.txt',matrix,fmt='%d')










