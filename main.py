import MySQLdb
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_mysqldb import MySQL
from config import *


app = Flask(__name__)
socketio = SocketIO(app)

app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_HOST"] = MYSQL_HOST
app.config["MYSQL_PORT"] = MYSQL_PORT

mysql = MySQL(app)


@app.route('/')
def main():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES;")
    if not cur.fetchall():
        cur.execute("CREATE TABLE messages (ID int NOT NULL AUTO_INCREMENT, date varchar(30), message text, "
                    "PRIMARY KEY (ID));")
        mysql.connection.commit()
        return render_template('index.html')
    else:
        cur.execute("SELECT `date`, `message` FROM `messages`;")
        data = cur.fetchall()
        return render_template('index.html', data=data)


@socketio.on('message')
def handle_message(data):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `messages`(`date`, `message`) VALUES ('" + data.split(' : ')[0] + "','" +
                data.split(' : ')[1] + "');")
    mysql.connection.commit()
    send(data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, port=80)
