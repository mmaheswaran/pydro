class PredictorCorrector:
  def __init__(self,initdt,initstep,st,et):
    self.dt = initdt
    self.step = initstep
    self.starttime = st
    self.endtime = et
    
  def solve(self, hydroprops):
      #hydroprops is a dictionary object
              