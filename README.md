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

###### Matriz de Confusión Datos Validación:

| 16361 | 1   | 0   | 0    | 0  | 0    | 0    | 6     | 97   | 0  | 0   | 0    | 0    | 1     | 0   | 0    | 0     | 0 | 0     |
|-------|-----|-----|------|----|------|------|-------|------|----|-----|------|------|-------|-----|------|-------|---|-------|
| 0     | 48  | 0   | 1    | 0  | 1    | 0    | 67    | 0    | 0  | 2   | 0    | 3    | 126   | 1   | 1    | 0     | 0 | 0     |
| 0     | 0   | 356 | 0    | 0  | 0    | 1    | 0     | 1    | 0  | 0   | 0    | 2    | 20    | 0   | 0    | 0     | 0 | 0     |
| 0     | 0   | 0   | 1102 | 0  | 0    | 0    | 0     | 3    | 0  | 2   | 1    | 0    | 53    | 1   | 0    | 0     | 2 | 0     |
| 0     | 0   | 0   | 0    | 52 | 0    | 0    | 29    | 0    | 0  | 0   | 0    | 0    | 6     | 0   | 0    | 0     | 0 | 0     |
| 9     | 166 | 3   | 1    | 0  | 1083 | 4    | 4     | 0    | 0  | 42  | 1    | 6    | 190   | 1   | 3    | 0     | 0 | 0     |
| 0     | 11  | 0   | 1    | 1  | 1    | 1858 | 19    | 6    | 1  | 0   | 0    | 18   | 62    | 0   | 1    | 0     | 0 | 0     |
| 0     | 0   | 0   | 0    | 0  | 0    | 0    | 21965 | 3    | 0  | 0   | 0    | 0    | 0     | 0   | 0    | 0     | 0 | 0     |
| 6     | 16  | 0   | 0    | 0  | 0    | 0    | 0     | 4633 | 0  | 0   | 0    | 0    | 0     | 0   | 1    | 0     | 0 | 0     |
| 0     | 28  | 0   | 0    | 0  | 0    | 0    | 0     | 0    | 38 | 0   | 0    | 0    | 9     | 0   | 0    | 0     | 0 | 0     |
| 0     | 2   | 0   | 0    | 0  | 0    | 0    | 1     | 0    | 0  | 629 | 0    | 3    | 8     | 0   | 0    | 0     | 0 | 0     |
| 0     | 12  | 2   | 0    | 1  | 5    | 3    | 0     | 0    | 1  | 0   | 1679 | 1    | 43    | 0   | 0    | 0     | 0 | 0     |
| 2     | 16  | 0   | 2    | 0  | 1    | 29   | 4     | 0    | 1  | 100 | 25   | 1083 | 98    | 1   | 1    | 0     | 4 | 0     |
| 0     | 31  | 3   | 4    | 0  | 1    | 94   | 0     | 5    | 3  | 14  | 4    | 27   | 51721 | 19  | 3    | 4     | 5 | 0     |
| 0     | 2   | 0   | 3    | 0  | 0    | 4    | 1     | 0    | 0  | 0   | 0    | 1    | 54    | 510 | 0    | 0     | 0 | 0     |
| 0     | 32  | 0   | 0    | 0  | 0    | 0    | 0     | 0    | 0  | 0   | 0    | 2    | 14    | 0   | 1926 | 1     | 0 | 0     |
| 1     | 101 | 0   | 0    | 0  | 2    | 1    | 0     | 0    | 1  | 0   | 0    | 3    | 6     | 0   | 0    | 31718 | 0 | 0     |
| 0     | 0   | 2   | 0    | 0  | 0    | 0    | 2     | 1    | 0  | 3   | 0    | 5    | 50    | 30  | 0    | 0     | 1 | 166   |
| 0     | 1   | 0   | 0    | 0  | 0    | 1    | 3     | 0    | 0  | 0   | 0    | 0    | 0     | 0   | 0    | 0     | 0 | 27340 |

###### Matriz de Confusión Datos Prueba:

