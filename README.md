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
bash scripts/test.sh ./cfg/coco.yml
```
El primer comando inicializa en entorno de Docker y el segundo se utiliza para realizar la evaluación de los modelos en las métricas de FID y CLIP. Este proceso duró alrededor de 40 minutos usando una tarjeta gráfica NVIDIA RTX 3090.

Para la ejecución del modelo de GLIGEN se tienen los siguientes comandos para poder la generación de imágenes, en este caso, usando cajas delimitadoras como configuración espacial:
```
sudo docker run --gpus=all -it --rm -v /mnt/e/Gligen:/workspace/glig your-env /bin/bash
```
```
python gligen_inference.py
```
El primer comando, de manera similar como en para GALIP, configura el entorno de Docker basado en el Dockerfile respectivo en este repositorio. El segundo comando ejecuta el programa de python destinado a la inferencia (generación) de imágenes. Se uso la misma tarjeta gráfica como en el primer modelo, tomando alrededor de 3 minutos para la ejecución.

### Procesamiento de datos

Para el procesmiento de los datos se implementaron los scripts en python y shell encontrados en la carpeta de Evaluation. Las funciones de cada scripts son explicadas a continuación:

- **process_data.py**: Este es el script principal del procesamiento. La primera función de este script es la modificación del tamaño de las imágenes para que estén acorde a la resolución del conjunto de datos de evaluación. La segunda en es balance del número de elementos en cada uno de los conjuntos de datos a ser evaluados para que la evaluación sea más consistente y significativa.

- **evaluate.sh**: Este script simplemente es usado para configurar los argumentos para el procesamiento de datos para posteriormente ser ejecutado.

- **clearfolders.sh**: Script usado para limpiar el contenido de los directorios de los conjuntos de datos generados.

- **utils.py**: Script usado para un preprocesamiento y separación de las imágenes generadas por el modelo GALIP, ya que la tiene una generación múltiple en una sola imagen.

### Métrica de evaluación (FID)

La métrica de Distancia de Incepción de Fréchet (FID) se utiliza para evaluar la calidad de las imágenes generadas por modelos como las Redes Generativas Antagónicas (GANs). Compara cuán similares son las imágenes generadas a las imágenes reales.

#### Implementación en PyTorch

PyTorch cuenta con una implementación para esta métrica, la cual será usada para los experimentos. Aquí se encuentra el repositorio de dicha implementación:

- **Repositorio**: [pytorch-fid](https://github.com/mseitzer/pytorch-fid)
- **Instalación**:

```sh
  pip install pytorch-fid
```
