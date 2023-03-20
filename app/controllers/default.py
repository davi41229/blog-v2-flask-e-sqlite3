from app import app
from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user
from datetime import datetime

from werkzeug.security import generate_password_hash

from app import app,db
from app.models.models import Blogger,Info 





# ROTA  DE APRESENTAÇÃO DO BLOGGER
@app.route('/')
def index():
    posts = Blogger.query.all()
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    date_Time = data_e_hora_em_texto
    return render_template("index.html", posts=posts, date_Time=date_Time)




# -----------------ROTAS NA PARTE ADMINISTRATIVA----------------

# ROTA DO PERFIL DE USUARIO LOGADO
@app.route('/perfil') 
def perfil():
    return render_template('perfil.html')

    
# ROTA ADMINISTRATIVA DE USUARIO
@app.route('/admin')
def admin():
    posts = Blogger.query.all()
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    date_Time = data_e_hora_em_texto
    return render_template("admin.html", posts=posts, date_Time=date_Time)

# ROTA DE CADASTRO DE USUARIO 
@app.route('/register', methods=['GET', 'POST']) # rota para cadastrar usuarios
def register():
    if request.method == 'POST': 
        name = request.form['name'] 
        email = request.form['email'] 
        pwd = request.form['password'] 

        info = Info(name, email, pwd)
        db.session.add(info)
        db.session.commit() 

    return render_template( 'cadastrar.html')


# ROTA LOGIN DE USUARIO CADASTRADO

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST': 
        email = request.form['email']
        pwd = request.form['password']


        info = Info.query.filter_by(email=email).first() 

        if not info or not info.verify_password(pwd): 
            return redirect(url_for('login'))
            
        login_user(info) 
        return redirect(url_for('perfil')) 

    return render_template('login.html') 



# ROTA PARA LOGOUT DE USUARIO
@app.route('/logout') 
def logout():
    logout_user() 
    return redirect(url_for('index')) 


# ROTA COM TODAS AS CONTAS DE USUARIO CADASTRADO
@app.route('/contas') 
def contas():
    contas = Info.query.all()
    return render_template( 'contas.html', contas=contas)


# ROTA DE DELEÇÃO DE CONTA DE USUARIO CADASTRADO
@app.route('/deletar/<int:id>') 
def deletar(id):
    usuario = Info.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('contas'))

# ROTA DE EDIÇÃO DE CONTA DE USUARIO CADASTRADO
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    editar_usuario = Info.query.get(id)
    if request.method == 'POST': 
        editar_usuario.name = request.form['name'] 
        editar_usuario.email = request.form['email']
        editar_usuario.password = generate_password_hash(request.form['password'])
        
        db.session.commit() 
        
        return redirect(url_for('contas'))
    return render_template( 'editar_conta.html', editar_usuario=editar_usuario)



# --------ROTAS PARA MANIPULAÇÃO DOS POSTS--------

# ROTA PARA CRIAÇÃO DE POST 
@app.route('/post/add', methods=["POST"])
def add_post():
    try:        
        form = request.form
        post = Blogger(title=form['title'], content=form['content'], author=form['author'])
        db.session.add(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
        
    return redirect(url_for("admin"))
    


# ROTA DE DELEÇÃO DE POST 
@app.route('/post/<id>/del')
def delete_post(id):
    try:        
        post = Blogger.query.get(id)
        db.session.delete(post)
        db.session.commit()
    except Exception as error:
        print("Error", error)
        
    return redirect(url_for("admin"))
    
# ROTA DE EDIÇÃO DE POST 
@app.route('/post/<id>/edit', methods=["POST", "GET"])
def edit_post(id):
    if request.method == "POST":
        try:
            post = Blogger.query.get(id)        
            form = request.form
            post.title = form["title"]
            post.content = form["content"]
            post.author = form["author"]
            db.session.commit()
        except Exception as error:
            print("Error", error)
            
        return redirect(url_for("admin")) 
    else:
        try:
            post = Blogger.query.get(id)        
            return render_template("edit.html", post=post) 
        except Exception as error:
            print("Error", error)
            
    return redirect(url_for("admin"))

