from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from photo.photo_api import photo_router


app = FastAPI(docs_url='/')

# Pегистрация компонентов
app.include_router(photo_router)

# Добавления ссылки для открытия локальных файлов
app.mount(path='/media', app=StaticFiles(directory='media'))


@app.get('/hello')
async def hello():
    return {'message': 'Hello World'}


