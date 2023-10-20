from flask import Flask, render_template, request, redirect, url_for
import send_email as se

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    global nome
    global idade
    
    if request.method == 'POST' and 'enviar' in request.form:
        nome = request.form['nome']
        idade = request.form['idade']
        
        return redirect(url_for('opcoes', nome=nome, idade=idade))

    return render_template('index.html')

@app.route('/opcoes', methods=['GET', 'POST'])
def opcoes():
    nome = request.args.get('nome') 
    idade = request.args.get('idade')

    if request.method == 'POST' and 'enviar' in request.form:
        cafe = request.form.getlist('opcoes-cafe')
        almoco = request.form.getlist('opcoes-almoco')
        
        se.send(nome, idade, cafe, almoco)
        
        return redirect(url_for('fim'))

    return render_template('opcoes.html')

@app.route('/fim')
def fim():
    
    return render_template('fim.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
