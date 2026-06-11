from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []

@app.route('/')
def home():
    return jsonify({"mensagem": "Olá, mundo!", "status": "ok"})

@app.route('/usuario/<int:id>')
def get_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuario/<int:id>/perfil')
def get_perfil(id):
    return jsonify({"id": id, "perfil": "público"})

@app.route('/usuario', methods=['POST'])
def criar_usuario():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({"erro": "Campo 'nome' obrigatório"}), 400

    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": dados['nome'],
        "email": dados.get('email', '')
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

if __name__ == '__main__':
    app.run(debug=True)