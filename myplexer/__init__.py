from flask import Flask
import os

# class Myplexer():
#     def __init__(self):
#         app = Flask("myplexer_app")
#         app.config.from_mapping(
#             SECRET_KEY='dev')

app = Flask("myplexer_app")
app.config.from_mapping(SECRET_KEY='dev')
# app = Myplexer()

@app.route('/hi')
def hi():
    return "Hello"
