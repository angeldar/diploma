__author__ = 'Vasiliy Zemlyanov'

class JelinskiMoranda:

    def __init__(self, X):
        '''
        t - произвольное время между обнаружением i-1 и i ошибок
        k - неизвестный коэффициенте
        B - неизвестное общее число ошибок в ПО
        m >= n+1 - число прогнозируемых (пока не обнаруженных ошибок)
        Xi - интервал времени между соседними ошибками
        :return:
        '''
        self.X = X
        self.n = len(X)
        self.find_m()
        self.func_b()
        self.func_k()
        self.func_lambda()
        self.func_x()
        self.func_t()
        pass

    def func_f(self, m):
        self.f = sum([1.0 / (m - i) for i in range(1, self.n+1)])
        return self.f

    def func_g(self, m):
        self.g = self.n / (m - self.a)
        return self.g

    def func_a(self):
        self.a = sum([i * self.X[i - 1] for i in range(1, self.n+1)]) / sum(self.X)
        return self.a

    def find_m(self):
        # TODO: Здесь нужно правильно найти минимальное значение |f - g|, сейчас халтура
        self.func_a()
        for m in range(self.n+1, 100 * self.n):
            g = self.func_g(m)
            f = self.func_f(m)
            dif = f - g
            #print("m: {0}\n g: {1}\n f: {2}\n dif: {3}".format(m, self.g, self.g, dif))
            if dif < 0:
                self.m = m - 1
                break
        return self.m

    # Коэффициенты
    def func_b(self):
        self.b = self.m - 1
        return self.b

    def func_k(self):
        self.k = self.n / ((self.b + 1) * sum(self.X) - sum([i * self.X[i-1] for i in range(1, self.n+1)]))
        return self.k

    # Определение оценок
    def func_lambda(self, i = None):
        '''
        Интенсивность возникновения ошибок в ПО, после того, как в нем уже обнаружена (i-1) ошибка
        :return:
        '''
        if i is None:
            i = self.n + 1
        self.lambd = self.k * (self.b - (i - 1))
        return self.lambd

    def func_x(self, i = None):
        '''
        Среднее время до появления (i+1) ошибки
        :return:
        '''
        if i is None:
            i = self.n + 1
        self.x = 1.0 / (self.k * (self.b - self.n))
        return self.x

    def func_t(self):
        '''
        Время до окончания тестирования
        :return:
        '''
        self.t = 1.0 / self.k * sum([1.0 / i for i in range(1, self.b - self.n + 1)])
        return self.t

    def debug_print(self):
        print('a: ', self.a)
        print('m: ', self.m)
        print('b: ', self.b)
        print('k: ', self.k)
        print('lambd: ', self.lambd)
        print('x: ', self.x)
        print('t: ', self.t)

test_data = [3, 2, 10, 7, 14, 8, 5, 1, 6, 9, 13, 3, 5, 5, 9, 2, 24, 1, 9, 8, 11, 6, 8, 2, 9, 74, 14, 7, \
             22, 45, 3, 22, 4, 9, 3, 83, 6, 8, 2, 6]

jm = JelinskiMoranda(test_data)
jm.debug_print()