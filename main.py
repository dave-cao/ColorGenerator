import os
import time
from datetime import date

import numpy as np
from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from PIL import Image
from werkzeug.utils import secure_filename

from image_handle import get_image_pallette

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
        start_time = time.time()

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
        filename = file.filename
        if file and allowed_file(filename):
            # file.save(os.path.join(app.config["UPLOAD_FOLDER"], f"current_image.jpg"))
            # image_path = uploaded_image_path(f"current_image.jpg")

            color_hexes = get_image_pallette(file)
            # color_hexes = ["#DFC3AA", "#1F1B15", "#9B806F", "#71C5DF", "#594C3D"]
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"It took {round(elapsed_time, 2)} seconds to generate.")

            return render_template(
                "index.html",
                generated_colors=True,
                filename=filename,
                color_hexes=color_hexes,
            )

    return render_template("index.html", generated_colors=False)


def uploaded_image_path(filename):
    return os.path.join(app.config["UPLOAD_FOLDER"], filename)


# allowing file types
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)
