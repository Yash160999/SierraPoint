from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    exe_file_path = 'prototype_v2_0.exe'

    return send_file(exe_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
