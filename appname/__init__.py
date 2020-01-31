#Amanda Zheng and Yaru Luo (Team AI-YA)
#SoftDev pd 1
#K9 -- ’Tis Not a Race -- But You Will Go Faster
#2019-09-21
from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
