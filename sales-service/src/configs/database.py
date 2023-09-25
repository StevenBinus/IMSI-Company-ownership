from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from src.configs.config import Settings

# param = Settings()

if param.db_driver.__contains__("sqlserver"):
    database_url = f"mssql+pymssql://{param.db_user}:{param.db_password}@{param.db_server}/{param.db_name}"
elif param.db_driver.__contains__("postgre"):
    database_url = f"postgresql://{param.db_user}:{param.db_password}@{param.db_server}:{param.db_port}/{param.db_name}"
else:
    server = 'LAPTOP-H9KDJVIG'
    database = 'test_API'
    database_url = 'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(
    database_url, pool_size=20, max_overflow=20, pool_timeout=30, pool_recycle=3600
)

Local_Session = Session(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

async def get_db():
    db = Local_Session  
    try:
        yield db
        db.close()
