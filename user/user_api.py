from fastapi import APIRouter
from user import RegisterUserModel, LoginUserModel, EditUserModel

from database.userservice import login_user_db, register_user_db, get_exact_users_db, get_all_users_db
# Создаем компонент
user_router = APIRouter(prefix='/user', tags=['Управления пользователями'])


# запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginUserModel):
    result = login_user_db(**data.model_dump())

    return {'status': 1, 'message': result}


# запрос на регистрацию
@user_router.post('/register')
async def register_user(data: RegisterUserModel):
    result = register_user_db(**data.model_dump())

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Пользователь с такой почтой есть базе'}


# запрос на изменения информации
@user_router.put('/change_info')
async def change_info_user(data: EditUserModel):
    pass


# запрос на получения пользователя
@user_router.get('/get_user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'status': 1, 'message': result}
