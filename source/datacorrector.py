
# coding: utf-8


import pandas as pd
import numpy as np
import csv


#Metodo que transforma texto em lista. Serve somente para o formato da última coluna do dataset
def strToList(array):
    array = array.replace("'","")
    array = array.replace("[","")
    array = array.replace("]","")
    array = array.replace(" ","")
    array = array.split(",")
    return array[:]


#Dados de entrada e corrigidos
original = "../data/data.csv"
adjusted = "../data/adjusted_data.csv"

#Carregando dados

def correction(datapath=original):
    """Corrects the original csv file by replacing some of it's structure"""

    rawData = []
    with open(datapath, 'r') as f:
        for line in f:
	    rawData.append(line)
	    #Corrigindo erro de imporatção
	    s = "\'"
	    d = "\""
	for i in range(0,len(rawData)):
	    rawData[i] = rawData[i].replace(d,s)
	    rawData[i] = rawData[i].replace("[",'\"[')
	    rawData[i] = rawData[i].replace("]",']\"')

	    
	with open(adjusted, 'w') as f:
	    for row in rawData:
		f.write(row)

	print('Data correction was successful')

