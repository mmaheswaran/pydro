import numpy as np

class ArtificialViscosity:
    def __init__(self,coeffs,boundary_conditions):
        self.quadratic_coeff = coeffs[0]
        self.linear_coeff = coeffs[1]
        self.left_bc = boundary_conditions[0]
        self.right_bc = boundary_conditions[1]
        
    def apply_boundary_conditions(self,gradv_l,gradv_r):
        #Apply boundary condition
        if(self.left_bc==1):
            gradv_l[0] = 0
        else:
            gradv_l[0] = gradv_l[1]
            
        if(self.right_bc==1):
            gradv_r[-1] = 0
        else:
            gradv_r[-1] = gradv_r[-2]
        
    def calculate_limiter(self,gradv_c):
        gradv_l = np.roll(gradv_c,1)
        gradv_r = np.roll(gradv_c,-1)
        self.apply_boundary_conditions(gradv_l,gradv_r)
        
        l_ratio = np.divide(gradv_l, gradv_c, out=np.zeros_like(gradv_l), where=gradv_c!=0)
        r_ratio = np.divide(gradv_r, gradv_c, out=np.zeros_like(gradv_r),where=gradv_c!=0)
        av_ratio = 0.5*(l_ratio+r_ratio)
        mincond = np.minimum(av_ratio,2*l_ratio)
        mincond = np.minimum(mincond,2*r_ratio)
        limiter = np.maximum(0.0, mincond)
        return limiter
    
    #Specify left and right boundary conditions:
    #  1 = rigid boundary
    #  2 = reflective boundary
    def solve(self,hydroprops,nel):
        ndpositions = hydroprops['Position']
        ndvelocity = hydroprops['Velocity']
        elccs2 = hydroprops['SoundSpeedSquared']
        eldensity = hydroprops['Density']

        cq = self.quadratic_coeff
        cl = self.linear_coeff

        ndveldata = ndvelocity.get_data()
        ndposdata = ndpositions.get_data()
        gradv_c = np.gradient(ndveldata,ndposdata)

        limiter = self.calculate_limiter(gradv_c)
        limitersq = limiter*limiter
        gradv_csq = gradv_c*gradv_c
        rho = eldensity.get_data()
        csq = elccs2.get_data()

        q = cq*rho*gradv_csq*(1-limitersq) + cl*rho*csq*gradv_csq*(1-limiter)
        return q



    





