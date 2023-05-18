import os

TORTOISE_ORM = {
    'connections': {'default': os.environ.get('DATABASE_URL')},
    'apps': {
        'models': {
            'models': ['course_fast_api.models.tortoise', 'aerich.models'],
            'default_connection': 'default',
        },
    },

}
