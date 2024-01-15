
from flask import Flask, render_template, request, jsonify  # importing necessary modules

app = Flask(__name__)  # creating a Flask web server

# route for the home page
@app.route('/')
def index():
    return render_template('Calculator Web Template.html')  # render the calculator web template

# route for calculating the expression
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # get the result from the request json
        result = request.json.get('result')
        # return the result as json
        return jsonify({'result': result})
    except Exception as e:
        # if there is an error, return the error message as json
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)  # run the web server in debug mode