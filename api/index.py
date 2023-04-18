from flask import Flask


app = Flask(__name__, static_url_path='', root_path='../static')


@app.route("/api/function/", methods=["GET"])
def index():
    return app.send_static_file('index.html')
