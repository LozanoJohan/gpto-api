# El poderoso Geppetto

## Descripción
Geppetto es una herramienta de análisis de datos empresariales diseñada para trabajar con bases de datos SQL. Facilita la visualización y el análisis de grandes volúmenes de datos a través de una interfaz interactiva desarrollada con Streamlit.

## Instalación y ejecución local
Sigue estos pasos para configurar y ejecutar Geppetto localmente:

1. **Clonar el repositorio:**
```
git clone [URL del repositorio]
```

2. **Crear un entorno virtual:**
```
python -m venv env
```

3. **Activar el entorno virtual:**
- En Windows:
  ```
  .\env\Scripts\activate
  ```
- En Unix o macOS:
  ```
  source env/bin/activate
  ```

4. **Instalar las dependencias:**
```
pip install -r requirements.txt
```

5. **Crea una carpeta .stramlit**

6. **Crea una archivo secrets.toml y pega lo siguiente:**
```
DATABASE = ""
USERNAME = ""
PASSWORD = ""
SERVER = ""
PORT = 

OPENAI_API_KEY = ""
CLOUDFLARE_API_KEY = ""
```

7. **Escribe tu configuración para las variables secretas**

8. **Ejecutar la aplicación:**
```
streamlit run frontend/view.py
```

9. Disfrutar