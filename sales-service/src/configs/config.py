from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_driver: str = Field(...,env="DB_DRIVER")
    db_password: str = Field(...,env="DB_PASSWORD")
    db_user: str = Field(...,env="DB_USER")
    db_server: str = Field(...,env="DB_SERVER")
    db_name: str = Field(...,env="DB_NAME")
    db_port: str = Field(...,env="DB_PORT")

    class Config:
        env_prefix = ""
        case_sensitivse = False
        env_file = './src/.env'
        env_file_encoding = 'utf-8'