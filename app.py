from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', nombre="Bruno")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/reservation")
def reservation():
    return render_template('reservation.html')



if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)