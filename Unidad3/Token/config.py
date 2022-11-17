class BaseConfig:
    USER_DB='postgres'
    PASS_DB='bumo'
    URL_DB='localhost'
    NAME_DB='clase_login'
    FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI=FULL_URL_DB
    SECRET_KEY="llavesecreta"
    DEBUG=False
    BCRYPT_LOG_ROUNDS=12
    SQLALCHEMY_TRACK_MODIFICATIONS=False