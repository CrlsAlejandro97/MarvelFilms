import requests
from flask import Flask, render_template, request, redirect, flash, session

app = Flask (__name__)
app.secret_key = "131543871l"

@app.route('/')
def index():
    return "Hola, estoy en el servidor"


if __name__ == '__main__':
    app.run(port=3000, debug=True)