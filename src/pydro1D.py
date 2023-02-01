import numpy as np
from predictor_corrector import PredictorCorrector

#1D try

nodimensions = 1
step = 0
tim = 0.0
initdt = 1e-4

endtime = 20.0

reg_lengths = [50.0, 50.0]
reg_meshsize = [50, 50]
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

pc = PredictorCorrector(initdt,step,tim,endtime)
