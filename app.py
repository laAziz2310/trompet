from flask import Flask, render_template

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
