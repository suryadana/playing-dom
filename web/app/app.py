from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__, template_folder="templates")


@app.route('/js/<path:path>')
def send_js(path):
    if request.accept_languages:
        return send_from_directory('js', path)
    return ''


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
