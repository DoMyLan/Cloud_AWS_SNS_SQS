from flask import Flask, render_template, request , flash
import boto3
app = Flask(__name__, template_folder = 'templates')
from werkzeug.utils import secure_filename

s3 = boto3.client('s3',
                    aws_access_key_id='ASIAYIGV5MH57IT5XOG5',
                    aws_secret_access_key= 'EhPox4/epYePRMQF+9HsxFUrTM8Ew+YGX1iyXqEw',
                    aws_session_token='FwoGZXIvYXdzEMT//////////wEaDHGx0Aps13YYmDpgyyLPAVcd7wz009nVsTEuHYPddqy0gmegbIbuzcd5wruMM4V4zczd3ytKqlYQXYOm69drfwJ+Jj/H44CqlKQN7c4bA34HVy33HCwF6XRlGEGos8tVkJqS5H92XbQz5GJp127MU7gaSkB/RpZwzxLZ+UEOlbgEOgEuNnLGiH9E/F1yGfxxEQ+7SIYnxxY7Sqsnvw2M3dxgGXJ3QGFP2nKl7f5Vd25DlbMzBrfS2MHlCn9+kPVmIUCexf6pmaTWZVrUp8j2/Va+CcVc2s13OSf3E8aePijFj7CcBjItvWBJS7pPZrq7whpP756EtAQ3awe+qmY5svz7ln+UZWSLSWkj72SGjd4bBr7z')


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
