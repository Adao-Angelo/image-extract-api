from flask import Flask, request, jsonify
from download import delete_image, download_image, process_image
from imageToText import query
from dotenv import load_dotenv
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)  
load_dotenv()

@app.route('/process-image', methods=['GET'])
def process_image_endpoint():
    """
    Process an image from a URL and return its description.
    ---
    parameters:
      - name: url
        in: query
        description: The URL of the image to be processed
        required: true
        type: string
        format: uri
    responses:
      200:
        description: The description of the processed image
        content:
          application/json:
            schema:
              type: object
              example:
                description: "Description of the processed image"
      400:
        description: URL not provided
        content:
          application/json:
            schema:
              type: object
              example:
                error: "URL not provided"
      500:
        description: Error in downloading or processing the image
        content:
          application/json:
            schema:
              type: object
              example:
                error: "Error downloading image"
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL not provided"}), 400

    image_path = download_image(url)
    if image_path:
        process_image(image_path)
        output = query(image_path)
        delete_image(image_path)
        return jsonify(output), 200
    else:
        return jsonify({"error": "Error downloading image"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
