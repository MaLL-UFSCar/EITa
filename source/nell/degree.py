import csv
import sys
import numpy as np

interest_category = ['animal', 'country', 'city', 'movie', 'person', 'writer', 'actor', 'sport']

out_degrees_dict = {'animal'	: {},
					'country'	: {},
					'city'		: {},
					'movie'		: {},
					'person'	: {},
					'writer'	: {},
					'actor'		: {},
					'sport'		: {}}

with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		if row[2] in interest_category:
			out_degrees_dict.get(row[2])[row[0]] = out_degrees_dict.get(row[2]).get(row[0], 0) + 1

for dictionary in sorted(out_degrees_dict.items()):
	print "======================"
	print "category: %s" % dictionary[0]
	print "out degree"
	print "elements: %s" % len(dictionary[1])
	if dictionary[1]:
		print "mean: %s" % round(float(np.mean(dictionary[1].values())), 2)
		print "sd: %s" % round(float(np.std(dictionary[1].values())), 2)