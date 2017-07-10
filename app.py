import os, subprocess, sys, time
from subprocess import check_output
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from werkzeug import secure_filename
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('sqlite:///webgpu.db', echo=True)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['py','c','sh','cu'])

def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def first():
    return render_template('index.html')


# PARTE DE LOGIN
'''
@app.route('/')
def first():
    if not session.get('logado'):
            return render_template("login-form/login.html")
    else:
         return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    post_ra = int(request.form['ra'])
    post_password = str(request.form['senha'])
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.ra==post_ra, User.password ==post_password)
    result = query.first()
    if result:
        session['logado'] = True
        #return render_template("index.html")
    else:
        flash("Senha ou RA errados!")
    return login()

@app.route('/logout')
def logout():
    session['logado'] = False
    return login()
'''

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
    extension = filename.rsplit('.',1)[1]
    # if(extension=="py"):
    #     exe = ["/usr/bin/python ./uploads/"+filename]
    #     p = subprocess.Popen(exe, stdout = subprocess.PIPE, shell=True)
    #     out,err = p.communicate()
    #     return out
    # elif(extension=="sh"):
    #     exe = ["/bin/sh ./uploads/"+filename]
    #     p = subprocess.Popen(exe, stdout = subprocess.PIPE, shell=True)
    #     out,err = p.communicate()
    #     return out
    if(extension=="c"):
        exe = ["/usr/bin/gcc ./uploads/"+filename +" -o ./uploads/"+filename+".exe"]
        p = subprocess.Popen(exe, stdout = subprocess.PIPE, shell=True)
        p.communicate()
        exe1 = ["./uploads/"+filename+".exe"]
        q = subprocess.Popen(exe1, stdout = subprocess.PIPE, shell=True)
        out,err = q.communicate()
        return out
    elif(extension=="cu"):
        #nvcc -I /usr/local/cuda/include -L /usr/local/cuda/lib64 -ccbin=g++-4.9 src/sumvector.cu -lcuda -lm -o sumvector-cuda
        exe = ["/usr/local/cuda/bin/nvcc -I /usr/local/cuda/include -L /usr/local/cuda/lib64 -ccbin=g++-4.9 ./uploads/"+filename +" -lcuda -lm -o ./uploads/"+filename+".exe"]
        p = subprocess.Popen(exe, stdout = subprocess.PIPE, shell=True)
        p.communicate()
        exe1 = ["./uploads/"+filename+".exe"]
        q = subprocess.Popen(exe1, stdout = subprocess.PIPE, shell=True)
        out,err = q.communicate()
        #print out
        return out

if __name__ == '__main__':
    #ip host = 172.16.255.169
    app.secret_key = os.urandom(12)
    app.run(
        host="localhost",
        port=int("5000"),
        debug=True
    )