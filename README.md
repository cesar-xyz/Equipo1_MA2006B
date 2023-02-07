<div align="center">

# Implementación de criptografía de clave pública para protección de comunicaciones con IoT en entornos de monitoreo y consumo de energía.

Eugenio Andrade Lozano - A01721296,
César Guillermo Vázquez Alvarez - A01197857,
Federico Medina García Corral - A01721441,
José Andrés Meyer Crabtree - A01366785,
Diego Paasche Portillo - A01028103,
Luis Leopoldo Jiménez Pérez - A01275004

En nuestro caso, el objetivo principal es implementar protocolos de criptografía de clave pública para proteger el intercambio de datos de sensores en ambientes IoT, donde se busca que esto sea de manera balanceada. Concretamente, datos que tienen que ver con el estado de dichos sensores dado cada cierto tiempo, así como la actualización de su firmware, por lo que de entrada se busca que ese intercambio sea automatizado. Concretamente, esos datos tienen que ver con el monitoreo y consumo de energía, los cuales son considerados datos sensibles.

[Requirimientos](#requirimientos) •
[Uso y disposición del repositorio](#uso-y-disposición-del-repositorio) •
[Pruebas](#pruebas) 

</div>

## Requirimientos

Primero vamos a analizar la topología con la que estamos trabajando, tenemos 2 auditores, un centro de control y conexión vía Wi-Fi. Para poder utilizar este servicio, los 2 auditores serán 2 Raspberry Modelo B, el cual está compuesto por un procesador ARMv8 con 4 puertos USB, conexión HDMI, ethernet, Wi-Fi, Bluetooth entre otras cosas, su procesador de 64 bits soporta el rango completo de distribución ARM GNU/Linux y Microsoft Windows 10, de igual manera, soporta herramientas de software como Python, Gnu, entre otros. Recomendamos utilizar el Raspberry Modelo B como mínimo requisito y de ser posible, utilizar Raspberry de nuevas generaciones así como lo es la Raspberry Modelo B+. El centro de control es el encargado de tener la base de datos, en este caso, lo recomendado sería una computadora ya sea portátil o de escritorio con los siguientes componentes para poder utilizar este servicio sin ningún problema. Un SSD y memoria RAM de 8 GB (la ventaja de estos 2 elementos es que se pueden encontrar a precios bajos), hablando ahora sobre el procesador, el requerimiento mínimo para poder correr el servicio es un Intel Core i3, si el centro de control se encuentra en una computadora de escritorio, de igual manera se necesitará tener un monitor, realmente aquí cualquier monitor logra funcionar para este servicio, el requerimiento mínimo sería que fuera al menos de 60 Hz, que es lo más normal en el mercado, ya que para esto, tener un monitor de más de 60 Hz pueda ser que sea de sobra. Para la tarjeta de video no es necesario ya que con el procesador i3 es más que suficiente, por otra parte, es necesario y un requisito indispensable el utilizar el lenguaje de programación Python 3, como recomendación podemos decir que siempre se utilice la versión más nueva que en este caso es la 3.11 que fue lanzada en Enero de 2023, dentro de esto, también como requerimiento es indispensable utilizar Django el cual es un framework de desarrollo web de código abierto. Cabe recalcar que estos son los requerimientos mínimos para poder utilizar este servicio, es recomendable tener mejores componentes. 

## Licencias.

En este sistema se utilizaron solamente librerias y software de uso público, a pesar de que sean de uso público se sabe que las librerías y el software utilizado tienen un excelente uso y entregan excelentes resultados, es por eso, que decidimos utilizarlos para la elaboración de este servicio de encriptamiento mediante curva elíptica;
1. Python 3 
2. Numpy 1.21.5
3. Pandas 1.4.1
4. matplotlib.pylot 3.4 
5. datetime 
6. hashlib 1.5
7. Socket 3.3
8. Time (Default)
9. Json 1.6.2
10. Django 4.0
11. Pathlib 1.0 
12. Os

Numpy es una librería de Python para el cálculo numérico y el análisis de datos. Pandas sirve para el manejo y análisis de estructuras de datos. Pyplot es un módulo Matplotlib que propone varias funciones sencillas para añadir elementos tales como líneas, imágenes o textos a los ejes de un gráfico. Datetime es una librería la cual permite el manejo y manipulación de fechas y horas. Hashlib nos sirve para hashear como bien el mismo nombre nos puede dar una idea, gracias al importar socket en Python podemos generar un enlace entre 2 aplicaciones para que de esta manera tengan comunicación. Time, no es lo mismo que datetime, la librería time nos sirve para retornar el valor en fracciones de la suma del sistema y el tiempo de CPU del usuario del proceso actual. Ahora, vamos a hablar de Django que es una de la librerías que más destacan dentro de este servicio, Django nos sirve para construir cualquier tipo de sitio web de manera eficiente, por otro lado, tenemos Json el cual es una librería que sirve para transferir información a través de la web y para almacenar ajustes y configuración, este, de igual forma es un formato ligero de intercambio de datos. La librería pathlib, sirve para las clases que representan rutas del sistema de archivos con semántica apropiada para diferentes sistemas operativos. Por último tenemos Os, que es una librería que provee una manera versátil de usar funcionalidades dependientes del sistema operativo.


## Instalación, compatibilidad y dependencias

Para poder utilizar este servicio de encriptación mediante curvas elípticas, se instaló Python 3 el cual es el lenguaje de programación con el que se trabajó este proyecto, Python 3 es de uso público así es que es muy probable que no se tenga ningún problema en descargarlo ni en utilizarlo, de igual manera se utilizaron librerías de uso libre las cuales son; 

1. Numpy importamos a np 1.16.0 a 1.24.0
2. Pandas importamos a pd 1.3.0. a 1.5.3
3. Matplotlib.pylot importamos a plt 3.0 a 3.6
4. datetime (versión viene por default)
5. hashlib importamos sha256 1.5 a 1.5.2
6. Socket 3.3 a 3.7 
7. Time (Default)
8. Json 1.1.1 a 1.6.3
9. Django importamos get_asgi_application, admin, include, path 3.1 a 4.1 
10. Pathlib importamos Path 0.6 a 1.0.1

El funcionamiento de cada librería viene explicado en el apartado anterior “Licencias”, de igual forma vienen las versiones de cada una de estas librerías con un rango de versiones anteriores a versiones mas nuevas que tienen compatibilidad con este servicio de encriptación 
Es necesario que al descargar estas librerías la computadora que se esté utilizando estén conectadas a internet para poder importarlas dentro de Python, así mismo, para poder utilizar este servicio se necesita una buena conexión a internet ya que de esta manera es como se están mandando los archivos encriptados del centro de control hacia los auditores. 
Para la instalación de las Raspberry, es necesario meter las trazas a estas para que de esta forma se pueda compartir la información de los auditores a el centro de control, cabe recalcar que las trazas (base de datos) tuvo un pre procesamiento antes de meterlas a las Raspberry para darles el formato correcto para el envío de información y se añaden al utilizar Python dentro de las Raspberry.

## Documentación de la Arquitectura del Código

Dentro del código se encuentran diferentes archivos y carpetas que de manera unida forman el API y la arquitectura que se decidió hacer. En la parte principal se encuentra la carpeta "Archivos_trazas", donde se encuentran los archivos csv que se utilizaron para hacer pruebas y saber como se envía la información. También, esta la carpeta Auditores, donde dentro está el código que se encarga de mandar las solicitudes a la API, verificar y tomar la acción correspondiente con base en esto, ya sea guardar la información o no aceptarla. La carpeta "Exploracion" contiene los archivos que se utilizaron para entender mejor la información que se va a recibir, incluye gráficas y pruebas JSON, hashing y de ECDSA. Los archivos .gitignore, README.md y requirements.txt son archivos que ayudan a facilitar y hacer los archivos más limpios. El archivo .gitignore incluye todos los tipos de archivos que se no se busca guardar, por ejemplo la base de datos local, el archivo README.md es justo el archivo donde toda esta información se está mostrando, finalmente el requirements.txt guarda todas las librerias que se tienen que instalar para que el código se pueda correr. Finalmente, la carpeta más importante es la de "main", aquí se encuentran todos los modelos y la comunicación entre ellos. Cada carpeta representa un modelo específico y todos tienen los mismos archivos. Los archivos son:

- **Carpeta “migrations”**: Contiene las migraciones (cambios en los modelos) que se han hecho, esto ayuda a que la base de datos cambie al mismo tiempo que se cambian los modelos.
- **__init__**.py: Permite guardar la información dentro de la carpeta para importarla como si fuera un paquete de python.
- **admin.py**: Registra el modelo en el sitio del administrador junto con la información que se quiere mostrar.
- **models.py**: Están los modelos (tablas) que se están creando. Incluye los campos del modelo y su representación como texto.
- **serializers.py**: Se encarga de convertir la información que se recibe (en formato JSON) a el formato que usa Django y vice versa. Esto para poder guardar la información en la base de datos y si se busca visualizarla que también se pueda.
- **viewsets.py**: Se encarga de permitir hacer las solicitudes, las más comunes siendo POST para crear información, GET para obtener información, PUT o PATCH para actualizar información y DELETE para borrar. Dentro también incluye los permisos para las acciones.
- **urls.py**: Contiene los urls que se van a agregar de su respectivo modelo para poder mandar la solicitud.

Modelos:
* auditors (Auditores)
* certificates (Certificados)
* control_center (Centro de Control)
* entries (Entradas)
* output (Salida o Respuesta)
* public_keys (Llave Pública)
* users (Usuarios)

## Comandos para Correr Servidor

1. pip install -r requirements.txt
2. cd main
3. python3 manage.py migrate
4. python3 manage.py runserver



