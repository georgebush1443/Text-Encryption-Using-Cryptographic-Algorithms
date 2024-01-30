from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.form['data']
    encrypted_data = cipher_suite.encrypt(data.encode()).decode()
    return render_template('result.html', result=encrypted_data)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.form['data']
    decrypted_data = cipher_suite.decrypt(data.encode()).decode()
    return render_template('result.html', result=decrypted_data)

if __name__ == '__main__':
    app.run(debug=True)