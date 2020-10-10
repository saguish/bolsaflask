from flask import Flask,render_template, json, request, redirect, url_for, jsonify
import os
from datetime import datetime
from flask_bootstrap import Bootstrap

import database.tradeDAO
from model.trade import Trade 

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

	# with open(data_file) as f:
	# 	json_data = f.read()
	# 	json_objects = json.loads(json_data)

	# 	for obj in json_objects:
	# 		trade_obj = Trade(obj)
	# 		database.tradeDAO.insert(trade_obj)
	# 		print("objeto inserido")
	dados = database.tradeDAO.read_all()
	print(dados)

	return render_template("consultar.html", dados_tabela = json.loads(dados))

@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
	if request.method == 'GET':
		return render_template("cadastrar.html")
	if request.method == 'POST':
		form_json = json.dumps(request.form)
		trade_obj = Trade(form_json)
		database.tradeDAO.insert(trade_obj)
		return redirect(url_for('index'))

