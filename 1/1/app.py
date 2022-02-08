from fileinput import filename
from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hola')
def hello_world():
    return 'Hola mundo Flask '+__name__

@app.route('/test')
def hello_world2():
    return 'Hola mundo Flask test!'


@app.route('/saludar')
@app.route('/saludar/<hi>')
@app.route('/saludar/<hi>/<lang>')
def saludar(hi='andres', lang='es'):
    return 'Hola: '+hi+' '+lang    


@app.route('/primer_html')
@app.route('/primer_html/<name>')
def primer_html(name='andres'):
    return '''
        <html>
            <body>
                <h1>Hola Flask</h1>
                <p>Hola %s</p>

                <ul>
                    <li>Itmen 1</li>
                    <li>Itmen 2</li>
                </ul>
            </body>
        </html>
    '''% name    


@app.route('/static_file')
def static_file():
    return "<img src="+url_for("static",filename="img/Bojack-Horseman.jpg")+">"
    #return "<img src='/static/img/Bojack-Horseman.jpg'>"


@app.route('/mi_primer_template')
@app.route('/mi_primer_template/<name>')
def mi_primer_template(name='andres'):
    return render_template('view.html', vname=name)


if __name__ == '__main__': #Se ejecuta cuando arrancamos el programa con 'python .\app.y'
    app.run()