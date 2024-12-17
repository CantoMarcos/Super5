from dotenv import dotenv_values
import os

def get_environment_config():
    if os.environ.get('ENVIRONMENT'): return os.environ
    env_file_path = os.environ.get('ENV_FILE_PATH')
    prefix_location = '../'
    if env_file_path: 
        values = dotenv_values(f'{prefix_location}{env_file_path}')
        return values
    
    config = dotenv_values(f'{prefix_location}environments/.env')
    environment = config['ENVIRONMENT']
    env_path = config[environment]
    values = dotenv_values(f'{prefix_location}{env_path}')
    return values
