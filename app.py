from flask import Flask, request, jsonify
from models.event import Event
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbdiet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/event', methods=['POST'])
def add_event():
    data = request.get_json()

    
    data_hora_str = data.get('data_hora')
    try:
        data_hora_obj = datetime.strptime(data_hora_str, '%d-%m-%Y %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Formato de data_hora inválido. Use o formato DD-MM-YYYY HH:MM:SS'}), 400

    
    esta_na_dieta_str = data.get('esta_na_dieta', '').lower() 
    if esta_na_dieta_str == 'true':
        esta_na_dieta = True
    elif esta_na_dieta_str == 'false':
        esta_na_dieta = False
    else:
        return jsonify({'error': 'Valor inválido para o campo esta_na_dieta. Use "true" ou "false".'}), 400

    
    new_event = Event(
        nome=data.get('nome'),
        descricao=data.get('descricao'),
        data_hora=data_hora_obj,
        esta_na_dieta=esta_na_dieta
    )

    
    db.session.add(new_event)
    db.session.commit()

    return jsonify({'message': 'Evento criado com sucesso!'}), 201

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
