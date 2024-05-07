from flask import Flask, jsonify
import jwt
import datetime
import uuid

app = Flask(__name__)

@app.route('/token', methods=['GET'])
def generate_token():
    user = 'slawek.potasz@vumo.ai'

    token = jwt.encode(
        {
            "iss": '5a16644c-fdc5-4af8-976a-ce8bbd799471',
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": user,
            "scp": ["tableau:views:embed", "tableau:metrics:embed"]
        },
        'VQMUbmz73LMO/m/ULzf7rfcTRX/a64TuTk49OERz4Qs=',
        algorithm="HS256",
        headers={
            'kid': '45aab1cc-4f5f-4ddb-b101-ff77ce128464',
            'iss': '5a16644c-fdc5-4af8-976a-ce8bbd799471'
        }
    )

    return jsonify({'token': token}), 200

if __name__ == '__main__':
    app.run(debug=True)
