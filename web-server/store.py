import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    #status code me da el status de la respuesta, 200 significa que todo salio bien
    print(r.status_code) 
    #con text tengo el contenido que obtuve de la consulta get
    #text viene en formato de string, por lo que para iterarlo debo convertirlo
    print(r.text)
    # con json transformo la respuesta del request en una lista
    categories = r.json()
    for category in categories:
        print(category['name'])