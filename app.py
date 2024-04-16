from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
# To make debugging server later, not working now, will fix    
#    if __name__ == "__main__":  
#        app.run(debug=True)
    return render_template('index.html')
