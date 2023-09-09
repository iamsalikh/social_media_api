from fastapi import APIRouter


# Создаем компонент
posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


@posts_router.post('/public_post')
async def public_post():
    pass


@posts_router.put('/change_post')
async def change_post():
    pass


@posts_router.delete('/delete_post')
async def delete_post():
    pass


@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass


###
@posts_router.post('/add_photo')
async def add_photo():
    pass


@posts_router.delete('/delete_photo')
async def delete_photo():
    pass
