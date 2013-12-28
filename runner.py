import sys
import time
from os import listdir
import subprocess as sub


# Reads in the answer key
def read_key():
    with open("data/key.dat") as f:
        keys = map(lambda x: x.split(":"), f.read().split("\n"))
    return {int(key[0]): key[1].strip() for key in keys if len(key) == 2}
key = read_key()

# Add directories to path
sys.path.insert(0, "solutions/python")


# Converts an integer to xxx string format
def convert(number):
    s = str(number)
    while len(s) < 3:
        s = "0" + s
    return s


# Run a python solution given number
def run_python(number):
    module_name = "p" + convert(number)
    solution = __import__(module_name)

    print 'Running ' + solution.__name__ + '.py'
    startTime = int(round(time.time() * 1000))
    result = str(solution.run())
    print 'Result: ' + result
    endTime = int(round(time.time() * 1000))
    runtime = str(endTime - startTime)
    print 'Runtime: ' + runtime + ' ms'
    return result == key[number], runtime


# Run all python solutions
def run_all_python():
    key = read_key()
    count, correct = 0, 0
    for module in listdir("solutions/python"):
        if module[0] == "p" and module[-2:] == "py":
            module = module.split(".")[0]
            result = run_python(int(module[1:]))
            count += 1
            correct += 1 if result else 0

    print "CORRECT: " + str(correct) + "/" + str(count)


# Run a c++ solution given number
def run_cpp(number, delete_build=True):
    # first compile the c++ file
    file_name = "p" + convert(number)
    src_path = "solutions/c++/" + file_name + ".cpp"
    _, errors = run_command(["g++", "-o", file_name, src_path])
    if errors:
        return errors

    # run the executable
    print "Running " + file_name
    startTime = int(round(time.time() * 1000))
    result, errors = run_command(["./" + file_name])
    endTime = int(round(time.time() * 1000))
    if errors:
        return errors

    result = result.strip()
    print "Result: " + result
    runtime = str(endTime - startTime)
    print "Runtime: " + runtime + " ms"

    # delete the compiled file
    if delete_build:
        _, errors = run_command(["rm", file_name])
        if errors:
            return errors

    return result == key[number], runtime


def run_command(command):
    p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
    return p.communicate()

if __name__ == "__main__":
    print run_python(51)
