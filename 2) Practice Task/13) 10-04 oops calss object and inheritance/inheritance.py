class Parent:
    def p_f_1(self):
        print('walking')


class Child(Parent):
    def c_f_1(self):
        print('crawling')
        self.walk()


d = Child()
d.p_f_1()
d.c_f_1()