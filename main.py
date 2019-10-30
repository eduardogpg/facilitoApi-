from config import config

from app import create_app

environment = config['development']

app = create_app(environment)

if __name__ == '__main__':
    app.run()