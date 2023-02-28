from artificial_viscosity import ArtificialViscosity

class PredictorCorrector:

    def __init__(self, initdt, initstep, st, et,qcoeffs,boundary_conditions):
        self.dt = initdt
        self.step = initstep
        self.starttime = st
        self.endtime = et
        self.artifical_visc = ArtificialViscosity(qcoeffs,boundary_conditions)
    
        
    def solve(self, hydroprops):
        # unpack hydroprops dictionary object
        elenergy = hydroprops['Energy']
        eldensity = hydroprops['Density']
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
        
        #update cell volumes
        elvolume = hydroprops['Volume']
        mesh = hydroprops['Mesh']
        elvolume.update(ndpositions,mesh)
        
        #Update densitites
        elmass = hydroprops['Mass']
        eldensity = hydroprops['Density']
        eldensity.update(elmass,elvolume)       
        print(eldensity.get_data())

        #smear shock
        elpressure = hydroprops['Pressure']
        noelements = len(elpressure)
        artifical_visc = self.artifical_visc.solve(hydroprops,noelements)
        smearedpressure = elpressure.get_data() + artifical_visc
        
              
