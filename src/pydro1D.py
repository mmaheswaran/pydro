import numpy as np
from predictor_corrector import PredictorCorrector
from vector_property import *
from scalar_property import *
from mesh import FEM1D

#Assume equal spacing and calculate connectivity
def init_nodepos(reg_origins,node_spacing,reg_numbers):
  nodpos = []
  el2nodmap = []
  
  noelements = len(reg_numbers)
  pos1 = reg_origins[0]
  pos2 = pos1
  nodpos.append(pos1)
  nod1 = 0
  nod2 = 0

  for e in range(noelements):
    reg = reg_numbers[e]
    spacing = node_spacing[reg]
    pos2 = pos1+spacing
    nod2 = nod2+1
    nodpos.append(pos2)
    el2nodmap.append([nod1,nod2])
    nod1 = nod2
    pos1 = pos2

  return nodpos,el2nodmap

#1D try

nodimensions = 1
step = 0
tim = 0.0
initdt = 1e-4
endtime = 20.0

reg_lengths = [50.0, 50.0]
reg_origins = [0.0,50.0]
reg_meshsize = [50, 50]
node_spacing = np.divide(np.array(reg_lengths),np.array(reg_meshsize))

#initialise region numbers for each element
reg_numbers = []
no_regions = len(reg_lengths)
no_elements = 0
for reg in range(no_regions):
  regsize = reg_meshsize[reg]
  no_elements = no_elements + regsize
  for e in range(regsize):
    reg_numbers.append(reg)

no_nodes = no_elements+1

#init scalar quantities
elenergy = Energy(no_elements)
eldensity = Density(no_elements)
elpressure = Pressure(no_elements)
elccs2 = SoundSpeed2(no_elements)
elmass = Mass(no_elements)
elvolume = Volume(no_elements)

#init vector quantites
nodepos,el2nodemap = init_nodepos(reg_origins,node_spacing,reg_numbers)
assert len(nodepos) == no_nodes, "number node positions not equal to {no_nodes}, got: {len(nodepos)}"
ndpositions = Position(nodepos)
ndvelocity = Velocity(no_nodes)

#setup mesh
mesh = FEM1D(no_elements)
mesh.get_connectivity(el2nodemap)

#Main solver
solver = PredictorCorrector(initdt,step,tim,endtime)
hydroproperties = {elenergy.__str__():elenergy, \
                   eldensity.__str__():eldensity, \
                   elpressure.__str__():elpressure, \
                   elccs2.__str__():elccs2, \
                   elmass.__str__():elmass, \
                   elvolume.__str__():elvolume, \
                   ndpositions.__str__():ndpositions, \
                   ndvelocity.__str__():ndvelocity}

solver.solve(hydroproperties)

