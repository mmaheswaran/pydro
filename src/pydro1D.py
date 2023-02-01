import numpy as np
from predictor_corrector import PredictorCorrector

#Assume equal spacing
def init_nodepos(reg_origins,node_spacing,reg_numbers):
  nodpos = []
  noelements = len(reg_numbers)
  pos1 = reg_origins[0]
  pos2 = pos1
  nodpos.append(pos1)

  for e in range(noelements):
    reg = reg_numbers[e]
    spacing = node_spacing[reg]
    pos2 = pos1+spacing
    nodpos.append(pos2)
    pos1 = pos2

  nodepositions = np.array(nodpos)
  return nodepositions

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
reg_numbers = []

no_regions = len(reg_lengths)
no_elements = 0

for reg in range(no_regions):
  regsize = reg_meshsize[reg]
  no_elements = no_elements + regsize
  for e in range(regsize):
    reg_numbers.append(reg)

print(len(reg_numbers))
no_nodes = no_elements+1

#init scalar quantities
eldensity = np.zeros(no_elements)
elenergy = np.zeros(no_elements)
elpressure = np.zeros(no_elements)
elccs2 = np.zeros(no_elements)
elmass = np.zeros(no_elements)
elvolume = np.zeros(no_elements)

#init vector quantites
ndvelocity = np.zeros(no_nodes)

ndpositions = init_nodepos(reg_origins,node_spacing,reg_numbers)
assert len(ndpositions) == no_nodes, "number node positions not equal {no_nodes}, got: {len(ndpositions)}"


pc = PredictorCorrector(initdt,step,tim,endtime)


