import csv
import sys
import numpy as np

interest_category = ['actor', 'animal', 'city', 'country', 'movie', 'person', 'sport', 'writer']

for category in interest_category:
	out_degree_dict = {}
	in_degree_dict = {}
	with open(sys.argv[1]) as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';')
		for row in spamreader:
			if row[2] == category:
				out_degree_dict[row[0]] = out_degree_dict.get(row[0], 0) + 1
			if row[3] == category:
				in_degree_dict[row[0]] = in_degree_dict.get(row[0], 0) + 1


	print "======================"
	# for key,value in out_degree_dict.iteritems():
	# 	print "%s: %s" % (key, value)

	print "category: %s" % category
	print "out degree"
	print "elements: %s" % len(out_degree_dict)
	if out_degree_dict:
		print "mean: %s" % round(float(np.mean(out_degree_dict.values())), 2)
		print "sd: %s" % round(float(np.std(out_degree_dict.values())), 2)
	# print "in degree"
	# print "elements: %s" % len(in_degree_dict)
	# if in_degree_dict:
	# 	print "mean: %s" % np.mean(in_degree_dict.values())
	# 	print "sd: %s" % round(float(np.std(in_degree_dict.values())), 2)
	# print "degree"
	# print "elements: %s" % len(in_degree_dict) + len(out_degree_dict)
	# print "mean: %s" % np.mean(in_degree_dict.values() + out_degree_dict.values())
	# print "sd: %s" % round(float(np.std(in_degree_dict.values() + out_degree_dict.values())), 2)
