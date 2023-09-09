from pydantic import BaseModel


# Валидатор публикации комментариев
class CommentModel(BaseModel):
    comment_text: str
    user_id: int


# Валидатор на изменение коммента
class EditCommentModel(BaseModel):
    new_text: str
    comment_id: int
