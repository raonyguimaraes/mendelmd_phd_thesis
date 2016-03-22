from fabric.api import run, local

def install():
    local('sudo apt-get install mysql-server libmysqlclient-dev')
    local('pip install -r requirements.txt')
