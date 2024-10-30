from flask import Flask, request, jsonify
from download import delete_image, download_image, process_image
from imageToText import query

app = Flask(__name__)


@app.route('/process-image', methods=['GET'])
def process_image_endpoint():
    url = request.args.get('url')
   

    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    image_path = download_image(url)
    if image_path:
 
        process_image(image_path)
    
        output = query(image_path)
      
        delete_image(image_path)

        print(output)
      
        return jsonify(output), 200
    else:
        return jsonify({"error": "Erro ao baixar a imagem"}), 500

if __name__ == "__main__":
    app.run(debug=True)
