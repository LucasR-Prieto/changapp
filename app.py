from flask import Flask , render_template, url_for ,request , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

#from requests import request

# congifuracion de la base de datos y de flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/changapp.db'
db  = SQLAlchemy(app)

class usuario(db.Model):# pedir datos usuario
    usuario_id = db.Column(db.Integer,primary_key=True)
    usuario_nombre = db.Column(db.String(200))
    usuario_apellido = db.Column(db.String(200))
    usuario_desc = db.Column(db.String(200))
    usuario_email = db.Column(db.String(200))
    usuario_pass = db.Column(db.String(200))
    usuario_done = db.Column(db.Boolean(200))


class empleo(db.Model): # datos empleo 
    empleo_id = db.Column(db.Integer,primary_key=True)
    empleo_nombre = db.Column(db.String(200))
    empleo_desc = db.Column(db.String(200))
    empleo_precio = db.Column(db.String(200))
    empleo_done = db.Column(db.Boolean(200))



#configuracion inicio y datos para la base de datos

@app.route("/")
def loggin():
    return render_template("loggin.html")


@app.route("/registro")
def inicio():
    #Usuario = usuario.query.all()
    return render_template("registro.html")#,Usuario=Usuario) # Usuario agrupa todas las tablas y muestra correcion del formulario html a la base de datos 



@app.route("/empleo")
def empleos():
    Empleo = empleo.query.all()
    return render_template("empleo.html", Empleo=Empleo)



@app.route('/usuario', methods=['POST', 'GET']) # metodo post y get 
def usuarios(): 
    if request.method == 'POST':
        Usuario = usuario(usuario_nombre=request.form['nombre'],
                    usuario_apellido=request.form['apellido'],
                    usuario_desc=request.form['descripcion'],
                    usuario_email=request.form['email'],
                    usuario_pass=request.form['password'],
                    usuario_done = False
                )
        db.session.add(Usuario)
        db.session.commit()
        return redirect (url_for('usuarios'))
    elif request.method == 'GET':
        id = 1
        Usuario= usuario.query.get(id)
        print(Usuario)
        return render_template('perfil.html',Usuario = Usuario)




@app.route('/nuevo_empleo', methods=['POST']) 
def crear_empleo():
    Empleo = empleo(nombre_empleo=request.form['empleo_nombre'],
                descripcion=request.form['empleo_desc'],
                precio=request.form['empleo_precio'],
                done = False
            )
    db.session.add(Empleo)
    db.session.commit()
    return redirect (url_for('empleos'))



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