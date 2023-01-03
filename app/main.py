import utils

def run():
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
