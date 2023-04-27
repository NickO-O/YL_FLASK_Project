import random

from flask import Flask, request, render_template, redirect
import os
import datetime
from data import db_session
from data.cosmodrome import Cosmodrome
from data.tickets import Ticket
app = Flask(__name__)


@app.route('/')
def sample_file_upload():
    if request.method == 'GET':
        return render_template('menu.html')

@app.route('/mars_tickets')
def mars_tickets():
    arrive1 = ['baikonur', 'plesetsk', 'vostochny', '']
    arrive = ['Байконур', 'Плесецк', 'Восточный', 'Мыс Канаверал', 'Космодром Куру']
    departure = ['Олимп', 'Впадина Эллада', 'Долина Маринер']
    return render_template('mars_tickets.html')


@app.route('/titan_tickets')
def titan_tickets():
    return render_template('titan_tickets.html')


@app.route('/moon_tickets')
def moon_tickets():
    return render_template('moon_tickets.html')


@app.route('/ticketsToMars', methods=['POST', 'GET'])
def ticketsToMars():
    if request.method == 'GET':
        arrive1 = ['baikonur', 'plesetsk', 'vostochny', '']
        arrive = ['Байконур', 'Плесецк', 'Восточный', 'Мыс Канаверал', 'Космодром Куру']
        departure = ['Олимп', 'Впадина Эллада', 'Долина Маринер', 'Кратер Гейл']
        return render_template('tickets.html', arrive=arrive, departure=departure, name='Марс')
    elif request.method == 'POST':
        s = [request.form['id'], request.form['start'], request.form['finish'], request.form['date'], request.form['price']]
        return str(s)
        if not all(s):
            return render_template('smthWrong.html', message='Не хватает параметров')
        db = db_session.create_session()
        a = [i for i in db.query(Ticket).all()]
        d = []
        for i in a:
            if [i.id, i.price, i.finish, i.date, i.price] == s[:-1]:
                d.append({'id': i.id, 'start': i.start, 'finish': i.finish, 'date': i.date, 'price': i.price})
        return render_template('find_tickets.html', tickets=d)



@app.route('/ticketsToTitan', methods=['POST', 'GET'])
def ticketsToTitan():
    if request.method == 'GET':
        arrive1 = ['baikonur', 'plesetsk', 'vostochny']
        arrive = ['Байконур', 'Плесецк', 'Восточный', 'Мыс Канаверал', 'Космодром Куру']
        departure = ['Море Кракена', 'Море Пунги', 'Лабиринт Эказ']
        return render_template('tickets.html', arrive=arrive, departure=departure, name='Титан')
    elif request.method == 'POST':
        s = [request.form['id'], request.form['start'], request.form['finish'], request.form['date'],
             request.form['price']]
        if not all(s):
            return render_template('smthWrong.html', message='Не хватает параметров')
        if request.form['arrival'] == request.form['departure']:
            return render_template('smthWrong.html')


