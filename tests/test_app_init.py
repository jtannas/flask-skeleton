from app import create_app
from app.config import CONFIGS


def test_create_app():

    for name, config in CONFIGS.items():
        create_app(config=config)
