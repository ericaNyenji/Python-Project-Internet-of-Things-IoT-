from flask import Flask, render_template, request
import main  # Import your main.py
import gui    # Import your gui.py (if needed)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run')
def run_code():
    # Assuming your main.py has a function named `execute()` to run the logic
    result = main.execute()  # Replace with your function
    return result

if __name__ == '__main__':
    app.run(debug=True)
