from flask import Flask, request, url_for
from werkzeug import secure_filename
import os
from flask.ext.cors import CORS
from src import solver

UPLOAD_FOLDER = '/tmp/wordbase-images'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app = Flask(__name__)
cors = CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['file']
	if not os.path.isdir(UPLOAD_FOLDER):
		os.makedirs(UPLOAD_FOLDER)
		
	if file and allowed_file(file.filename):
		color = request.form["color"]
		filename = secure_filename(file.filename)
		img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(img_path)
		res = solver.solve(color, img_path, 'src/Word-List.txt')
		return " ".join([x[0] for x in res])
	return "failure"


if __name__ == "__main__":
    app.run(debug=True)