| 16845 | 0  | 0   | 0    | 0  | 0 | 0    | 4     | 108  | 0  | 0   | 0    | 0    | 1     | 0   | 0    | 0     | 0   | 0     |
|-------|----|-----|------|----|---|------|-------|------|----|-----|------|------|-------|-----|------|-------|-----|-------|
| 0     | 66 | 0   | 0    | 0  | 1 | 1    | 53    | 0    | 0  | 2   | 0    | 2    | 106   | 0   | 0    | 0     | 0   | 0     |
| 0     | 0  | 397 | 0    | 0  | 0 | 2    | 0     | 1    | 0  | 0   | 1    | 1    | 33    | 1   | 1    | 0     | 1   | 0     |
| 0     | 0  | 0   | 1122 | 0  | 0 | 0    | 0     | 0    | 0  | 1   | 0    | 1    | 66    | 3   | 0    | 0     | 0   | 0     |
| 0     | 1  | 0   | 0    | 53 | 0 | 0    | 26    | 0    | 0  | 0   | 0    | 0    | 7     | 0   | 0    | 0     | 0   | 0     |
| 0     | 0  | 0   | 0    | 0  | 0 | 0    | 0     | 0    | 0  | 0   | 0    | 0    | 0     | 0   | 0    | 0     | 0   | 0     |
| 1     | 14 | 0   | 0    | 0  | 0 | 1775 | 16    | 7    | 0  | 0   | 2    | 26   | 71    | 0   | 1    | 0     | 3   | 0     |
| 0     | 0  | 0   | 0    | 0  | 0 | 0    | 22342 | 1    | 0  | 0   | 0    | 0    | 0     | 0   | 0    | 0     | 0   | 0     |
| 11    | 13 | 0   | 0    | 0  | 0 | 0    | 0     | 4824 | 0  | 0   | 0    | 0    | 0     | 0   | 5    | 0     | 0   | 0     |
| 0     | 29 | 0   | 0    | 0  | 2 | 0    | 1     | 2    | 52 | 0   | 1    | 0    | 18    | 0   | 4    | 0     | 0   | 0     |
| 0     | 1  | 0   | 0    | 0  | 0 | 0    | 0     | 0    | 0  | 616 | 0    | 2    | 8     | 0   | 0    | 0     | 0   | 0     |
| 0     | 11 | 2   | 1    | 0  | 3 | 3    | 1     | 0    | 0  | 0   | 1664 | 1    | 50    | 0   | 1    | 0     | 0   | 0     |
| 0     | 19 | 0   | 1    | 0  | 1 | 30   | 5     | 0    | 1  | 95  | 17   | 1128 | 101   | 1   | 2    | 0     | 4   | 0     |
| 1     | 36 | 5   | 4    | 1  | 3 | 83   | 2     | 6    | 7  | 23  | 11   | 14   | 51802 | 26  | 2    | 3     | 4   | 0     |
| 0     | 6  | 0   | 7    | 0  | 1 | 3    | 1     | 0    | 0  | 1   | 0    | 2    | 53    | 475 | 0    | 1     | 0   | 0     |
| 1     | 35 | 0   | 0    | 0  | 0 | 2    | 0     | 0    | 0  | 0   | 2    | 3    | 8     | 0   | 1989 | 0     | 0   | 0     |
| 0     | 96 | 0   | 0    | 0  | 0 | 1    | 0     | 0    | 0  | 0   | 1    | 0    | 10    | 2   | 0    | 31949 | 0   | 0     |
| 0     | 2  | 0   | 0    | 0  | 0 | 2    | 3     | 1    | 4  | 0   | 1    | 48   | 43    | 0   | 0    | 0     | 161 | 0     |
| 0     | 1  | 0   | 0    | 0  | 0 | 0    | 6     | 0    | 0  | 0   | 0    | 0    | 0     | 0   | 0    | 0     | 0   | 27371 |

###### Muestra Datos No Etiquetados
Tomamos una muestra de alrededor del 10% de los datos no etiquetados. Haciendo uso del kNN entrenado clasificamos esos datos y obtuvimos los siguientes resultados:

**Número Transacciones por Categoria**

![numero_transacciones](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Supporting_Files/kNN_TransaccionPSE.jpeg?raw=true)


**Valor Transacciones por Categoria**

![valor_transacciones](https://github.com/AlejandroMllo/DatatonBC_2018/blob/master/Supporting_Files/kNN_ValorTransaccionesPSE.jpeg?raw=true)


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
