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

## Licencias

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non lobortis justo. Integer bibendum ex nec metus congue, et venenatis turpis laoreet. Proin rutrum, mauris in varius rutrum, ante nunc auctor ex, ac sagittis leo orci at lectus. Nunc laoreet lacinia orci eget fermentum. Nunc eu sollicitudin neque. Nullam sed turpis finibus, laoreet sem id, semper lectus. Aenean mauris sem, egestas eu ex sed, blandit rhoncus enim. Quisque velit tortor, rhoncus quis nibh sed, sollicitudin rhoncus erat. Praesent at purus nec erat rhoncus pellentesque sit amet at magna. Integer vel aliquet felis. Cras imperdiet sapien id enim pulvinar tincidunt. Quisque metus sem, condimentum eget sollicitudin ut, porta sed ante. Sed molestie lacus sit amet euismod lobortis. Maecenas congue imperdiet interdum. 

## Pruebas

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non lobortis justo. Integer bibendum ex nec metus congue, et venenatis turpis laoreet. Proin rutrum, mauris in varius rutrum, ante nunc auctor ex, ac sagittis leo orci at lectus. Nunc laoreet lacinia orci eget fermentum. Nunc eu sollicitudin neque. Nullam sed turpis finibus, laoreet sem id, semper lectus. Aenean mauris sem, egestas eu ex sed, blandit rhoncus enim. Quisque velit tortor, rhoncus quis nibh sed, sollicitudin rhoncus erat. Praesent at purus nec erat rhoncus pellentesque sit amet at magna. Integer vel aliquet felis. Cras imperdiet sapien id enim pulvinar tincidunt. Quisque metus sem, condimentum eget sollicitudin ut, porta sed ante. Sed molestie lacus sit amet euismod lobortis. Maecenas congue imperdiet interdum. 






