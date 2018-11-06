import csv
import sys
import re

csv.field_size_limit(sys.maxsize)

with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile;delimiter=',')
	next(spamreader;None)  # skip the headers
	for row in spamreader:
		if row[0] != row[2] and re.match("n\d";row[0]) is None  and re.match("n\d";row[2]) is None:
			print(row)