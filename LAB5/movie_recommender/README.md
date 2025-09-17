# Sistema Recomendador de Películas

Un sistema de recomendación de películas basado en Django que proporciona sugerencias personalizadas basadas en las preferencias del usuario y filtrado colaborativo.

## Descripción

Este proyecto es un recomendador de películas completo construido con Django. Permite a los usuarios calificar películas, mantener perfiles con géneros favoritos y recibir recomendaciones personalizadas. El sistema utiliza un enfoque híbrido que combina recomendaciones basadas en géneros y filtrado colaborativo para sugerir películas que los usuarios podrían disfrutar.

## Características

- **Gestión de Usuarios**: Perfiles de usuario con géneros y películas favoritas
- **Base de Datos de Películas**: Información completa de películas incluyendo directores, actores, géneros y calificaciones
- **Sistema de Calificación**: Los usuarios pueden calificar películas en una escala de 1-10 con comentarios opcionales
- **Motor de Recomendación**:
  - Recomendaciones basadas en géneros según los géneros favoritos del usuario
  - Filtrado colaborativo basado en las calificaciones de usuarios similares
- **Interfaz de Administración**: Admin completo de Django con filtros personalizados, inlines y acciones
- **Soporte de Imágenes**: Subida y visualización de pósters de películas y fotos de personas
- **Población de Datos**: Comando de gestión para poblar la base de datos con datos de muestra
- **Pruebas Completas**: Pruebas unitarias para modelos y algoritmos de recomendación

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (instalador de paquetes de Python)

### Configuración

1. **Clona el repositorio** (si aplica) o navega al directorio del proyecto:
   ```bash
   cd movie_recommender
   ```

2. **Crea un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r src/requirements.txt
   ```

4. **Navega al proyecto Django**:
   ```bash
   cd src
   ```

5. **Ejecuta las migraciones de base de datos**:
   ```bash
   python manage.py migrate
   ```

6. **Puebla la base de datos con datos de muestra**:
   ```bash
   python manage.py seed_data
   ```

7. **Crea un superusuario** (opcional, para acceso admin):
   ```bash
   python manage.py createsuperuser
   ```

## Uso

### Ejecutando el Servidor de Desarrollo

```bash
python manage.py runserver
```

Accede a la aplicación en `http://127.0.0.1:8000/`

### Interfaz de Administración

Accede al admin de Django en `http://127.0.0.1:8000/admin/`

Incluye:
- Gestionar películas, directores, actores y géneros
- Ver y gestionar calificaciones de usuarios
- Usar la acción "Get movie recommendations" en perfiles de usuario
- Filtros y funcionalidad de búsqueda personalizados

### Poblando Datos

Para poblar la base de datos con datos de muestra:

```bash
python manage.py seed_data
```

Esto crea directores, actores, géneros, películas y calificaciones de usuario de muestra.

## Estructura del Proyecto

```
movie_recommender/
├── src/
│   ├── config/                 # Configuración del proyecto Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── movies/                 # App principal de Django
│   │   ├── models.py           # Modelos de base de datos (Movie, Director, Actor, etc.)
│   │   ├── admin.py            # Configuración del admin de Django
│   │   ├── recomendations.py   # Algoritmos de recomendación
│   │   ├── utils.py            # Funciones de utilidad para admin
│   │   ├── tests.py            # Pruebas unitarias
│   │   ├── views.py            # Vistas de Django (actualmente vacío)
│   │   ├── apps.py
│   │   └── management/
│   │       └── commands/
│   │           └── seed_data.py # Comando para poblar base de datos
│   ├── db.sqlite3              # Base de datos SQLite
│   ├── manage.py               # Script de gestión de Django
│   └── requirements.txt        # Dependencias de Python
├── .gitignore
└── README.md
```

## Modelos

- **Person**: Modelo base para personas en la industria cinematográfica
- **Director**: Hereda de Person, con campo de premios
- **Actor**: Hereda de Person, con campo de premios
- **Genre**: Géneros de películas con descripciones
- **Movie**: Modelo principal de película con relaciones a directores, actores, géneros
- **MovieActor**: Modelo intermedio para relaciones película-actor
- **UserProfile**: Información extendida de usuario con géneros/películas favoritas
- **Rating**: Calificaciones de usuarios para películas (escala 1-10)

## Algoritmo de Recomendación

El sistema utiliza dos estrategias principales de recomendación:

1. **Recomendaciones Basadas en Géneros**: Sugiere películas de los géneros favoritos del usuario que no han calificado aún, ordenadas por calificación promedio y relevancia.

2. **Filtrado Colaborativo**: Encuentra usuarios con calificaciones altas similares y recomienda películas que esos usuarios gustaron que el usuario actual no ha calificado.

La función `get_recommendations()` combina ambos enfoques para sugerencias completas.

## Pruebas

Ejecuta el conjunto de pruebas:

```bash
python manage.py test
```

Las pruebas cubren:
- Creación de modelos y relaciones
- Cálculos de calificación promedio
- Algoritmos de recomendación

## Contribuyendo

1. Haz fork del repositorio
2. Crea una rama de funcionalidad
3. Haz tus cambios
4. Agrega pruebas para nueva funcionalidad
5. Asegúrate de que todas las pruebas pasen
6. Envía un pull request

## Tecnologías Utilizadas

- **Django 5.2.6**: Framework web
- **SQLite**: Base de datos
- **Pillow**: Procesamiento de imágenes
- **Python 3.8+**: Lenguaje de programación

## Mejoras Futuras

- API REST para integración con frontend
- Autenticación y registro de usuarios
- Búsqueda y filtrado de películas
- Algoritmos de recomendación avanzados (filtrado basado en contenido)
- Interfaz de usuario para calificar y navegar películas
- Características sociales (seguir usuarios, compartir recomendaciones)

## Licencia

Este proyecto es de código abierto. Por favor revisa el archivo de licencia para detalles.
