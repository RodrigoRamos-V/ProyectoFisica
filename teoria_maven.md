# Teoria de Maven

## Que es Maven?
Maven es una herramienta de gestion y automatizacion de proyectos Java.  
Se usa principalmente para compilar, empaquetar, probar y gestionar dependencias de forma automatica.  
Fue desarrollada por Apache y es muy utilizada en proyectos profesionales de Java porque organiza todo el proceso de construcción del software.

Maven trabaja con un archivo principal llamado `pom.xml' donde se define la información del proyecto sus dependencias complementos y configuraciones.

## Por que usar Maven?
Maven facilita mucho el trabajo en proyectos grandes o con varios modulos.  
Algunas razones por las que vale la pena usarlo son:

- **Gestión automática de dependencias:** No es necesario descargar manualmente las librerías, Maven las obtiene de un repositorio central.  
- **Estandarización:** Todos los proyectos siguen una misma estructura.  
- **Automatización:** Permite compilar, probar y empaquetar el código con simples comandos.  
- **Integración con IDEs:** Funciona perfectamente con Eclipse, IntelliJ o VS Code.  
- **Facilita el trabajo en equipo:** Todos los desarrolladores usan la misma configuración y versión de librerías.

En resumen, **ahorra tiempo y evita errores** al manejar dependencias y configuraciones de forma automática.

## Cuando usar Maven?
Se recomienda usar Maven cuando:
- Se trabaja en **proyectos medianos o grandes en Java**.  
- Hay **múltiples dependencias externas** (librerías de terceros).  
- Se necesita **automatizar tareas repetitivas** como compilar, ejecutar pruebas o crear archivos `.jar` o `.war`.  
- El proyecto debe ser **fácil de compartir y mantener** en equipo.

Para proyectos muy simples, puede no ser necesario, pero en cuanto el proyecto crece, Maven se vuelve una gran ventaja.

## Como usar Maven?

##Comandos básicos

mvn clean: Elimina el directorio target y todo su contenido. Es útil para empezar una compilación desde cero. 
mvn compile: Compila el código fuente y genera los archivos .class en el directorio target/classes. 
mvn test: Ejecuta las pruebas unitarias definidas en el proyecto. 
mvn package: Empaqueta el proyecto compilado en un archivo, como un .jar o .war. 
mvn install: Compila el proyecto, empaqueta el artefacto y lo instala en el repositorio local. Esto lo hace disponible para otros proyectos en la misma máquina. 

##Comandos comunes y avanzados

mvn archetype:generate: Crea un nuevo proyecto a partir de una plantilla (archetype). 
mvn dependency:tree: Muestra un árbol de todas las dependencias del proyecto, lo que ayuda a depurar conflictos. 
mvn javadoc:javadoc: Genera la documentación Javadoc del proyecto. 
mvn install: Instala el artefacto en el repositorio local para que pueda ser utilizado por otros proyectos en tu sistema. 
mvn deploy: Despliega el artefacto en un repositorio remoto. 

##Combinar comandos

mvn clean install: Una combinación común que primero limpia el proyecto, luego compila, prueba y empaqueta, y finalmente instala el artefacto en el repositorio local. 
Opciones de línea de comandos
-Dtest=NombreDeTuClaseDeTest: Ejecuta solo una prueba específica. 
-X o --debug: Ejecuta Maven en modo de depuración para obtener información detallada. 
-q o --quiet: Suprime la mayor parte de la salida, mostrando solo los mensajes de error. 
-P <nombre_perfil>: Activa un perfil de Maven específico definido en el archivo pom.xml. 
mvn -version: Muestra la versión de Maven instalada. 
