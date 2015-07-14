import sys
import random
import math

#Constants
CYCLES = 1000
#ENVIRONMENT_LIST = [1,7,9,5,3,14,35,77,90,8,77,45,35,243,45,33,66,89,655,166,78,34,21, 11, 97,878,45,63,23,28,6,91]
ENVIRONMENT_LIST = [15 * i for i in xrange(55,95)]
ENVIRONMENT_LIST.sort()

class GeneticSpace(object):
    __lowGen = 0
    __highGen = 50

    @staticmethod
    def getLow():
        return GeneticSpace.__lowGen
    
    @staticmethod
    def getHigh():
        return GeneticSpace.__highGen

class Mutation:
    def __init__(self):
        self.__hit_set = set()
        self.__equal_node = None
        self.__height = random.randint(GeneticSpace.getLow(), GeneticSpace.getHigh())
        self.__inclination = random.randint(GeneticSpace.getLow(), GeneticSpace.getHigh())
        self.__checkSurvivalRate()
    
    def race(self, mutation):
        self_survival_rate = self.getSurvivalRate()
        mutation_survival_rate = mutation.getSurvivalRate()
        
        print "race m1:%d vs m2:%d" % (self_survival_rate, mutation_survival_rate)
        if mutation_survival_rate > self_survival_rate:
            self.__equal_node = None
            return mutation
        
        if mutation_survival_rate == self_survival_rate:
            self.__equal_node = mutation
        
        del mutation
        return self
        
    def __checkSurvivalRate(self):
        global ENVIRONMENT_LIST
        
        _env_list = list(ENVIRONMENT_LIST)
        survival_rate = 0
        
        for i in xrange(0, ENVIRONMENT_LIST[-1]):
            num = self.__height + (self.__inclination * i)
            
            if num in _env_list:
                survival_rate = survival_rate + 1
                self.__hit_set.add(num)
                _env_list.remove(num) 

        self.__survival_rate = survival_rate
        
    def printSurvivalRate(self):
        global ENVIRONMENT_LIST
        
        _env_list = list(ENVIRONMENT_LIST)
        survival_rate = 0
        
        for i in xrange(0, ENVIRONMENT_LIST[-1]):
            num = self.__height + (self.__inclination * i)
            
            if num in _env_list:
                survival_rate = survival_rate + 1
                self.__hit_set.add(num)
                _env_list.remove(num)
                print "%d = %d + (%d)*(%d)" % (self.__height + (self.__inclination * i), self.__height, self.__inclination, i) 

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

def main():
    m1 = Mutation()
    m2 = Mutation()
    
    for i in xrange(CYCLES):
        m_temp = m1.race(m2)
        m2 = Mutation()
        m1 = m_temp

    m1.printString()
    m1.printSurvivalRate()
    print ENVIRONMENT_LIST

if __name__ == "__main__":
    sys.exit(main())