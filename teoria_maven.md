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

### 🔹 1. Instalar Maven
- Descarga desde la página oficial de Apache Maven.  
- Configura la variable de entorno `PATH` para que puedas usar el comando `mvn` en la terminal.  
- Verifica la instalación:
  ```bash
  mvn -version
