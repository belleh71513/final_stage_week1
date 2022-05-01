from flask import Flask, jsonify, render_template, request
from model.s3 import upload_file_to_s3, AWS_STORAGE_BUCKET_NAME
from model.connect_mysql import insert_message, get_message
import os


app = Flask(__name__, static_folder="static", static_url_path="/")

app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

AWS_CLOUD_FRONT = "https://dk9dkz6ihqn2o.cloudfront.net"


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/api/files", methods=["POST"])
def upload_file():
  message = request.form.get("message")
  image = request.files["image"]
  try:
    upload_file_to_s3(image, AWS_STORAGE_BUCKET_NAME, image.filename)
  except:
    res = {
      "error" : True,
      "message" : "AWS S3 伺服器錯誤"
    }
    print("upload file to s3 error")
    return jsonify(res), 500

  image_url = f"https://dk9dkz6ihqn2o.cloudfront.net/{image.filename}"
  try:
    insert_message(message, image_url)
  except:
    res = {
      "error" : True,
      "message" : "RDS 伺服器錯誤"
    }
    print("upload file to s3 error")
    return jsonify(res), 500

  return jsonify({"ok" : True}), 200

@app.route("/api/files", methods=["GET"])
def get_file():
  try:
    files = get_message()
    print(files)
  except:
    res = {
      "error" : True,
      "message" : "RDS 伺服器錯誤"
    }
    return jsonify(res), 500
  return jsonify({"data" : files}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)