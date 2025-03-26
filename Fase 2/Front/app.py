from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predecir')
def predecir():
    return render_template('predicir.html')

@app.route('/prediccionesArchivo')
def predecirArchivo():
    return render_template('predecirArchivo.html')

@app.route('/reentreno')
def reentreno():
    return render_template('reentreno.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)