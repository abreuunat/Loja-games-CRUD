from app import app
from flask import render_template, request, redirect, url_for
from app.service.compra_service import CompraService
from app.service.jogo_service import JogoService
from app.models.compra_model import CompraModel
from app.models.jogo_model import JogoModel

compra_service = CompraService()
jogo_service = JogoService()

@app.route('/')
def index():
    jogos = jogo_service.get_all_jogos()
    return render_template('jogos/lista.html', jogos=jogos)

# =========================
# Rotas Jogo
# =========================
@app.route('/jogos')
def listar_jogos():
    jogos = jogo_service.get_all_jogos()
    return render_template('jogos/lista.html', jogos=jogos)

@app.route('/jogos/novo', methods=['GET', 'POST'])
def criar_jogo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        plataforma = request.form['plataforma']
        preco = float(request.form['preco'])
        jogo_service.create_jogo(JogoModel(
            id=None,
            titulo=titulo,
            genero=genero,
            plataforma=plataforma,
            preco=preco
        ))
        return redirect(url_for('listar_jogos'))
    return render_template('jogos/formulario.html')

@app.route('/jogos/editar/<int:id>', methods=['GET', 'POST'])
def editar_jogo(id):
    jogo = jogo_service.get_jogo_by_id(id)
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        plataforma = request.form['plataforma']
        preco = float(request.form['preco'])
        jogo_service.update_jogo(JogoModel(
            id=id,
            titulo=titulo,
            genero=genero,
            plataforma=plataforma,
            preco=preco
        ))
        return redirect(url_for('listar_jogos'))
    return render_template('jogos/formulario.html', jogo=jogo)

@app.route('/jogos/excluir/<int:id>')
def excluir_jogo(id):
    jogo_service.delete_jogo(id)
    return redirect(url_for('listar_jogos'))

# =========================
# Rotas Compra
# =========================
@app.route('/compras')
def listar_compras():
    compras = compra_service.get_all_compras()
    return render_template('compras/lista.html', compras=compras)

@app.route('/compras/nova', methods=['GET', 'POST'])
def criar_compra():
    jogos = jogo_service.get_all_jogos()
    if request.method == 'POST':
        data_compra = request.form['data_compra']
        cliente_nome = request.form['cliente_nome']  # Corrigido de clinete_nome para cliente_nome
        jogo_id = request.form['jogo_id']

        compra_service.create_compra(CompraModel(
            id=None,
            data_compra=data_compra,
            cliente_nome=cliente_nome,
            jogo_id=jogo_id
        ))
        return redirect(url_for('listar_compras'))
    return render_template('compras/formulario.html', jogos=jogos)

@app.route('/compras/editar/<int:id>', methods=['GET', 'POST'])
def editar_compra(id):
    compra = compra_service.get_compra_by_id(id)
    jogos = jogo_service.get_all_jogos()
    if request.method == 'POST':
        data_compra = request.form['data_compra']
        cliente_nome = request.form['cliente_nome']
        jogo_id = request.form['jogo_id']
        compra_service.update_compra(CompraModel(
            id=id,
            data_compra=data_compra,
            cliente_nome=cliente_nome,
            jogo_id=jogo_id
        ))
        return redirect(url_for('listar_compras'))
    return render_template('compras/formulario.html', compra=compra, jogos=jogos)

@app.route('/compras/excluir/<int:id>')
def excluir_compra(id):
    compra_service.delete_compra(id)
    return redirect(url_for('listar_compras'))
