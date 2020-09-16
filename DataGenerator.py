import numpy as np


class ArtDataGenerator:
    def __init__(self, data_range: list, func):
        self.data_range = data_range
        self.func = func

    def get_data_with_noise(self, data_number):
        np.random.seed(0)
        data_x = (max(self.data_range) - min(self.data_range)) * np.random.rand(data_number) + min(self.data_range)
        data_y = self.func(data_x) + np.random.randn(data_number)

        return data_x, data_y


# if __name__ == '__main__':
#     datarange = [0, 4*np.pi]
#
#     def f(x_arr):
#         return 2 * np.sin(x_arr) + 3 * np.cos(2 * x_arr) + 5 * np.sin(2 / 3 * x_arr)
#
#     data_gen = ArtDataGenerator(data_range=datarange,
#                              func=lambda x_arr: 2 * np.sin(x_arr) + 3 * np.cos(2 * x_arr) + 5 * np.sin(2 / 3 * x_arr))
#     data_x, data_y = data_gen.get_art_data_with_noise(data_number=100)
#     print(data_x)
#     print(data_y)
