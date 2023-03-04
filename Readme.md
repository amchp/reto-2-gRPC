# Reto 2

![Arquitectura de aplicación](https://github.com/amchp/reto-2-gRPC/blob/main/img/Diagrama.drawio.png)


Esta es una aplicación de archivos. La aplicación va a ser con una arquitectura MVC implementada con microservicios. Primero, tenemos el Frontend o la vista que es donde el usuario va a ver la información desde el navegador. Este podria ser programado con HTML y CSS solamente pero vamos a usar postman para ahorrar tiempo. Esta se comunica con él un servidor el Controlador atreves de una conexión HTTP. El Controlador es el controlador del proyecto que llama los diferentes microservicios. Se programará usando Node.js. Él se comunicará con tres microservicios. El microservicio de usuarios, el de archivos, y el de buscador. Cada uno de estos microservicios implementaran su proprio servicio.  Las cuatro aplicaciones se comunican por gRPC. Cada microservicio tiene su propia base de datos.

Este repositorio tiene los tres archivos con Readmes de como montarlos.
