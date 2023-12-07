import datetime
from werkzeug.security import generate_password_hash
from flask import Flask, jsonify, request, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# configuro l'app Flask
app = Flask(__name__)
# specifico l'url del database sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pazienti.db' # test.db -> Pazienti.db
# disabilito il monitoraggio delle modifiche al database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# definisco il modello paziente
class Paziente(db.Model):
    # Codice_fiscale, nome, cognome, data_di_nascita, username, password, medico
    Codice_fiscale = db.Column(db.String(16), primary_key=True, nullable=False)
    data_di_nascita = db.Column(db.Date, primary_key=True, nullable=False) #(+) primary_key=True (chiave composta codice fiscale e data di nascita)
    nome = db.Column(db.String(50), nullable=False)
    cognome = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(50), nullable=True)
    medico = db.Column(db.String(50), nullable=True)
    
def index():
    # gestisco richieste post per la creazione di nuovi pazienti
    if request.method == 'POST':
        if not _Codice_fiscale or not _nome or not _cognome or not _data_di_nascita: #(+) check sulla presenza dei dati
            return 'Missing required fields. Please fill in all required fields.'

        # _Codice_fiscale, _nome, _cognome, _data_di_nascita, _username, _password, _hashed_password, _medico
        _Codice_fiscale = request.form['codiceFiscale']
        _nome = request.form['nome']
        _cognome = request.form['cognome']
        _data_di_nascita = request.form['dataDiNascita']
        try: #(+) controllo data di nascita valida
            data_di_nascita = datetime.strptime(_data_di_nascita, '%d-%m-%Y').date()
        except ValueError:
            return 'Invalid date format for dataDiNascita. Use DD-MM-YYYY format.'
        _username = request.form['username']
        _password = request.form['password']
        _hashed_password = generate_password_hash(_password, method='sha256') #(+) hash della password
        _medico = request.form['medico']
        
        # creo un nuovo paziente con le informazioni ricevute
        new_paziente = Paziente(
            Codice_fiscale=_Codice_fiscale,
            nome=_nome,
            cognome=_cognome,
            data_di_nascita=_data_di_nascita,
            username=_username,
            password=_hashed_password, #(+) _password -> _hashed_password
            medico=_medico
        )

        # aggiungo il nuovo paziente al database
        try:
            db.session.add(new_paziente)
            db.session.commit()
            return 'Paziente added successfully'
        except Exception as e:
            return f'There was an issue adding the Paziente: {str(e)}'
    else:
        return render_template('index.html', modal_open=False)

# definisco la route principale che reindirizza a index.html
@app.route('/') #(+) index 
def login():
    return render_template('/index.html')

# definisco la route create-item per la creazione di nuovi pazienti mediante richieste POST
@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.json
    new_item = Paziente(**data)
    try: #(+) try & except con controllo errori nel commit e rollback
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'Codice_fiscale': new_item.Codice_fiscale}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# definisco la route /get-item/<string:cf> per ottenere dettagli di un paziente mediante richieste GET 
@app.route('/get-item/<string:cf>', methods=['GET'])
def get_item(cf):
    try: #(+) try & except con controllo errori
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
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Definisco la route /update-item/<string:cf> per aggiornare i dettagli di un paziente tramite richieste PUT
@app.route('/update-item/<string:cf>', methods=['PUT'])
def update_item(cf):
    if request.method != 'PUT': #(+) controllo sul metodo utilizzato
        return jsonify({'error': 'Method not allowed'}), 405
    item = Paziente.query.get(cf)
    if not item:
        return jsonify({'error': 'Item not found'}), 404 # message -> error
    if item:
        data = request.json
        for key, value in data.items():
            setattr(item, key, value)
        try: #(+) try & except con controllo errori nel commit e rollback
            db.session.commit()
            return jsonify({'message': 'Item updated successfully'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

# Definisco la route /delete-item/<string:cf> per l'eliminazione di un paziente tramite richieste DELETE
@app.route('/delete-item/<string:cf>', methods=['DELETE'])
def delete_item(cf):
    item = Paziente.query.get(cf)
    try: #(+) try & except con controllo errori 
        if item:
            try: #(+) try & except con controllo errori
                db.session.delete(item)
                db.session.commit()
                return jsonify({'message': 'Item deleted successfully'})
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': str(e)}), 500 
        return jsonify({'message': 'Item not found'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        # inizializzo il database
        db.create_all()
    # avvio l'app in modalità debug
    app.run(debug=True)


