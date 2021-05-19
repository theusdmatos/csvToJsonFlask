import csv
import json
import os
from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)  # Variavel que controlar nossa aplicação

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

# Passando o arquivo CSV


def csvTojson(csvFilePath):

    # Recebendo o CSV e abrindo ele
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            # Passando a chave
            key = rows['TIME']
            data[key] = rows
	

    dictionary = data
    print(dictionary)
    jsonFilePath = r'jsonInput.json'
    with open(jsonFilePath, "r+") as jsonf:
        data = json.load(jsonf)
        data.update(dictionary)
        jsonf.seek(0)
        json.dump(data, jsonf)

    return jsonFilePath

# Esse é um decorator que no Python significa aplicar uma função
# em cima de outra, então aqui estou aplicando a função .route() em cima
# da função home(), esse metodo route() define uma rota para a minha pagina "/"
# Home page


@app.route("/")
# Por padrão, o Flask irá procurar o arquivo index.html no diretório templates do projeto.
def home():
    return render_template("index.html")

# Aqui defino uma rota para" /converter"
@app.route("/converter", methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")
    else:
        file = request.files["csv"]
        upload_csv_path = os.path.join(UPLOAD_FOLDER, file.filename)
        print(upload_csv_path)
        file.save(upload_csv_path)
        path = csvTojson(upload_csv_path)

    return render_template("converter.html", path=path)


@app.route("/converter/<filename>")
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
