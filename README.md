# Administración de Clientes y Servicios

Aplicación web desarrollada con **Django** para la gestión integral de clientes y servicios. El proyecto está estructurado de forma modular mediante aplicaciones independientes (`main`, `clientes` y `servicios`), integrando soporte para carga de fotografías con `Pillow`, avatares predeterminados mediante archivos estáticos y hojas de estilo personalizadas por módulo.

## Características principales

- **Panel principal (`main`):** Punto de entrada centralizado con navegación directa hacia los módulos de clientes y servicios.
- **Gestión de clientes (`clientes`):** Registro de nuevos clientes con validaciones personalizadas, listado con vista previa de fotografías y página de detalle individual.
- **Gestión de servicios (`servicios`):** Administración de servicios con nombre, descripción, estado (`activo`) y fotografía, incluyendo listado y vista de detalle.
- **Manejo de multimedia y avatares por defecto:** Subida de imágenes mediante `ImageField` (`Pillow`) y respaldo automático con imagen predeterminada (`avatardefault.png`) desde `static` cuando el registro no cuenta con fotografía.

## Estructura del proyecto

```text
.
├── clientes/
│   ├── static/clientes/
│   │   ├── css/styles.css
│   │   └── img/avatardefault.png
│   ├── templates/clientes/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── main/
│   ├── static/main/css/styles.css
│   ├── templates/main/
│   ├── urls.py
│   └── views.py
├── servicios/
│   ├── static/servicios/
│   │   ├── css/styles.css
│   │   └── img/avatardefault.png
│   ├── templates/servicios/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── proyecto/
│   ├── settings.py
│   └── urls.py
├── .gitignore
├── manage.py
└── README.md
```

## Requisitos previos

- **Python** 3.10 o superior
- **Django**
- **Pillow** (necesario para procesar campos `ImageField`)

## Instalación y ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   cd TU_REPOSITORIO
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # En Linux / macOS:
   source .venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install django pillow
   ```

4. **Generar y aplicar las migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   Ingresa a `http://127.0.0.1:8000/` desde tu navegador.

## Tecnologías utilizadas

- **Backend:** Python, Django
- **Procesamiento de imágenes:** Pillow
- **Frontend:** HTML5, CSS3, Django Templates

## Autor

**Antonio Milián**