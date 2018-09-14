import csv
import sys
import numpy as np

interest_category = ['animal', 'country', 'city', 'movie', 'person', 'writer', 'actor', 'sport']

in_degree_dict = {}

for category in interest_category:
	out_degree_dict = {}
	with open(sys.argv[1]) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';')
		for row in spamreader:
			if row[2] == category:
				out_degree_dict[row[0]] = out_degree_dict.get(row[0], 0) + 1

	print "======================"
	# for key,value in out_degree_dict.iteritems():
	# 	print "%s: %s" % (key, value)

	print "category: %s" % category
	print "elements: %s" % len(out_degree_dict)
	print "mean: %s" % np.mean(out_degree_dict.values())
	print "sd: %s" % round(float(np.std(out_degree_dict.values())), 2)