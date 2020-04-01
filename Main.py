from flask import Flask, render_template, request
from pprint import pprint
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

        if not controller.get_is_configured():
            doubleColors = bool(result.get('doubleColor'))
            colorAmount = int(result.get('colorAmount'))
            positionAmount = int(result.get('positionAmount'))
            if colorAmount < positionAmount and not doubleColors:
                return render_template("gamesettings.html")
            controller.add_settings(doubleColors, colorAmount, positionAmount)



        availableColors = controller.get_available_colors()
        positionAmount = controller.get_position_amount()
        list = []
        history = {}
        for i in range(positionAmount):
            if result.get("color" + str(i)) is not None:
                list.append(result.get("color" + str(i)))
        if len(list) > 0:
            results = controller.play_turn(list)
            history = controller.get_history()
            if results[0]:
                return render_template("endscreen.html")
            else:
                print(results[1])
                return render_template("game.html", positionAmount=positionAmount, availableColors=availableColors, pinlist=results[1], history=history)

        return render_template("game.html", positionAmount=positionAmount, availableColors=availableColors)


if __name__ == '__main__':
    controller = MainController()
    app.run(debug=True)
