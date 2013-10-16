import p030 as solution
import time

def run():
    return solution.run()
    
if __name__=="__main__":
    print "Running " + solution.__name__
    startTime = int(round(time.time() * 1000))
    print "Result: " + str(run())
    endTime = int(round(time.time() * 1000))
    
    print "Runtime: " + str(endTime - startTime) + " ms"
    
    
    