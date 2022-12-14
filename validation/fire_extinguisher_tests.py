def validate(function):
    INPUTS = [
        """%%%%%%%%%%
%..%..%00%
%.0%.0%00%
%%%%%%%%%%
%..%..%..%
%..%..%..%
%%%%%%%%%%
%..%..%..%
%.0%..%..%
%%%%%%%%%%""".split('\n'),
        """%%%%%%%%%%
%.....%00%
%.0%.0%00%
%%%%%.%%.%
%..%..%..%
%..%..%..%
%%%%.%%%.%
%.....%..%
%.0%.....%
%%%%%%%%%%""".split('\n'),
        """%%%%%%%%%%%%%%%%%%%%
%..%%%%.%0.....%...%
%.%..%.......%.0.%.%
%.%%%...%....%..0.%%
%.%%.%..0..%..%0...%
%%..%0%..%%0...%...%
%...%.%..........%%%
%.%..%%.%%.%%..%...%
%%...%..0..%..%....%
%.%.%%.00%...000.%.%
%....%....%...0%...%
%%..%.%......%.....%
%%0.%0..000.....%%.%
%....%%0%%.....%.%.%
%.%..%%%.%%00.%..%.%
%%.0..0%.........%%%
%...%%%......0%%.%.%
%%....%.....0..0...%
%0..0.....%.%..%..%%
%%%%%%%%%%%%%%%%%%%%""".split('\n'),
        """%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%....%%.%...%%00%....%%....%0.%..%.%%%.%
%..%%.0..%....%.%..%%.%.%..0%.%..%..%0%%
%..%%.%%%.%%..%.%%.0....%%0..%.%0..%%..%
%%%%..%..%%%..%.%......%..%%...%.....%.%
%..%.%.%.%..%...%.%......%.%%.%.....%..%
%%...%%%%...%...%..%....%.%%%%%%0......%
%..%%%%..%.....%0...%%%%0%..%%%.%.%.%..%
%.%..%0.%.......%%.%.%......%0.%..%..%%%
%%.%0...%..%%.0...0%%.....%%.0%.%...%%.%
%%%..%.0..%.%.%%.....%..%%0%..%.%0..%.%%
%.%.%.%%%.%%%.%%0.%.%%....00..%%%.%%%%.%
%%.%..%%...%...%0%%.%%...%.....0.%%%.%.%
%.%.%..0..0%%%...%.%.%.%.%..0%%......%.%
%%..%.%%...%%%..%..0.....%..%..%%..%..%%
%.0....%.%...%..%..%%%.%0.%.%.%..%%.%%%%
%....%..%...%%%%%%.%.0......%...%.%%%..%
%0%.%.%.%.....%.%..%%..%.....%%%..%%%%.%
%%.0%..%.%%..%.%...%.%.%.%.%.%.%..%%%%%%
%.0......%......%%.%%%%%.%%.%%%.%....%%%
%....%..%%...0..0%0%0%%%%..%%...%.%%...%
%...0.%%.%.%..%.%.%..%.%%%%..%..0.%...%%
%..0.%...%%...%%0%%.%..%%00%..%%...0...%
%%.%......%%....%%%..%....%..0..00.%.%.%
%%..0......%.%%%..00..%%...%%.%..%.%..%%
%.%..%%%.0%%..0.%%%..%%%%%........%.%..%
%..%........%%....%.%...%.%%0%%.%..%%%.%
%%%%..%0.%%..%.%...%%%...%%%...%.00%...%
%.%....%%.%.%%%....%..%%.%%.....%......%
%%%.%%%........%.%...%%..%..%...0%...%.%
%%.%...%%..%%.%%....%%.%%.%.%.%..%%.00%%
%%.%%.....%%%.%.%..%.0%%%.....%....%...%
%......0.%.%.%..%.%%0...%%0.%%%%%.%..%%%
%..%0.%.%.%...%0..%0%.%...%%..%%.%%%%..%
%%..%%0%.0%%%..%%%%%..%..%......%...%.%%
%.......%%..0..%%.%%%.%%%.%.%....%%...%%
%%%%.%%%%.0..%%%%.%.%.....%.%..%..%....%
%..%.0..%..%...0.0..%.........%...%...0%
%.%.%.0%.%..%.%.%...%%.....%..%.%%.%%%.%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%""".split('\n')
    ]
    EXP_OUTPUTS = [
        5,
        1,
        3,
        39
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return a bool"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f"Test Case {i+1} Failed")
            if i >= 3:
                continue
            
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')