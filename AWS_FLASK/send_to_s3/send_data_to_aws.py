from flask import Flask, render_template, request , flash
import boto3
app = Flask(__name__, template_folder = 'templates')
from werkzeug.utils import secure_filename

s3 = boto3.client('s3',
                    aws_access_key_id='ASIAYIGV5MH5WCMW546I',
                    aws_secret_access_key= 'QDvMsQDFcgTHTpqZugnjOerYTQ2kvzzOW9HRZoxS',
                    aws_session_token='FwoGZXIvYXdzEOn//////////wEaDMP1DrOj1/R2bWd2GCLPAfsUWlui6ujT0Tc+LjGMH4LAXP8IufPD2ypQsL7ZE9A40cZTuEDptNzpo3cjdcXvLyDXi5bjrv+iQGoTyNX/x7uWs3lTvSC26YfmhIWnwTE0PjZ5K8NMe9UUOufXC7jyfc1T7+OCfSESWNadA/vRKug9qwXPCxBcfL5TvMonf/I+lznYbx5lvtXUBTrYEk7g1Z9wKSdHiBPplnl7/05F8l7+a8yGqj0AedUXZtLCPG7EeGvOcTacw8hvWQbNObsNMxiA8l93jNbjHNN+4vXMJCjvqricBjItXWjB6Ai+K2ML07lFY+5OZTci3t9wdSZ3BoBmdSPLvpk0R/LEOBR4iu6mOVpA'
                    )

BUCKET_NAME='mybucketcloudfinal'

@app.route('/')  
def home():
    return render_template("Cloud.html")


@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "
        else :
            flash('No file path')

    return render_template("Cloud.html",msg =msg)



if __name__ == "__main__":
    
    app.run(debug=True)
