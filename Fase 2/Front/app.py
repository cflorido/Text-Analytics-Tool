from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)