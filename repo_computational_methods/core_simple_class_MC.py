import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#########################################################################################################################################
#########################################################################################################################################
###################################### Simple CLASS XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ###################################################
#########################################################################################################################################
#########################################################################################################################################

class DistStress_Force_Mom_Frame():
    '''
    Calulate Stress - Force - Moment distribution along the transversal section of Frame
    ------------------------------------------------------------------------------------
    
    * Calculate Stress distribution along the transversal section of Frame
    * Calculate Force distribution along the transversal section of Frame
    * Calculate Moment distribution along the transversal section of Frame
    '''
    def __init__(self, h, numdiv, M, I):
        self.h = h
        self.numdiv = numdiv
        self.M = M
        self.I = I
    
    def StressDistribution_Frame(self):
        '''
        hola
        '''
        h = self.h
        numdiv = self.numdiv
        M = self.M
        I = self.I
        
        hframe = []                                                                 # initialize empty list for heights along frame section
        S11_frame = []                                                              # initialize empty list for bending stresses along section
        size_div = h/numdiv                                                         # compute size of each division (height step)
        for i in np.arange(0,numdiv + 1, 1):                                        # loop over divisions including both ends
            hframe.append(i*size_div - h/2)                                         # append height value measured from neutral axis
            S11_frame.append(M * (hframe[i]) / I * -1                               # compute bending stress at that height (sign inverted)
                            )                                              
        hframe = np.array(hframe)                                                   # convert heights list to numpy array
        S11_frame = np.array(S11_frame)                                             # convert stresses list to numpy array
        S11_frame_df = pd.DataFrame(                                                # create DataFrame for bending stress
            S11_frame, 
            columns=['Bending Stress Frame [T/m2]']
        )
        hframe_df = pd.DataFrame(hframe, columns=['Height Frame [m]'])              # create DataFrame for heights
        Resl_frame = pd.concat([hframe_df, S11_frame_df], 
                            axis=1, ignore_index= False)                         # concatenate heights and stresses into one DataFrame
        
        return Resl_frame, hframe, S11_frame, size_div
