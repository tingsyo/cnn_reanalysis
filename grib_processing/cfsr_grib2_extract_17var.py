#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
cfsr_grib2_extract_17var.py: 
    This script use wgrib2 program to extract 17 variables from NCEP-CFSR dataset. 
"""

# meta-data
__author__ = "Ting-Shuo Yo"
__copyright__ = "Copyright 2019, DataQualia Lab Co. Ltd."
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.1"
__maintainer__ = "Ting-Shuo Yo"
__email__ = "tingyo@dataqualia.com"
__status__ = "Development"
# end of meta-data

import os, re, subprocess, logging, argparse
import pandas as pd

# Define parameters
VARS = ['h500', 'mslp', 'u200', 'v200', 't200', 'rh700', 't700', 'u700', 'v700',\
        'rh850', 't850', 'u850', 'v850', 'rh925', 't925', 'u925', 'v925']
VAR_PATTERN = {'h500': "HGT:500", 'mslp':"PRMSL:mean",\
            'u200':"UGRD:200", 'v200':"VGRD:200", 't200':"TMP:200", \
            'rh700':"RH:700", 't700':"TMP:700", 'u700':"UGRD:700", 'v700':"VGRD:700",\
            'rh850':"RH:850", 't850':"TMP:850", 'u850':"UGRD:850", 'v850':"VGRD:850",\
            'rh925':"RH:925", 't925':"TMP:925", 'u925':"UGRD:925", 'v925':"VGRD:925"}

print(VAR_PATTERN)

# Search and parse all NCEP-CFSR data files in grb2 format
def searchCFSR(srcdir):
    df = []
    for fn in os.listdir(srcdir): 
        if os.path.isfile(os.path.join(srcdir, fn)) and fn.endswith('.grb2') and ('.pg' in fn):
            timestamp = fn.split('.')[0]
            df.append({'time':timestamp, 'uri':os.path.join(srcdir, fn)})
    df = pd.DataFrame(df)
    return(df) 

# Extract 17 vars from the specified grb2 file
def extract17Vars(srcfile, timestamp, outdir, vars=VARS, var_pattern=VAR_PATTERN):
    # Execute the command through subprocess
    # wgrib2 $INFILE -match "HGT:500" -lola 60:241:0.5 0:121:0.5 -netcdf $OUTFILE
    res = []
    for v in VARS:
        outfile = os.path.join(outdir, timestamp+'.'+v+'.nc')
        cmd = ['wgrib2', srcfile, '-match', VAR_PATTERN[v], '-netcdf', outfile]
        print(' '.join(cmd))
        res.append(subprocess.call(cmd))
    return(res)


#-----------------------------------------------------------------------
def main():
    # Configure Argument Parser
    parser = argparse.ArgumentParser(description='use wgrib2 program to extract 17 variables from NCEP-CFSR dataset.')
    parser.add_argument('--inputpath', '-i', help='the directory containing NCEP-CFSR data in grb2 format.')
    parser.add_argument('--output', '-o', help='the directory to store the output data.')
    parser.add_argument('--log', '-l', default='reg.log', help='the log file.')
    args = parser.parse_args()
    # Set up logging
    #logging.basicConfig(filename=args.log, filemode='w', level=logging.DEBUG)
    # Search and parse all data files
    datainfo = searchCFSR(args.inputpath)
    print(datainfo)
    # done
    return(0)
    
#==========
# Script
#==========
if __name__=="__main__":
    main()
