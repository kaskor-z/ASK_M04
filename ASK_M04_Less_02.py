def test_function():
    global inner_function  # Если закомментим, возникае ошибки :

    # NameError: name 'inner_function' is not defined.
    # Did you mean: 'test_function'?

    def inner_function():
        print(F'Я в области видимости функции test_function')

    inner_function()


print('\n*********** begin *******************')
test_function()  # при обращении к этой функции текст выводится первый раз
print('\n-------------------------------------')
inner_function()
print('\n************ END *********************')
