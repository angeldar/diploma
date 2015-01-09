__author__ = 'Vasiliy Zemlyanov'

import numpy as np
from scipy.optimize import fsolve

class JelinskiMoranda:

    def __init__(self, X):
        '''t - time from i-1 and i error
        phi - unknoun coefficient, in some resources - K
        N - unknon total number of errors in program, in some resources - B
        m >= n+1 - number of errors, that are not found
        Xi - time interval between closest errors'''

        self.X = X
        self.n = len(X)
        self.find_N()

        self.func_phi()
        self.func_lambda()


    def func_left(self, cur_n): #+
        res = sum([1.0 / (cur_n - i) for i in range(0, self.n)])
        return res

    def func_right(self, cur_n): #+
        # self.g = self.n / (cur_n - self.a)
        res = self.n / (cur_n - \
                (1.0 / sum(self.X)) *\
                sum([i * self.X[i] for i in range(0, len(self.X))]))
        return res

    def func_phi(self): #+
        '''Coefficient, that shows the input to Intensivnost otkazor by each Otkaz'''
        self.phi = self.n / (self.N *\
                   sum(self.X) - sum([(i) * self.X[i] for i in range(0, len(self.X))]))
        return self.phi

    def find_N(self): #+
        N_init_guess = self.n + 1
        func = lambda tau: self.func_left(tau) - self.func_right(tau)
        self.N = np.ceil(fsolve(func, N_init_guess))
        return self.N

    def func_lambda(self, i = None): #+
        ''' Intensity of the errors, after i-1 error was found'''
        if i is None:
            i = self.n# + 1
        self.lambd = self.phi * (self.N - i)
        return self.lambd

    def func_MTTF(self, i = None): #+
        # Mean Time To Failure
        if i is None:
            i = self.n
        res = 1.0 / (self.phi * (self.N - (i)))
        return res

    def func_f(self, i = None): #+
        '''Function of the density of errors'''
        if i is None:
            i = self.n - 1
        res = self.phi * (self.N - i) * np.exp(-self.phi * (self.N - (i)) * self.X[i])
        return res

    def func_F(self, i = None): #+
        '''Function of distribution of the errors'''
        if i is None:
            i = self.n - 1
        res = 1.0 - np.exp(-self.phi * (self.N - (i)) * self.X[i])
        return res

    def func_R(self, i = None): #+
        '''Function of reliability on the i-th interval'''
        if i is None:
            i = self.n - 1
        res = 1.0 - self.func_F(i)
        return res

    def debug_print(self):
        print('N: ', self.N)
        print('phi: ', self.phi)
        print('lambd: ', self.lambd)
        print('f: ', self.func_f())
        print('F: ', self.func_F())
        print('R: ', self.func_R())
        print('MTTF: ', self.func_MTTF())

        print('func_n', self.func_n())

    # Not canonical, but can be used
    def func_t(self):
        '''Time before end of testing'''
        self.t = 1.0 / self.phi * sum([1.0 / i for i in range(1, self.N - self.n + 1)])
        return self.t

    def func_n(self, tau = None):
        '''Function of mean value of errors'''
        if tau is None:
            tau = sum(self.X)
            print(tau)
        func = lambda tau: self.n * (1 - np.exp(-self.phi * tau))
        return func(tau)

# test_data = [3, 2, 10, 7, 14, 8, 5, 1, 6, 9, 13, 3, 5, 5, 9, 2, 24, 1, 9, 8, 11, 6, 8, 2, 9, 74, 14, 7, \
#              22, 45, 3, 22, 4, 9, 3, 83, 6, 8, 2, 6]
#
#
# jm = JelinskiMoranda(test_data)
# jm.debug_print()