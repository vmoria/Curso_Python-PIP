import Store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

App = FastAPI()

@App.get('/') # @ is a Decorater - This is the main path
def Get_List():
    return [1, 2, 3]

@App.get('/Contact', response_class=HTMLResponse) # This is the contact path
def Get_List():
    return """
        <h1>Hola soy una página</h1>
        <p>Soy un párrafo</p>
    """
def run():
    Store.Get_Categories()

if __name__ == '__main__':
    run()