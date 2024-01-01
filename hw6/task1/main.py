from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = FastAPI()

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    email: str
    address: str


@app.post('/users/')
def create_user(user: UserCreate):
    with Session() as session:
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            birth_date=user.birth_date,
            email=user.email,
            address=user.address
        )
        session.add(new_user)
        session.commit()
        return {"id": new_user.id}


@app.get('/users/{user_id}')
def get_user(user_id: int):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return {"id": user.id, "имя": user.first_name, "фамилия": user.last_name,
                "дата рождения": user.birth_date, "email": user.email, "адрес": user.address}


@app.put('/users/{user_id}')
def update_user(user_id: int, user: UserCreate):
    with Session() as session:
        user_to_update = session.query(User).filter_by(id=user_id).first()
        if user_to_update is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        user_to_update.first_name = user.first_name
        user_to_update.last_name = user.last_name
        user_to_update.birth_date = user.birth_date
        user_to_update.email = user.email
        user_to_update.address = user.address
        session.commit()
        return {"id": user_to_update.id}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    with Session() as session:
        user_to_delete = session.query(User).filter_by(id=user_id).first()
        if user_to_delete is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        session.delete(user_to_delete)
        session.commit()
        return {"id": user_to_delete.id}
