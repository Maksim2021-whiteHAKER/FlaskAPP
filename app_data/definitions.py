from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass
mysql_user = 'admin'
mysql_passw = '3211'
mysql_achemy_connect_str = f"mysql+pymysql://{mysql_user}:{mysql_passw}@localhost/aqua_db?charset=utf8mb4_unicode_ci"

my_connect = create_engine(mysql_achemy_connect_str)