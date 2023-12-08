def gen_unit_test(func, input, output):
    act_out = func(input) #actual output
    success = act_out == output
    if type(success) != bool:
        success = success.all()
    print("     Function name:", func.__name__)
    print("          Input(s):", input)
    print("Expected output(s):", output)
    print("  Actual output(s):", act_out)
    print("\nThe test did " + int(success) * "not " + "fail!\n")
    assert success
    return