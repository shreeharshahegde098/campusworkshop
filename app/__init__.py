"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaad8jhp8u791gtihug-a",
        database="todo_hthq",
        user="root",
        password="Ir3elBFNmHVvzaSFboULojqfOHbXsFFT")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
