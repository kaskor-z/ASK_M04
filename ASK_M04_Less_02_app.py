def test_function():
    global inner_function, b, a, c, m_2  # Если закомментим, возникают ошибки :
                                        # UnboundLocalError: cannot access local variable 'b'
                                        # where it is not associated with a value    и
                                        # main-программа не видит функцию inner_function()
    print(F'inside 3 - Это функция test_function()')
    print(locals())

    def inner_function(*args):
        global a
        print('______________________________________')
        print(F'Я в области видимости функции test_function')
        a += 8
        d = 24
        m_4 = m_3 + 100
        print(locals())
        print(F'------- m_4 = {m_4}-------------------------------')
        return d
        pass

    print(F'    4 - Вызов функции test_function():')
    b += 3
    c = 54
    m = 15
    m_2 += m
    m_3 = 1
    m_3 += m_2
    inner_function(m_3)
    print(F'm_3 = {m_3}')
    print(locals())
    pass


a = 2
b = 12
m_2 = 25
print(globals())
print(F'    1 - Вызов функции test_function():')
test_function()
print(F'    2 - Вызов функции inner_function():')
print(F'c = {c}  !!!!!!!!!!!!!!!!!!!!!!!!!!!')
c = inner_function()
print(F'a = {a} ; b = {b} ; c = {c} ; m_2 = {m_2}  ====================')
print(globals())
print('\n************ END *********************')
