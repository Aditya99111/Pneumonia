from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/result')
def get_result():
    result = random.choice(['positive', 'negative'])
    assurance = random.uniform(0.6, 1)
    return jsonify({'result': result, 'assurance': assurance})

if __name__ == '__main__':
    app.run(debug=True)