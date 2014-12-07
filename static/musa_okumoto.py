__author__ = 'Vasiliy Zemlyanov'

import numpy as np
from scipy.optimize import fsolve

class MusaOkumoto:

    def __init__(self, x, t, beta_init_guess = 0.0001):
        ''':param x: - time from the last error
        :param t: - array with the times of erros'''
        # HACK: VERY IMPORTANT!
        # Musa and Okumoto have mada the error in they book. Instead if tn must be(tn + x)
        self._beta0 = lambda beta, tn   : float(self.n) / (np.log(1 + beta * tn))
        self._lambd = lambda tau        : self.b0 * self.b1 / (self.b1 * tau + 1.0)
        self._mu    = lambda tau        : self.b0 * np.log(self.b1 * tau + 1)
        self._r     = lambda tau, deltat: ((self.b1 * tau + 1) /\
                           (self.b1 * (tau + deltat) + 1)) ** self.b0
        self.x = x
        self.t = t
        self.n = len(t)
        self.tn = t[-1]
        self.beta_init_guess = beta_init_guess
        self.func_beta1()
        self.func_beta0()

    def func_beta0(self):
        # VERY IMPORTANT!
        # Musa and Okumoto have mada the error in they book. Instead if tn must be(tn + x)
        real_tn = self.tn + self.x
        func = self._beta0
        self.b0 = func(self.b1, real_tn)
        return self.b0

    def func_beta1(self):
        # VERY IMPORTANT!
        # Musa and Okumoto have mada the error in they book. Instead if tn must be(tn + x)
        real_tn = (self.tn + self.x)
        # Hard to move from here - because of real and_tn need to solve numerical write here.
        func = lambda beta : - 1.0 / beta * sum([1.0 / (1.0 + beta * ti) for ti in self.t]) \
            + self.n * real_tn / ((1 + beta * real_tn) * np.log(1 + beta * real_tn))
        self.b1 = fsolve(func, self.beta_init_guess, maxfev = 10000)
        return self.b1

    def func_lambd(self, tau = None):
        '''Intensity of errors at the time tau'''
        if tau is None:
            tau = self.t[-1] + self.x
        func = self._lambd
        return func(tau)

    def func_mu(self, tau = None):
        '''Mean number of errors'''
        if tau is None:
            tau = self.t[-1] + self.x
        func = self._mu
        return func(tau)

    def func_r(self, tau = None, deltat = None):
        '''The function of reliability'''
        if tau is None: # if the time is not set - use the time of last error
            tau = self.t[-1]
        if deltat is None: # if deltat is not set - use the time of last error
            deltat = self.x

        func = self._r

        return func(tau, deltat)

    def debug_output(self):
        print("Musa model:\n"
              "n: {0}\n"
              "tn: {1}\n"
              "x: {2}\n"
              "t: {3}\n"
              "sum(t): {4}\n"
              "b0: {5}\n"
              "b1: {6}".format(self.n, self.tn, self.x, self.t, self.sum_t, self.b0, self.b1))

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

def test_musa():
    print("Musa model test: ")
    time_passed = 15
    times_of_falls = [10, 18, 32, 49, 64, 86, 105, 132, 167, 207]
    m = MusaOkumoto(time_passed, times_of_falls)
    m.plot_mu_and_errors()
    print("b1: {0}".format(m.b1))          # [ 0.01138508]
    print("b0: {0}".format(m.b0))          # [ 7.93281954]
    print("lambda: {0}".format(m.func_lambd())) # [ 0.02560343]
    print("mu: {0}".format(m.func_mu()))        # [ 10.]
    print("r: {0}".format(m.func_r()))          # [ 0.67458381]
    print("Done")

# test_musa()