# Teoría de Git

## Que es Git?
sistema de control de versiones distribuido, gratuito y de código abierto que se utiliza para rastrear los cambios en los archivos de un proyecto, principalmente código fuente.
Es muy útil para que los equipos de desarrolladores colaboren de manera eficiente en el mismo proyecto, ya que permite a múltiples personas trabajar simultáneamente, gestionar conflictos y mantener un historial detallado de todos los cambios realizados. 

## Por que usar Git?
Usar Git tiene muchas ventajas:
- Evita perder versiones antiguas del trabajo.
- Permite trabajar con otras personas sin pisar los cambios.
- Se puede tener un registro completo del progreso.
- Es muy útil cuando se quiere probar algo nuevo en una rama y no afectar el proyecto principal.
- Con plataformas como GitHub o GitLab, se puede compartir el proyecto fácilmente.

## Cuando usar Git?
Git se usa practicamente siempre que uno trabaja en proyectos que cambian con el tiempo especialmente si son de programacion.  
Tambien es util si uno trabaja solo pero quiere mantener un historial de lo que ha hecho o si trabaja en grupo y necesita coordinar los cambios.

## Como usar Git? 
       
   
## 1. Iniciar un área de trabajo
- **clone** → Clonar un repositorio en un nuevo directorio  
- **init** → Crear un repositorio Git vacío o volver a inicializar uno existente  

## 2. Trabajar en la corriente (zona de trabajo)
- **add** → Agregar el contenido de archivos al índice (área de preparación)  
- **mv** → Mover o renombrar un archivo, directorio o enlace simbólico  
- **restore** → Restaurar archivos del árbol de trabajo  
- **rm** → Eliminar archivos del árbol de trabajo y del índice  

## 3. Examinar el historial y el estado  
*(véase también: `git help revisions`)*
- **bisect** → Usar una búsqueda binaria para encontrar el *commit* que introdujo un error  
- **diff** → Mostrar los cambios entre *commits*, o entre el *commit* y el árbol de trabajo  
- **grep** → Imprimir líneas que coincidan con un patrón  
- **log** → Mostrar los registros de *commits*  
- **show** → Mostrar distintos tipos de objetos  
- **status** → Mostrar el estado del árbol de trabajo  

## 4. Hacer crecer, marcar y ajustar tu historial común
- **backfill** → Descargar objetos faltantes en un clon parcial  
- **branch** → Listar, crear o eliminar ramas  
- **commit** → Registrar los cambios en el repositorio  
- **merge** → Unir dos o más historiales de desarrollo  
- **rebase** → Reaplicar *commits* sobre otra base  
- **reset** → Restablecer la cabeza actual (*HEAD*) al estado especificado  
- **switch** → Cambiar entre ramas  
- **tag** → Crear, listar, eliminar o verificar una etiqueta firmada con GPG  

## 5. Colaborar  
*(véase también: flujos de trabajo de ayuda de git)*
- **fetch** → Descargar objetos y referencias desde otro repositorio  
- **pull** → Obtener e integrar cambios desde otro repositorio o rama local  
- **push** → Actualizar las referencias remotas junto con los objetos asociados  
