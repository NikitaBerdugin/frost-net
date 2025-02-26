import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from data import users
from data import db_session
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
app.config.from_object(__name__)
db_session.global_init("db/profile.sqlite")
# Загружаем конфиг по умолчанию и переопределяем в конфигурации часть
# значений через переменную окружения
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

class RegistrationForm(Form):
    username = StringField('имя', [validators.Length(min=4, max=25)])
    email = StringField('почта', [validators.Length(min=6, max=35)])
    password = PasswordField('пароль', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ])
    confirm = PasswordField('Повторите пароль')
    accept_tos = BooleanField('Я принимаю TOS', [validators.DataRequired()])

@app.route('/regist', methods=['GET', 'POST'])
def regi():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = users.User(username=form.username.data, email=form.email.data,
                    password=form.password.data)
        sessio = db_session.create_session()
        sessio.add(user)
        sessio.commit()
        flash('спасибо за регистрацию')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def connect_db():
    #Соединяет с указанной базой данных.
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    #Если ещё нет соединения с базой данных, открыть новое - для текущего контекста приложения
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                [request.form['title'], request.form['text']])
    db.commit()
    flash('Новая запись была успешно размещена')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    sessio = db_session.create_session()
    if request.method == 'POST':
        if sessio.query(users.User).filter(users.User.username == request.form['username']).first():
                    if sessio.query(users.User).filter(users.User.password == request.form['password']).first():
                        session['logged_in'] = True
                        flash('вы вошли в систему') 
                        return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('вы вышли из системы')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)