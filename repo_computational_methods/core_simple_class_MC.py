import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import os
import glob

#########################################################################################################################################
#########################################################################################################################################
############################################## XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ########################################################
#########################################################################################################################################
#########################################################################################################################################

class DistStress_Force_Mom_Frame_CofSimp():
    '''
    Calulate Stress - Force - Moment distribution along the transversal section of Frame
    ------------------------------------------------------------------------------------
    
    * Calculate Stress distribution along the transversal section of Frame
    * Calculate Force distribution along the transversal section of Frame
    * Calculate Moment distribution along the transversal section of Frame
    '''
    def __init__(self, h, numdiv, M, I, n):
        self.h = h
        self.numdiv = numdiv
        self.M = M
        self.I = I
        self.n = n
    
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
    
    def simpson_like_coeffs(self):                                                 # define Simpson-like weights generator function
        n = self.n
        
        if n < 3:                                                               # ensure at least three points
            raise ValueError("n must be >= 3")                                  # raise error if insufficient points
        w = np.ones(n, dtype=int)                                               # initialize weight array of ones with integer type
        if n > 2:                                                               # apply Simpson pattern only if more than two points
            w[1:-1:2] = 4                                                       # set odd-indexed interior weights to 4
            w[2:-1:2] = 2                                                       # set even-indexed interior weights to 2   
        return w                                                                # return the weight vector


#########################################################################################################################################
#########################################################################################################################################
############################################## Plotting ########################################################
#########################################################################################################################################
#########################################################################################################################################

