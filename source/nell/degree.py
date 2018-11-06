import csv
import sys
import numpy as np

interest_category = ['animal', 'country', 'city', 'movie', 'person', 'writer', 'actor', 'sport', 'disease', 'sport', 'legume', 'bacteria']

out_degrees_dict = {'animal'	: {},
					'country'	: {},
					'city'		: {},
					'movie'		: {},
					'person'	: {},
					'writer'	: {},
					'actor'		: {},
					'sport'		: {},
					'disease'	: {},
					'sport'		: {},
					'legume'	: {},
					'bacteria'	: {}}

with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		if row[2] in interest_category:
			out_degrees_dict.get(row[2])[row[0]] = out_degrees_dict.get(row[2]).get(row[0], 0) + 1

if (sys.argv[2] == "-l"):
	for dictionary in sorted(out_degrees_dict.items()):
		print('\t\t\\textit{' + dictionary[0] + '} & $' + str(round(float(np.mean(dictionary[1].values())), 2)) + ' \\pm ' + str(round(float(np.std(dictionary[1].values())), 2)) + '$ & ' + str(len(dictionary[1])) + ' \\\\')
else:
	for dictionary in sorted(out_degrees_dict.items()):
		print "======================"
		print "category: %s" % dictionary[0]
		print "out degree"
		print "elements: %s" % len(dictionary[1])
		if dictionary[1]:
			print "mean: %s" % round(float(np.mean(dictionary[1].values())), 2)
			print "sd: %s" % round(float(np.std(dictionary[1].values())), 2)