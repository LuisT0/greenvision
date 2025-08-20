# GreenVisionModel: Clasificación de Residuos con Visión Computacional

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📖 Descripción

**GreenVisionModel** es un proyecto de **Visión Computacional (Computer Vision)** que utiliza un modelo de Deep Learning para la **clasificación automática de residuos**. La solución se expone a través de una **API REST**, lista para ser desplegada, que puede identificar si una imagen de un residuo corresponde a material orgánico, reciclable o no reciclable.

El objetivo es proporcionar una herramienta tecnológica que facilite y automatice los procesos de reciclaje y gestión ambiental.

## 🚀 API en Acción

¡Así es como se ve la API funcionando! Primero, la interfaz principal y luego un ejemplo de una predicción en tiempo real.

![Pantalla principal de la API](docs/Pantalla_principal.png)
_Interfaz principal de la API_

![Ejemplo de predicción](docs/Predicción.png)
_Resultado de una clasificación en formato JSON_

*   **Link directo a la app:** [Greenvision](https://huggingface.co/spaces/LuisTo97/GreenVision-Docker)

## ✨ Características Clave

*   **Modelo de Clasificación:** Utiliza técnicas de Deep Learning para distinguir entre múltiples categorías de residuos con alta precisión.
*   **API Lista para Producción:** Desarrollada para ser robusta y escalable, lista para integrarse en sistemas más grandes.
*   **Despliegue con Docker:** Incluye un `Dockerfile` para una fácil contenerización y despliegue en cualquier entorno, garantizando consistencia.
*   **Procesamiento en Tiempo Real:** Envía una imagen y recibe una clasificación casi instantánea en formato JSON.

## 🛠️ Tecnologías Usadas

<p align="left">
  <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
  <a href="https://www.docker.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a>
  <a href="https://fastapi.tiangolo.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="fastapi" width="40" height="40"/> </a>
  <a href="https://pytorch.org/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg" alt="pytorch" width="40" height="40"/> </a>
  <a href="https://opencv.org/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/opencv/opencv-original.svg" alt="opencv" width="40" height="40"/> </a>
  <a href="https://git-scm.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" alt="git" width="40" height="40"/> </a>
</p>

## ⚙️ Instalación y Uso

Puedes levantar la API usando Docker (recomendado) o directamente en tu máquina local.

1.  **Clona el repositorio:**
    ```
    git clone https://github.com/LuisT0/greenvision.git
    cd greenvision
    ```
2.  **Opción A: Usando Docker (Recomendado)**
    ```
    # Construye la imagen del contenedor
    docker build -t greenvision-api ./api

    # Ejecuta el contenedor
    docker run -p 8000:8000 greenvision-api
    ```
3.  **Opción B: Instalación Local**
    ```
    # (Opcional pero recomendado) Crea y activa un entorno virtual
    python -m venv venv
    source venv/bin/activate # En Windows: venv\Scripts\activate

    # Instala las dependencias
    pip install -r api/vision_requirements.txt

    # Inicia la API
    python api/main.py
    ```
Una vez iniciada, la API estará disponible en `http://localhost:8000`.

## 📂 Estructura del Repositorio

| Carpeta/Archivo               | Descripción                                          |
|-------------------------------|------------------------------------------------------|
| `api/`                        | Código fuente de la API (FastAPI/Flask)              |
| `api/main.py`                 | Script principal para iniciar la API                 |
| `api/models/`                 | Modelos entrenados (`.h5`, `.pth`, etc.) y utilidades |
| `api/vision_requirements.txt` | Dependencias de Python para la API                   |
| `api/Dockerfile`              | Configuración para el contenedor Docker de la API    |
| `data/`                       | Imágenes de ejemplo para probar la clasificación     |
| `docs/`                       | Imágenes para la documentación (como este README)    |
| `README.md`                   | ¡Estás aquí!                                         |


## 🤝 Contribuciones y Licencia

Este proyecto está protegido bajo la **Licencia MIT**. Las contribuciones son más que bienvenidas. Si tienes una idea, abre un *issue* o envía un *pull request*.

## 👤 Autor

¡Conéctame para hablar de IA, desarrollo y cómo la tecnología puede cambiar el mundo!

*   **GitHub:** [LuisT0](https://github.com/LuisT0)
*   **LinkedIn:** [Luis Antonio Torres Villalobos](https://www.linkedin.com/in/luis-antonio-torres-villalobos/)
