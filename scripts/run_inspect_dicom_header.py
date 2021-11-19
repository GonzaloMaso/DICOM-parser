'''
Created on 19/11/2021

@author: Gonzalo D. Maso Talou
'''

import pydicom

if __name__ == '__main__':
    
    filename = "/eresearch-neonatal/datasets/Arterial\ Study/DIRW0000"
    
    ds = pydicom.dcmread(filename)