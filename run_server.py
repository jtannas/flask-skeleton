#!/usr/bin/env python3.6
"""Runs the flask application with the specified configuration"""

from app import create_app
from app.config import CONFIGS
from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: run_server <config>")

    config = CONFIGS[argv[1]]
    app = create_app(config=config)
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    main()
