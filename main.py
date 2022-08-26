from turtle import title
from flask import Flask, render_template # вытащил объект

app = Flask(__name__)


@app.route('/') # Создание главной страницы - декоратор через @
def main():
     return render_template('base.html', title = 'Главная страница')

@app.route('/myplans') # Создание главной страницы - декоратор через @
def plan():
     return render_template('myplans.html', title = 'Планы')

@app.route('/aboutme') # Создание главной страницы - декоратор через @
def about():
     return render_template('aboutme.html', title = 'Обо мне')

if __name__ == '__name__':
     app.run()

app.run()     