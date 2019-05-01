import os
import sys

def get_environ(tag):
    _TAG_ = os.environ.get(tag)
    if not _TAG_:
        print(tag + " not defined on ENVIRON")
        print("finalizando...")
        sys.exit()

    return _TAG_

_PSQL_HOST_ = get_environ('PSQL_HOST')
_PSQL_USER_ = get_environ('PSQL_USER')
_PSQL_PASSWORD_ = get_environ('PSQL_PASSWORD')
_PSQL_DB_ = get_environ('PSQL_DB')

_API_KEY_= get_environ('API_KEY')
_API_URL_ = get_environ('API_URL')