from static.musa import Musa
from static.musa_okumoto import MusaOkumoto
from static.jelinski_moranda import  JelinskiMoranda

import numpy as np

def read_data(filename):
    f = open(filename)
    data = []
    for row in f:
        data.append(int(row.strip()))
    return data


def musa_for_real_data():
    # data = read_data('test_commercial_data.txt')
    data = read_data('dataset_6.txt')
    for i in range(1, len(data)):
        data[i] += data[i-1]
    times_of_falls = data[:-1]
    time_passed = 450 #data[-1] - data[-2]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    # m.debug_plot_b1(-0.000001, 0.000001, 1000)
    print('lambd: ', m.func_lambd())
    print('r  ', m.func_r())
    # m.plot_func(1, 10000, 1000)
    m.plot_mu_and_errors()
    # For commercial data
    #b0 = [ 843.97619457] b1 = [  9.85557815e-08]

    # m = Musa(times_of_falls[i-1] - times_of_falls[i-2], times_of_falls[:i-1])
    # times_of_falls = data
    # res = []
    # for i in range(2, len(times_of_falls)+1):
    #     m = Musa(times_of_falls[i-1] - times_of_falls[i-2], times_of_falls[:i-1])
    #     print("Test: {0}".format(i-1))
    #     print("Time: {0}".format(times_of_falls[i-1] - times_of_falls[i-2]))
    #     print("Data: {0}".format(times_of_falls[:i]))
    #     print("Res: {0}\n===\n".format(m.mu()))
    #     res.append(m.mu()[0])
    # print(res)

def musa_okumoto_for_real_data():
    # data = read_data('dataset_6.txt')
    data = read_data('test_commercial_data.txt')
    for i in range(1, len(data)):
        data[i] += data[i-1]
    times_of_falls = data[:-1]
    time_passed = data[-1] - data[-2]
    # 0.00000001 - for commercial data
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)
    print('lambd: ', m.func_lambd())
    print('r  ', m.func_r())
    m.plot_mu_and_errors()

def jelinski_moranda_for_real_data():
    # TODO IMPORTANT!!! Нужно уточнить - массив - по модели нужны времена отказов или времена с прошедшего отказа
    # data = read_data('dataset_6.txt')
    # data = read_data('test_commercial_data.txt')
    data = [3, 2, 10, 7, 14, 8, 5, 1, 6, 9, 13, 3, 5, 5, 9, 2, 24, 1, 9, 8, 11, 6, 8, 2, 9, 74, 14, 7, \
             22, 45, 3, 22, 4, 9, 3, 83, 6, 8, 2, 6]
    times_of_falls = data
    j = JelinskiMoranda(times_of_falls)

    j.debug_print()
    print(j.func_n())

    import matplotlib.pyplot as plt
    # Plot real errors
    for i in range(1, len(times_of_falls)):
        times_of_falls[i] += times_of_falls[i-1]
    errors_count = [[],[]]
    count = 1
    for val in times_of_falls:
        errors_count[0].append(val)
        errors_count[1].append(count)
        count += 1
    plt.plot(errors_count[0], errors_count[1])


  # Plot model errors
    tau = np.linspace(0, 1.2 * errors_count[0][-1], 1000)
    func = j.func_n
    plt.plot(tau, func(tau))
    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()


def plot_musa_and_musa_okumoto():
    # data = read_data('dataset_6.txt')
    data = read_data('test_commercial_data.txt')
    for i in range(1, len(data)):
        data[i] += data[i-1]
    print(data[-1])
    times_of_falls = data[:-1]
    time_passed = data[-1] - data[-2]
    init_guess = 0.00000001
    m = Musa(time_passed, times_of_falls, init_guess)
    mo = MusaOkumoto(time_passed, times_of_falls, init_guess)

    import matplotlib.pyplot as plt
    # Plot real errors
    errors_count = [[],[]]
    count = 1
    for val in times_of_falls:
        errors_count[0].append(val)
        errors_count[1].append(count)
        count += 1
    plt.plot(errors_count[0], errors_count[1])

    # Plot model errors
    tau = np.linspace(0, 1.2 * errors_count[0][-1], 1000)
    func = m._mu
    plt.plot(tau, func(tau))
    func = mo._mu
    plt.plot(tau, func(tau))

    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()

# musa_for_real_data()
# musa_okumoto_for_real_data()
jelinski_moranda_for_real_data()
# plot_musa_and_musa_okumoto()