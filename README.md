
# Votify - API de Encuestas

**Votify** es una API sencilla construida con **Django Rest Framework (DRF)** que permite a los usuarios crear encuestas, votar en ellas y ver los resultados. Este proyecto es ideal para aprender sobre la creación de APIs con Django y el manejo de relaciones entre modelos, autenticación y lógica de votos.

## Funcionalidades

- **Crear encuestas** con múltiples opciones de respuesta.
- **Permitir votar** en las encuestas disponibles.
- **Ver los resultados** de las encuestas, mostrando el número de votos por opción.
- **Autenticación de usuarios** para asegurar que solo los usuarios registrados puedan votar.

## Tecnologías utilizadas

- **Django** - Framework para desarrollo web.
- **Django Rest Framework (DRF)** - Para la creación de la API.
- **SQLite** (por defecto en Django) - Base de datos.
- **JWT (JSON Web Tokens)** o **Token Authentication** - Para la autenticación de usuarios.

## Estructura del Proyecto

Este proyecto tiene los siguientes modelos y relaciones:

- **Survey**: Representa una encuesta, que contiene un título y una fecha de vencimiento.
- **Option**: Cada encuesta tiene múltiples opciones de respuesta.
- **Vote**: Cada voto está asociado a un usuario y a una opción específica de una encuesta.

## Endpoints

- **POST /surveys/**: Crea una nueva encuesta.
- **GET /surveys/**: Obtiene todas las encuestas disponibles.
- **GET /surveys/{id}/**: Obtiene los detalles de una encuesta específica.
- **POST /surveys/{id}/vote/**: Vota por una opción de una encuesta.
- **GET /surveys/{id}/results/**: Obtiene los resultados de una encuesta específica.

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/votify.git
   cd votify
   ```

2. Crea un entorno virtual:

   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

5. Crea un superusuario para poder acceder al panel de administración de Django:

   ```bash
   python manage.py createsuperuser
   ```

6. Corre el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Accede a la API en `http://127.0.0.1:8000/` y prueba los endpoints.

## Autenticación

Para algunos endpoints (como votar), los usuarios necesitan estar autenticados. Puedes obtener un token de autenticación utilizando el siguiente endpoint (si usas JWT):

- **POST /api/token/**: Obtén un JWT al enviar el nombre de usuario y contraseña.

### Ejemplo de solicitud de autenticación:

```bash
POST /api/token/
{
    "username": "usuario",
    "password": "contraseña"
}
```

La respuesta contendrá el token:

```json
{
    "access": "token_aqui",
    "refresh": "token_refresh_aqui"
}
```

Incluye el token en las cabeceras de las solicitudes que requieren autenticación:

```bash
Authorization: Bearer token_aqui
```

## Modelos

### Survey

Representa una encuesta con múltiples opciones.

```python
class Survey(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.title
```

### Option

Opciones disponibles para votar en una encuesta.

```python
class Option(models.Model):
    survey = models.ForeignKey(Survey, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text
```

### Vote

Relación entre usuarios y las opciones que han votado.

```python
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'option']
```

## Contribución

Si deseas contribuir a este proyecto, puedes hacer un **fork** del repositorio y enviar un **pull request** con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT.