class Plot_Distribution_Stress_Force_Moments():
    def __init__(self, title = 'Model', eje_n = 0, b = 0.2, h = 3.0,
                 S11_frame = any, hframe = any, F_A_frame = any, M_frame = any):
        self.title = title
        self.eje_n = eje_n
        self.b = b
        self.h = h
        self.S11_frame = S11_frame
        self.hframe = hframe
        self.F_A_frame = F_A_frame
        self.M_frame = M_frame
    
    def plot_stress_force_moment(self):
        
        title = self.title
        eje_n = self.eje_n
        b = self.b
        h = self.h
        S11_frame = self.S11_frame
        hframe = self.hframe
        F_A_frame = self.F_A_frame
        M_frame = self.M_frame
        
        fig, ax = plt.subplots(1, 4, figsize=(18, 10), sharey=True)                                         # create 1x4 subplots and share y-axis across them
        fig.suptitle(f"Computational Methods in Structural Engineering GR1 2026 - 01 \n {title}", fontsize=14, y=0.98)  # set overall figure title

        eje_n = 0                                                                                     # neutral axis position for the frame (y = 0)

        ###################### Section Plot ######################
        left = -b / 2                                                                                       # left x-coordinate of the rectangle section
        bottom = -h / 2                                                                                     # bottom y-coordinate of the rectangle section
        rect = Rectangle((left, bottom), b, h,                                                              # create a Rectangle patch for the cross section
                        linewidth=1.5, edgecolor=(0, 0, 0),
                        facecolor=(0.8, 0.8, 0.8), alpha=1.0)

        ax[0].axhline(eje_n, color=(1, 0, 0), linestyle='--', linewidth=2.0,                          # plot neutral axis as dashed red line
                    label=f"Neutral Axis = {title}")
        ax[0].add_patch(rect)                                                                               # add the rectangular section patch to the axes
        ax[0].annotate('', xy=(-b/2, -h/2 + 0.15*h), xytext=(b/2, -h/2 + 0.15*h),                           # draw double-headed arrow for width b
                    arrowprops=dict(arrowstyle='<->', linewidth=1))
        ax[0].text(0 , -h/2 + 0.17*h, f"b = {b:.2f} m", ha='center', va='top', fontsize=8)                  # label the width b
        ax[0].annotate('', xy=(b/2 + 0.15*b, -h/2), xytext=(b/2 + 0.15*b, h/2),                             # draw double-headed arrow for height h
                    arrowprops=dict(arrowstyle='<->', linewidth=1))
        ax[0].text(b/2 + 0.25*b, 0, f"h = {h:.2f} m", rotation=90, va='center', ha='left', fontsize=8)      # label the height h

        ax[0].set_xlim(-b, b)                                                                               # set x-limits for section plot
        ax[0].set_aspect('equal')                                                                           # keep equal aspect ratio
        ax[0].set_xlabel("Width (m)", fontsize=8)                                                           # x-axis label
        ax[0].set_title("Rectangular Section", fontsize=9, color=(0, 0, 0))                                 # title for the section subplot
        ax[0].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)                 # legend for subplot 0


        ###################### Stress vs Height Plot ######################
        s11_1d = S11_frame.flatten()                                                                        # flatten bending stress array to 1D
        hframe_1d = hframe.flatten()                                                                        # flatten height array to 1D

        ax[1].axhline(eje_n, color=(1, 0, 0), linestyle='--', linewidth=2.0,                          # plot neutral axis on stress plot
                    label=f'Neutral Axis = {title}')
        ax[1].plot(s11_1d, hframe_1d, color=(0, 0, 1), marker='o', markersize=5, markerfacecolor='w', markeredgewidth=1, linestyle='-', linewidth=1.0,  # plot stress vs height
                    label=f'Max S11 ={np.max(np.abs(s11_1d)):.2f}')
        ax[1].fill_betweenx(hframe, 0, s11_1d, color=(0, 0, 1), alpha=0.1)                                  # fill area under stress curve horizontally

        for x, y in zip(s11_1d, hframe_1d):                                                                 # annotate each stress point with its value
            ax[1].text(x + np.max(np.abs(s11_1d))*0.05, y,f'{x:.2f} [T/m2]', fontsize=8, color= (0, 0, 1), ha='left', va='bottom')

        ax[1].set_xlabel("Stress [T/m2]", fontsize=8)                                                       # x-axis label for stress plot
        ax[1].set_ylabel("Height (m)", fontsize=8)                                                          # y-axis label for stress plot
        ax[1].set_title(f'Stress vs Height', fontsize= 9, color=(0, 0, 0))                                  # title for stress subplot
        ax[1].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)                 # legend for subplot 1
        ax[1].grid(which='both', axis='y', alpha=0.5)                                                       # enable horizontal grid lines


        ###################### Force vs Height Plot ######################
        F_A_frame_1d = F_A_frame.flatten()                                                                  # flatten axial force contributions to 1D

        ax[2].axhline(eje_n, color=(1, 0, 0), linestyle='--', linewidth=2.0,                          # plot neutral axis on force plot
                    label=f'Neutral Axis = {title}')
        ax[2].plot(F_A_frame_1d, hframe_1d, color=(0, 0, 1), marker='o', markersize=5, markerfacecolor='w', markeredgewidth=1, linestyle='-', linewidth=1.0,  # plot force vs height
                    label=f'Max Force ={np.max(np.abs(F_A_frame_1d)):.2f}')
        ax[2].fill_betweenx(hframe, 0, F_A_frame_1d, color=(0, 0, 1), alpha=0.1)                            # fill area under force curve horizontally

        for x, y in zip(F_A_frame_1d, hframe_1d):                                                           # annotate each force point with its value
            ax[2].text(x + np.max(np.abs(F_A_frame_1d))*0.05, y,f'{x:.2f} [T]', fontsize=8, color= (0, 0, 1), ha='left', va='bottom')

        ax[2].set_xlabel("Force [T]", fontsize=8)                                                           # x-axis label for force plot
        ax[2].set_ylabel("Height (m)", fontsize=8)                                                          # y-axis label for force plot
        ax[2].set_title(f'Force vs Height', fontsize= 9, color=(0, 0, 0))                                   # title for force subplot
        ax[2].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)                 # legend for subplot 2
        ax[2].grid(which='both', axis='y', alpha=0.5)                                                       # enable horizontal grid lines


        ###################### Moment vs Height Plot ######################
        M_frame_1d = M_frame                                                                                # moment contributions are already 1D

        ax[3].axhline(eje_n, color=(1, 0, 0), linestyle='--', linewidth=2.0,                          # plot neutral axis on moment plot
                    label=f'Neutral Axis = {title}')
        ax[3].plot(M_frame_1d, hframe_1d, color=(0, 0, 1), marker='o', markersize=5, markerfacecolor='w', markeredgewidth=1, linestyle='-', linewidth=1.0,  # plot moment vs height
                    label=f'Max Moment ={np.max(np.abs(M_frame_1d)):.2f}')
        ax[3].fill_betweenx(hframe, 0, M_frame_1d, color=(0, 0, 1), alpha=0.1)                              # fill area under moment curve horizontally

        for x, y in zip(M_frame_1d, hframe_1d):                                                             # annotate each moment point with its value
            ax[3].text(x + np.max(np.abs(M_frame_1d))*0.05, y,f'{x:.2f} [T]', fontsize=8, color= (0, 0, 1), ha='left', va='bottom')

        ax[3].set_xlabel("Moment [T-m]", fontsize=8)                                                        # x-axis label for moment plot
        ax[3].set_ylabel("Height (m)", fontsize=8)                                                          # y-axis label for moment plot
        ax[3].set_title(f'Moment vs Height', fontsize= 9, color=(0, 0, 0))                                  # title for moment subplot
        ax[3].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)                 # legend for subplot 3
        ax[3].grid(which='both', axis='y', alpha=0.5)                                                       # enable horizontal grid lines

        plt.tight_layout()                                                                                  # adjust subplots to fit into figure area
        plt.show()                                                                                          # display the figure 
        

#########################################################################################################################################
#########################################################################################################################################
############################################## Read Excel Files and calculate Avarage Stress ########################################################
#########################################################################################################################################
#########################################################################################################################################

class ReadExcelFies_compute_avarage_stress():
    def __init__(self, excel_files):
        self.excel_files = excel_files
        pass
    
    def FileSelect(self):
        excel_files = self.excel_files
        
        stress_file = excel_files[0]
        stress_files_df = pd.read_excel(stress_file)

        joint_name = excel_files[1]
        joint_name_df = pd.read_excel(joint_name)
        
        stress_files_df1 = stress_files_df.copy()
        stress_files_df1.columns = stress_files_df1.iloc[0]          
        stress_files_df1 = stress_files_df1.iloc[2:].reset_index(drop=True)
        
        return stress_files_df1, joint_name_df
