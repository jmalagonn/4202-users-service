# 4202-Grupo4-ArquitecturasAgiles

## Integrantes
| Nombre | Email |
|------|----------------------------------------------|
|Juan Nicolas Malagón Navarro | jn.malagon@uniandes.edu.co |
|Manuel Sanchez Ballen| mg.sanchezb1@uniandes.edu.co |
|Sergio Arturo Perez Rincon | sa.perezr12@uniandes.edu.co |

## Pasos para la ejecución

Descargar los codigos y ejecutar en el editor de su preferencia y en cada uno realizar los siguientes pasos 
- py -m pip --version
- py -m pip install --upgrade pip
  
### crear entorno virtual
- py -m venv venv
- .\venv\Scripts\activate

### ejecutar los requerimientos
- pip install -r requirements.txt  


## ApiGateway
### Descargar código 
- https://github.com/saperezr/ApiGateway
- flask run --port=5000

## Servicio de clientes

### Descargar código 

- https://github.com/jmalagonn/4202-servicio-clientes
- flask run --port=5001

## Servicio de Autenticación
### Descargar código 
- https://github.com/jmalagonn/4202-users-service
- flask run --port=5002


# Flujo del Experimento

1. Realizar el registro de usuario desde Postman

   ### Endpoint
   `POST http://127.0.0.1:5000/gateway/register`

   ### Encabezados
   - `Content-Type: application/json`

   ### Parámetros del Cuerpo
   - `username` (string): El nombre de usuario para la nueva cuenta.
   - `password` (string): La contraseña para la nueva cuenta.
   - `user_type` (int): El tipo de usuario que puede ser 0 o 1

   ### Ejemplo de Cuerpo de Solicitud
   ```json
   {
     "username": "miso",
     "password": "1234",
     "user_type": "1"
   }
   
2. Capturar el `secret_key` y registrarlo en una aplicación para generar el código OTP

   ### Instrucciones
   - Una vez registrado el usuario, recibirás un `secret_key`.
   - Abre tu aplicación de autenticación (Se recomienda usar la extension de google chrome 'Authenticator').
   - Añade una nueva cuenta en la aplicación.
   - Introduce el `secret_key` proporcionado.
   - La aplicación generará un código OTP (One-Time Password) que podrás usar para la autenticación de dos factores.

3. Realizar el login usando OTP

   ### Endpoint
   `POST http://127.0.0.1:5000/gateway/login`

   ### Encabezados
   - `Content-Type: application/json`

   ### Parámetros del Cuerpo
   - `username` (string): El nombre de usuario registrado.
   - `password` (string): La contraseña del usuario registrado.
   - `otp` (int): El código OTP generado por la aplicación de autenticación.

   ### Ejemplo de Cuerpo de Solicitud
   ```json
   {
     "username": "miso",
     "password": "1234",
     "otp": 543075
   }
   ```
4. Capturar el token generado

   ### Instrucciones
   - Después de realizar el login con el OTP, recibirás una respuesta del servidor.
   - La respuesta incluirá un campo `token` con un valor generado.
   - Captura este `token` para usarlo en futuras solicitudes que requieran autenticación.

   ### Ejemplo de Respuesta del Servidor
   ```json
   {
     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "username": "miso"
   }
   ```
5. Realizar la consulta a `clients` para obtener la información del cliente usando el JWT generado

   ### Endpoint
   `GET http://localhost:5000/api/gateway/clients`

   ### Encabezados
   - `Authorization: Bearer <token>`

   ### Instrucciones
   - Usa el token JWT generado en el paso anterior.
   - En la solicitud, incluye el encabezado de autorización con el token JWT.
   - Envía la solicitud para obtener la información del cliente.

   ### Ejemplo de Solicitud
   ```http
   GET /api/gateway/clients HTTP/1.1
   Host: localhost:5000
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
   ### Ejemplo de Response
    El servicio debe retornar la información del cliente:
    ```json
    {
      "id": 125,
      "name": "John Doe",
      "address": "123 Main St. Anytown, USA",
      "email": "john.doe@example.com",
      "phone": "+1234567899",
      "ssn": "123-45-6789",
      "credit_card": {
        "number": "4111111111111111",
        "expiry": "12/25",
        "cvv": "123"
      }
    }
    ```



