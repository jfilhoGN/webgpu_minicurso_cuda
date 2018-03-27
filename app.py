import os, subprocess, sys, time
from subprocess import check_output
import flask
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['py','c','sh','cu'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercicio1/')
def exercicio1():
    return render_template('upload_exercicio.html')

@app.route('/exercicio1/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
            filename=filename))


@app.route('/uploads/<filename>.exe')
def uploaded_file(filename):
    def inner():
        extension = filename.rsplit('.',1)[1]
        if(extension=="cu"):
            exe = ["/usr/local/cuda/bin/nvcc -I /usr/local/cuda/include -L /usr/local/cuda/lib64 -ccbin=g++-4.9 ./uploads/"+filename +" -lcuda -lm -o ./uploads/"+filename+".exe"]
            p = subprocess.Popen(exe, stdout = subprocess.PIPE, shell=True)
            p.communicate()
            exe1 = ["./uploads/"+filename+".exe"]
            q = subprocess.Popen(exe1, stdout = subprocess.PIPE, shell=True)
            for line in iter(q.stdout.readline,''):
                #time.sleep(1)
                yield line.rstrip() + '<br/>\n'
    return render_template('view.html', out=inner()) 

if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("5000"),
        debug=True
)
