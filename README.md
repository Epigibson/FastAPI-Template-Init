Este proyecto es una aplicación web API RESTful que utiliza el framework FastAPI para Python y la base de datos NoSQL MongoDB. Está diseñado para ser ejecutado en un entorno de Docker y se incluye un archivo docker-compose.yml para facilitar la configuración.

Requerimientos:
Docker
Docker Compose

Configuración:
Clona este repositorio: git clone https://github.com/tu_usuario/tu_proyecto.git
Entra en el directorio del proyecto: cd tu_proyecto
Crea un archivo .env con las variables de entorno necesarias (ver sample.env para un ejemplo)
Ejecuta el comando docker-compose up -d para construir y ejecutar los contenedores de Docker.

Uso:
Para acceder a la interfaz de la API, abre tu navegador y entra en http://localhost:8000/. Desde aquí, podrás probar los endpoints de la API utilizando una herramienta como Postman o cURL.

API:
La API expone los siguientes endpoints:
/items: CRUD para items en la base de datos MongoDB. Incluye endpoints para obtener un item por ID, crear un nuevo item, actualizar un item existente y eliminar un item existente.
Contribución

¡Agradecemos cualquier contribución a este proyecto! Si deseas informar de un problema o sugerir una nueva función, utiliza la sección "Issues" en este repositorio. Si deseas contribuir al código fuente, realiza una solicitud de extracción (PR) y haremos lo posible por revisarla lo antes posible.

Licencia:
Este proyecto se encuentra bajo la Licencia MIT. Consulta el archivo LICENSE para más información.
