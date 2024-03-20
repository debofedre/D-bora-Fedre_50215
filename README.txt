Autora: Débora Fedre
Fecha: 19/03/24
Nombre del proyecto: D-bora-Fedre_50215
Objetivo: Crear una página con recursos editables para crear subtítulos para personas sordas

La página cuenta con los siguientes modelos:

1.	Glosarios: sección con una lista de sonidos.
2.	Guías: sección con una lista de normas.
3.	Acrónimos: sección con una lista de acrónimos comunes en el área de la traducción audiovisual.
4.	Herramientas: sección con una lista de herramientas de subtitulado.

En cada uno de los modelos, los usuarios pueden editar, crear y eliminar elementos de las listas. Además el Glosario cuenta con un buscador al que se puede acceder haciendo clic en la lupita.

Se puede acceder al formulario de cada modelo para agregar campos de la siguiente manera:

•	http://localhost:8000/glosariosForm/
•	http://localhost:8000/guíasForm/
•	http://localhost:8000/acrónimosForm/
•	http://localhost:8000/herramientasForm/

Se puede acceder al buscador del glosario de la siguiente manera:

•	http://localhost:8000/buscarGlosarios/

Datos del usuario administrador:

•	Nombre de usuario: admin
•	Dirección de correo electrónico: admin@gmail.com
•	Contraseña: debo2024

Posibles fallas que ya mencioné en entregas anteriores:

1.	Cuando en el navegador pongo “Localhost:8000”, la página se ve bien.
Sin embargo, cuando pongo http://127.0.0.1:8000/, pareciera que quedaron imágenes superpuestas de otros templates
que fui probando, pero borré todo lo perteneciente a estos templates
y creé un proyecto desde cero con el template que terminé eligiendo, así que no debería verse nada de eso.
2.	Cuando puse git add., me salió el siguiente WARNING (aviso porque no sé si afectará cómo se ve mi página en otros dispositivos):
C:\Users\hpdeb\OneDrive\Escritorio\Tercera_entrega-Débora_Fedre>git add . warning: in the working copy of 'proyecto/aplicacion/templates/aplicacion/index.html', LF will be replaced by CRLF the next time Git touches it

