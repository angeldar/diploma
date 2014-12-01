__author__ = 'Vasiliy Zemlyanov'

import numpy as np
from scipy.optimize import fsolve

class Musa:
    # TODO: test

    def __init__(self, x, t, beta_init_guess = 1):
        '''
        :param x: - время прошедшее с момента последнего отказа
        :param t: - массив, содержащий временя отказов
        :return:
        '''
        self._beta0 = lambda beta : self.n / (1 - np.exp(-beta * (self.tn + self.x)))
        self._beta1 = lambda beta : self.n / beta -\
                             (self.n * (self.tn + self.x)) /\
                             (np.exp((self.tn + self.x) * beta)  - 1) - self.sum_t
        self._mu    = lambda tau: self.b0 * (1 - np.exp(-self.b1 * tau))
        self._lambd = lambda tau: self.b0 * self.b1 * np.exp(-self.b1 * tau)
        self._r     = lambda tau, i: np.exp(-self.b0 * np.exp(-self.b1 * self.t[i]) * (1 - np.exp(-self.b1 * tau)))

        self.x = x
        self.t = t
        self.n = len(t)
        self.tn = t[-1]
        self.sum_t = sum(t)
        self.beta_init_guess = beta_init_guess
        self.func_beta1()
        self.func_beta0()

    def func_beta0(self):
        func = self._beta0 #lambda beta : self.n / (1 - np.exp(-beta * (self.tn + self.x)))
        self.b0 = func(self.b1)
        return self.b0

    def func_beta1(self):
        func = self._beta1 #lambda beta : self.n / beta -\
                            #              (self.n * (self.tn + self.x)) /\
                            #              (np.exp((self.tn + self.x) * beta)  - 1) - self.sum_t
        self.b1 = fsolve( func, self.beta_init_guess)
        return self.b1

    def func_mu(self, tau = None):
        # Среднее количество отказов
        func = self._mu #lambda tau: self.b0 * (1 - np.exp(-self.b1 * tau))
        if tau is None:
            tau = self.t[-1] + self.x
        return func(tau)

    def func_lambd(self, tau = None):
        # Интенсивность отказов
        func = self._lambd #tau: self.b0 * self.b1 * np.exp(-self.b1 * tau)
        if tau is None:
            tau = self.t[-1] + self.x
        return func(tau)

    def func_r(self, tau = None, i = None):
        # TODO: Переделать эту фуикцнию. Нужно отказаться от индекса в массиве I и указывать время
        # Функция надежности
        if tau is None:
            tau = self.x
        if i is None:
            i = self.n - 1
        # old version: lambda tau: np.exp(-self.b0 * np.exp(-self.b1 * self.t[i]) * (1 - np.exp(-self.b1 * tau)))
        func = self._r
        return func(tau, i)

    def debug_output(self):
        print("Musa model:\n"
              "n: {0}\n"
              "tn: {1}\n"
              "x: {2}\n"
              "t: {3}\n"
              "sum(t): {4}\n"
              "b0: {5}\n"
              "b1: {6}".format(self.n, self.tn, self.x, self.t, self.sum_t, self.b0, self.b1))

    def debug_plot_b1(self, minx=-0.0001, maxx=2, step=2000):
        import matplotlib.pyplot as plt
        func = self._beta1
        tau = np.linspace(minx, maxx, step)
        plt.plot(tau, func(tau))
        plt.xlabel("tau")
        plt.ylabel("expression value")
        plt.grid()
        plt.show()

    def plot_mu_and_errors(self):
        import matplotlib.pyplot as plt

        # Plot real errors
        errors_count = [[],[]]
        count = 1
        for val in self.t:
            errors_count[0].append(val)
            errors_count[1].append(count)
            count += 1
        plt.plot(errors_count[0], errors_count[1])

        # Plot model errors
        tau = np.linspace(0, 1.2 * errors_count[0][-1], 1000)
        func = self._mu
        plt.plot(tau, func(tau))

        plt.xlabel("tau")
        plt.ylabel("expression value")
        plt.grid()
        plt.show()

    def plot_func(self, minx=-0.0001, maxx=2, step=2000):
        import matplotlib.pyplot as plt
        tau = np.linspace(minx, maxx, step)
        func = self._mu
        plt.plot(tau, func(tau))
        plt.xlabel("tau")
        plt.ylabel("expression value")
        plt.grid()
        plt.show()


def test_musa(plot_graph = False):
    print("Musa model test: ")
    time_passed = 15
    times_of_falls = [10, 18, 32, 49, 64, 86, 105, 132, 167, 207]
    musa = Musa(time_passed, times_of_falls, 1)

    if plot_graph:
        musa.debug_plot_b1(-0.1, 0.1)

    print("b0: {0}\nb1: {1}".format(musa.b0[0], musa.b1[0]))
    assert musa.b0 == 13.569632291454864, "Wrong value of b0 : " + str(musa.b0)
    assert musa.b1 == 0.00601518822260904, "Wrong value of b1 : "  + str(musa.b1)
    assert musa.func_mu() == 10.0, "Wrong value of mu : " + str(musa.func_mu())
    assert musa.func_lambd() == 0.0214720101186, "Wrong value of lambda : " +  str(musa.func_lambd()) # Странно, в каноническом пимере здесь 22
    assert musa.func_r() == 0.713867792842, "Wrong value of r : " + str(musa.func_r())
    print("Done")

def dinamic_musa_test():
    time_passed = 15
    times_of_falls = [10, 18, 32, 49, 64, 86, 105, 132, 167, 207, 222]
    res = []
    for i in range(2, len(times_of_falls)+1):
        m = Musa(times_of_falls[i-1] - times_of_falls[i-2], times_of_falls[:i-1])
        print("Test: {0}".format(i-1))
        print("Time: {0}".format(times_of_falls[i-1] - times_of_falls[i-2]))
        print("Data: {0}".format(times_of_falls[:i]))
        print("Res: {0}\n===\n".format(m.func_mu()))
        res.append(m.func_mu()[0])
    print(res)

# test_musa()