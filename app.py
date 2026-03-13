from flask import Flask, render_template, request, redirect, url_for
from modelo import Agenda

app = Flask(__name__)
# Instanciamos nuestra clase de POO
mi_agenda = Agenda()

# --- RUTAS PARA CONTACTOS ---


@app.route('/')
def vista_contactos():
    id_editar = request.args.get('edit', type=int)
    contacto_edit = None
    if id_editar:
        contacto_edit = mi_agenda.obtener_contacto(id_editar)
    
    return render_template('contactos.html', 
                           contactos=mi_agenda.datos['contactos'], 
                           contacto_edit=contacto_edit)

@app.route('/contacto/add', methods=['POST'])
def add_contacto():
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    mi_agenda.agregar_contacto(nombre, telefono)
    return redirect(url_for('vista_contactos'))

@app.route('/contacto/delete/<int:id>')
def delete_contacto(id):
    mi_agenda.eliminar_contacto(id)
    return redirect(url_for('vista_contactos'))

@app.route('/contacto/update/<int:id>', methods=['POST'])
def update_contacto(id):
    nombre = request.form.get('nombre')
    telefono = request.form.get('telefono')
    mi_agenda.actualizar_contacto(id, nombre, telefono)
    return redirect(url_for('vista_contactos'))

# --- RUTAS PARA NOTAS ---
@app.route('/notas')
def vista_notas():
    return render_template('notas.html', notas=mi_agenda.datos['notas'])

@app.route('/nota/add', methods=['POST'])
def add_nota():
    titulo = request.form.get('titulo')
    contenido = request.form.get('contenido')
    mi_agenda.agregar_nota(titulo, contenido)
    return redirect(url_for('vista_notas'))

@app.route('/nota/delete/<int:id>')
def delete_nota(id):
    mi_agenda.eliminar_nota(id)
    return redirect(url_for('vista_notas'))

if __name__ == '__main__':
    app.run(debug=True)