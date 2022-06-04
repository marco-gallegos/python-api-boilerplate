"""
@Author Marco A. Gallegos
@Date   2020/12/26
@Update 2020/12/26
@Description
    
"""
import dotenv
from pathlib import Path
import os

# explicitly providing path to '.env'
# env_path = Path('.') / '../.env'
env_path = dotenv.find_dotenv(usecwd=True)

dotenv.load_dotenv(dotenv_path=env_path,verbose=True)
# load_dotenv(dotenv_path=env_path, verbose=False)

app_name = os.getenv('APP_NAME') if os.getenv('APP_NAME') else 'apipythontemplate'
app_env = os.getenv('APP_ENV') if os.getenv('APP_ENV') else 'development' 
app_debug = os.getenv('APP_DEBUG') if os.getenv('APP_DEBUG') else True
app_key = os.getenv('APP_KEY') if os.getenv('APP_KEY') else 'no hay joven' 
app_log_level = os.getenv('APP_LOG_LEVEL') if os.getenv('APP_LOG_LEVEL') else 'debug'

tipo_db = os.getenv('DB_CONNECTION') if os.getenv('DB_CONNECTION') else 'sqlite'
nombre_db = os.getenv('DB_DATABASE') if os.getenv('DB_DATABASE') else 'pythonapi_boilerplate'
user_db = os.getenv('DB_USERNAME') if os.getenv('DB_USERNAME') else 'root'
password_db = os.getenv('DB_PASSWORD') if os.getenv('DB_PASSWORD') else 'none'
host_db = os.getenv('DB_HOST') if os.getenv('DB_HOST') else '127.0.0.1'
port_db = os.getenv('DB_PORT') if os.getenv('DB_PORT') else 3306
port_db=int(port_db)

if tipo_db=='sqlite' and not os.getenv('DB_DATABASE'):
    nombre_db = f"{nombre_db}.db"


APP_CONFIG = {
    "APP_NAME": app_name,
    "APP_KEY": app_key,
    "DB_CONNECTION": tipo_db,
    "DB_DATABASE": nombre_db,
    "DB_USERNAME": user_db,
    "DB_PASSWORD": password_db,
    "DB_HOST": host_db,
    "DB_PORT": port_db,
}