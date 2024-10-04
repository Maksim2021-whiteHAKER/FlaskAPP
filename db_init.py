from models.User import User
from models.State import AquaState
from app_data.definitions import mysql_connect
from app_data.definitions import Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=mysql_connect)

with Session(autoflush=False, bind=mysql_connect) as db:
    # создаем объект Person для добавления в бд
    user = User(
        surname = 'Ivanov',
        firstname = 'Ivan',
        middlename = 'Ivanovich',
        phone = '89121234567',
        email = 'ivanov@mail.ru',
        password = '123',
        token_hash =  None,
        token_created = None )
    db.add(user)     # добавляем в бд


    d1 = AquaState(
        device_name = 'Air pump',
        device_type = 'switch',
        device_status = 0,
    )
    d2 = AquaState(
        device_name = 'Light',
        device_type = 'switch',
        device_status = 0,
    )
    d3 = AquaState(
        device_name = 'Temperature sensor',
        device_type = 'sensor',
        device_status = 25,
    )
    db.add_all([d1, d2, d3])
    db.commit()     # сохраняем изменения
    print(user.id)   # можно получить установленный id