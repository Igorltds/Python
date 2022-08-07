import os

class Config():
    CSRF_ENABLE = True
    SECRET = '314159265'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLETE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None 

class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'


class TestingConfig(Config):
    pass


app_config = {
    'development' : DevelopmentConfig(), 
    'testing' : TestingConfig()
}

# pedindo esclarecimento de tipo de env para definir qual subclasse dessa pagina usar usar
app_active = os.getenv('FLASK_ENV')



# Isso não funciona de vdd como parece que deveria
# aqui só é colocado o tipo 'poduction' por padrão (mesmo sem eu ter feito essa classe)
# Temos que declarar o Flask_ENV como dito no 'README.md' (mas no momento deixo isso aqui pq faz funcionar sem precisar declarar pq a classe production não está declarada)
if app_active is None: 
    app_active = 'development' 


# Para iniciar corretamente temos que declarar qual tipo de env vc quer usar logo anstes de iniciar o código:
# export FLASK_ENV=development
# Veja mais em "/READEME.md" 
