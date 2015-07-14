import sys
import random
import math
import matplotlib.pyplot as plt

class EnvironmentData():
    #Defs
    __ENVIRONMENT_LIST = None
    __LOW_BOUND = 1
    __HIGH_BOUND = 100
    
    def __init__(self, number_of_points):
        self.__number_of_points = number_of_points
        self.__generateData()
        self.__sort()
    
    def getEnvironmentList(self):
        return self.__ENVIRONMENT_LIST

    def __generateData(self):
        self.__ENVIRONMENT_LIST = list()
        
        for i in xrange(self.__number_of_points):
             self.__ENVIRONMENT_LIST.append((random.randint(EnvironmentData.__LOW_BOUND, EnvironmentData.__HIGH_BOUND),\
                                             random.randint(EnvironmentData.__LOW_BOUND, EnvironmentData.__HIGH_BOUND)))

    def __sort(self):
        self.__ENVIRONMENT_LIST.sort()
        
    @staticmethod
    def getLow():
        return EnvironmentData.__LOW_BOUND

    @staticmethod
    def getHigh():
        return EnvironmentData.__HIGH_BOUND

class Mutation:
    #Defs
    __ENVIRONMENT_LIST = None
    
    def __init__(self, env_list):
        self.__ENVIRONMENT_LIST = env_list 
        self.__hit_set = set()
        self.__equal_node = None
        self.__height = random.randint(EnvironmentData.getLow(), EnvironmentData.getHigh())
        self.__inclination = random.randint(EnvironmentData.getLow(), EnvironmentData.getHigh())
        self.__checkSurvivalRate()
    
    def race(self, mutation):
        self_survival_rate = self.getSurvivalRate()
        mutation_survival_rate = mutation.getSurvivalRate()
        
        print "race m1 hit %d points and m2 hit %d points" % (self_survival_rate, mutation_survival_rate)
        if mutation_survival_rate > self_survival_rate:
            self.__equal_node = None
            return mutation
        
        if mutation_survival_rate == self_survival_rate:
            self.__equal_node = mutation
        
        del mutation
        return self
        
    def __checkSurvivalRate(self):
        survival_rate = 0
        
        for _node in self.__ENVIRONMENT_LIST:
            value = self.__height + (self.__inclination * _node[0])
            
            if(value == _node[1]):
                survival_rate = survival_rate + 1
                self.__hit_set.add(_node)

        self.__survival_rate = survival_rate

    def printSurvivalRate(self):
        survival_rate = 0
        
        for _node in self.__ENVIRONMENT_LIST:
            value = self.__height + (self.__inclination * _node[0])
            
            if(value == _node[1]):
                survival_rate = survival_rate + 1
                self.__hit_set.add(_node)
                print "%d = %d + (%d)*(%d)" % (self.__height + (self.__inclination * _node[0]),
                                               self.__height,
                                               self.__inclination,
                                               _node[0])

        self.__survival_rate = survival_rate

    def getSurvivalRate(self):
        return self.__survival_rate
    
    def printString(self):
        if self.__equal_node != None:
            print "\nMutations:"
            self.__equal_node.printString()
            print "="*30
            print "Self:"
        
        print "Height:%d\tInclination:%d\tSurvival Rate:%d" % (self.__height,\
                                                               self.__inclination,\
                                                               self.__survival_rate)
        print "Hit Set:\n%s" % self.__hit_set
        
    def getHitSet(self):
        return self.__hit_set
    
    def showPlot(self):
        plt.plot([hit[0] for hit in self.__hit_set],\
                 [hit[1] for hit in self.__hit_set], 'ro')
        plt.show()

def main():
    #Constants
    DEFAULT_NUMBER_OF_CYCLES = 10 ** 4
    DEFAULT_NUMBER_OF_POINTS = 1000
    
    #Getting number of cycles
    cycles = DEFAULT_NUMBER_OF_CYCLES
    number_of_points = DEFAULT_NUMBER_OF_POINTS
    
    if len(sys.argv) > 2:
        number_of_points = int(sys.argv[2])
    
    if len(sys.argv) > 1:
        cycles = int(sys.argv[1])
    
    env_list = EnvironmentData(number_of_points)
    
    m1 = Mutation(env_list.getEnvironmentList())
    m2 = Mutation(env_list.getEnvironmentList())
    
    for i in xrange(cycles):
        m_temp = m1.race(m2)
        m2 = Mutation(env_list.getEnvironmentList())
        m1 = m_temp

    m1.printString()
    m1.printSurvivalRate()
    m1.showPlot()
    
    print "Number of cycles run: {0}".format(cycles)
    print "Number of points in the grid: {0}".format(number_of_points)

if __name__ == "__main__":
    sys.exit(main())