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
        controller.add_new_player('test')
        return render_template("result.html", result=result)


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        result = request.form
        username = str(result.get('name'))
        controller.add_new_player(username)
        return render_template("gamesettings.html")


@app.route('/play', methods=['POST', 'GET'])
def play():
    if request.method == 'POST':
        result = request.form
        doubleColors = result.get('doubleColor')
        colorAmount = result.get('colorAmount')
        positionAmount = result.get('positionAmount')
        controller.add_settings(doubleColors, colorAmount, positionAmount)
        return render_template("game.html")




if __name__ == '__main__':
    controller = MainController()
    app.run(debug=True)
