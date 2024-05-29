from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    session_data = db.Column(db.Text, nullable=False)


@app.route('/sessions', methods=['POST'])
def get_sessions_by_user_id():
    data = request.json
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    sessions = Session.query.filter_by(user_id=user_id).all()
    sessions_list = [{'id': session.id, 'session_data': session.session_data} for session in sessions]
    return jsonify(sessions_list)


@app.route('/session', methods=['POST'])
def get_session_by_id():
    data = request.json
    session_id = data.get('session_id')
    if not session_id:
        return jsonify({'error': 'session id is needed'}), 400
    session = Session.query.filter_by(id=session_id).first()
    if not session:
        return jsonify({'error': 'Session not found'}), 404
    session_details = {'id': session.id, 'user_id': session.user_id, 'session_data': session.session_data}
    return jsonify(session_details) # return result


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)