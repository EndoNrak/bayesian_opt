import numpy  as np

class DataGenerator:
    def __init__(self, data_range, func):
        self.data_range = data_range
        self.func = func

    def get_art_data_with_noise(self, data_number):
        data_x = np.linspace(self.data_range[0], self.data_range[1], data_number)
        data_y = self.func(data_x) + np.random.randn(data_number)

        return data_x, data_y