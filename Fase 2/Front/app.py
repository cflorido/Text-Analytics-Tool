from flask import Flask, jsonify, render_template, request, send_from_directory
import pandas as pd

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

    #TODO--------------------Envio de texto a la API (HACER)------------------

    #--------------------RESPUESTA FALSA DEL API-----------------
    
    #TODOLa respuesta es un json que hay que hacerle parsing
    
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


@app.route('/clasificarEnvioArchivo', methods=["POST"])
def clasificarEnvioArchivo():
    if 'file' not in request.files:
        return jsonify({"error": "No ha enviado el archivo"}), 400

    file = request.files['file']

    # Check if a file was selected
    if file.filename == '':
        return jsonify({"error": "No ha seleccionado un archivo"}), 400

    # Validate the file extension
    if not file.filename.rsplit('.', 1)[1].lower() == 'csv':
        return jsonify({"error": "Solo se permiten archivos de tipo CSV "}), 400
    

    #TODO--------------------Envio de texto a la API ()------------------

    # --------------------RESPUESTA FALSA DEL API-----------------
    
    #TODO La respuesta es un json que hay que hacerle parsing
    
    fake_response = [
    {
        "titulo": "Descubrimiento de agua en Marte",
        "cuerpo": "Científicos confirman la presencia de agua líquida en Marte.",
        "clasificacion": "Verdadero",
        "ProbVerdadera": 0.92,
        "ProbFalsa": 0.08
    },
    {
        "titulo": "Nueva dieta milagrosa",
        "cuerpo": "Expertos aseguran que esta dieta te hace perder 10 kg en una semana sin esfuerzo.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.10,
        "ProbFalsa": 0.90
    },
    {
        "titulo": "Avance en energía renovable",
        "cuerpo": "Investigadores desarrollan un panel solar con un 50% más de eficiencia.",
        "clasificacion": "Verdadero",
        "ProbVerdadera": 0.87,
        "ProbFalsa": 0.13
    },
    {
        "titulo": "Conspiración sobre el 5G",
        "cuerpo": "Las redes 5G están diseñadas para controlar la mente de las personas.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.05,
        "ProbFalsa": 0.95
    },
    {
        "titulo": "Vacuna contra el cáncer",
        "cuerpo": "Científicos anuncian ensayos exitosos de una vacuna contra el cáncer.",
        "clasificacion": "Verdadero",
        "ProbVerdadera": 0.89,
        "ProbFalsa": 0.11
    },
    {
        "titulo": "Fin del mundo en 2025",
        "cuerpo": "Un vidente asegura que el mundo se acabará el próximo año.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.07,
        "ProbFalsa": 0.93
    },
    {
        "titulo": "Nueva batería con 10 veces más duración",
        "cuerpo": "Empresa tecnológica presenta prototipo de batería revolucionaria.",
        "clasificacion": "Verdadero",
        "ProbVerdadera": 0.82,
        "ProbFalsa": 0.18
    },
    {
        "titulo": "Descubrimiento de civilización alienígena",
        "cuerpo": "Astrónomos detectan señales de radio de una civilización avanzada.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.20,
        "ProbFalsa": 0.80
    },
    {
        "titulo": "Chocolate ayuda a bajar de peso",
        "cuerpo": "Nuevo estudio sugiere que comer chocolate en la noche reduce el peso.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.30,
        "ProbFalsa": 0.70
    },
    {
        "titulo": "Robots con conciencia propia",
        "cuerpo": "Investigadores aseguran que han creado un robot con conciencia de sí mismo.",
        "clasificacion": "Falso",
        "ProbVerdadera": 0.15,
        "ProbFalsa": 0.85
    }]

    response_list =  fake_response
    
    #return response_list 
    return render_template('clasificarArchivo.html', results=response_list)

#----------Main--------------------------
if __name__ == '__main__':
    app.run(debug=True)