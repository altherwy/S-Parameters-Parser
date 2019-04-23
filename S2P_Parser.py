import numpy as num
import scipy as scp
import pandas as pnd
import sys 



def parse_S2P_file(file_name):
    labels = ["Frequency","S11_r","S11_i","S21_r","S21_i","S12_r","S12_i","S22_r","S22_i"]
    with open(file_name) as f:
        lines = [line.rstrip('\n') for line in f] 
    
    lines = lines[9:len(lines)]
    frequency = []
    s11_r = []
    s11_i = []
    s21_r = []
    s21_i = []
    s12_r = []
    s12_i = []
    s22_r = []
    s22_i = []

    for line in lines:
        line_segments = line.split()
        s_parameters = pnd.Series(line_segments,index=labels)
        frequency.append(s_parameters['Frequency'])
        s11_r.append(s_parameters['S11_r'])
        s11_i.append(s_parameters['S11_i'])
        s21_r.append(s_parameters['S21_r'])
        s21_i.append(s_parameters['S21_i'])
        s12_r.append(s_parameters['S12_r'])
        s12_i.append(s_parameters['S12_i'])
        s22_r.append(s_parameters['S22_r'])
        s22_i.append(s_parameters['S22_i'])  

    s_parameters_df = pnd.DataFrame({"Frequency":frequency,
                                    "S11 Real"  : s11_r,
                                    "S11 Imag"  : s11_i,
                                    "S21 Real"  : s21_r,
                                    "S21 Imag"  : s21_i,
                                    "S12 Real"  : s12_r,
                                    "S12 Imag"  : s12_i,
                                    "S22 Real"  : s22_r,
                                    "S22 Imag"  : s22_i})   

    return s_parameters_df  



file_names = []
all_data_frames = []
[file_names.append(str(sys.argv[i])) for i in range(1,len(sys.argv))]
[all_data_frames.append(parse_S2P_file(file_name)) for file_name in file_names]
all_data_frames

