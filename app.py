import os
import openai
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/model/<string:api_key>')
def get_model_list(api_key):
    openai.organization = "*"
    openai.api_key = api_key
    #os.getenv(OPENAI_API_KEY)
    #openai.Model.retrieve("text-davinci-003") 
    return openai.Model.list()
