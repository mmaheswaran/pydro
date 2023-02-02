class PredictorCorrector:

    def __init__(self, initdt, initstep, st, et):
        self.dt = initdt
        self.step = initstep
        self.starttime = st
        self.endtime = et
        
        
    def solve(self, hydroprops):
        # unpack hydroprops dictionary object
        elenergy = hydroprops['Energy']
        eldensity = hydroprops['Density']
        elpressure = hydroprops['Pressure']
        elccs2 = hydroprops['SoundSpeedSquared']
        elmass = hydroprops['Mass']
        elvolume = hydroprops['Volume']
        ndpositions = hydroprops['Position']
        ndvelocity = hydroprops['Velocity']
        
        self.halfstep(hydroprops)
        
      
      
      
    def halfstep(self,hydroprops):
        #update nodal coordinates for half step
        ndpositions = hydroprops['Position']
        ndvelocity = hydroprops['Velocity']
        ndpositions.update(ndvelocity,self.dt)
        
        
              
