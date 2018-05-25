# coding: utf-8
import snap
import pandas as pd
import numpy as np

#Metodo que transforma texto em lista. Serve somente para o formato da última coluna do dataset
def strToList(array):
    array = array.replace("'","")
    array = array.replace("[","")
    array = array.replace("]","")
    array = array.replace(" ","")
    array = array.split(",")
    return array[:]

#Método que gera e salva o grafo
def generate(adjusted):
    #Lendo o arquivo corrigido
    s = "\'"
    data = pd.read_csv(adjusted)

    #Gerando um dicionário com os ids
    ids = {}

    for i in data.index:
        person_id = data.iloc[i,0].replace(s, "")
        ids[person_id] = i


    # ## Gerando grafo do snap
    G = snap.TNGraph.New()

    for i in data.index:
        #Gerando os nós
        node = ids[str(data.iloc[i,0]).replace(s,"")]
        G.AddNode(node)

        #Gerando as arestas
        friends = strToList(data.iloc[i,-1])
        for friend in friends:
            try:
                G.AddEdge(i,ids[friend])
            except:
                pass

    #Removendo nós de grau zero
    snap.DelZeroDegNodes(G)

    #Salvando o grafo
    snap.SaveEdgeList(G, "grafo.txt", "Save as tab-separated list of edges")