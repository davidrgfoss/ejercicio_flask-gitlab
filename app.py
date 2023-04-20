from flask import Flask, render_template, abort
from lxml import etree
doc = etree.parse('libros.xml')
app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html")

@app.route('/potencia',methods=["GET","POST"])
@app.route('/potencia/<base>/<exponente>',methods=["GET","POST"])
def potencia(base=2,exponente=3):
	return render_template("potencia.html",operando1=int(base),operando2=int(exponente))

@app.route('/contarletras',methods=["GET","POST"])
@app.route('/contarletras/<palabra>/<letra>',methods=["GET","POST"])
def contarletras(palabra="Informatica",letra="a"):
    count=0
    if palabra and letra:
        for i in palabra:
            if i==letra:
                count+=1
        print ("Hay un total de %i de coincidencias para el caracter %s." %(count,letra))
    else:
        abort(404)
    return render_template("contarletras.html",cad1=str(palabra),cad2=str(letra),repeticiones=int(count))

@app.route('/libros',methods=["GET","POST"])
@app.route('/libros/<int:codigo>',methods=["GET","POST"])
def codigolibro(codigo=125):
    try:
        int(codigo)
        if not str(codigo) in doc.xpath('//codigo/text()'):
            abort(404)
        lista=zip(doc.xpath('//libro[codigo/text() = "%i"]/titulo/text()' %(codigo)), doc.xpath('//libro[codigo/text() = "%i"]/autor/text()' %(codigo)))
        return render_template("libros.html",num=codigo,resultado=lista)
    except:
        abort(404)

app.run(debug=True)