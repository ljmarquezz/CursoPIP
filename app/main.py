import utils
import pandas as pd

def run():
    #utilizando pandas
    df = pd.read_csv('./data.csv')
    #asi se seleccionan solo los paises en sur america
    df = df[df['Continent'] == 'Africa']
    #se obtiene el nombre de los paises
    countries = df['Country'].values
    #el wpp
    percentages = df['World Population Percentage'].values
    #se genera la grafica
    utils.generate_pie_chart('Africa', countries, percentages)
    
    #sin utilizar pandas
    data=utils.read_csv('./data.csv')
    country=input('Type Country => ')
  
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country=result[0]
        country_population=utils.population_by_year(country)
        labels = list(country_population.keys())
        values = list(country_population.values())
        utils.generate_bar_chart(country['Country'], labels, values)
    else:
        print('El pais ingresado no se encuentra en la data.')
    


if __name__ == '__main__':
  run()
