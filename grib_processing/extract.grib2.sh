#!/bin/bash
# [Purpose] Extract 17 layers from specified Grib2 data file (the 1st argument) 
# and output the plain text files to a specified directory ($2).
# [Dependency] wgrib2
INFILE=$1
OUTDIR=$2
dt=$(date '+%Y%m%d%H00')
# Extract pre-defined 17 layers
wgrib2 $INFILE -match "HGT:500" -lola 60:241:0.5 0:121:0.5 $OUTDIR/h500.txt text
wgrib2 $INFILE -match "PRMSL:mean" -lola 60:241:0.5 0:121:0.5 $OUTDIR/mslp.txt text
wgrib2 $INFILE -match "UGRD:200" -lola 60:241:0.5 0:121:0.5 $OUTDIR/u200.txt text
wgrib2 $INFILE -match "VGRD:200" -lola 60:241:0.5 0:121:0.5 $OUTDIR/v200.txt text
wgrib2 $INFILE -match "TMP:200" -lola 60:241:0.5 0:121:0.5 $OUTDIR/t200.txt text
wgrib2 $INFILE -match "RH:700" -lola 60:241:0.5 0:121:0.5 $OUTDIR/rh700.txt text
wgrib2 $INFILE -match "TMP:700" -lola 60:241:0.5 0:121:0.5 $OUTDIR/t700.txt text
wgrib2 $INFILE -match "UGRD:700" -lola 60:241:0.5 0:121:0.5 $OUTDIR/u700.txt text
wgrib2 $INFILE -match "VGRD:700" -lola 60:241:0.5 0:121:0.5 $OUTDIR/v700.txt text
wgrib2 $INFILE -match "RH:850" -lola 60:241:0.5 0:121:0.5 $OUTDIR/rh850.txt text
wgrib2 $INFILE -match "TMP:850" -lola 60:241:0.5 0:121:0.5 $OUTDIR/t850.txt text
wgrib2 $INFILE -match "UGRD:850" -lola 60:241:0.5 0:121:0.5 $OUTDIR/u850.txt text
wgrib2 $INFILE -match "VGRD:850" -lola 60:241:0.5 0:121:0.5 $OUTDIR/v850.txt text
wgrib2 $INFILE -match "RH:925" -lola 60:241:0.5 0:121:0.5 $OUTDIR/rh925.txt text
wgrib2 $INFILE -match "TMP:925" -lola 60:241:0.5 0:121:0.5 $OUTDIR/t925.txt text
wgrib2 $INFILE -match "UGRD:925" -lola 60:241:0.5 0:121:0.5 $OUTDIR/u925.txt text
wgrib2 $INFILE -match "VGRD:925" -lola 60:241:0.5 0:121:0.5 $OUTDIR/v925.txt text
#


