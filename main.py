from flask import Flask, request, jsonify
from app.email_service import send_email

app = Flask(__name__)


@app.route('/send_email', methods=['POST'])
def send_email_endpoint():
    data = request.get_json()
    to_email = data.get('to')
    cc_email = data.get('cc')
    body = data.get('body')

    # Additional information you can add to the email body.
    extra_info = data.get('extra_info', '')

    if not to_email or not body:
        return jsonify({'error': 'Missing required parameters'}), 400

    result = send_email(to_email, cc_email, body, extra_info)
    return jsonify({'message': 'Email sent successfully', 'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
