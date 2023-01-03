import csv
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./img/{name}.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values,labels = labels)
  ax.axis('equal')
  plt.savefig(f'./img/{name}.png')
  plt.close()
  
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #A veces los datos vienen separador por ; o , esto se verifica
    #en el archivo
    header = next(reader) #primera fila del csv
    countries=[]
    for row in reader: #cada fila es una lista
      iterable = zip(header, row)
      county_dict = {key:value for key,value in iterable}
      #genero un diccionario con la lista de tuplas anterior
      countries.append(county_dict) 
      #agrego el diccionaro generado a mi lista
    return countries

'''Asi quedan los diccionarios generados:
{'Rank': '74',
 'CCA3': 'ZWE',
 'Country/Territory': 'Zimbabwe',
 'Capital': 'Harare',
 'Continent': 'Africa',
 '2022 Population': '16320537',
 '2020 Population': '15669666',
 '2015 Population': '14154937',
 '2010 Population': '12839771',
 '2000 Population': '11834676',
 '1990 Population': '10113893',
 '1980 Population': '7049926',
 '1970 Population': '5202918',
 'Area (km²)': '390757',
 'Density (per km²)': '41.7665',
 'Growth Rate': '1.0204',
 'World Population Percentage': '0.2'}
'''

def population_by_year(data, country = {}):
  for key,value in data.items():
    if key == '2022 Population':
      country['2022']=int(value)
    elif key == '2020 Population':
      country['2020']=int(value)
    elif key == '2015 Population':
      country['2015']=int(value)
    elif key == '2010 Population':
      country['2010']=int(value)
    elif key == '2000 Population':
      country['2000']=int(value)
    elif key == '1990 Population':
      country['1990']=int(value)
    elif key == '1980 Population':
      country['1980']=int(value)
    elif key == '1970 Population':
      country['1970']=int(value)
  return country

def population_by_country(data, country):
  result = list(filter(lambda item:item['Country']==country, data))
  return result

def world_population(data):
  wpp=list(map(lambda x:float(x['World Population Percentage']), data))
  countries=list(map(lambda x:x['Country'], data))
  return countries, wpp