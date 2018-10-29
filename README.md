# DatatonBC 2018
DatatonBC 2018. Transaction Classification/Clasificación de Transacciones.

Clasificación de transacciones PSE.
Se espera que el usuario entienda la naturaleza de sus
movimientos bancarios a través de PSE. Adicionalmente, Bancolombia
podrá detectar el destino del dinero.

![Prototipo App Personas](https://raw.githubusercontent.com/AlejandroMllo/DatatonBC_2018/master/Supporting_Files/App.png)

### Equipo: Eafitting
##### Integrantes:
- Alejandro Murillo G.
- Juan Pablo Vidal C.
- Henry Velasco V.

-----------------------------

### Metodología y Resultados

En el documento ['Clasificacion_de_TransaccionesPSE_con_kNN.pdf'](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Clasificacion_de_TransaccionesPSE_con_kNN.pdf) se encuentra
una descripcion breve y detallada de la metodología usada y de los resultados obtenidos. La siguiente
tabla resume algunos resultados:



| Dataset       | Score    | Accuracy | Recall   | Precision | F1       | R^2      | Size
|---------------|----------|----------|----------|-----------|----------|----------| --------
| Entrenamiento | 0.991257 | 0.991257 | 0.991257 | 0.991208  | 0.991076 | 0.984354 | 1'350.000
| Validación    | 0.990373 | 0.990373 | 0.990373 | 0.990338  | 0.990435 | 0.978653 | 75.000
| Prueba        | 0.98808  | 0.98808  | 0.98808  | 0.989438  | 0.988381 | 0.974052 | 75.000

**En [Additional_Models](https://github.com/AlejandroMllo/DatatonBC_2018/tree/master/Additional_Models) puede encontrar unos notebook con los _prometedores_ resultados al tratar de clasificar con otros modelos.**  

### Uso
1. Preprocesamiento dataset original: __'dt_trxpse_personas_2016_2018_muestra_adjt.csv'__.
    1. Esto se lleva a cabo con el script [trxpse_persona_data_scraper.py](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Transaction_Classifier/trxpse_persona_data_scraper.py).
    1. Se reemplaza en la variable *dataset_path* con el path del CSV *'dt_trxpse_personas_2016_2018_muestra_adjt.csv'*.
    1. Se corre el script.
    1. El script crea dos data sets (estos contienen las transacciones **con** y **sin** label, desordenadas):
        1. 'LABELED_DATA_TRXPSE_BC.csv'
        1. 'UNLABELED_DATA_TRXPSE_BC.csv'
2. Carga de datos:
    1. Se hace uso de la clase [LoadData.py](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Transaction_Classifier/LoadData.py).
    1. Se reemplaza el atributo *__dataset_path* con el path de 'LABELED_DATA_TRXPSE_BC.csv'; y
       en *x_path* y *y_path* los paths de 'X_DATA_TRXPSE_BC.csv' y 'Y_DATA_TRXPSE_BC.csv', respectivamente.
    1. Si es la primera vez que se usa, es necesario hacer el parámetro de inicialización __load_unprocessed_data=True__.
       Esto guarda los datos procesados en dos archivos ('X_DATA_TRXPSE_BC.csv', 'Y_DATA_TRXPSE_BC.csv'),
       que serán usados para crear los sets de *Entrenamiento*, *Validación* y *Prueba*.
       En caso contrario, una vez instanciado *LoadData* se llama el método *load_processed_data()*, que cargará
       'X_DATA_TRXPSE_BC.csv' y 'Y_DATA_TRXPSE_BC.csv' y creará los data sets necesarios.
3. Clasificación:
    1. Se hace uso de la clase [TransactionClassifier.py](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Transaction_Classifier/TransactionClassifier.py).
    1. Una vez instanciado se llama el método *train()* y se le pasan los datos
       cargados en el paso anterior.
    1. Use de acuerdo a su necesidad los métodos *test()*, *predict()*, *get_confusion_matrix()*,
       *save_model()* y *load_model()*.
       
----------------------------------

Octubre 29, 2018.
