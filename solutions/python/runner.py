import time
from os import listdir

def run(module, answer):
    exec "import " + module + " as solution"
    
    print "Running " + solution.__name__
    startTime = int(round(time.time() * 1000))
    result = str(solution.run())
    print "Result: " + result
    endTime = int(round(time.time() * 1000))
    runtime = str(endTime - startTime)
    print "Runtime: " + runtime + " ms"
    
    return result == answer, runtime

def read_key():
    with open("key.dat") as f:
        keys = map(lambda x: x.split(":"), f.read().split("\n"))
    return {int(key[0]) : key[1].strip() for key in keys if len(key) == 2}

def run_all():
    key = read_key()
    count, correct = 0, 0
    for module in listdir("solutions/python"):
        if module[0] == "p" and module[-2:] == "py":
            module = module.split(".")[0]
            number = int(module[1:])
            result = run(module, key[number])
            
            count += 1
            correct += 1 if result else 0 
    
    print "CORRECT: " + str(correct) + "/" + str(count)
     
if __name__ == "__main__":
    key = read_key()
    problem = 50
    print run("p0" + str(problem), key[problem])
