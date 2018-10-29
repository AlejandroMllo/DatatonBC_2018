import csv

from LabelClassification import label_for


class LoadData:
    """
    Data Handling class.
    """

    def __init__(self, x_input_features=None, load_unprocessed_data=False):

        self.__dataset_path = # 'LABELED_DATA_TRXPSE_BC.csv'
        self.__x_input_features = x_input_features
        self.__data = dict()
        self.__categories = dict()

        if load_unprocessed_data:
            self.__load_data()
            self.__split_data()
            self.__save_processed_data()

        self.__data_split_idx = 0
        self.__val_split_idx = 0


    # Public Methods
    def load_dataset(self, dataset_name='train'):

        x, y = self.__data[dataset_name]

        return self.__pick_features(x), y

    def load_all_data(self):
        """
        Returns the whole dataset.
        :return: x, y.
        """

        x = self.__data['all_x']
        y = self.__data['all_y']

        return self.__pick_features(x), y

    def load_train_data(self):
        """
        Returns the training data.
        :return: x, y validation data.
        """

        return self.load_dataset(dataset_name='train')

    def load_validation_data(self):
        """
        Returns the validation data.
        :return: x, y validation data.
        """

        return self.load_dataset(dataset_name='validation')

    def load_test_data(self):
        """
        Returns the test data.
        :return: x, y test data.
        """

        return self.load_dataset(dataset_name='test')

    def get_input_features(self):
        """
        Returns the indices that compose each entry from the complete entry.
        :return: List of indices.
        """

        x_features = self.__x_input_features

        return x_features if x_features is not None else [i for i in range(8)]

    def load_processed_data(self):
        """
        Loads the X and Y datasets.
        :return:
        """

        x = []
        y = []

        x_path = # 'X_DATA_TRXPSE_BC.csv'
        y_path = # 'Y_DATA_TRXPSE_BC.csv'

        with open(x_path, newline='') as csvfile:
            x_reader = csv.reader(csvfile)
            for r in x_reader:
                x.append(r)

            self.__data['all_x'] = x

        with open(y_path, newline='') as csvfile:
            y_reader = csv.reader(csvfile)
            for r in y_reader:
                y.append(r)

            self.__data['all_y'] = y

        self.__data_split_idx = int(len(x) * 0.9)
        self.__val_split_idx = int(len(x) * 0.95)

        self.__data['train'] = x[0:self.__data_split_idx], \
                               y[0:self.__data_split_idx]
        self.__data['validation'] = x[self.__data_split_idx:self.__val_split_idx], \
                                    y[self.__data_split_idx:self.__val_split_idx]
        self.__data['test'] = x[self.__val_split_idx:], \
                              y[self.__val_split_idx:]

    # --- Private Methods -----------------------------------------------------
    def __save_processed_data(self):
        """
        Saves the input features and their corresponding labels
        into two CSV files (X_DATA_TRXPSE_BC.csv, Y_DATA_TRXPSE_BC.csv').
        :return:
        """

        x_data = self.__data['all_x']
        x_name = 'X_DATA_TRXPSE_BC.csv'

        self.__save_dataset(x_data, x_name)

        y_data = self.__data['all_y']
        y_name = 'Y_DATA_TRXPSE_BC.csv'

        self.__save_dataset(y_data, y_name)

    def __load_data(self):
        """
        Loads the data.
        :return:
        """

        data = []
        file_path = str(self.__dataset_path)
        with open(file_path) as csv_data:
            csv_reader = csv.reader(csv_data)
            for row in csv_reader:
                if len(row) >= 10 and (row is not None):
                    data.append(row)

        self.__data['all'] = data

    def __split_data(self):
        """
        Splits the data into input features and labels.
        :return:
        """

        assert 'all' in self.__data

        data = self.__data['all']

        x = []
        y = []

        for entry in data:

            x_entry = entry[0:8].copy()
            x_entry[5] = str(x_entry[5]).replace('_', ' ').lower()
            x_entry[6] = str(x_entry[6]).replace('_', ' ').lower()
            x_entry[7] = str(x_entry[7]).replace('_', ' ').lower()
            x.append(x_entry)
            label = self.__find_label(entry)

            if label in self.__categories:
                self.__categories[label] = self.__categories[label] + 1
            else:
                self.__categories[label] = 1

            y.append(label)

        self.__data_split_idx = int(len(x) * 0.9)
        self.__val_split_idx = int(len(x) * 0.95)

        self.__data['all_x'] = x
        self.__data['all_y'] = y

        self.__data['train'] = x[0:self.__data_split_idx], y[0:self.__data_split_idx]
        self.__data['validation'] = x[self.__data_split_idx:self.__val_split_idx], y[self.__data_split_idx:self.__val_split_idx]
        self.__data['test'] = x[self.__val_split_idx:], y[self.__val_split_idx:]

    def __pick_features(self, x):
        """
        Picks the features given by x_input_features.
        :param x: Entry to pick features from.
        :return: The processed entry.
        """

        x_features = self.get_input_features()

        if x_features == [i for i in range(8)]:
            return x

        retrieved_x = []

        for entry in x:
            e = []
            for f in x_features:
                if f < len(entry):
                    e.append(entry[f])
            retrieved_x.append(e)

        return retrieved_x

    @staticmethod
    def __save_dataset(data, name):
        """
        Saves the given @data@ as a CSV file.
        :param data: Data to save.
        :param name: Data's name.
        :return:
        """

        with open(name, 'w', newline='') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            for row in data:
                data_writer.writerow([row])

    @staticmethod
    def __find_label(l):
        """
        Picks an specific label for the entry.
        :param l: List representing the entry.
        :return: Label for the given entry.
        """

        i = -2 if len(l) >= 2 else (-len(l))
        while i < 0:
            label = str(l[i]).strip("'").lstrip().rstrip().lower()
            if (not label.isnumeric()) and (label is not '') and (label != '\\n'):
                return label_for(label)
            i += 1
        if len(l) >= 3:
            label = str(l[-3]).strip("'").lstrip().rstrip().lower()
            if (not label.isnumeric()) and (label is not '') and (label != '\\n'):
                return label_for(label)

        return 'DEFAULT_LABEL'
