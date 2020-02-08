from flask import Flask
from flask import request

app = Flask(__name__)

# Global seed value
seed = 0

# Simple web server
# GET will return seed number as string
# POST will assign JSON value "{"num": int}" to seed number
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        postObject = request.get_json()
        set_seed(postObject["num"])
        return ""
    return get_seed()


# Get global seed value
def get_seed():
    global seed
    return str(seed)

'''
Set global seed value, 
take an integer and then 
assign the value to seed
'''
def set_seed(num):
    global seed
    seed = num
    return ""

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
