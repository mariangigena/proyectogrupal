# Review Insights - Análisis de Reseñas y Recomendaciones

![Review](https://raw.githubusercontent.com/parzibyte/WaterPy/master/assets/ImagenV1.png)3.

## Introducción

Review Insights es una empresa de análisis de datos que tiene como objetivo proporcionar información valiosa a otras empresas sobre las reseñas y recomendaciones que reciben de los usuarios en plataformas como Yelp y Google Maps. Nuestro enfoque principal es recopilar, analizar y ofrecer información significativa sobre las experiencias de los usuarios en diferentes comercios.

## Contexto

La industria vinícola se destaca por su enfoque único en la valoración de la marca a través de opiniones personales y recomendaciones de expertos en guías especializadas, así como del poderoso efecto del boca a boca entre los consumidores. Estados Unidos, conocido tradicionalmente por su cultura cervecera, ha experimentado un crecimiento constante en el consumo de vino en los últimos años. Esta tendencia positiva representa una oportunidad valiosa para comercializar productos vinícolas en el país.

La capacidad de identificar y clasificar a los reviewers en profesionales o consumidores circunstanciales, junto con el análisis comparativo de las calificaciones otorgadas por ambos grupos, permitirá a las empresas entender mejor el impacto de las opiniones expertas y del público general en la percepción y éxito de sus establecimientos.

Adicionalmente, la estimación realizada por estudios de marketing, sobre el aumento del consumo de vino en los años venideros fortalece aún más la relevancia del proyecto. La información proporcionada por esta plataforma será invaluable para las empresas vinícolas en sus esfuerzos de marketing, toma de decisiones estratégicas y mejora continua de la calidad del servicio.

## Problemática:

En el contexto de la industria vinícola en Estados Unidos, las empresas enfrentan el desafío de evaluar la percepción y opinión de los usuarios sobre sus bodegas y bares o clubes de vinos. La creciente tendencia en el consumo de vino en el país, junto con la importancia que los clientes otorgan a las reseñas y recomendaciones, demanda una comprensión profunda de las experiencias vividas por los usuarios en estos establecimientos.

La falta de una herramienta efectiva para identificar a aquellos reviewers con expertise en vinos y diferenciarlos de los consumidores circunstanciales, así como la necesidad de evaluar las calificaciones promedio otorgadas por ambos grupos para distintas bodegas y bares de vino, representa una problemática crucial para las empresas del sector. Además, es esencial comprender qué aspectos priorizan los reviewers en sus comentarios, especialmente en los primeros y últimos, para mejorar la calidad del servicio y la satisfacción del cliente.



## Objetivo

El objetivo principal de nuestro proyecto, es proporcionar a las empresas del sector vinícola una valiosa visión sobre las experiencias y opiniones de los usuarios en relación con bodegas y bares o clubes de vinos en Estados Unidos. A través de un análisis exhaustivo de las reseñas y recomendaciones, buscamos identificar a aquellos reviewers que han puntuado establecimientos vinícolas de manera significativa, determinando así a los conocedores con expertise en vinos.

Uno de nuestros enfoques clave es la categorización de los reviewers en dos grupos distintos: profesionales y consumidores circunstanciales. Mediante esta clasificación, pretendemos evaluar el score promedio otorgado por cada grupo con relación a diferentes bodegas o bares de vino. De esta manera, podremos identificar posibles diferencias en sus opiniones, permitiendo a las empresas entender mejor el impacto de las opiniones expertas y del público general en la percepción y éxito de sus establecimientos
 

Además, en nuestro análisis, prestamos especial atención a qué aspectos priorizan los reviewers en sus comentarios, especialmente enfocándonos en los primeros y últimos comentarios. Esto brindará información valiosa a las empresas para comprender qué aspectos de sus servicios o productos reciben mayor atención y cómo pueden mejorar la experiencia del cliente.

Como se explicó en el contexto, el mercado vitivinícola, caracterizado por su énfasis en la valoración de la marca a través de opiniones personales y recomendaciones de expertos, ofrece una oportunidad única para este proyecto.

Nuestra misión es convertir el conocimiento de las experiencias del cliente en una herramienta valiosa para el éxito empresarial en el dinámico y creciente mercado vinícola de Estados Unidos.


## KPIs

Los KPIs que encontramos mediante el analisis exploratorio de los datos fueron :

1. **Cantidad de Reviewers Identificados como Conocedores de Vinos:** Este KPI está directamente relacionado con el objetivo del proyecto de identificar a los usuarios que tienen experiencia y conocimiento en vinos, lo que aporta valor al recibir opiniones de expertos.

2. **Distribución de Reviewers según su Categoría:** Este KPI proporciona información importante sobre la composición de los usuarios que realizan reseñas, lo que ayudará a determinar si el negocio atrae a reviewers profesionales o si la mayoría son consumidores circunstanciales.

3. **Score Promedio de Expertos y Aficionados:** Al comparar el score promedio entre reviewers profesionales y amateurs, se puede evaluar si las opiniones de los expertos tienen un impacto significativo en la calificación general de las bodegas o bares de vinos.

4. **Comparativa de Score Promedio de Bodegas o Bares de Vinos:** Este KPI permitirá identificar cuáles son los establecimientos mejor valorados por los reviewers, proporcionando información valiosa a las empresas para mejorar su desempeño

5. **Volumen de Reseñas por Establecimiento:**muestra la popularidad y la satisfacción general de los clientes con el lugar.
.

## Implementación del Stack Propuesto

Hemos seleccionado un stack tecnológico que nos permitirá llevar a cabo el análisis de datos y la generación de modelo de manera efectiva:

1. Power BI: Utilizaremos Power BI para crear visualizaciones interactivas y paneles de control que permitan a las empresas explorar y entender los datos de manera intuitiva. Es la  herramienta de visualización que mejor manejamos con el equipo.

2. ETL Automatizado: Implementaremos un proceso ETL (Extract, Transform, Load) automatizado en la nube para recopilar y procesar los datos de reseñas y recomendaciones de las plataformas en línea. Decidimos utilizar la que ya nos brinda Azure.

3. Servicios en la Nube: Almacenaremos y procesaremos los datos en servicios en la nube de Azure para garantizar su disponibilidad y escalabilidad.La eleccion estuvo basada en la cantidad de servicios que nos ofrecia el proveedor y la cantidad de documentacion y las recomendaciones de otros usuarios acerca del cobro de los servicios.

4. Python y Librerías: Utilizaremos el lenguaje de programación Python junto con librerías como pandas, NumPy y scikit-learn para realizar el análisis de datos y la creación del modelo. 

5. Trello: elegimos esta herramienta para poder ordenar el trabajo en equipo y para poder seguir un flujo de trabajo.

5. Canva: usamos esta herramienta para poder apoyarnos visualmente en las demos del proyecto, así como para la generación de imágenes de nuestra autoría.


