def validate(function):
    INPUTS = [
        "He1lo!",
        "123456",
        'wjadiowadwa41!',
        'wjadiowadwa41',
        "2!grt",
        "PA££W0RD",
    ]
    EXP_OUTPUTS = [
        True,
        False,
        True,
        False,
        False,
        True,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, bool), "Function did not return bool"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')