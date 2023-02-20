class ArtificialViscosity:

  def __init__(self,linceoff,quadcoeff):
    self.linear_coeff = lincoeff
    self.quadratic_coeff = quadcoeff

  def solve(hydroprops,nel):
    ndpositions = hydroprops['Position']
    ndvelocity = hydroprops['Velocity']
    elccs2 = hydroprops['SoundSpeedSquared']
    eldensity = hydroprops['Density']

    ndveldata = ndvelocity.get_data()
    ndposdata = ndpositions.get_data()
    gradL = np.diff(ndveldata)/np.diff(ndposdata)
    
    