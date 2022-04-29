from flask import Flask, render_template, request
from model.s3 import upload_file_to_s3, AWS_STORAGE_BUCKET_NAME
import os


app = Flask(__name__, static_folder="static", static_url_path="/")

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

AWS_STORAGE_BUCKET_NAME = "wehelp-third-phase-week1"
AWS_CLOUD_FRONT = "https://dk9dkz6ihqn2o.cloudfront.net"


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
  file = request.files["file"]
  file.save(os.path.join("uploads", file.filename))
  upload_file(f"uploads/{file.filename}", AWS_STORAGE_BUCKET_NAME)
  return



if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)

