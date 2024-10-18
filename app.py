from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

produtos = []
contador_cod = 0

def enumerarCod():
    global contador_cod
    retornar = contador_cod
    contador_cod += 1
    return retornar

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def cadastrar_produto():
    global produtos
    novo_produto = request.json
    novo_produto['cod'] = enumerarCod()
    novo_produto['quantidade'] = 0
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201

@app.route('/produtos/<int:cod>', methods=['DELETE'])
def remover_produto(cod):
    global produtos
    produtos = [p for p in produtos if p['cod'] != cod]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

