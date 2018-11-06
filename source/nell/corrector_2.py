import csv
import sys

csv.field_size_limit(sys.maxsize)

# Padroniza o arquivo 'every belief in the KB' para ser usado pelo degree.py
# O output deste programa deve ser redirecionado para um arquivo .csv
print('Entity;Relation;Domain;Range;Value')
with open(sys.argv[1]) as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	next(spamreader, None)  # skip the headers
	for row in spamreader:
		row = row[0]
		entity, relation, value, garbage = row.split('	', 3)
		try:
			garbage, domain, entity = entity.split(':', 2)

			if  'concept' in relation:
				garbage, relation = relation.split(':', 1)

				if value.startswith('concept'):
					garbage, _range, value = value.split(':', 2)

					print('\"' + relation + '\"' + '\"' + domain + '\"' + '\"' + _range + '\"')
		except Exception as e:
			entity = entity