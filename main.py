from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
import random

chrome_options = Options()
# chrome_options.add_argument('--headless')  #descomentar para que no lanze chrome
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


chrome_driver_path = "C:/Users/..."  # Reemplaza con tu ruta

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.3))



def login_instagram(username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    try:
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'username'))
        )
        password_input = driver.find_element(By.NAME, 'password')

        human_typing(username_input, username)
        time.sleep(random.uniform(1, 2))
        human_typing(password_input, password)
        time.sleep(random.uniform(1, 2))
        password_input.send_keys(Keys.RETURN)


        WebDriverWait(driver, 20).until(
            EC.any_of(
                EC.url_to_be('https://www.instagram.com/'),
                EC.url_contains('#reactivated')
            )
        )


        try:
            not_now_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Ahora no']"))
            )
            not_now_button.click()
        except Exception as e:
            print("No se encontró la ventana emergente de notificaciones. Continuando...")

        print("Inicio de sesión exitoso.")
    except Exception as e:
        print(f"Error al iniciar sesión: {e}")
        driver.save_screenshot('login_error_screenshot.png')
        driver.quit()
        return False
    return True



def comment_on_post(post_url, comment_text):
    driver.get(post_url)
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Añade un comentario...']"))
        )

        attempts = 0
        while attempts < 3:
            try:
                comment_box = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Añade un comentario...']")
                comment_box.click()
                human_typing(comment_box, comment_text)
                comment_box.send_keys(Keys.RETURN)
                break
            except StaleElementReferenceException:
                attempts += 1
                print(f"Intento {attempts} de 3: Elemento obsoleto, reintentando...")
                time.sleep(2)

        if attempts == 3:
            raise Exception("No se pudo interactuar con el textarea después de 3 intentos.")


        time.sleep(2)
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//span[text()='{comment_text}']"))
        )
        print(f"Comentario publicado en {post_url}.")
    except Exception as e:
        print(f"Ocurrió un error al comentar en {post_url}: {e}")
        driver.save_screenshot('comment_error_screenshot.png')


# Cambiar por tus datos de inicio de sesion
username = "usuario"
password = "contraseña"

#Aqui las url de las publicaciones que quieres comentar
post_urls = [
    "https://www.instagram.com/p/...",
    "https://www.instagram.com/p/..."
]

# Aqui los comentarios que quieras añadir en las publicaciones(no se publican en el orden que los pongas, esta puesto para que sea en orden aleatorio)
comments = [
    "¡Qué gran publicación!",
    "comentario..."
]

# Número de veces que quieres que se comente en cada publicacion
num_comments_per_post = 1

# Tiempo de espera mínimo y máximo entre publicacion de comentarios (en segundos)
min_wait = 30
max_wait = 90

if login_instagram(username, password):
    for post_url in post_urls:
        for i in range(num_comments_per_post):
            try:
                comment_text = random.choice(comments)

                comment_on_post(post_url, comment_text)

                wait_time = random.randint(min_wait, max_wait)
                print(
                    f"Comentario {i + 1} publicado en {post_url}. Esperando {wait_time} segundos antes del siguiente comentario.")
                time.sleep(wait_time)
            except Exception as e:
                print(f"Ocurrió un error al comentar en {post_url}: {e}")

        print(f"Esperando 3 minutos antes de comentar en la siguiente publicación.")
        time.sleep(180)  # Espera 3 minutos (180 segundos) antes de publicar en la siguiente publicación

    print("Proceso de comentarios automatizados completado.")
else:
    print("No se pudo iniciar sesión. Revisa las capturas de pantalla para más detalles.")

driver.quit()
