#
# MIT License
#
# Copyright (c) 2020 Pablo Rodriguez Nava, @pablintino
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#


import logging
from os import environ

__logger__ = logging.getLogger(__name__)


class Config:
    # General Flask Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_DEBUG = environ.get('FLASK_DEBUG', 1)

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_LOG_LEVEL = environ.get('APP_LOG_LEVEL', 'DEBUG')

    # Redis
    REDIS_URL = environ.get('REDIS_URL') or 'redis://'

    # Git repo and identity settings
    REPO_PATH = environ.get('REPO_PATH') or '/altium-repo'
    REPO_URL = environ.get('REPO_URL')
    REPO_BRANCH = environ.get('REPO_BRANCH') or 'master'
    SSH_IDENTITY = environ.get('SSH_IDENTITY') or '/ssh-dir/id_rsa'
    SSH_HOSTS_FILE = environ.get('SSH_HOSTS_FILE') or '/ssh-dir/known_hosts'

    @staticmethod
    def log_config():
        __logger__.info(
            f'APP Configuration:\n\tFLASK_ENV={Config.FLASK_ENV}\n\tFLASK_APP={Config.FLASK_APP}'
            f'\n\tFLASK_DEBUG={Config.FLASK_DEBUG}\n\tSQLALCHEMY_ECHO={Config.SQLALCHEMY_ECHO}'
            f'\n\tSQLALCHEMY_TRACK_MODIFICATIONS={Config.SQLALCHEMY_TRACK_MODIFICATIONS}'
            f'\n\tAPP_LOG_LEVEL={Config.APP_LOG_LEVEL}\n\tREDIS_URL={Config.REDIS_URL}'
            f'\n\tREPO_PATH={Config.REPO_PATH}\n\tREPO_URL={Config.REPO_URL}\n\tREPO_BRANCH={Config.REPO_BRANCH}'
            f'\n\tSSH_IDENTITY={Config.SSH_IDENTITY}\n\tSSH_HOSTS_FILE={Config.SSH_HOSTS_FILE}')
