from unittest import TestCase


def print_foobar():
    my_list = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            my_list.append('FooBar')
        elif i % 3 == 0:
            my_list.append('Foo')
        elif i % 5 == 0:
            my_list.append('Bar')
        else:
            my_list.append(i)
    return my_list


print(print_foobar())


def is_foo(n):
    return print_foobar()[n - 1] == 'Foo'


def is_bar(n):
    return print_foobar()[n - 1] == 'Bar'


def is_foobar(n):
    return is_foo(n) == is_bar(n)


class TestIsFoo(TestCase):

    def test_is_foo(self):
        self.assertTrue(is_foo(3))


class TestIsBar(TestCase):
    def test_is_bar(self):
        self.assertTrue(is_bar(10))


class TestIsFoobar(TestCase):
    def test_is_foobar(self):
        self.assertTrue(is_foobar(15))
