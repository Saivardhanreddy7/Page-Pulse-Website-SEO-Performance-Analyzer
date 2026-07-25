from flask import Flask,request,jsonify
from seo import analyze

app=Flask(__name__)

@app.route("/analyze",methods=["POST"])
def report():

    url=request.json["url"]

    data=analyze(url)

    return jsonify(data)

app.run(debug=True)
