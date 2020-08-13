from flask import Flask, request


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'HELLO WORLD'

if __name__ == '__main__':
   app.run()
