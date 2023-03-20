## Blogger simples em Flask
<div style="width='30px';heigth='20px'"><img src='https://www.criarsite.online/wp-content/uploads/2017/09/blog.png' alt='imagem blog'</img></div>

## Com Tela Inicial e Administração

## rota principal
- botao login
- loop com todos os Posts
- rodape 
- navbar

## rota de cadastro
- cadastrar: nome, email, senha

## rota de login
- login: email, senha

## rota de Admin
- postar
- editar 
- deletar: titulo, autor, conteudo


## tecnologias
- python3.10.8 
- flask
- sqlite3
- html5 
- css 
- bootstrap5 


## banco ==> sqlite3
- nome: storage.db


## para criar ambiente virtual
* python -m venv environment
## para ativar ambiente
* cd environment\scripts\activate
## para instalar as bibliotecas
* pip install -r requirements.txt
## para salvar as dependencias
* pip freeze> requirements.txt


## bibliotecas

- pip install flask==2.2.2
- pip install Flask-SQLAlchemy==2.5.0
- pip install sqlalchemy-connector==0.1.37
- pip install SQLAlchemy==1.4.9


## rodar

´´´
python main.py

´´´



* exemplo  de tabela com data e hora 

´´´
CREATE TABLE venda (
  idVenda SMALLINT PRIMARY KEY AUTO_INCREMENT,
  horaVenda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  dataEntrega DATE,
  horaEntrega TIME
);    

´´´
