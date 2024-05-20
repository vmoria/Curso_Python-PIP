import requests

def Get_Categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    Categories = r.json()
    for Category in Categories:
        print(Category['name'])