from base import app
from flask import jsonify, request
from .resources import user
from .resources import category
from .resources import record


if __name__ == "__main__":
    app.run()
