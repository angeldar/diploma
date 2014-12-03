__author__ = 'Vasiliy Zemlyanov'

import numpy as np
from scipy.optimize import fsolve

class JelinskiMoranda:

    def __init__(self, X):
        '''
        t - произвольное время между обнаружением i-1 и i ошибок
        phi - неизвестный коэффициенте (в ряде источников обозначен как K)
        N - неизвестное общее число ошибок в ПО (в ряде источников обозначен как B)
        m >= n+1 - число прогнозируемых (пока не обнаруженных ошибок)
        Xi - интервал времени между соседними ошибками
        :return:
        '''

        self.X = X
        self.n = len(X)
        self.find_N()

        self.func_phi()
        self.func_lambda()


    def func_left(self, cur_n): #+
        res = sum([1.0 / (cur_n - (i - 1)) for i in range(1, self.n+1)])
        return res

    def func_right(self, cur_n): #+
        # self.g = self.n / (cur_n - self.a)
        res = self.n / (cur_n - \
                (1.0 / sum(self.X)) *\
                sum([(i - 1) * self.X[i-1] for i in range(1, len(self.X)+1)]))
        return res

    def find_N(self): #+
        N_init_guess = self.n + 1
        func = lambda tau: self.func_left(tau) - self.func_right(tau)
        self.N = np.ceil(fsolve(func, N_init_guess))
        return self.N

    def func_phi(self): #+
        '''
        Коэффициент пропорциональности, показывающий вклад в интенсивность отказов
        внесенный каждым отказом
        :return:
        '''
        self.phi = self.n / (self.N *\
                   sum(self.X) - sum([(i-1) * self.X[i-1] for i in range(1, len(self.X)+1)]))
        return self.phi

    # Определение оценок
    def func_lambda(self, i = None): #+
        '''
        Интенсивность возникновения ошибок в ПО, после того, как в нем уже обнаружена (i-1) ошибка
        :return:
        '''
        if i is None:
            i = self.n# + 1
        self.lambd = self.phi * (self.N - (i - 1))
        return self.lambd

    def func_MTTF(self, i = None): #+
        # Mean Time To Failure
        if i is None:
            i = self.n
        res = 1.0 / (self.phi * (self.N - (i - 1)))
        return res

    def func_f(self, i = None): #+
        '''
        Функция плотности отказов
        '''
        if i is None:
            i = self.n - 1
        res = self.phi * (self.N - (i - 1)) * np.exp(-self.phi * (self.N - (i - 1)) * self.X[i])
        return res

    def func_F(self, i = None): #+
        '''
        Функция распределения ошибок
        '''
        if i is None:
            i = self.n - 1
        res = 1.0 - np.exp(-self.phi * (self.N - (i - 1)) * self.X[i])
        return res

    def func_R(self, i = None): #+
        '''
        Функция надежности на i-м интервале
        '''
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


    # def func_x(self, i = None):
    #     '''
    #     Среднее время до появления (i+1) ошибки
    #     :return:
    #     '''
    #     if i is None:
    #         i = self.n + 1
    #     self.x = 1.0 / (self.phi * (self.N - self.n))
    #     return self.x

    # Коэффициенты
    # def func_N(self): #+
    #     '''
    #     Неизвестное общее количество ошибок. В ряде источников N.
    #     :return:
    #     '''
    #     self.N = self.m - 1
    #     return self.N

    # def func_a(self):
    #     self.a = sum([i * self.X[i - 1] for i in range(1, self.n+1)]) / sum(self.X)
    #     return self.a

    # Не совсем канонично, но можно использовать
    def func_t(self):
        '''
        Время до окончания тестирования
        :return:
        '''
        self.t = 1.0 / self.phi * sum([1.0 / i for i in range(1, self.N - self.n + 1)])
        return self.t

    def func_n(self, tau = None):
        # TODO: TEST
        '''
        Функция среднего значения текущего количества отказов
        '''
        if tau is None:
            tau = sum(self.X)
            print(tau)
        func = lambda tau: self.n * (1 - np.exp(-self.phi * tau))
        return func(tau)

    # def odl_debug_print(self):
    #     print('a: ', self.a)
    #     print('m: ', self.m)
    #     print('b: ', self.b)
    #     print('k: ', self.k)
    #     print('lambd: ', self.lambd)
    #     print('x: ', self.x)
    #     print('t: ', self.t)
    #     print('n: ', self.func_n())

# test_data = [3, 2, 10, 7, 14, 8, 5, 1, 6, 9, 13, 3, 5, 5, 9, 2, 24, 1, 9, 8, 11, 6, 8, 2, 9, 74, 14, 7, \
#              22, 45, 3, 22, 4, 9, 3, 83, 6, 8, 2, 6]
#
#
# jm = JelinskiMoranda(test_data)
# jm.debug_print()