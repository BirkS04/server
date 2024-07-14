import templates
from flask import Flask, render_template, url_for

app = Flask(__name__)

if __name__== "__main__":
    app.run(debug=True)    


# @app.route("/")
# def hello_world():
#     return render_template("index.html")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)



# def routing():
#     for i in templates:
#         @app.route(f'/{i}')
#         def hi():
#             return render_template(f'/{i}')
    
# routing()