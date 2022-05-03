
from flask import Flask , render_template, url_for ,request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true


# congifuracion de la base de datos y de flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/changapp.db'
db  = SQLAlchemy(app)

class User(db.Model):# pedir datos usuario
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(200))
    user_last_name = db.Column(db.String(200))
    user_desc = db.Column(db.String(200))
    user_email = db.Column(db.String(200))
    user_pass = db.Column(db.String(200))
    user_done = db.Column(db.Boolean(200))


class Job(db.Model): # datos empleo 
    job_id = db.Column(db.Integer,primary_key=True)
    job_name = db.Column(db.String(200))
    job_desc = db.Column(db.String(200))
    job_price = db.Column(db.String(200))
    job_done = db.Column(db.Boolean(200))


#configuracion inicio y datos para la base de datos
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register(): 
    if request.method == 'POST':
        user = User(
            user_name=request.form['name'],
            user_last_name=request.form['last_name'],
            user_desc=request.form['desc'],
            user_email=request.form['email'],
            user_pass=request.form['password'],
            user_done = False
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/create-job', methods=['POST']) 
def create_job():
    job = Job(
        job_name=request.form['job_name'],
        job_desc=request.form['job_desc'],
        job_price=request.form['job_price'],
        job_done = False
    )
    db.session.add(job)
    db.session.commit()
    return redirect (url_for('index'))



#eliminar datos 
# @app.route("/delete/<id>")
# def delete(id):
#     task = User.query.filter_by(id=int(id)).delete()
#     db.session.commit()
#     return redirect (url_for('inicio'))

# @app.route("/delete_empleo/<id>")
# def delete_empleo(id):
#     empleo2 = Empleador.query.filter_by(id=int(id)).delete()
#     db.session.commit()
#     return redirect (url_for('inicio2'))


if __name__ == "__main__":
    app.run(debug=True)