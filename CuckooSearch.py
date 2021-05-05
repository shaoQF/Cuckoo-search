import  CSIndividual
import numpy  as  np
import  math,random,random,time,copy

class CuckooSearch:
    def __init__(self,popsize,vardim,bound,Maxgen):
        self.popsize=popsize
        self.bound=bound
        self.vardim=vardim
        self.Maxgen=Maxgen
        self.population=[]
        self.trace=np.zeros((self.Maxgen,1))

    '''
    Initialization 
    '''
    def Initlize(self):
        for  i in range(self.popsize):
            ind=CSIndividual.CSIndividual(self.vardim,self.bound)
            ind.gernate()
            '''Initialization Fitness'''
            ind.calcuateFitness()
            self.population.append(ind)

    '''
    levy flight 
    '''
    def levy_flight(self):
        Lambda=1.5
        sigma1=np.power((math.gamma(1+Lambda) * np.sin((np.pi*Lambda) / 2)) \
            / math.gamma((1+Lambda) / 2) * np.power(2,(Lambda-1) / 2),1 / Lambda)
        sigma2=1
        u=np.random.normal(0,sigma1,size=self.vardim)
        v=np.random.normal(0,sigma2,size=self.vardim)
        step=u/np.power(np.fabs(v),1/Lambda)
        return  step

    '''
    global search by levy flight
    '''
    def  update_nest(self):
        step_size_factor=0.01
        for i in range(self.popsize):
            ind=copy.deepcopy(self.population[i])
            '''update position'''
            ind.position=ind.position+self.levy_flight()*step_size_factor

            for  x in range(self.vardim):
                if ind.position[x]>self.bound[1,x]:
                    ind.position[x]=self.bound[1,x]
                if ind.position[x]<self.bound[0,x]:
                    ind.position[x]=self.bound[0,x]
            ind.calcuateFitness()
            self.population.append(ind)
            """random  choice  (say j)"""
            j=np.random.randint(low=0,high=self.popsize)
            while i==j:#random id[say j] ≠ i
                j=np.random.randint(low=0,high=self.popsize)
            if self.population[i].fitness<self.population[j].fitness:
                j=i
        '''sort (to keep best)'''
        self.population=sorted(self.population,key=lambda ID:ID.fitness)

    '''
    local search by Pa 
    '''
    def  abandon_nest(self):
        for  i in range(self.popsize):
            ind=copy.deepcopy(self.population[i])
            for x in range(self.vardim):
                r=np.random.rand()
                pa=0.25
                if r<pa:
                    ind.position[x]=self.bound[0,x]+np.random.rand()*(self.bound[1,x]-self.bound[0,x])
                    ind.calcuateFitness()
                self.population.append(ind)
        '''sort (to keep best)'''
        self.population=sorted(self.population,key=lambda ID:ID.fitness)

    '''
    find the best solution
    '''
    def findbest(self):
        index=0
        currentsize=len(self.population)
        for i in range(1,currentsize):
            if self.population[i].fitness<self.population[index].fitness:
                index=i
        return  index

    '''
    求解
    '''
    def  solve(self):
        start=time.time()
        self.t=0
        self.Initlize()
        bestIndex=self.findbest()
        self.best=copy.deepcopy(self.population[bestIndex])
        self.trace[self.t,0]=self.best.fitness
        while self.t<self.Maxgen-1:
            self.t+=1
            self.update_nest()
            self.abandon_nest()
            bestIndex=self.findbest()
            if self.best.fitness>self.population[bestIndex].fitness:
                self.best=copy.deepcopy(self.population[bestIndex])
                self.trace[self.t, 0] = self.best.fitness
        end=time.time()
        print("Execution time of the entire algorithm",end-start)
        print("the best fitness:",self.best.fitness)





