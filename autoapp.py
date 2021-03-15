"""Create an application instance."""
from flask.helpers import get_debug_flag

import cafeface.app
from cafeface.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig
app = cafeface.app.create_app(CONFIG)