from flask import Flask, render_template,request,redirect, url_for,flash
import pytesseract as tess
from PIL import Image
import os

# from werkzeug.utils import secure_filename
# UPLOAD_FOLDER = "images"


ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app = Flask(__name__)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

app.secret_key = 'secrectkey'



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['POST','GET'])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            imagefile = request.files.get('file', '') 
            # uploadimg = imagefile
            img = Image.open('images/hi.png')
            text = tess.image_to_string(img)
            f = open("sample.txt", "a")
            f.truncate(0)
            f.write(text)
            f.close()
            # if text != None :
            #     os.remove(uploadimg)
            
            return render_template("index.html",text=text)
    else:
        return render_template("index.html")

#for debug
# if __name__ == "__main__":
#     app.run(debug=True)

