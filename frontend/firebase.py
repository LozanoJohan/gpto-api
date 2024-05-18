import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase.json')
    firebase_admin.initialize_app(cred)

# Obtener el cliente de Firestore
db = firestore.client()
messages_ref = db.collection("messages")

def upload_chat_message(prompt, output, like = None):
    datos = {
        "prompt": prompt,
        "output": output,
        "like": like
    }
    
    documento_ref = messages_ref.document()
    documento_ref.set(datos)


# datos_usuario = {
#     "nombre": "Juan",
#     "apellido": "Perez",
#     "edad": 30,
#     "ciudad": "Bogota",
#     "empresa": "ABC",
#     "email": "XXXXXXXXXXXXXX"
# }