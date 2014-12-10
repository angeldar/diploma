from static.musa import Musa
from static.musa_okumoto import MusaOkumoto
from static.jelinski_moranda import  JelinskiMoranda
import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    f = open(filename)
    data = []
    for row in f:
        data.append(int(row.strip()))
    return data

def musa_for_real_data():
    # data = read_data('test_commercial_data.txt')
    data = [10, 18, 32, 49, 64, 86, 105, 132, 167, 207, 222]#read_data('datasets/dataset_6.txt')
    time_passed = data[-1] - data[-2]
    for i in range(1, len(data)):
        data[i] += data[i-1]
    times_of_falls = data[:-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    print(m.func_r())
    # m.debug_plot_b1(-0.000001, 0.000001, 1000)
    m.plot_func(1, 10000, 1000)
    # m.plot_mu_and_errors()
    # For commercial data
    #b0 = [ 843.97619457] b1 = [  9.85557815e-08]

def musa_okumoto_for_real_data():
    # data = read_data('dataset_6.txt')
    data = read_data('test_commercial_data.txt')
    time_passed = data[-1] - data[-2]
    for i in range(1, len(data)):
        data[i] += data[i-1]
    times_of_falls = data[:-1]
    # 0.00000001 - for commercial data
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)
    print('lambd: ', m.func_lambd())
    print('r  ', m.func_r())
    m.plot_mu_and_errors()


def jelinski_moranda_for_real_data():
    data = read_data('datasets/journal_of_computer_application_dataset.txt')
    # data = read_data('datasets/test_commercial_data.txt')
    # data = read_data('datasets/dataset_6.txt')
    times_of_falls = data
    j = JelinskiMoranda(times_of_falls)

    # Good MTTF plot
    # data_plot = [[],[]]
    # for i in range(len(times_of_falls)):
    #     data_plot[0].append(i)
    #     data_plot[1].append(j.func_MTTF(i))
    # plt.plot(data_plot[0], data_plot[1][::-1])
    # data_plot = [[],[]]
    # for i in range(len(times_of_falls)):
    #     data_plot[0].append(i)
    #     data_plot[1].append(times_of_falls[i])
    # plt.plot(data_plot[0], data_plot[1][::-1])
    # plt.grid()
    # plt.show()

    # Plot real errors
    for i in range(1, len(data)):
        data[i] += data[i-1]
    errors_count = [[],[]]
    count = 1
    for val in data:
        errors_count[0].append(val)
        errors_count[1].append(count)
        count += 1
    plt.plot(errors_count[0], errors_count[1])

  # Plot model errors
    tau = np.linspace(0, errors_count[0][-1], 1000)
    func = j.func_n
    plt.plot(tau, func(tau))
    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()

def print_failure_rate_for_jm():
    data = read_data('datasets/journal_of_computer_application_dataset.txt')
    times_of_falls = data
    j = JelinskiMoranda(times_of_falls)
    import matplotlib.pyplot as plt
    tau = [i for i in range(0, len(data))]
    print(tau)
    func = j.func_MTTF
    plt.plot(tau, [func(i) for i in tau])
    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()

def plot_musa_and_musa_okumoto():
    # data = read_data('dataset_6.txt')
    # data = read_data('test_commercial_data.txt')
    data = read_data('datasets/journal_of_computer_application_dataset.txt')
    time_passed = data[-1] - data[-2]
    for i in range(1, len(data)):
        data[i] += data[i-1]
    times_of_falls = data[:-1]
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

def plot_all_models():
    data = read_data('datasets/dataset_6.txt')
    # data = read_data('datasets/test_commercial_data.txt')
    # data = read_data('datasets/journal_of_computer_application_dataset.txt')
    musa_data = data[:]
    jm_data = data[:]
    time_passed = musa_data[-1] - musa_data[-2]
    for i in range(1, len(musa_data)):
        musa_data[i] += musa_data[i-1]
    times_of_falls = musa_data[:-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    mo = MusaOkumoto(time_passed, times_of_falls, init_guess)
    j = JelinskiMoranda(jm_data)

    # Plot real errors
    errors_count = [[],[]]
    count = 1
    for val in times_of_falls:
        errors_count[0].append(val)
        errors_count[1].append(count)
        count += 1
    plt.plot(errors_count[0], errors_count[1])

    # Plot model errors
    tau = np.linspace(0, 2 * errors_count[0][-1], 100)
    # tau = musa_data
    func = m._mu
    plt.plot(tau, func(tau))
    func = mo._mu
    plt.plot(tau, func(tau))
    func = j.func_n
    plt.plot(tau, func(tau))
    plt.xlabel("tau")
    plt.ylabel("expression value")
    plt.grid()
    plt.show()




# musa_for_real_data()
# musa_okumoto_for_real_data()
# jelinski_moranda_for_real_data()
# print_failure_rate_for_jm()
# plot_musa_and_musa_okumoto()

plot_all_models()