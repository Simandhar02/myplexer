from flask import Flask
import os

class Myplexer(Flask):
    def __init__(self):
        Flask.__init__(self, __name__)
    # def __init__(self):
    #     app = Flask("myplexer_app")
    #     app.config.from_mapping(
    #         SECRET_KEY='dev')

# app = Flask("myplexer_app")
# app.config.from_mapping(SECRET_KEY='dev')
# app = Myplexer()
