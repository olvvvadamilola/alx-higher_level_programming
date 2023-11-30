def magic_calculation(a, b):
    imported_module = __import__(
        'magic_calculation_102',
        globals(),
        locals(),
        ['add', 'sub']
    )
    add_func = imported_module.add
    sub_func = imported_module.sub

    if a < b:
        c = add_func(a, b)
        for i in range(4, 6):
            c = add_func(c, i)
        return c
    else:
        return sub_func(a, b)
