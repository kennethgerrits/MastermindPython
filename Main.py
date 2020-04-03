from flask import Flask, render_template, request
from pprint import pprint
from controllers.MainController import MainController

app = Flask(__name__)


@app.route('/')
def index():
    controller.resetGame()
    return render_template('index.html')

@app.route('/statistics')
def statistics():
    rows = controller.get_total_turn_amount_all()
    return render_template('statistics.html', rows=enumerate(rows))

@app.route('/details')
def details():
    if request.method == 'POST':
        result = request.form
        username = str(result.get('username'))
        rows=controller.get_details_of_player(username)
        return render_template('detailedstatistics.html', rows=enumerate(rows))


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if request.method == 'POST':
        result = request.form
        username = str(result.get('name'))
        if result.get('name') == '':
            return render_template('index.html')
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
        userColorInput = []
        player = controller.get_player()
        turnsTaken = controller.get_turns_taken()
        history = {}
        if controller.get_turns_taken() > 9:
            return render_template("gameover.html", player=player, turnsTaken=turnsTaken, maxTurnAmount=10)
        for i in range(positionAmount):
            if result.get("color" + str(i)) is not None:
                userColorInput.append(result.get("color" + str(i)))
        if len(userColorInput) > 0:
            results = controller.play_turn(userColorInput)
            history = controller.get_history()
            if results[0]:

                return render_template("endscreen.html", player=player, turnsTaken=turnsTaken)
            else:
                print(results[1])
                print(userColorInput)
                return render_template("game.html", positionAmount=positionAmount, availableColors=availableColors,
                                       pinlist=results[1], history=history, userColorInput=userColorInput)

        return render_template("game.html", positionAmount=positionAmount, availableColors=availableColors)


if __name__ == '__main__':
    controller = MainController()
    app.run(debug=True)
