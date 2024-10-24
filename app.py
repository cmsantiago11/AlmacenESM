from flask import Flask, render_template, request
from DatosDB import ConsultarDiametrosUnicos, ConsultarLargosUnicos, ConsultarTiposDeTornillos, ConsultarTiposDeCabeza, ConsultarMaterial,ConsultarTornillo,ConsultarRosca
app = Flask(__name__)

tornillos = {"tipoDeTornillo":ConsultarTiposDeTornillos(),"tipoDeCabeza":ConsultarTiposDeCabeza(),"Diametros":ConsultarDiametrosUnicos(),"Largos":ConsultarLargosUnicos(),"Material":ConsultarMaterial(),"tipoDeRosca":ConsultarRosca()}

@app.route('/')
def index():
    
    return render_template('index.html',misdyl=tornillos,variable_html=" ",resultado_html=" ")

@app.route('/procesar', methods=['POST'])
def procesar():
    # Recoger los datos del formulario
    insumo = request.form.get('opciones')
    diametro = request.form.get('diametros')
    material = request.form.get('material')
    cabeza = request.form.get('cabeza')
    largo = request.form.get('largos')
    tipo = request.form.get('tipo')
    rosca = request.form.get('rosca')

    if not (tipo and cabeza and diametro and largo and material and rosca):
        error_message = "Todos los campos son obligatorios."
        return render_template('index.html', misdyl=tornillos, variable_html=error_message,resultado_html="Intenta de nuevo")

    # Procesar los datos con Python
    resultado_tor = f"TOR {tipo} {cabeza} {diametro}x{largo}\"{rosca} {material}"

    if len(resultado_tor)>40:
        resultado_busqueda="Intenta de nuevo"
        #resultado_tor="Excediste el número de carácteres"
    else:
        resultado_busqueda=ConsultarTornillo(resultado_tor)

    #request_DB=ConsultarTornillo(resultado)
    
    # Hacer más procesamiento aquí con los datos si es necesario
     
    return render_template('index.html',misdyl=tornillos,variable_html=(resultado_tor),resultado_html=resultado_busqueda)


if __name__ == '__main__':
    app.run(debug=True,port=3000)
