from flask import Flask

app = Flask(__name__)


@app.route("/")

# yaha se link krna pdega index html ko kisse link krna padegaa? example:
def helo():
    return "Hello Aman"

if __name__ == "__main__":
    app.run()