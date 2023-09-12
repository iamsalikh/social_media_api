from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Подключение и выбор СУБД
SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session = sessionmaker(bind=engine)

Base = declarative_base()

# Импорт всех моделей
from database import models


# Генератор подключений
def get_db():
    db = session()
    try:
        yield db

    except:
        db.rollback()
        raise

    finally:
        db.close()