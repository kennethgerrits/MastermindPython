from flask import Flask, render_template, request

from controllers.MainController import MainController

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        username = result.get('Name')
        controller.add_new_player(username)
        return render_template("result.html", result=result)


if __name__ == '__main__':
    controller = MainController
    app.run(debug=True)
