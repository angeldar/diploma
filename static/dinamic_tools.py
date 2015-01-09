from static.musa import Musa
from static.musa_okumoto import MusaOkumoto
from static.jelinski_moranda import  JelinskiMoranda
import static.plot as plot
import static.data_processing as dp
import numpy as np

# Musa model

def get_musa_data(path_to_data):
    data = dp.read_data(path_to_data)
    time_passed = data[-1] - data[-2]
    errors = dp.convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    time_of_last_error = times_of_falls[-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)

    x = [int(i) for i in np.linspace(1, 1.2 * time_of_last_error, 20)]
    # Mean time of errors to the time of work
    y_mu = [int(m.func_mu(i)) for i in x]
    # Failure raite aka Intensivnost otkazov
    y_lambda = [round(float(m.func_lambd(i)),4) for i in x]
    # Reliability function aka Funkciya nadezhnosti
    prediction_time_of_work = 100
    y_r = [round(float(m.func_r(i, prediction_time_of_work)),4) for i in x]

    return {
        'mu': {'x': x, 'y': y_mu},
        'lambda': {'x': x, 'y': y_lambda},
        'r': {'x': x, 'y': y_r}}

# Musa-Okumoto model

def get_musa_okumoto_data(path_to_data):
    data = dp.read_data(path_to_data)
    time_passed = data[-1] - data[-2]
    errors = dp.convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    time_of_last_error = times_of_falls[-1]
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)

    x = [int(i) for i in np.linspace(1, 1.2 * time_of_last_error, 20)]
    # Mean time of errors to the time of work
    y_mu = [int(m.func_mu(i)) for i in x]
    # Failure raite aka Intensivnost otkazov
    y_lambda = [round(float(m.func_lambd(i)),4) for i in x]
    # Reliability function aka Funkciya nadezhnosti
    prediction_time_of_work = 100
    y_r = [round(float(m.func_r(i, prediction_time_of_work)),4) for i in x]

    return {
        'mu': {'x': x, 'y': y_mu},
        'lambda': {'x': x, 'y': y_lambda},
        'r': {'x': x, 'y': y_r}}

def musa_okumoto_plot(path_to_data):
    data = dp.read_data(path_to_data)
    time_passed = data[-1] - data[-2]
    errors = dp.convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)
    plot.add_errors_plot(data)
    plot.add_func_plot(m._mu, 0, 1.2 * m.t[-1], 1000)
    plot.grid()
    plot.show()

## Jelinsky-Morands plots

def jelinski_moranda_MTTF(path_to_data, file_to_write_data = ''):
    data = dp.read_data(path_to_data)
    times_of_falls = data[:]
    j = JelinskiMoranda(times_of_falls)
    x = [i for i in range(len(times_of_falls))]
    y = [j.func_MTTF(i) for i in x]

    if file_to_write_data:
        with open(file_to_write_data, 'w+') as f:
            f.write("i\treal_falls\tmttf\n")
            for i in range(len(times_of_falls)):
                f.write("{0}\t{1}\t{2:.2f}\n".format(i, times_of_falls[i], y[i][0]))

    plot.add_xy_plot(x, y)           # style '--', label = 'JM-model error'
    plot.add_xy_plot(x, times_of_falls) # style label = 'Real error'
    plot.xlabel("Error")
    plot.ylabel("Mean time error")
    plot.grid()
    plot.show()

def jelinski_moranda_plot_errors(path_to_data):
    '''Plot Errors for Jelinsky-moranda model'''
    data = dp.read_data(path_to_data)
    times_of_falls = data[:]
    j = JelinskiMoranda(times_of_falls)
    plot.add_errors_plot(times_of_falls)
    plot.add_func_plot(j.func_n, 0, dp.time_of_last_error(times_of_falls), 1000)
    plot.xlabel("Time")
    plot.ylabel("Errors")
    plot.grid()
    plot.show()

## Combined plots

def plot_musa_and_musa_okumoto(path_to_data):
    data =dp.read_data(path_to_data)
    time_passed = data[-1] - data[-2]
    times_of_errors = dp.convert_time_between_errors_to_time_of_errors(data)[:-1]
    init_guess = 0.00000001
    time_of_last_error = dp.time_of_last_error(data)
    m = Musa(time_passed, times_of_errors, init_guess)
    mo = MusaOkumoto(time_passed, times_of_errors, init_guess)
    plot.add_errors_plot(data)
    plot.add_func_plot(m._mu, 0, 1.2 * time_of_last_error, 1000)
    plot.add_func_plot(mo._mu, 0, 1.2 * time_of_last_error, 1000)
    plot.xlabel("Time")
    plot.ylabel("Errors")
    plot.grid()
    plot.show()

def plot_all_models(path_to_data, init_guess = 0.000001):
    data = dp.read_data(path_to_data)
    time_passed = data[-1] - data[-2]
    jm_data = data[:]
    times_of_falls = dp.convert_time_between_errors_to_time_of_errors(data)[:-1]
    time_of_last_error = dp.time_of_last_error(data)
    m = Musa(time_passed, times_of_falls, init_guess)
    mo = MusaOkumoto(time_passed, times_of_falls, init_guess)
    j = JelinskiMoranda(jm_data)
    plot.add_errors_plot(data, {'label': 'Real errors'}) # label = 'Real error'
    plot.add_func_plot(m._mu, 0, 1*time_of_last_error, 100, {'label': "Musa"})     # style : '--', label = "Musa"
    plot.add_func_plot(mo._mu, 0, 1*time_of_last_error, 100, {'label': "Musa-Okumoto"})    # style : '-.', label = "Musa - Okumoto"
    plot.add_func_plot(j.func_n, 0, 1*time_of_last_error, 100, {'label': 'Jelinsky-Moranda'})  # style : ':',  label = "Jelinski - Moranda"

    plot.legend()

    # with open("G:/dynamic_models.csv", 'w+') as f:
    #     f.write('tau\treal_error\tmusa\tmusa_okumoto\tjm\n')
    #     err = 1
    #     for i in tau:
    #         f.write("{0:.2f}\t{1}\t{2:.2f}\t{3:.2f}\t{4:.2f}\n".format(i, err, m._mu(i)[0], mo._mu(i)[0], j.func_n(i)[0]))
    #         err += 1

    plot.xlabel("Time")
    plot.ylabel("Number of erros")
    plot.grid()
    plot.show()

if __name__ == '__main__':
    get_musa_data('./datasets/dataset_6.txt')
    # jelinski_moranda_MTTF('./datasets/dataset_6.txt')
    # plot_all_models('./datasets/dataset_6.txt')
    # plot_all_models('./datasets/journal_of_computer_application_dataset.txt')
    # plot_all_models('./datasets/dataset_40.txt')

    # jelinski_moranda_MTTF('./datasets/dataset_6.txt', 'G:/jm_6.csv')
    # jelinski_moranda_MTTF('./datasets/journal_of_computer_application_dataset.txt', 'G:/jm_journal_of_ca.csv')
    # jelinski_moranda_MTTF('./datasets/dataset_40.txt', 'G:/jm_40.csv')

    # plot_all_models('./datasets/test_commercial_data.txt', init_guess = 0.00000001)
