import unittest
import numpy as np
import cpnest.model

class RingModel(cpnest.model.Model):
    """
    A circular ring in parameter space
    logZ ~ -2.31836
    """
    names=['x','y']
    bounds=[[-2,2],[-2,2]]
    data = None
    analytic_log_Z = -2.31836
    @staticmethod
    def log_likelihood(x):
        return log_ring(x['x'],x['y'])


def log_ring(x, y, radius=1.0, thickness=0.1):
    r = np.sqrt(x**2+y**2)
    return -0.5*(radius-r)**2/thickness**2

class RingTestCase(unittest.TestCase):
    """
    Test the gaussian model
    """
    def setUp(self):
        self.model=RingModel()
        self.work=cpnest.CPNest(self.model,verbose=1,Nthreads=4,Nlive=1000,maxmcmc=1000)
        self.work.run()


    def test_evidence(self):
        # 2 sigma tolerance
        tolerance = 2.0*np.sqrt(self.work.NS.state.info/self.work.NS.Nlive)
        print('2-sigma statistic error in logZ: {0:0.3f}'.format(tolerance))
        print('Analytic logZ {0}'.format(self.model.analytic_log_Z))
        print('Estimated logZ {0}'.format(self.work.NS.logZ))

def test_all():
    unittest.main(verbosity=2)

if __name__=='__main__':
        unittest.main(verbosity=1)

