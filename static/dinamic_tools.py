from static.musa import Musa
from static.musa_okumoto import MusaOkumoto
from static.jelinski_moranda import  JelinskiMoranda
import static.plot as plot

## Data reading and transforming
def read_data(filename):
    f = open(filename)
    data = []
    for row in f:
        data.append(int(row.strip()))
    return data

# TODO: Move to data processing helpers
def convert_time_between_errors_to_time_of_errors(time_between_errors):
    res = time_between_errors[:]
    for i in range(1, len(res)):
        res[i] += res[i-1]
    return res

def time_of_last_error(time_between_errors):
    return sum(time_between_errors)

# Musa plots

def musa_for_real_data():
    data = read_data('datasets/dataset_6.txt')
    time_passed = data[-1] - data[-2]
    errors = convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    plot.add_func_plot(m._lambd, 1, 10000, 1000)
    plot.grid()
    plot.show()
    plot.add_errors_plot(data)
    plot.add_func_plot(m._mu, 0, time_of_last_error(data), 1000)
    plot.grid()
    plot.show()

# Musa-Okumoto plots

def musa_okumoto_for_real_data():
    data = read_data('datasets/test_commercial_data.txt')
    time_passed = data[-1] - data[-2]
    errors = convert_time_between_errors_to_time_of_errors(data)
    times_of_falls = errors[:-1]
    init_guess = 0.00000001
    m = MusaOkumoto(time_passed, times_of_falls, init_guess)
    plot.add_errors_plot(data)
    plot.add_func_plot(m._mu, 0, 1.2 * m.t[-1], 1000)
    plot.grid()
    plot.show()

## Jelinsky-Morands plots

def jelinski_moranda_MTTF():
    data = read_data('datasets/dataset_6.txt')
    times_of_falls = data[:]
    j = JelinskiMoranda(times_of_falls)
    x = [i for i in range(len(times_of_falls))]
    MTTF = j.func_MTTF(x)
    plot.add_xy_plot(x, MTTF)           # style '--', label = 'JM-model error'
    plot.add_xy_plot(x, times_of_falls) # style label = 'Real error'
    plot.xlabel("Error")
    plot.ylabel("Mean time error")
    plot.grid()
    plot.show()

def jelinski_moranda_plot_errors():
    '''Plot Errors for Jelinsky-moranda model'''
    data = read_data('datasets/dataset_6.txt')
    times_of_falls = data[:]
    j = JelinskiMoranda(times_of_falls)
    plot.add_errors_plot(times_of_falls)
    plot.add_func_plot(j.func_n, 0, time_of_last_error(times_of_falls), 1000)
    plot.xlabel("Time")
    plot.ylabel("Errors")
    plot.grid()
    plot.show()

## Combined plots

def plot_musa_and_musa_okumoto():
    data = read_data('datasets/journal_of_computer_application_dataset.txt')
    time_passed = data[-1] - data[-2]
    times_of_errors = convert_time_between_errors_to_time_of_errors(data)[:-1]
    init_guess = 0.00000001
    m = Musa(time_passed, times_of_errors, init_guess)
    mo = MusaOkumoto(time_passed, times_of_errors, init_guess)
    plot.add_errors_plot(data)
    plot.add_func_plot(m._mu, 0, 1.2 * time_of_last_error(data), 1000)
    plot.add_func_plot(mo._mu, 0, 1.2 * time_of_last_error(data), 1000)
    plot.xlabel("Time")
    plot.ylabel("Errors")
    plot.grid()
    plot.show()

def plot_all_models():
    data = read_data('datasets/dataset_6.txt')
    time_passed = data[-1] - data[-2]
    jm_data = data[:]
    times_of_falls = convert_time_between_errors_to_time_of_errors(data)[:-1]
    init_guess = 0.000001
    m = Musa(time_passed, times_of_falls, init_guess)
    mo = MusaOkumoto(time_passed, times_of_falls, init_guess)
    j = JelinskiMoranda(jm_data)
    plot.add_errors_plot(data) # label = 'Real error'

    plot.add_func_plot(m._mu, 0, time_of_last_error(data), 100)     # style : '--', label = "Musa"
    plot.add_func_plot(mo._mu, 0, time_of_last_error(data), 100)    # style : '-.', label = "Musa - Okumoto"
    plot.add_func_plot(j.func_n, 0, time_of_last_error(data), 100)  # style : ':',  label = "Jelinski - Moranda"

    # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
    #       fancybox=True, shadow=True, ncol=5)

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

plot_all_models()
