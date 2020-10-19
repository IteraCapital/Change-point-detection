# Change-point-detection

Descripción

En este repositorio se podrá encontrar el código generado para hacer un estudio del change point detection. El propósito al que se quiere llegar es generar variables que en un punto futuro nos ayuden para la separación de variables, asi como el punto exacto en el cual el cambio de tendencia existe. Para poder llegar a estos resulatdos primero tenemos que decir que se utiliaron los metodos del change point que son el de segmentación binaria y el de segmentación basada en ventanas (binary segmentation & window-based segmentation).
Creamos dos funciones que nos permiten encontrar estos resultados de forma clara y solo al hacer llamado de la función que necesites. Las dos funciones son en base a los métodos analizados que como dijimos anteriormente son los de segmentación binaria y el de segmentación basada en ventanas.

Instalar dependencias. 

En la terminal se debera de instalar la libreria de ruptures.

    pip install ruptures

Funcionalidad

El ejemplo mostrado durante el pryecto es el caso del par "EURUSD", es de interés general saber cuando ocurren los cambios estructurales dentro de la serie de tiempo. Asi como saber la confirmación de la tendencia. En base a la libreria de ruptures creamos una función a la cual le tienes que entregar una variable Esta variable es la serie de tiempo a analizar. En base a esta serie de tiempo se haran los calculos necesarios para entregar al final los puntos dentro de la serie en donde ocurrieron cambios estructrales o posibles confirmaciones de tendencia.

Autores

Creado por Carlos Alfonso Barboza Espinoza y Jaime Eduardo Vázquez Guzmán, estudiantes de Ingeniería Financiera en la universidad ITESO de México.

Licencia

GNU General Public License v3.0

Los permisos de esta licencia están condicionados a poner a disposición el código fuente completo de los trabajos con licencia y las modificaciones, que incluyen trabajos más grandes que utilizan un trabajo con licencia, bajo la misma licencia. Se deben conservar los avisos de derechos de autor y licencias. Los contribuyentes proporcionan una concesión expresa de derechos de patente.

Contacto

Para obtener mas información acerca de este repositorio, contactame a traves de caulquiera de los correos siguientes:

casoso1010@gmail.com
jaimevazquezguz37@gmail.com
