from flask import Flask, jsonify, render_template, request, send_from_directory

app = Flask(__name__)
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
#----------Interaccion con el API-----------

@app.route('/clasificarEnvio', methods=["POST"])
def clasificarEnvio():
    titulo = request.form.get("titulo") 
    cuerpo = request.form.get("cuerpo") 

    #--------------------Envio de texto a la API (HACER)------------------
    a ="""     payload = {
        "titulo": titulo,
        "cuerpo": cuerpo
    }
    try:
       response = requests.post('http://API/clasificar', json=payload)
        if response.status_code == 200:
                return jsonify(response.json()) 
                ...
        else:
            return jsonify({"error": "Failed to get a valid response from the API"}), response.status_code
            ...
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Request failed: {str(e)}"}), 500 """
    # --------------------RESPUESTA FALSA DEL API-----------------
    
    #La respuesta es un json que hay que hacerle parsing
    
    fake_response = {
        "titulo": titulo,
        "cuerpo": cuerpo,
        "clasificacion": "Verdadero" if "ejemplo" in titulo.lower() else "Falso",
        "ProbVerdaderpa": 0.85,  
        "ProbFalsa": 0.15
    }
    response_dict =  fake_response
    
    #return response_json    
    return render_template('clasificar.html', results=response_dict)


#----------Main--------------------------
if __name__ == '__main__':
    app.run(debug=True)