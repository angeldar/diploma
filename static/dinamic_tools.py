from static.musa import Musa
from static.musa_okumoto import MusaOkumoto
from static.jelinski_moranda import  JelinskiMoranda
import numpy as np
import matplotlib.pyplot as plt

plt = plt

## Plotting
def add_func_plot(func, xmin, xmax, number_of_steps):
    '''Add the plot of the function using linspace'''
    tau = np.linspace(xmin, xmax, number_of_steps)
    plt.plot(tau, func(tau))

def add_errors_plot(time_between_errors):
    '''Add the plot of real errors '''
    numbers_of_errors = [i + 1 for i in range(0, len(time_between_errors))]
    times_of_errors = convert_time_between_errors_to_time_of_errors(time_between_errors)
    plt.plot(times_of_errors, numbers_of_errors)

def xlabel(label):
    plt.xlabel(label)

def ylabel(label):
    plt.ylabel(label)

def grid():
    plt.grid()

## Data reading and transforming
def read_data(filename):
    f = open(filename)
    data = []
    for row in f:
        data.append(int(row.strip()))
    return data

def convert_time_between_errors_to_time_of_errors(time_between_errors):
    res = time_between_errors[:]
    for i in range(1, len(res)):
        res[i] += res[i-1]
    return res

def musa_for_real_data():
    data = read_data('datasets/dataset_6.txt')
    time_passed = data[-1] - data[-2]
    errors = convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    add_func_plot(m._lambd, 1, 10000, 1000)
    grid()
    plt.show()
    add_errors_plot(data)
    add_func_plot(m._mu, 0, 1.2 * m.t[-1], 1000)
    grid()
    plt.show()

def musa_okumoto_for_real_data():
    data = read_data('datasets/test_commercial_data.txt')
    time_passed = data[-1] - data[-2]
    errors = convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)
    add_errors_plot(data)
    add_func_plot(m._mu, 0, 1.2 * m.t[-1], 1000)
    grid()
    plt.show()

# TODO: Refactor from here

def jelinski_moranda_for_real_data():
    data = read_data('datasets/dataset_6.txt')
    times_of_falls = data
    j = JelinskiMoranda(times_of_falls)

    # Good MTTF plot
    data_plot = [[],[]]
    for i in range(len(times_of_falls)):
        data_plot[0].append(i)
        data_plot[1].append(j.func_MTTF(i))

    data_plot[1] = data_plot[1]#[::-1]
    times_of_falls = times_of_falls#[::-1]
    # with open('G:/jm_model.csv', 'w+') as f:
    #     f.write("i\treal_falls\tmttf\n")
    #     for i in range(len(times_of_falls)):
    #         f.write("{0}\t{1}\t{2:.2f}\n".format(i, times_of_falls[i], data_plot[1][i][0]))

    plt.plot(data_plot[0], data_plot[1], '--', label = 'JM-model error')
    plt.plot(data_plot[0], times_of_falls, label = 'Real error')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
        fancybox=True, shadow=True, ncol=5)
    plt.xlabel("Error")
    plt.ylabel("Mean time to error")
    plt.grid()
    plt.show()

def jelinski_moranda_plot_errors():
    '''Plot Errors for Jelinsky-moranda model'''
    data = read_data('datasets/dataset_6.txt')
    times_of_falls = data[:]
    j = JelinskiMoranda(times_of_falls)
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
    plt.xlabel("Time")
    plt.ylabel("Errors")
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
    # data = read_data('datasets/dataset_6.txt')
    # data = read_data('datasets/test_commercial_data.txt')
    data = read_data('datasets/journal_of_computer_application_dataset.txt')
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
    plt.plot(errors_count[0], errors_count[1], label = 'Real error')

    # Plot model errors
    tau = musa_data#np.linspace(0, 2 * errors_count[0][-1], 100)
    func = m._mu
    plt.plot(tau, func(tau), '--', label = "Musa")
    func = mo._mu
    plt.plot(tau, func(tau), '-.', label = "Musa - Okumoto", )
    func = j.func_n
    plt.plot(tau, func(tau), ':', label = "Jelinski - Moranda")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)

    # with open("G:/dynamic_models.csv", 'w+') as f:
    #     f.write('tau\treal_error\tmusa\tmusa_okumoto\tjm\n')
    #     err = 1
    #     for i in tau:
    #         f.write("{0:.2f}\t{1}\t{2:.2f}\t{3:.2f}\t{4:.2f}\n".format(i, err, m._mu(i)[0], mo._mu(i)[0], j.func_n(i)[0]))
    #         err += 1

    plt.xlabel("Time")
    plt.ylabel("Number of erros")
    plt.grid()
    plt.show()




musa_for_real_data()
# musa_okumoto_for_real_data()
# jelinski_moranda_for_real_data()
# print_failure_rate_for_jm()
# plot_musa_and_musa_okumoto()

# plot_all_models()