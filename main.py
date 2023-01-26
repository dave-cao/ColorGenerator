import os
from datetime import date

from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "./static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdlkfj41t34tasldkfj12451234tasdlkfjg;asl"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Global Variables
@app.context_processor
def get_year():
    return dict(year=date.today().year)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]

        # check if file is a file ?? reread on this
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        # check if user actually selected a file
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        # secure filename cuz user input cannot be trusted
        filename = secure_filename(file.filename)
        if file and allowed_file(filename):
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            image_path = uploaded_image_path(filename)
            return render_template(
                "index.html", image_path=image_path, filename=filename
            )

    return render_template("index.html", image_path=None)


def uploaded_image_path(filename):
    return os.path.join(app.config["UPLOAD_FOLDER"], filename)


# allowing file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)
