import numpy as np

from DataGenerator import ArtDataGenerator


def main():
    data_gen = ArtDataGenerator(data_range=[0, 4*np.pi],
                                func=lambda x_arr: 2*np.sin(x_arr) + 3*np.cos(2*x_arr) + 5*np.sin(2/3*x_arr))
    data_x, data_y = data_gen.get_data_with_noise(data_number=100)
    print(data_x)
    print(data_y)


if __name__ == '__main__':
    main()
