import csv

from pandas import DataFrame

from numpy import ravel

from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, r2_score
from sklearn.metrics import accuracy_score, recall_score, precision_score
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.preprocessing.text import Tokenizer

from LoadData import LoadData


class TransactionClassifier:
    """
    PSE Transaction Classifier.
    """

    def __init__(self, name='TransactionClassifier'):

        self.__name = str(name)

        self.__knn_classifier = KNeighborsClassifier(3)

        self.__tokenizer = None
        self.__label_encoder = None

        self.__num_tokens = None

    # --- Public Methods ------------------------------------------------------

    def train(self, data, num_tokens=20000):
        """
        Trains the TransactionClassifier.
        :param data: A data set from LoadData.
        :param num_tokens: The number of (most frequent) tokens to use
        in pre-processing.
        :return:
        """
        self.__num_tokens = num_tokens

        x, y = self.__preprocess_data(data)

        self.__knn_classifier.fit(x, y)

    def test(self, data):
        """
        Tests the TransactionClassifier.
        :param data: A data set from LoadData.
        :return: Returns the metrics
        """
        x, y = self.__preprocess_data(data)

        return self.__compute_metrics(x, y)

    def predict(self, x):
        """
        Returns the label(s) for a given input.
        :param x: Input data.
        :return: Input's predicted label.
        """
        data = x, []
        x, _ = self.__preprocess_data(data=data)

        predictions = self.__knn_classifier.predict(x)

        return self.__label_encoder.inverse_transform(predictions)

    def get_confusion_matrix(self, data):
        """
        Returns the Confusion Matrix to describe @data@.
        :param data: A data set from LoadData.
        :return: Confusion Matrix.
        """
        x, y = self.__preprocess_data(data)

        predictions = self.__knn_classifier.predict(x)

        return confusion_matrix(y, predictions)

    def save_model(self):
        """
        Saves the model using joblib.
        :return:
        """
        joblib.dump(self.__tokenizer, self.__name + '_tokenizer.joblib')
        joblib.dump(self.__label_encoder, self.__name + '_label_encoder.joblib')
        joblib.dump(self.__num_tokens, self.__name + '_num_tokens.joblib')
        joblib.dump(self.__knn_classifier, self.__name + '_knn_classifier.joblib')

    def load_model(self):
        """
        Loads any previously saved models.
        :return:
        """
        self.__tokenizer = joblib.load(self.__name + '_tokenizer.joblib')
        self.__label_encoder = joblib.load(self.__name + '_label_encoder.joblib')
        self.__num_tokens = joblib.load(self.__name + '_num_tokens.joblib')
        self.__knn_classifier = joblib.load(self.__name + '_knn_classifier.joblib')

    # --- Private Methods -----------------------------------------------------

    def __preprocess_data(self, data):
        """
        Performs data pre-processing.
        :param data: A data set from LoadData.
        :return: (x, y) preprocessed values.
        """
        x, y = data
        y = ravel(y)

        if self.__tokenizer is None:
            self.__tokenizer = Tokenizer(num_words=self.__num_tokens,
                                         oov_token=-1)
            self.__tokenizer.fit_on_texts(x)

        tokenized_x = self.__tokenizer.texts_to_sequences(x)

        if self.__label_encoder is None:
            self.__label_encoder = LabelEncoder()
            self.__label_encoder.fit(y)

        if len(y) > 0:
            encoded_y = self.__label_encoder.transform(y)
        else:
            encoded_y = None

        return tokenized_x, encoded_y

    def __compute_metrics(self, x, y):
        """
        Computes Score, Accuracy, Recall, Precision, F1 and R^2 for the
        trained model.
        :param x: preprocessed input.
        :param y: preprocessed labels.
        :return: Pandas DataFrame with the computed metrics.
        """
        predictions = self.__knn_classifier.predict(x)

        score = self.__knn_classifier.score(x, y)
        accuracy = accuracy_score(y, predictions)
        recall = recall_score(y, predictions, average='weighted')
        precision = precision_score(y, predictions, average='weighted')
        f1 = f1_score(y, predictions, average='weighted')
        r2 = r2_score(y, predictions)

        metrics_data_frame = DataFrame(
            data=[[score, accuracy, recall, precision, f1, r2]])
        metrics_data_frame.columns = \
            ['Score', 'Accuracy', 'Recall', 'Precision', 'F1', 'R^2']

        return metrics_data_frame


def train_and_get_metrics():

    print('LOADING DATA')
    # Load Data
    data = LoadData(x_input_features=[5, 6, 7])
    data.load_processed_data()

    train_data = data.load_train_data()
    validation_data = data.load_validation_data()
    test_data = data.load_test_data()

    print('TRAINING CLASSIFIER')
    # Run Model
    transaction_classifier = TransactionClassifier()
    transaction_classifier.train(train_data)

    print('TESTING CLASSIFIER')
    train_results = transaction_classifier.test(train_data)
    val_results = transaction_classifier.test(validation_data)
    test_results = transaction_classifier.test(test_data)

    print('STATS:')
    print('------------ TRAIN SET -------------')
    print('LENGTH =', len(train_data[0]))
    print('Metrics:\n', train_results)

    print('------------ VALIDATION SET -------------')
    print('LENGTH =', len(validation_data[0]))
    print('Metrics:\n', val_results)

    print('------------ TEST SET -------------')
    print('LENGTH =', len(test_data[0]))
    print('Metrics:\n', test_results)

    print('++++++++++++++++++++++++++++++++++++++++')

    print('SAVING CLASSIFIER')
    transaction_classifier.save_model()


def load_model_and_predict(data=None):

    transaction_classifier = TransactionClassifier()
    transaction_classifier.load_model()

    if data is None:
        data = LoadData(x_input_features=[5, 6, 7])
        data.load_processed_data()

    val_data = data.load_validation_data()
    test_data = data.load_test_data()

    print(transaction_classifier.get_confusion_matrix(val_data))
    print(transaction_classifier.get_confusion_matrix(test_data))


def assign_label_to_unlabeled_data():

    unlabeled_data_path = # 'UNLABELED_DATA_TRXPSE_BC.csv'

    transaction_classifier = TransactionClassifier()
    transaction_classifier.load_model()

    i = 0
    with open('ASSIGNED_LABELS_TO_UNLABELED_DATA.csv', 'w', newline='') as write_csv:
        data_writer = csv.writer(write_csv, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        print('CREATED FILE')

        with open(unlabeled_data_path,
                  newline='') as read_csv:
            data_reader = csv.reader(read_csv)

            print('STARTED DATA READING')
            for row in data_reader:

                pred_features = row[5:8]
                prediction = list(transaction_classifier.predict([pred_features]))

                entry = list(row[:-3])
                entry.append(prediction[0])
                data_writer.writerow(entry)

                if i % 500000:
                    print('***** Prediction #', i)

                i += 1


if __name__ == '__main__':

    # train_and_get_metrics()
    load_model_and_predict()
    # assign_label_to_unlabeled_data()