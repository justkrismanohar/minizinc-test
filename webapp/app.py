import os
import subprocess

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello world! - Minizinc! From github!'
    p = subprocess.Popen("Your command", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    return 'Hello world! - Minizinc! From github!' + "<br/>" + str(p)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
