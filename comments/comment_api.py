from fastapi import APIRouter


# Создаем компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комменатрием'])


@comment_router.post('/add_comment')
async def add_comments():
    pass


@comment_router.put('/change_comment')
async def change_comment():
    pass


@comment_router.delete('/delete_comment')
async def delete_comment():
    pass


@comment_router.get('/get_comments')
async def get_comments():
    pass
