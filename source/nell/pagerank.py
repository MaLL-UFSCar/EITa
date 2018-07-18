import csv
import sys
import networkx as nx
import matplotlib.pyplot as plt

# Salva um grafo em formato de imagem
#
# param G: Grafo do NetworkX para ser salvo
# param output_name: nome da imagem a ser salva
def print_graph(G, output_name):
    labels= dict([((u,v,), d['relation_name']) for u, v, d in G.edges(data=True)])
    pos = nx.spring_layout(G, k=1)

    plt.clf()
    nx.draw(G, pos, with_labels = True)
    nx.draw_networkx_edge_labels(G, pos, labels)
    plt.savefig(output_name, dpi = 600)

if __name__ == "__main__":
	# G = nx.read_edgelist(sys.argv[1], delimiter='	')
	G = nx.read_edgelist(sys.argv[1], delimiter=';', data=(('relation_name',str),))
	G.edges(data=True)
	print_graph(G, 'graph.png')
	pr = nx.pagerank(G, 0.9)
	for key, value in sorted(pr.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s" % (key, value)
