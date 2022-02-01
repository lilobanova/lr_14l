#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(tag):
    def fun2(s):
        return f'<{tag}>{s}</{tag}>'
    return fun2


if __name__ == "__main__":
    tag = input("Введите тег: ").split()
    s = input("Введите строку: ").split()
    print(fun1(tag)(s))
