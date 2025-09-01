# Backend Django con MariaDB

Este proyecto es un backend desarrollado con **Django** y conectado a **MariaDB**.  
Este README está pensado para usuarios que quieren ejecutar el proyecto rápidamente.

---

## Requisitos

- Python 3.x  
- pip  
- MariaDB  
- Git  

---

## 1️⃣ Clonar el Proyecto

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo/backend-inacap

2️⃣ Instalar Dependencias y Activar Entorno
# Crear y activar entorno virtual
python3 -m venv env
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

3️⃣ Configurar Base de Datos y Ejecutar

Inicia MariaDB y crea la base de datos:

mysql -u root -p
CREATE DATABASE nombre_de_tu_base_de_datos;


Configura la conexión en backend-inacap/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


Ejecuta migraciones y corre el servidor:

python manage.py migrate
python manage.py runserver


Accede al backend en http://127.0.0.1:8000/.
