from flask import Flask, request
import qrcode
from jinja2 import Environment, FileSystemLoader, Template

with open('C:\\Users\Hp\\OneDrive\\Documentos\\pagina web intento 2\\registro.html') as file:
    lugar = Template(file.read())
env = Environment(loader=FileSystemLoader('.'))
destino = env.get_template('registro.html')
app = Flask(__name__)
rendered_template = str()
qr = qrcode.QrCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4)
@app.route('/procesar.py', methods=['POST'])
def procesar_formulario():
    global rendered_template
    TI = request.form['ID']
    nombre = request.form['nombre']
    profesion = request.form['profesión']
    data = str(TI)+'/'+str(nombre)+'/'+str(profesion)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color='black',back_color='white')
    rendered_template = destino.render(qr=image)

with open('C:\\Users\\Hp\\OneDrive\\Documentos\\pagina web intento 2\\registro.html','w') as file:
    file.write(rendered_template)
if __name__ == '__main__':
    app.run()

