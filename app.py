from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# configuro l'app Flask
app = Flask(__name__)
# specifico l'url del database sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pazienti.db' # test.db -> Pazienti.db
# disabilito il monitoraggio delle modifiche al database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# definisco il modello paziente
class Paziente(db.Model):
    CodiceFiscale = db.Column(db.String(16), primary_key=True, nullable=False, default='XXX-XXX-00-X-00-X-00-0-X')
    DataDiNascita = db.Column(db.String, primary_key=True, nullable=False, default='00-00-0000') #(+) primary_key=True (chiave composta codice fiscale e data di nascita)
    Nome = db.Column(db.String(50), nullable=False)
    Cognome = db.Column(db.String(50), nullable=False)
    Username = db.Column(db.String(50), nullable=True)
    Password = db.Column(db.String(50), nullable=True)
    Medico = db.Column(db.String(50), nullable=True)
    
@app.route('/', methods=['POST','GET'])
def index():

    # gestisco richieste post per la creazione di nuovi pazienti
    if request.method == 'POST':

        print(request.get_json)

        _CodiceFiscale = request.form['CodiceFiscale']
        _DataDiNascita = request.form['DataDiNascita']
        _Nome = request.form['Nome']
        _Cognome = request.form['Cognome']
        _Username = request.form['Username']
        _Password = request.form['Password']
        _Medico = request.form['Medico']

        # creo un nuovo paziente con le informazioni ricevute
        newPaziente = Paziente(
            CodiceFiscale=_CodiceFiscale,
            DataDiNascita=_DataDiNascita,
            Nome=_Nome,
            Cognome=_Cognome,
            Username=_Username,
            Password=_Password,
            Medico=_Medico
        )

        # aggiungo il nuovo paziente al database
        try:
            db.session.add(newPaziente)
            db.session.commit()
            return 'Paziente added successfully'
        except Exception as e:
            return f'There was an issue adding the Paziente: {str(e)}'
    else:
        return render_template('index.html', modal_open=False)
    
"""
# definisco la route create-item per la creazione di nuovi pazienti mediante richieste POST
@app.route('/create-item', methods=['POST'])
def create_item():
    data = request.json
    new_item = Paziente(**data)
    try: #(+) try & except con controllo errori nel commit e rollback
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'CodiceFiscale': new_item.Codice_fiscale}), 201
    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({'error': str(e)}), 500

# definisco la route /get-item/<string:cf> per ottenere dettagli di un paziente mediante richieste GET 
@app.route('/get-item/<string:cf>', methods=['GET'])
def get_item(cf):
    try: #(+) try & except con controllo errori
        item = Paziente.query.get(cf)
        if item:
            return jsonify({
                'CodiceFiscale': item.CodiceFiscale,
                'Nome': item.Nome,
                'Cognome': item.Cognome,
                'DataDiNascita': str(item.DataDiNascita),
                'Username': item.Username,
                'Password': item.Password,
                'Medico': item.Medico
            })
        return jsonify({'error': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Definisco la route /update-item/<string:cf> per aggiornare i dettagli di un paziente tramite richieste PUT
@app.route('/update-item/<string:cf>', methods=['PUT'])
def update_item(cf):
    if request.method != 'PUT': #(+) controllo sul metodo utilizzato
        return jsonify({'error': 'Method not allowed'}), 405
    item = Paziente.query.get(cf)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
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
"""

if __name__ == '__main__':
    with app.app_context():
        # inizializzo il database
        db.create_all()
    # avvio l'app in modalità debug
    app.run(debug=True)


