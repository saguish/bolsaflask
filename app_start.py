from flask import Flask,render_template, json, request, redirect, url_for, jsonify
import os
from datetime import datetime
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
Bootstrap(app)


basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/controledeaplicacoes.json')


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/consultar')
def consultar():

	with open(data_file) as f:
		json_data = f.read()
	return render_template("consultar.html", dados_tabela = json.loads(json_data))

@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
	if request.method == 'GET':
		return render_template("cadastrar.html")
	if request.method == 'POST':
		inputX = request.form.get("inputNota")
		inputAtivo = request.form.get("inputAtivo")
		inputQtd = request.form.get("inputQtd")
		inputData = request.form.get("inputData")
		inputModalidade = request.form.get("inputModalidade")
		inputMercado = request.form.get("inputMercado")
		inputTiopoOp = request.form.get("inputATiopoOp")
		inputPreco = request.form.get("inputPreco")
		inputCorretagem = request.form.get("inputCorretagem")
		inputIss = request.form.get("inputIss")
		inputEmolumentos = request.form.get("inputEmolumentos")
		inputLiquidacao = request.form.get("inputLiquidacao")
		inputCorretora = request.form.get("inputCorretora")

		msg = """
		X: {}
		Ativo: {}
		QTD: {}
		data: {}
		Modalidade: {}
		Mercado: {}
		Tipo: {}
		Preço: {}
		Corretagem: {}
		ISS: {}
		Emolumentos: {}
		Liquidacao: {}
		Corretora: {}
		"""
		return msg.format(inputX,inputAtivo,inputQtd,inputData,inputModalidade,inputMercado,inputTiopoOp,inputPreco,inputCorretagem,inputIss,inputEmolumentos,inputLiquidacao,inputCorretora)

