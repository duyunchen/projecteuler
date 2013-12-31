import sys
import time
from os import listdir
import subprocess as sub

NUM = 2
LANGUAGE = 'java'


##############################################################################
##############################################################################

# Reads in the answer key
def read_key():
    with open('data/key.dat') as f:
        keys = map(lambda x: x.split(':'), f.read().split('\n'))
    return {int(key[0]): key[1].strip() for key in keys if len(key) == 2}
key = read_key()

# Add directories to path
sys.path.insert(0, 'solutions/python')


# Converts an integer to xxx string format
def convert(number):
    s = str(number)
    while len(s) < 3:
        s = '0' + s
    return s


# Run a python solution given number
def run_python(number):
    module_name = 'p' + convert(number)
    print 'Running ' + module_name + '.py'
    solution = __import__(module_name)
    startTime = int(round(time.time() * 1000))
    result = str(solution.run())
    print 'Result: ' + result
    endTime = int(round(time.time() * 1000))
    runtime = str(endTime - startTime)
    print 'Runtime: ' + runtime + ' ms'
    print key[number]
    return result == key[number], runtime


# Run all python solutions
def run_all_python():
    key = read_key()
    count, correct = 0, 0
    for module in listdir('solutions/python'):
        if module[0] == 'p' and module[-2:] == 'py':
            module = module.split('.')[0]
            result = run_python(int(module[1:]))
            count += 1
            correct += 1 if result else 0

    print 'CORRECT: ' + str(correct) + '/' + str(count)


# Run a c++ solution given number
def run_cpp(number, delete_build=True):
    # first compile the c++ file
    file_name = 'p' + convert(number)
    src_path = 'solutions/c++/' + file_name + '.cpp'
    _, errors = run_command(['g++', '-o', file_name, src_path])
    if errors:
        return errors

    # run the executable
    print 'Running ' + file_name
    startTime = int(round(time.time() * 1000))
    result, errors = run_command(['./' + file_name])
    endTime = int(round(time.time() * 1000))
    if errors:
        return errors

    result = result.strip()
    print 'Result: ' + result
    runtime = str(endTime - startTime)
    print 'Runtime: ' + runtime + ' ms'

    # delete the compiled file
    if delete_build:
        _, errors = run_command(['rm', file_name])
        if errors:
            return errors

    return result == key[number], runtime


def run_java(number, delete_build=True):
    # first compile the java file
    file_name = 'p' + convert(number)
    src_path = 'solutions/java/'
    file_path = src_path + file_name + '.java'
    class_path = src_path + file_name.upper() + '.class'

    _, errors = run_command(['javac', '-sourcepath', src_path,
                             file_path])
    if errors:
        return errors

    print 'Running ' + file_name
    startTime = int(round(time.time() * 1000))
    result, errors = run_command(['java', '-classpath', 'solutions/java',
                             file_name.upper()])
    endTime = int(round(time.time() * 1000))
    if errors:
        return errors

    result = result.strip()
    print 'Result: ' + result
    runtime = str(endTime - startTime)
    print 'Runtime: ' + runtime + ' ms'

    # delete the compiled file
    if delete_build:
        _, errors = run_command(['rm', class_path])
        if errors:
            return errors

    return result == key[number], runtime


def run_command(command):
    p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
    return p.communicate()


if __name__ == '__main__':
    if LANGUAGE == 'python':
        print run_python(NUM)
    elif LANGUAGE == 'java':
        print run_java(NUM, delete_build=True)
    elif LANGUAGE == 'c++':
        print run_cpp(NUM, delete_build=True)
    else:
        print 'Unsupported language :('
