from flask import Flask, render_template, jsonify
app = Flask(__name__)

# Home route rendering the HTML template
@app.route('/')
def home():
    return render_template('index.html')

# Example API route returning JSON
@app.route('/api/data')
def get_data():
    return jsonify({"message": "Сообщение получено!"})

if __name__ == '__main__':
    app.run(debug=True)
