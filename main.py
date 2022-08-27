from email import message
from multiprocessing.dummy import Manager
from turtle import title
from flask import Flask, render_template # вытащил объект
from auth import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'world world world hello'



@app.route('/', methods =['GET', 'POST']) # Создание главной страницы - декоратор через @
def main():
     form = LoginForm()
     if form.validate_on_submit():
          name = form.name.data
          surname = form.surname.data
          email = form.email.data
          print(name,surname,email)
          return render_template('authorisation.html', title = 'Авторизация', 
                              message ='Вы авторизовались')
     return render_template('authorisation.html', title = 'Авторизация', 
                              form = form)
@app.route('/base')
def base():
     return render_template('base.html', title ='Главная')     

@app.route('/myplans') # Создание главной страницы - декоратор через @
def plan():
     return render_template('myplans.html', title = 'Планы')

@app.route('/aboutme') # Создание главной страницы - декоратор через @
def about():
     return render_template('aboutme.html', title = 'Обо мне')

if __name__ == '__name__':
     app.run()

app.run()     