from flask import Flask, render_template, request, flash, redirect, url_for
import os
import urllib.request
from prediction import predict_image_classification
from werkzeug.utils import secure_filename
from yolo_v5 import predict_object_detection
app = Flask(__name__)
# creates a Class for our app
app.secret_key = "manbearpig_MUDMAN888"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def calcul():
    one = 15
    two = 30
    return two


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    # print(request.form.get('models'))
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)

        if request.form.get('models')=="Yolo_v5":
            filename=predict_object_detection(filename)
            flash("Object detected shown below!!")
        else:
            flash('Welcome back, ' + str(predict_image_classification('static\\uploads\\'+filename,request.form.get('models'))))

        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)