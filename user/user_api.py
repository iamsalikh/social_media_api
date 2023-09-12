from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel


# Создаем компонент
user_router = APIRouter(prefix='/user', tags=['Управления пользователями'])


# запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    pass


# запрос на регистрацию
@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    pass


# запрос на изменения информации
@user_router.put('/change_info')
async def change_info_user(data: EditUserModel):
    pass


# запрос на получения пользователя
@user_router.get('/get_user')
async def get_user(user_id: int):
    pass
