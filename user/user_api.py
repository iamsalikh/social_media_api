from fastapi import APIRouter


# Создаем компонент
user_router = APIRouter(prefix='/user', tags=['Управления пользователями'])


# запрос на вход в аккаунт
@user_router.post('/login')
async def login_user():
    pass


# запрос на регистрацию
@user_router.post('/register')
async def register_user():
    pass


# запрос на изменения информации
@user_router.put('/change_info')
async def change_info_user():
    pass


# запрос на получения пользователя
@user_router.get('/get_user')
async def get_user():
    pass
