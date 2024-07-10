# PFC-1
Repositorio destinado a la implementación de las técnicas evaluadas en la primera parte del curso. 
## Código fuente de los modelos
La implementación orignial de los autores de los modelos GALIP y GLIGEN pueden encontrarse en los siguientes repositorios:
- **GALIP:** https://github.com/tobran/GALIP
- **GLIGEN:** https://github.com/gligen/GLIGEN
## Configuración de entorno y pruebas
Para poder configurar el entorno para la ejecución y prueba de los modelos se utilizó Docker para considerar todas las dependencias necesarias. Los archivos Docker para cada uno de los modelos se encuentran en este repositorio.
### Consideraciones para la ejecución
Para la evaluación de los modelos pre-entrenados presentados en el repositorio original de GALIP, se deben ejecutar los siguientes comandos una vez construida la imagen de Doker:
```
sudo docker run --gpus=all -it -v $(pwd):/app your-env
```
```
python3 generate.py "A dog next to a tree"
```
El primer comando inicializa en entorno de Docker y el segundo se utiliza para generar imágenes basadas en una descripción de texto como argumento. Cada imagen generata tomó aproximadamente 12 segundos utilizando una tarjeta gráfica NVIDIA RTX 3090.

Para la ejecución del modelo de GLIGEN se tienen los siguientes comandos para poder la generación de imágenes, en este caso, usando cajas delimitadoras como configuración espacial:
```
sudo docker run --gpus=all -it --rm -v /mnt/e/Gligen:/workspace/glig your-env /bin/bash
```
```
python3 gligen_inference.py --prompt "descripción" --phrase "entidades" --location "localización"
```
El primer comando, de manera similar como en para GALIP, configura el entorno de Docker basado en el Dockerfile respectivo en este repositorio. El segundo comando ejecuta el programa de python destinado a la inferencia (generación) de imágenes basandose en la descripción de texto, además de las entidades en esta descripción con sus respectivas localizaciones. Se uso la misma tarjeta gráfica como en el primer modelo, tomando alrededor de 1 minuto para la ejecución.

### Procesamiento de datos

Para el procesmiento de los datos se implementaron los scripts en python y shell encontrados en la carpeta de Evaluation. Las funciones de cada scripts son explicadas a continuación:

- **process_data.py**: Este es el script principal del procesamiento. La primera función de este script es la modificación del tamaño de las imágenes para que estén acorde a la resolución del conjunto de datos de evaluación. La segunda en es balance del número de elementos en cada uno de los conjuntos de datos a ser evaluados para que la evaluación sea más consistente y significativa.

- **evaluate.sh**: Este script simplemente es usado para configurar los argumentos para el procesamiento de datos para posteriormente ser ejecutado.

- **clearfolders.sh**: Script usado para limpiar el contenido de los directorios de los conjuntos de datos generados.

### Métrica de evaluación (FID)

La métrica de Distancia de Incepción de Fréchet (FID) se utiliza para evaluar la calidad de las imágenes generadas por modelos como las Redes Generativas Antagónicas (GANs). Compara cuán similares son las imágenes generadas a las imágenes reales.

#### Implementación en PyTorch

PyTorch cuenta con una implementación para esta métrica, la cual será usada para los experimentos. Aquí se encuentra el repositorio de dicha implementación:

- **Repositorio**: [pytorch-fid](https://github.com/mseitzer/pytorch-fid)
- **Instalación**:

```sh
  pip install pytorch-fid
```

### Métrica de evaluación (IS)

El Inception Score (IS) es una métrica utilizada para evaluar la calidad de las imágenes generadas. Valora cuán realistas y diversas son las imágenes utilizando un modelo preentrenado Inception v3. El IS considera tanto la confianza del modelo en sus predicciones como la diversidad de las clases predichas. Para calcular el IS de las imágenes generadas en este proyecto, utilizamos un script (inception.py) que procesa las imágenes a través del modelo Inception v3 y calcula la puntuación basada en la entropía de las distribuciones de clases predichas.

La puntuación IS para las imágenes generadas se calcula utilizando la función inception_score en el script proporcionado.