@app.route('/ticketsToMoon', methods=['POST', 'GET'])
def ticketsToMoon():
    if request.method == 'GET':
        arrive1 = ['baikonur', 'plesetsk', 'vostochny', '']
        arrive = ['Байконур', 'Плесецк', 'Восточный', 'Мыс Канаверал', 'Космодром Куру']
        departure = ['Пик Гюйгенса', 'Море Москвы', 'Кратер Королёв', 'Кратер Пастера']
        return render_template('tickets.html', arrive=arrive, departure=departure, name='Луну')
    elif request.method == 'POST':
        s = [request.form['id'], request.form['start'], request.form['finish'], request.form['date'],
             request.form['price']]
        if not all(s):
            return render_template('smthWrong.html', message='Не хватает параметров')
        if request.form['arrival'] == request.form['departure']:
            return render_template('smthWrong.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.errorhandler(400)
def error400(e):
    return render_template('error.html',
                           code=400,
                           mess="неправильный, некорректный запрос")


@app.errorhandler(401)
def error401(e):
    return render_template('error.html',
                           code=401,
                           mess="не авторизован (не представился)")


@app.errorhandler(403)
def error403(e):
    return render_template('error.html',
                           code=403,
                           mess="запрещено (не уполномочен)")


@app.errorhandler(404)
def error404(e):
    return render_template('error.html',
                           code=404,
                           mess="не найдено")


@app.errorhandler(405)
def error405(e):
    return render_template('error.html',
                           code=405,
                           mess="метод не поддерживается")


@app.errorhandler(406)
def error406(e):
    return render_template('error.html',
                           code=406,
                           mess="неприемлемо")


@app.errorhandler(408)
def error408():
    return render_template('error.html',
                           code=408,
                           mess="истекло время ожидания")


@app.errorhandler(409)
def error409(e):
    return render_template('error.html',
                           code=409,
                           mess="конфликт")


@app.errorhandler(410)
def error410(e):
    return render_template('error.html',
                           code=410,
                           mess="удалён")


@app.errorhandler(411)
def error411(e):
    return render_template('error.html',
                           code=411,
                           mess="необходима длина")


@app.errorhandler(412)
def error412(e):
    return render_template('error.html',
                           code=412,
                           mess="условие ложно")


@app.errorhandler(413)
def error413(e):
    return render_template('error.html',
                           code=413,
                           mess="полезная нагрузка слишком велика")


@app.errorhandler(414)
def error414(e):
    return render_template('error.html',
                           code=414,
                           mess="URI слишком длинный")


@app.errorhandler(415)
def error415(e):
    return render_template('error.html',
                           code=415,
                           mess="неподдерживаемый тип данных")


@app.errorhandler(416)
def error416(e):
    return render_template('error.html',
                           code=416,
                           mess="диапазон не достижим")


@app.errorhandler(417)
def error417(e):
    return render_template('error.html',
                           code=417,
                           mess="ожидание не удалось")


@app.errorhandler(418)
def error418(e):
    return render_template('error.html',
                           code=418,
                           mess="я — чайник")


@app.errorhandler(422)
def error422(e):
    return render_template('error.html',
                           code=422,
                           mess="необрабатываемый экземпляр")


@app.errorhandler(423)
def error423(e):
    return render_template('error.html',
                           code=423,
                           mess="заблокировано")


@app.errorhandler(424)
def error424(e):
    return render_template('error.html',
                           code=424,
                           mess="невыполненная зависимость")


@app.errorhandler(428)
def error428(e):
    return render_template('error.html',
                           code=428,
                           mess="необходимо предусловие")


@app.errorhandler(429)
def error429(e):
    return render_template('error.html',
                           code=429,
                           mess="слишком много запросов")


@app.errorhandler(431)
def error431(e):
    return render_template('error.html',
                           code=431,
                           mess="поля заголовка запроса слишком большие")


@app.errorhandler(451)
def error451(e):
    return render_template('error.html',
                           code=451,
                           mess="недоступно по юридическим причинам")


@app.errorhandler(500)
def error500(e):
    return render_template('error.html',
                           code=500,
                           mess="внутренняя ошибка сервера")


@app.errorhandler(501)
def error501(e):
    return render_template('error.html',
                           code=501,
                           mess="не реализовано")


@app.errorhandler(502)
def error502(e):
    return render_template('error.html',
                           code=502,
                           mess="плохой, ошибочный шлюз")


@app.errorhandler(503)
def error503(e):
    return render_template('error.html',
                           code=503,
                           mess="сервис недоступен")


@app.errorhandler(504)
def error504(e):
    return render_template('error.html',
                           code=504,
                           mess="шлюз не отвечает")


@app.errorhandler(505)
def error505(e):
    return render_template('error.html',
                           code=505,
                           mess="версия HTTP не поддерживается")


def find_tickets():
    pass

def fill_rand_tickets():
    db = db_session.create_session()
    mindate = datetime.date.fromisoformat('2023-09-09')
    maxdate = datetime.date.fromisoformat('2025-09-09')
    s = db.query(Cosmodrome).all()

    s = [(i.id, i.planet_id) for i in db.query(Cosmodrome).all()]
    s1 = [(i.id, i.planet_id) for i in db.query(Cosmodrome).filter(Cosmodrome.planet_id == 0)]
    print(s1)
    for i in range(10 ** 5):
        tik = Ticket()
        tik.id = i
        tik.date = f'{random.randint(2024, 2026)}-{str(random.randint(1, 12)).rjust(2, "0")}-{str(random.randint(1, 12)).rjust(2, "0")}'
        fir = random.choice(s1)
        tik.start = fir[0]
        while True:
            sec = random.choice(s)
            if sec[1] != fir[1]:
                break

        tik.finish = sec[0]
        if (sec[1] == 1):
            tik.price = random.randint(50000, 100000)
        elif (sec[1] == 2):
            tik.price = random.randint(150000, 200000)
        elif (sec[1] == 3):
            tik.price = random.randint(100000, 150000)
        db.add(tik)
    db.commit()
    db.close()


if __name__ == '__main__':
    db_session.global_init('db/data.db')

    app.run(port=5000, host='127.0.0.1')