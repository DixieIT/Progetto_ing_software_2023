from flask import Flask, jsonify, request, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Paziente(db.Model):
    Codice_fiscale = db.Column(db.String(16), primary_key=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    data_di_nascita = db.Column(db.Date, nullable=False)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    medico = db.Column(db.String(50), nullable=True)
    
def index():
    if request.method == 'POST':
        _Codice_fiscale = request.form['codiceFiscale']
        _nome = request.form['nome']
        _cognome = request.form['cognome']
        _data_di_nascita = request.form['dataDiNascita']
        _username = request.form['username']
        _password = request.form['password']
        _medico = request.form['medico']
        
        new_paziente = Paziente(
            Codice_fiscale=_Codice_fiscale,
            nome=_nome,
            cognome=_cognome,
            data_di_nascita=_data_di_nascita,
            username=_username,
            password=_password,
            medico=_medico
        )

        try:
            db.session.add(new_paziente)
            db.session.commit()
            return 'Paziente added successfully'
        except Exception as e:
            return f'There was an issue adding the Paziente: {str(e)}'
    else:
        return render_template('index.html', modal_open=False)

@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.json
    new_item = Paziente(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'Codice_fiscale': new_item.Codice_fiscale}), 201  # 201 Created status code

@app.route('/get-item/<string:cf>', methods=['GET'])
def get_item(cf):
    item = Paziente.query.get(cf)
    if item:
        return jsonify({
            'Codice_fiscale': item.Codice_fiscale,
            'nome': item.nome,
            'cognome': item.cognome,
            'data_di_nascita': str(item.data_di_nascita),
            'username': item.username,
            'password': item.password,
            'medico': item.medico
        })
    return jsonify({'message': 'Item not found'}), 404

@app.route('/update-item/<string:cf>', methods=['PUT'])
def update_item(cf):
    item = Paziente.query.get(cf)
    if item:
        data = request.json
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify({'message': 'Item updated successfully'})
    return jsonify({'message': 'Item not found'}), 404

@app.route('/delete-item/<string:cf>', methods=['DELETE'])
def delete_item(cf):
    item = Paziente.query.get(cf)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


