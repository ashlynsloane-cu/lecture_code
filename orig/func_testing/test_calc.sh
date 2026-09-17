test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_add python calc.py add 10 5
assert_exit_code 0
assert_in_stdout "15.0"

run test_sub python3 calc.py sub 10 5
assert_exit_code 0
assert_in_stdout "5.0"

run test_div_by_zero python calc.py div 10 0
assert_exit_code 0
assert_in_stdout "None"

run test_bad_operation python calc.py mul 10 5
assert_exit_code 1
assert_in_stderr "unknown operation"
