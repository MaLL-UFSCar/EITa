import csv
import sys

csv.field_size_limit(sys.maxsize)

nodes_dict = {}
node_id = 1

# Padroniza o arquivo 'every belief in the KB' para ser usado pelo degree.py
# O output deste programa deve ser redirecionado para um arquivo .csv
# print('value,domain')
print(':TYPE:START_ID(Entity),:END_ID(Entity)')
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

					# print '\"' + relation + '\"',
					key_1 = '\"' + entity + '\"' + ',' + '\"' + domain + '\"'
					if key_1 not in nodes_dict:
						nodes_dict[key_1] = node_id
						# print(key_1)
						node_id = node_id + 1

					key_2 = '\"' + value + '\"' + ',' + '\"' + _range + '\"'
					if key_2 not in nodes_dict:
						nodes_dict[key_2] = node_id
						# print(key_2)
						node_id = node_id + 1

					print nodes_dict.get(key_1),
					print ','+ '\"' + entity + '\"' + ',' + '\"' + domain + '\"'
					print()
					print nodes_dict.get(key_2),
					print ','+ '\"' + value + '\"' + ',' + '\"' + _range + '\"'

					# print nodes_dict.get(key_1),
					# print nodes_dict.get(key_2)

					# print('\"' + relation + '\"' + ',' + nodes_dict.get(key_1) + ',' + nodes_dict.get(key_2))
		except Exception as e:
			entity = entity