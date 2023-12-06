from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Paziente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    data_di_nascita = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    medico = db.Column(db.String(50), nullable=True)

@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.json
    new_item = Paziente(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id}), 201  # 201 Created status code

@app.route('/get-item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Paziente.query.get(item_id)
    if item:
        return jsonify({
            'id': item.id,
            'nome': item.nome,
            'cognome': item.cognome,
            'data_di_nascita': str(item.data_di_nascita),
            'username': item.username,
            'password': item.password,
            'medico': item.medico
        })
    return jsonify({'message': 'Item not found'}), 404

@app.route('/update-item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Paziente.query.get(item_id)
    if item:
        data = request.json
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify({'message': 'Item updated successfully'})
    return jsonify({'message': 'Item not found'}), 404

@app.route('/delete-item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Paziente.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
