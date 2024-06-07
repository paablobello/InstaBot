
# Instagram Comment Bot

Este proyecto es un bot de automatización para comentar en publicaciones de Instagram utilizando Selenium y Python. El bot inicia sesión en Instagram y comenta en una lista de publicaciones especificada.

## Requisitos

- Python 3.7 o superior
- Google Chrome
- ChromeDriver

## Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu_usuario/instagram-comment-bot.git
cd instagram-comment-bot
```

2. **Crear y activar un entorno virtual:**

```bash
python -m venv .venv
source .venv/bin/activate # En Windows: .venv\Scripts\activate
```

3. **Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Descargar ChromeDriver:**

   - Descarga la versión de ChromeDriver que coincide con tu versión de Google Chrome desde [aquí](https://developer.chrome.com/docs/chromedriver/downloads).
   - Extrae el archivo descargado y coloca el ejecutable en la ruta especificada en el script (`chrome_driver_path`).

## Uso

1. **Configurar tus credenciales y publicaciones:**

   Edita el archivo `main.py` y reemplaza las variables `username`, `password`, `post_urls` y `comments` con tus datos:

   ```python
   username = "tu_usuario"
   password = "tu_contraseña"

   post_urls = [
       "https://www.instagram.com/p/ID1/",
       "https://www.instagram.com/p/ID2/"
   ]

   comments = [
       "¡Qué gran publicación!",
       "Me encanta este contenido."
   ]
   ```

2. **Ejecutar el bot:**

```bash
python main.py
```


