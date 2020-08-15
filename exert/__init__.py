import os
import sys
from sanic import Sanic


def get_here():
    '''
    获取程序运行根目录。
    '''
    me = os.path.realpath(sys.argv[0])
    return os.path.dirname(me)


class Application(Sanic):
    '''
    应用程序类。
    '''

    def __init__(self, name):
        '''
        初始化日志配置和静态文件。
        '''
        super().__init__(
            name=name,
            log_config={
                'version': 1,
                'disable_existing_loggers': False,
                'loggers': {
                    'sanic.root': {
                        'level': 'DEBUG',
                        'handlers': ['console', 'access_file'],
                        'propagate': True
                    },
                    'sanic.error': {
                        'level': 'ERROR',
                        'handlers': ['error_file'],
                        'propagate': True
                    },
                    'sanic.access': {
                        'level': 'INFO',
                        'handlers': ['access_file'],
                        'propagate': True
                    },
                },
                'handlers': {
                    'console': {
                        'class': 'logging.StreamHandler',
                        'level': 'DEBUG',
                        'formatter': 'generic',
                    },
                    'error_file': {
                        'class': 'logging.handlers.RotatingFileHandler',
                        'level': 'ERROR',
                        'formatter': 'generic',
                        'encoding': 'utf-8',
                        'filename': './log/error.log',
                        'maxBytes': 1024 * 1024 * 200,
                        'backupCount': 5,
                    },
                    'access_file': {
                        'class': 'logging.handlers.RotatingFileHandler',
                        'level': 'INFO',
                        'formatter': 'access',
                        'encoding': 'utf-8',
                        'filename': './log/access.log',
                        'maxBytes': 1024 * 1024 * 200,
                        'backupCount': 5,
                    },
                },
                'formatters': {
                    'generic': {
                        'format': '%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s',
                    },
                    'access': {
                        'format': '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d | %(message)s',
                    },
                }
            }
        )
        here = get_here()
        self.static('/', os.path.join(here, 'public'))
