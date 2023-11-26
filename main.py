from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"ФИО": "Емельяненков Григорий Алексеевич"}

@app.get('/tools')
async def f_indexT():
    return "Бездарь!"

@app.get('/users')
async def f_indexT():
    return {"Телефон": "+79628166881", "Электронная почта": "ghorickckrolik@mail.ru"}