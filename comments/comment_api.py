from fastapi import APIRouter

from comments import CommentModel, EditCommentModel

# Создаем компонент
comment_router = APIRouter(prefix='/comment', tags=['Работа с комменатрием'])


# запрос на добавления комментария
@comment_router.post('/add_comment')
async def add_comments(data: CommentModel):
    pass


# запрос на изменения комментария
@comment_router.put('/change_comment')
async def change_comment(data: EditCommentModel):
    pass


# запрос на удаление комментария
@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass


# запрос на получение комментариев к определенной публикации
@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    pass
