import json
import os

class GestorBase:
    """Clase base para gestionar la persistencia en JSON"""
    def __init__(self, archivo='data.json'):
        self.archivo = archivo
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            return {"contactos": [], "notas": []}
        with open(self.archivo, 'r', encoding='utf-8') as f:
            return json.load(f)

    def guardar(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

class Agenda(GestorBase):
    """Clase que hereda de GestorBase y añade lógica CRUD"""
    
    # CRUD CONTACTOS
    def agregar_contacto(self, nombre, telefono):
        # Generamos un ID simple
        nuevo_id = len(self.datos['contactos']) + 1
        nuevo_contacto = {"id": nuevo_id, "nombre": nombre, "telefono": telefono}
        self.datos['contactos'].append(nuevo_contacto)
        self.guardar()

    def eliminar_contacto(self, id_contacto):
        self.datos['contactos'] = [c for c in self.datos['contactos'] if c['id'] != id_contacto]
        self.guardar()

    # CRUD NOTAS
    def agregar_nota(self, titulo, contenido):
        nuevo_id = len(self.datos['notas']) + 1
        nueva_nota = {"id": nuevo_id, "titulo": titulo, "contenido": contenido}
        self.datos['notas'].append(nueva_nota)
        self.guardar()

    def eliminar_nota(self, id_nota):
        self.datos['notas'] = [n for n in self.datos['notas'] if n['id'] != id_nota]
        self.guardar()

    def obtener_contacto(self, id_contacto):
        """Busca un contacto específico por su ID"""
        for c in self.datos['contactos']:
            if c['id'] == id_contacto:
                return c
        return None

    def actualizar_contacto(self, id_contacto, nombre, telefono):
        """Busca el contacto y actualiza sus valores"""
        for c in self.datos['contactos']:
            if c['id'] == id_contacto:
                c['nombre'] = nombre
                c['telefono'] = telefono
                break
        self.guardar()