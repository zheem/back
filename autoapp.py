"""Create an application instance."""

import cafeface.app
from cafeface.settings import Config

CONFIG = Config
app = cafeface.app.create_app(CONFIG)