from flask import Flask , render_template, url_for ,request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

#from requests import request

# congifuracion de la base de datos y de flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'
db  = SQLAlchemy(app)

class User(db.Model):# pedir datos empleado
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    describe = db.Column(db.String(200))
    contrasena = db.Column(db.String(200))
    done = db.Column(db.Boolean(200))


class Empleador(db.Model): # datos Empleador 
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200))
    apellido = db.Column(db.String(200))
    describe = db.Column(db.String(200))
    tags = db.Column(db.String(200))
    contrasena = db.Column(db.String(200))
    done = db.Column(db.Boolean(200))



#configuracion inicio y datos para la base de datos

@app.route("/")
def loggin():
    return render_template("loggin.html")


@app.route("/ini")
def inicio():
    tasks = User.query.all()
    return render_template("ini.html",objeto1=tasks) # tasks agrupa tsodas las tareas y muestra 
# corecion del formulario html a la base de datos 



@app.route("/empleador")
def inicio2():
    empleos2 = Empleador.query.all()
    return render_template("empleador.html", objeto2=empleos2)



@app.route('/user', methods=['POST', 'GET']) # metodo post es el metodo de conexion y create task es la ruta 
def user(): # task es el nombre en el que guardamos la tarea
    if request.method == 'POST':
        user = User(nombre=request.form['nombre'],
                    apellido=request.form['apellido'],
                    describe=request.form['describe'],
                    contrasena=request.form['contrasena'],
                    done = False
                )
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('inicio'))
    elif request.method == 'GET':
        id = 4
        user= User.query.get(id)
        print(user)
        return render_template('perfil.html',user = user)




@app.route('/create-empleador', methods=['POST']) # metodo post es el metodo de conexion y create task es la ruta 
def crear_empleo(): # task es el nombre en el que guardamos la tarea
    empleos2 = Empleador(content=request.form['content'],
                apellido=request.form['apellido'],
                describe=request.form['describe'],
                contrasena=request.form['contrasena'],
                done = False
            )
    db.session.add(empleos2)
    db.session.commit()
    return redirect (url_for('inicio2'))



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