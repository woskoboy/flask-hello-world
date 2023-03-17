from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/gpt/')
def gpt():
    openai.api_key = "xxx"
    # list models #This basically defines what content
    models = openai.Model.list()
    # print the first model's id
    print(models.data[0].id)
    # create a completion
    completion = openai.Completion.create(model="ada", prompt="Hello>
    # print the completion
    print(completion.choices[0].text)
if __name__ == "__main__":
    app.run(host='0.0.0.0')