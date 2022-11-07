from clickart_forms import db # importação do arquivo app_tarefas.py

class Artista(db.Model):
    __tablename__ = 'artista'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    sexo = db.Column(db.String(45), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    biografia_resumo = db.Column(db.String(800), nullable=False)
    curriculum = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.sexo} - {self.email}'

class Telefone(db.Model):
    __tablename__ = 'telefone'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(45), nullable=False)

    def __str__(self):
        return f'{self.id} - {self.numero}'

class Arquivo(db.Model):
    __tablename__ = 'arquivo'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(45), nullable=False)
    links = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.id} - {self.tipo} - {self.descricao}'