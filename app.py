from flask import Flask
from flask import request
from scrap import bazar_search
app = Flask(__name__)

@app.route('/api/offers', methods=["GET"])
def offer():
    game = request.args.get('game')
    response = app.response_class(
        response=bazar_search(game),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run()