<h1 align='center'>
 <b>Review Insights - Análisis de Reseñas y Recomendaciones</b>
</h1>


![Review](https://github.com/mariangigena/proyectogrupal/blob/main/imagenes/Banner%20de%20LinkedIn%20Sencillo%20Tecnolog%C3%ADa.png).


## 1. Proyecto: El inicio 

## **Introducción**

`Review Insights` es una empresa de análisis de datos que tiene como objetivo proporcionar información valiosa a otras empresas sobre las reseñas y recomendaciones que reciben de los usuarios en plataformas como Yelp y Google Maps. Nuestro enfoque principal es recopilar, analizar y ofrecer información significativa sobre las experiencias de los usuarios en diferentes comercios.

## **Contexto**

La industria vinícola se destaca por su enfoque único en la valoración de la marca a través de opiniones personales y recomendaciones de expertos en guías especializadas, así como del poderoso efecto del boca a boca entre los consumidores. Estados Unidos, conocido tradicionalmente por su cultura cervecera, ha experimentado un crecimiento constante en el consumo de vino en los últimos años. Esta tendencia positiva representa una oportunidad valiosa para comercializar productos vinícolas en el país.

La capacidad de identificar y clasificar a los `reviewers` en profesionales o consumidores circunstanciales, junto con el análisis comparativo de las calificaciones otorgadas por ambos grupos, permitirá a las empresas entender mejor el impacto de las opiniones expertas y del público general en la percepción y éxito de sus establecimientos.

Adicionalmente, la estimación realizada por estudios de marketing, sobre el aumento del consumo de vino en los años venideros fortalece aún más la relevancia del proyecto. La información proporcionada por esta plataforma será invaluable para las empresas vinícolas en sus esfuerzos de marketing, toma de decisiones estratégicas y mejora continua de la calidad del servicio.

## **Problematica**:

En el contexto de la industria vinícola en Estados Unidos, las empresas enfrentan el desafío de evaluar la percepción y opinión de los usuarios sobre sus bodegas y bares o clubes de vinos. La creciente tendencia en el consumo de vino en el país, junto con la importancia que los clientes otorgan a las reseñas y recomendaciones, demanda una comprensión profunda de las experiencias vividas por los usuarios en estos establecimientos.

La falta de una herramienta efectiva para identificar a aquellos reviewers con expertise en vinos y diferenciarlos de los consumidores circunstanciales, así como la necesidad de evaluar las calificaciones promedio otorgadas por ambos grupos para distintas bodegas y bares de vino, representa una problemática crucial para las empresas del sector. Además, es esencial comprender qué aspectos priorizan los reviewers en sus comentarios, especialmente en los primeros y últimos, para mejorar la calidad del servicio y la satisfacción del cliente.



## **Alcances y Objetivo**:

Vamos a tomar los datos de todos los estados de Estados Unidos como primer instancia, porque el volumen de los mismos nos ayuda para un analisis mas significativo de los datos.
El objetivo principal de nuestro proyecto, es proporcionar a las empresas del sector vinícola una valiosa visión sobre las experiencias y opiniones de los usuarios en relación con bodegas y bares o clubes de vinos en Estados Unidos. A través de un análisis exhaustivo de las reseñas y recomendaciones, buscamos identificar a aquellos reviewers que han puntuado establecimientos vinícolas de manera significativa, determinando así a los conocedores con expertise en vinos.

Uno de nuestros enfoques clave es la categorización de los`reviewers` en dos grupos distintos: profesionales y consumidores circunstanciales. Mediante esta clasificación, pretendemos evaluar el score promedio otorgado por cada grupo con relación a diferentes bodegas o bares de vino. De esta manera, podremos identificar posibles diferencias en sus opiniones, permitiendo a las empresas entender mejor el impacto de las opiniones expertas y del público general en la percepción y éxito de sus establecimientos
 

Además, en nuestro análisis, prestamos especial atención a qué aspectos priorizan los reviewers en sus comentarios, especialmente enfocándonos en los primeros y últimos comentarios. Esto brindará información valiosa a las empresas para comprender qué aspectos de sus servicios o productos reciben mayor atención y cómo pueden mejorar la experiencia del cliente.

Como se explicó en el contexto, el mercado vitivinícola, caracterizado por su énfasis en la valoración de la marca a través de opiniones personales y recomendaciones de expertos, ofrece una oportunidad única para este proyecto.

Nuestra misión es convertir el conocimiento de las experiencias del cliente en una herramienta valiosa para el éxito empresarial en el dinámico y creciente mercado vinícola de Estados Unidos.


## **KPI`s**

Los KPIs que encontramos mediante el analisis exploratorio de los datos fueron :

1. **Cantidad de Reviewers Identificados como Conocedores de Vinos:** Este KPI está directamente relacionado con nuestro objetivo principal. Buscamos identificar a los usuarios que poseen experiencia y conocimiento en el mundo del vino. Esta métrica nos permite aprovechar opiniones de expertos que aportan un alto valor en sus evaluaciones.Una vez que los identifiquemos queremos llegar a ver un aumento sucesivo de los mismos mediante el uso de la herramienta, incrementando de manera progresiva proponiendo un aumento del 10%


2. **Distribución de Reviewers según su Categoría:**  Este KPI proporciona información crucial sobre la composición de los usuarios que realizan reseñas. Al analizar esta distribución, podremos determinar si estamos atrayendo principalmente a reviewers profesionales con un conocimiento sólido en vinos o si la mayoría son consumidores casuales.Queremos medir localizaciones de esos comentarios por lo que apuntamos a que a mayor rango geografico y mayores reseñas hay un potencial de expertis. La idea es aumentar la media de los lugares con mas de 3 ubicaciones, ya que se vio que la mayor cantidad de reviews esta en dos ubicaciones. 


3. **Score Promedio de Expertos y Aficionados:** Al comparar los scores promedio entre reviewers profesionales y amateurs, estaremos en condiciones de evaluar el impacto que tienen las opiniones de los expertos en la calificación general de bodegas y bares de vinos. Este KPI nos ayudará a comprender si las voces de los conocedores influyen significativamente en la percepción del lugar.El score promedio debe ser mayor y aumentar (mas del 10%) con el tiempo para que sea significativo.Tomamos en cuenta que un score mas alto de los no conocedores no es un indice a tener en cuenta en las reseñas.


4. **Comparativa de Score Promedio de Bodegas o Bares de Vinos:** Este KPI nos permitirá identificar y destacar los establecimientos mejor valorados por los revisores. Esta información será extremadamente valiosa para las empresas, ya que podrán ajustar sus estrategias y mejorar su desempeño basándose en los aspectos que destacan en las opiniones positivas.El score deberia mantenerse o aumentar (mas del 5%) para que este indicador muestre mejora.

5. **Volumen de Reseñas por Establecimiento:** Este KPI refleja la popularidad y la satisfacción general de los clientes en cada lugar. Cuantas más reseñas reciba un establecimiento, más visible será su experiencia para el público en general. Este KPI se convierte en un barómetro clave para evaluar la aceptación del público y la calidad del servicio ofrecido.Se piensa como ramping de mejora que haya una mejora del 10% en un principio.


## **Implementación del Stack Propuesto**

Hemos seleccionado un stack tecnológico que nos permitirá llevar a cabo el análisis de datos y la generación de modelo de manera efectiva:

1. ` Power BI`: Utilizaremos Power BI para crear visualizaciones interactivas y paneles de control que permitan a las empresas explorar y entender los datos de manera intuitiva. Es la  herramienta de visualización que mejor manejamos con el equipo.

2. `ETL Automatizado`: Implementaremos un proceso ETL (Extract, Transform, Load) automatizado en la nube para recopilar y procesar los datos de reseñas y recomendaciones de las plataformas en línea. Decidimos utilizar la que ya nos brinda Azure.

3. `Servicios en la Nube`: Almacenaremos y procesaremos los datos en servicios en la nube de `Azure` para garantizar su disponibilidad y escalabilidad.La eleccion estuvo basada en la cantidad de servicios que nos ofrecia el proveedor y la cantidad de documentacion y las recomendaciones de otros usuarios acerca del cobro de los servicios.

4. `Python y Librerías`: Utilizaremos el lenguaje de programación Python junto con librerías como pandas, NumPy y scikit-learn para realizar el análisis de datos y la creación del modelo.
   
5. `Streamlit`: La utilizaremos para la visualización de datos y la creación de interfaces de usuario de manera rápida y sencilla, la elegimos debido a su facilidad de uso y su capacidad para crear aplicaciones de manera eficiente sin la necesidad de conocimientos profundos en desarrollo web.![App](https://review-insights.streamlit.app/)

6. `Trello`: elegimos esta herramienta para poder ordenar el trabajo en equipo y para poder seguir un flujo de trabajo.![Tablero](https://trello.com/b/Wgepholb/google-yelp)

7. `Canva`: usamos esta herramienta para poder apoyarnos visualmente en las demos del proyecto, así como para la generación de imágenes de nuestra autoría.


## 2. **Proceso ETL en Azure Data Warehouse**

El proceso ETL (Extract, Transform, Load) del almacén de datos consistió en incorporar y procesar conjuntos de datos de Google y Yelp. El objetivo era crear un conjunto de datos completo para el análisis y la comprensión de los establecimientos relacionados con el vino. El proceso se diseñó para garantizar la precisión de los datos, las actualizaciones incrementales y una transformación eficaz.
![Esquema](https://github.com/mariangigena/proyectogrupal/blob/main/imagenes/Azure2.png)
### **Ingesta y almacenamiento de datos**

El almacén de datos se construyó utilizando los servicios Azure, y los conjuntos de datos de Google y Yelp se introdujeron en contenedores de bloques para su almacenamiento y posterior procesamiento. este es el esquema de las tablas con sus claves : ![Diagrama](imagenes/reviews_insights_schema.png)

### **Actualizaciones Incrementales y ETL Básico**

Para los conjuntos de datos que constituían tablas de dimensiones, se implementó un enfoque de actualización incremental. Esto se logró mediante la función Dataflow de Azure Data Factory. Dataflow permite la creación de pipelines que aplican operaciones ETL básicas a un conjunto de datos y luego transfieren los datos transformados a una base de datos MySQL. Este enfoque resultó eficaz para gestionar tablas de dimensiones en las que los cambios de datos a lo largo del tiempo son menos frecuentes.

### **Actualizaciones incrementales impulsadas por canalizaciones**

Para los conjuntos de datos que requerían transformaciones y actualizaciones más complejas, se adoptó un enfoque de canalización. Esto implicaba la supervisión de una carpeta designada dentro del contenedor de bloques. Cada vez que llegaba un nuevo conjunto de datos, se activaba la ejecución de un cuaderno en Azure Databricks. El cuaderno contenía lógica ETL avanzada para actualizar varias tablas de la base de datos. Este enfoque basado en canalizaciones resultó especialmente útil para actualizar las tablas de dimensiones y hechos.

### **Control de calidad de los datos**

El control de calidad de los datos fue una consideración clave durante todo el proceso ETL. Para garantizar la integridad de los datos cargados, se comprobaron y gestionaron las filas duplicadas. Esta verificación se realizó de forma programática, ya fuera mediante automatización o secuencias de comandos en Azure Databricks.

### **Verificación automatizada y guionizada**

El proceso de verificación consistía en comprobar si había filas duplicadas antes de cargarlas en la base de datos. En caso de duplicación, la carga de datos se gestionaba automáticamente o mediante scripts personalizados. Este paso era crucial para mantener la precisión y coherencia de los datos.

Al estructurar el proceso ETL de esta manera, pudimos gestionar eficazmente los datos de múltiples fuentes, aplicar las transformaciones adecuadas, garantizar actualizaciones incrementales y mantener los estándares de calidad de los datos. Este sólido proceso ETL sentó las bases para un análisis preciso y profundo dentro del almacén de datos.

Para más detalles sobre los scripts, pipelines y transformaciones específicos aplicados durante el proceso ETL, consulte el código y la documentación pertinentes en el repositorio del proyecto[Código](https://github.com/mariangigena/proyectogrupal/blob/main/scripts/metadata_sitios_unir_jsons.ipynb)

### **ETL final para alimentar los modelos**

Para llevar a cabo un análisis efectivo de las reseñas, implementamos un proceso de ETL detallado que nos permitió recopilar, limpiar y consolidar datos de múltiples fuentes en un conjunto de datos final coherente y relevante.

**Extracción de Datos:**

Primero, iniciamos el proceso de ETL con la extracción de datos de múltiples fuentes, que incluyeron conjuntos de datos de Google, Yelp y Wine Magazine. Estas fuentes proporcionaron una amplia variedad de reseñas relacionadas con negocios, pero nuestra atención se centró en las categorías que involucraban la palabra "vinos".

**Transformación de Datos:**

1. **Filtrado de Categorías Relevantes:** Inicialmente, aplicamos un filtro para seleccionar negocios específicos relacionados con vinos. Las categorías de interés incluyeron "winery," "vineyard," "wineries," y "wine tasting room."

2. **Limitación de Categorías:** Para mantener la coherencia y relevancia en nuestro conjunto de datos, restringimos las categorías a aquellas que tenían un máximo de tres categorías asociadas.

3. **Selección de Reseñas:** Utilizando los criterios anteriores, filtramos las reseñas de los negocios seleccionados, lo que nos permitió centrarnos en las revisiones que eran más relevantes para nuestro estudio.

4. **Limpieza de Datos:** Realizamos una limpieza exhaustiva de los datos, eliminando campos no relevantes y asegurándonos de que la calidad de los datos fuera alta. Esto incluyó la normalización de campos como "state" para mantener la consistencia.

5. **Concatenación de Conjuntos de Datos:** Para enriquecer nuestra base de datos con una variedad de reseñas específicas, combinamos los tres conjuntos de datos: Google, Yelp y Wine Magazine.

**Carga de Datos:**

Con el conjunto de datos final de "business reviews" preparado, eliminamos duplicados para garantizar la integridad de los datos y crear un conjunto limpio y coherente listo para su análisis.

Este proceso de ETL nos permitió reunir y preparar cuidadosamente los datos para el análisis subsiguiente, proporcionando un conjunto sólido de reseñas y detalles comerciales específicos que han sido fundamentales para nuestras evaluaciones y conclusiones en este proyecto.

## 3. **Exploratory Data Analysis**

### Análisis Preliminar

Para realizar este analisis utilizamos Python y sus librerias : pandas, seaborn, matplotlib y wordcloud. Y para la visualizacion de los Kpis y del analisis Power BI. Los analisis que se detallan a continuacion son extraidos de la carpeta [EDA](https://github.com/mariangigena/proyectogrupal/tree/main/EDA)de este repositorio.

 `Origen de los Datos `: Se trabajó con dos conjuntos de datos, uno de Google Maps y otro de Yelp, que contenían reseñas de negocios y lugares. Aunque no fue posible unirlos directamente, se identificó que ambas fuentes compartían el componente de reseñas.

 `Insights de Yelp `: Se destacaron algunos hallazgos del análisis de los datos de Yelp, como la prevalencia de reseñas que mencionaban problemas en lugar de elogios. Además, se notó la falta de usuarios con el estatus "elite" en 2022 y se observó que los usuarios con un gran número de seguidores o reseñas podrían considerarse "influencers". También se notó que los usuarios que otorgaban calificaciones extremas (1 o 5 estrellas) no habían realizado muchas reseñas y carecían de amigos en la plataforma.

 `Palabra Clave "Wine" `: Se identificó la palabra clave "Wine" en las reseñas y se decidió centrar el análisis en torno a esta palabra clave debido a su presencia en varias categorías.

 `Datos de Google Maps `: En el análisis de los datos de Google Maps, se notaron valores nulos en algunas columnas, lo que llevó a una selección cuidadosa de las columnas a utilizar. Se observaron palabras relacionadas con el servicio y la gastronomía en las reseñas, lo que llevó a la elección de "Wine" como enfoque.

 `Categoría "Wine" `: Se observó que todas las categorías relacionadas con "Wine" tenían calificaciones promedio por encima de 4, lo que indicaba calificaciones positivas.

### Análisis Completo

 `Imputación de Datos `: Se acordó imputar valores nulos en las reseñas con "Not Description" debido a su impacto significativo en el análisis.

 `Palabras Clave Frecuentes `: Se identificaron palabras clave más utilizadas en las reseñas, destacando términos como "Great", "Love", "Owner", y "Nice".
![Nube](https://github.com/mariangigena/proyectogrupal/blob/main/imagenes/nube.png)

`Outliers`: Se decidió incluir los valores atípicos en el análisis, ya que su proporción no sesgaba significativamente los resultados. Esto nos permite comprender mejor la diversidad en las reseñas y capturar posibles aspectos excepcionales.

`Correlación`:Encontramos una correlación débilmente negativa entre la longitud de las reseñas y la puntuación. Esto sugiere que, en general, las reseñas más largas tienden a tener puntuaciones ligeramente más bajas. Aunque la relación es tenue, arroja luz sobre cómo los revisores expresan sus opiniones.

`Distribución de Reseñas`:Observamos que la mayoría de las reseñas se concentraban en Nueva York, seguida de California y Washington. Además, notamos que las puntuaciones más altas se otorgaban en la costa este de EE. UU., especialmente en Nueva York. Esta distribución geográfica de reseñas proporciona información valiosa sobre las preferencias de los revisores en diferentes regiones.

`Usuarios con Múltiples Ubicaciones`: Identificamos a 1421 usuarios que realizaron reseñas en más de una ubicación. Sorprendentemente, el 90% de estos usuarios revisaron en exactamente dos ubicaciones diferentes. Nueva York y California concentraron la mayoría de estas reseñas múltiples, lo que sugiere su atractivo como destinos de vinos.

`Selección de Categorías para el Análisis`: Decidimos enfocar nuestro análisis en categorías específicas, como "wine store," "winery," y "wine bar," debido a su significativa cantidad de reseñas y altas puntuaciones. Esto nos permitió profundizar en las experiencias relacionadas con estas categorías específicas.

`Comparativa de Establecimientos`: Al analizar los 10 establecimientos con más reseñas, encontramos que categorías como "wine store," "wine bar," "winery," y "wine club" estaban presentes. Entre estos, los establecimientos de "wine store" obtuvieron las calificaciones más altas, lo que sugiere una experiencia especialmente satisfactoria para los revisores.

`Segmentación de Usuarios`:Identificamos dos segmentos de usuarios basados en el análisis de las palabras clave en sus reseñas. Los usuarios clasificados como "Conocedores" destacan palabras relacionadas con las sensaciones del gusto, la vista y el olfato, así como sabores, olores y colores, lo que sugiere un enfoque en la apreciación sensorial. Por otro lado, los "Consumidores Casuales" emplean palabras relacionadas con las instalaciones, la atención del personal y la compañía, lo que refleja una experiencia más centrada en el ambiente y los servicios ofrecidos por el lugar.

`Rating Promedio`: Observamos que el rating promedio de los "Conocedores" es de 3.95, por debajo del rating promedio general que se establece en 4.25. En contraste, los "Consumidores Casuales" tienen un rating promedio de 4.67, por encima del promedio rating general. Esto resalta las diferencias en las valoraciones y expectativas de estos dos segmentos de usuarios.

`Distribución Geográfica`: La mayoría de las reseñas se concentran en la costa oeste, incluyendo los estados de California, Washington y Oregón, y también se destaca Nueva York. Las reseñas de los "Conocedores" predominan en estos cuatro estados, mientras que las de los "Consumidores Casuales" se distribuyen en varios estados, lo que refleja su mayor diversidad geográfica.

`Cantidad de Usuarios`: En total, identificamos 32 "Conocedores" y 24,865 "Consumidores Casuales" en nuestro conjunto de datos. Esta diferencia en la cantidad de usuarios entre los dos segmentos es notable y subraya la importancia de comprender las preferencias y expectativas de ambos grupos.

`Comparativa de Categorías`: En cuanto a la categoría, observamos que "Vineyard" tiene el rating promedio más alto, con un valor de 4.67, en comparación con "Winery," que tiene un rating promedio de 4.22. Esto indica que los revisores tienden a tener una experiencia especialmente satisfactoria en las "Vineyards."

`Distribución de Negocios`: La mayor cantidad de reseñas se encuentra en California, seguido de Washington, Oregón y Nueva York. California lidera con 3,597 negocios, seguido de Washington con 814, Oregón con 625 y Nueva York con 276. Esta distribución de negocios coincide con la concentración de reseñas.

`Establecimientos con Mayor Cantidad de Reseñas`: Entre los establecimientos con más reseñas, encontramos nombres como Chateau Ste. Michelle en Washington con 171 reseñas, Columbia Crest con 146 en segundo lugar, y de manera interesante, Peace Water Winery en Indiana con 143 en tercer lugar. Estos datos revelan la popularidad de ciertos establecimientos.

`Actividad de Usuarios`: Identificamos casos atípicos donde algunos usuarios realizaron reseñas en un número excepcionalmente alto de negocios diferentes. Por ejemplo, un usuario revisó 1,559 negocios, otro 978, y otro 844. Estas situaciones destacan la diversidad de comportamientos de los usuarios.

`Usuarios en Múltiples Estados`: Aunque la mayoría de los usuarios realizan reseñas en un solo estado, identificamos 209 usuarios que realizaron reseñas en dos estados diferentes, 16 en tres estados y cuatro en cuatro estados. Esto refleja la movilidad geográfica de ciertos revisores.

`Reseñas Múltiples en un Establecimiento`:Es importante reconocer que algunos usuarios realizaron múltiples reseñas en un mismo establecimiento. Por ejemplo, el usuario WM-8 realizó 99 reseñas en Testarossa, mientras que el usuario WM-10 hizo 96 reseñas en Chateau Ste. Michelle, entre otros casos similares.

Este análisis exhaustivo nos ha proporcionado una comprensión profunda de las reseñas y los revisores en la industria del vino, permitiéndonos identificar tendencias, preferencias y segmentos clave. Estos hallazgos son fundamentales para la toma de decisiones informadas y la formulación de estrategias de marketing efectivas en la industria del vino y la hostelería.

## 4. **Machine Learning y producto final**

Nuestro objetivo principal es identificar a los usuarios que poseen experiencia y conocimiento en el mundo del vino,  que aportan un alto valor en sus evaluaciones.
Consideraremos a un revisor como 'Conocedor de Vinos' no solo si ha realizado numerosas reseñas, sino también si ha explorado diversos lugares y ciudades en busca de experiencias en vinos.
Para segmentar a los revisores utilizamo el algoritmo de Clustering K-means es uno de los más usados para segmentar o discriminar grupos no visibles a sumple vista en un conjunto de datos no etiquetado.

### Modelo No Supervisado (K-Means++) para Identificar Conocedores de Vinos
El objetivo principal de este modelo es identificar a los usuarios que poseen experiencia y conocimiento en el mundo del vino, que aportan un alto valor en sus evaluaciones. Para lograr esto, se utilizó el algoritmo de Clustering K-Means++. Algunas ventajas de K-Means++ incluyen:

- Inicialización inteligente de centroides.
- Convergencia más rápida.
- Mejor rendimiento en la búsqueda de soluciones objetivamente mejores.

Con K-Means++, se segmentaron a los revisores en dos grupos: conocedores de vinos y consumidores casuales. Estos grupos se basaron en las palabras más representativas de cada cluster, relacionadas con las reseñas de los usuarios. Los conocedores destacaban palabras relacionadas con la textura, color y sabor del vino, mientras que los consumidores casuales se centraban en aspectos como instalaciones y atención del personal.

El resultado del modelo no supervisado se guardó en un archivo que se utilizará para alimentar el modelo supervisado de clasificación.

### Modelo Supervisado para Clasificar Usuarios
El objetivo del modelo supervisado es clasificar a los usuarios en dos categorías: conocedores de vinos y consumidores casuales. Para ello, se utilizaron datos de entrenamiento etiquetados previamente con las categorías obtenidas del modelo no supervisado.[Modelo](https://github.com/mariangigena/proyectogrupal/tree/main/ML/PropuestaA)


El proceso del modelo supervisado involucra:

- Preprocesamiento de datos de texto, incluyendo conversión a minúsculas, eliminación de caracteres especiales, tokenización y eliminación de palabras irrelevantes.
- Vectorización de texto, usando TF-IDF o CountVectorizer.
- Selección de algoritmo de clasificación, en este caso, LinearSVC.
- Optimización de hiperparámetros utilizando Grid Search.
- Creación de un pipeline para la vectorización y el modelo.
- Entrenamiento del modelo y evaluación utilizando métricas como precisión, recall y matriz de confusión.

Este modelo supervisado proporciona resultados satisfactorios para la clasificación de usuarios como conocedores de vinos o consumidores casuales. Se evaluaron las métricas y se tomaron reseñas al azar para verificar el rendimiento del modelo.

Estos dos modelos, el no supervisado para segmentar usuarios y el supervisado para clasificar usuarios, son componentes esenciales para identificar y aprovechar las reseñas de conocedores de vinos en el proyecto.

### Conclusiones y producto final: 

A pesar de que gigantes de la industria como Google o Yelp cuentan con métodos para filtrar reseñas no auténticas, hasta donde nosotros sabemos, ninguno de ellos se enfoca en evaluar la experiencia y el conocimiento real de los revisores. Nuestro enfoque ha sido especialmente loable, ya que hemos logrado identificar de manera eficiente a los conocedores de vinos a partir de un vasto conjunto de datos de reseñas que, en su mayoría, ni siquiera estaban orientadas al vino. Estas reseñas solían centrarse en la calidad del servicio, el ambiente y el personal, aspectos que no suelen ser abordados por otros sistemas de clasificación.

Nuestro producto final es una solución integral que aborda esta problemática. Se realizó el deploy en Streamlit, lo que significa que hemos implementado una interfaz interactiva que permite a los usuarios probar y experimentar con nuestro sistema. Hemos incluido un botón de prueba que les permite obtener una revisión aleatoria del conjunto de datos de prueba. Los usuarios pueden hacer clic en este botón y, como respuesta, verán el texto de la revisión, junto con la clasificación de la revisión, que la categoriza como realizada por un conocedor de vinos o un consumidor casual.

Esta implementación en Streamlit agrega un nivel de accesibilidad y usabilidad al producto final. No solo hemos desarrollado un modelo de clasificación de revisores, sino que hemos creado una herramienta interactiva que permite a las empresas y usuarios finales interactuar directamente con nuestro sistema. Esto marca un avance significativo en la evaluación de reseñas y la toma de decisiones basadas en datos para la industria del vino y la hostelería.[Prueba](https://review-insights.streamlit.app/Usa_nuestro_Modelo_Machine_Learning)

## Documentacion 
1- [Analisis sobre el mercado vitivinicola](https://www.tecnovino.com/estados-unidos-el-pais-que-mas-gasta-en-vino-del-mundo/).

2- [Caso de estudio de exportacion de vinos a California](https://es.scribd.com/document/499977209/Dialnet-ExportacionDeVinoTintoAlEstadoDeCalifornia-7242720)

3- [Diccionario de los Dataset](https://docs.google.com/spreadsheets/d/1yqzhAJYQmZR4UNs7w-sYEJx5k-rC_-pfw1gnUHxsuPc/edit#gid=0)


## Integrantes del grupo :

**Diego Forcato** [Linkedin](https://www.linkedin.com/in/diegoforcato)

**Fernando Mubarqui** [Linkedin](https://www.linkedin.com/in/fernando-mubarqui-540136106/)

**Harlan Tonguino** [Linkedin](https://www.linkedin.com/in/harlan-tonguino-37048a174/)

**Renar Zamora** [Linkedin](https://www.linkedin.com/in/renar-arnoldo-zamora-54bb9024/)

**Mariana Gigena** [Linkedin](https://www.linkedin.com/in/mariana-gigena/)

