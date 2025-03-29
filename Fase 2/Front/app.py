from flask import Flask, jsonify, render_template, request, send_from_directory
import pandas as pd
import requests

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000"

#------------Front------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clasificar')
def clasificar():
    return render_template('clasificar.html')

@app.route('/clasificarArchivo')
def clasificarArchivo():
    return render_template('clasificarArchivo.html')

@app.route('/reentreno')
def reentreno():
    return render_template('reentreno.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

#----------Interacción con el API-----------

@app.route('/clasificarEnvio', methods=["POST"])
def clasificarEnvio():
    titulo = request.form.get("titulo")
    cuerpo = request.form.get("cuerpo")
    
    payload = {"Titulo": titulo, "Descripcion": cuerpo, "Fecha": "2025-03-28"}  
    try:
        response = requests.post(f"{API_URL}/predict/", json=payload)
        response.raise_for_status()  
        result = response.json()
        clasificacion = "Verdadero" if result["prediction"] == 1 else "Falso"
        probabilidades = result.get("probabilidades", [0, 0])
        response_dict = {
            "titulo": titulo,
            "cuerpo": cuerpo,
            "clasificacion": clasificacion,
            "ProbVerdadera": probabilidades[1],
            "ProbFalsa": probabilidades[0]
        }
    except requests.exceptions.RequestException:
        response_dict = {"error": "No se pudo conectar con la API"}

    return render_template('clasificar.html', results=response_dict)

def validar_archivo(file):
    """Verifica si el archivo es válido (CSV no vacío)"""
    if 'file' not in request.files:
        return "No ha enviado el archivo"
    if file.filename == '':
        return "No ha seleccionado un archivo"
    if not file.filename.lower().endswith('.csv'):
        return "Solo se permiten archivos de tipo CSV"
    return None 

@app.route('/clasificarEnvioArchivo', methods=["POST"])
def clasificarEnvioArchivo():
    file = request.files.get('file')
    error = validar_archivo(file)
    if error:
        return jsonify({"error": error}), 400

    try:
        df = pd.read_csv(file, sep=";")
        df["Fecha"] = df.get("Fecha", pd.Timestamp.today().strftime("%d/%m/%Y"))  

        noticias = df.to_dict(orient="records")
        response = requests.post(f"{API_URL}/predictMany", json=noticias)
        response.raise_for_status()
        resultados = response.json()
        response_list = []

        for i, item in enumerate(noticias):
            clasificacion = "Verdadero" if resultados["predictions"][i] == 1 else "Falso"
            probabilidades = resultados["probabilidades"][i]
            response_list.append({
                "titulo": item.get("Titulo", "Sin título"),
                "cuerpo": item.get("Descripcion", "Sin descripción"),
                "clasificacion": clasificacion,
                "ProbVerdadera": probabilidades[1],
                "ProbFalsa": probabilidades[0]
            })
    except pd.errors.ParserError:
        return jsonify({"error": "Error al leer el archivo CSV. Verifica el formato."}), 400
    except requests.exceptions.RequestException:
        return jsonify({"error": "No se pudo conectar con la API"}), 500

    return render_template('clasificarArchivo.html', results=response_list)

@app.route('/reentrenar', methods=["POST"])
def reentrenarEnvioArchivo():
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No se proporcionó ningún archivo"}), 400

    try:
        df = pd.read_csv(file, sep=";")

        df.rename(columns=lambda x: x.strip(), inplace=True)


        columnas_requeridas = {"ID", "Label", "Titulo", "Descripcion", "Fecha"}
        if not columnas_requeridas.issubset(df.columns):
            return jsonify({"error": "El archivo CSV no tiene las columnas requeridas"}), 400


        df["ID"] = df["ID"].astype(str)
        df["Label"] = df["Label"].astype(int)
        df["Fecha"] = df["Fecha"].astype(str)
        df["Titulo"] = df["Titulo"].astype(str)
        df["Descripcion"] = df["Descripcion"].astype(str)

   
        datos = df.to_dict(orient="records")


        response = requests.post(f"{API_URL}/retrain/", json=datos)
        response.raise_for_status()
        result = response.json()


        formatted_response = {key: f"{value*100:.2f}%" for key, value in result.items()}

    except pd.errors.ParserError:
        return jsonify({"error": "Error al leer el archivo CSV. Verifica el formato."}), 400
    except ValueError as e:
        return jsonify({"error": f"Error en los datos del CSV: {str(e)}"}), 400
    except requests.exceptions.RequestException:
        return jsonify({"error": "No se pudo conectar con la API"}), 500
    
    return render_template('reentreno.html', results=formatted_response)

#----------Main--------------------------
if __name__ == '__main__':
    app.run(debug=True)
