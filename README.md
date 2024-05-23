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
sudo docker run --gpus=all -it -v $(pwd):/app python-3.9-env
```
```
bash scripts/test.sh ./cfg/coco.yml
```
El primer comando inicializa en entorno de Docker y el segundo se utiliza para realizar la evaluación de los modelos en las métricas de FID y CLIP. Este proceso duró alrededor de 40 minutos usando una tarjeta gráfica NVIDIA RTX 3090.
