#!/bin/bash

if [ ${#1} -eq 0 ] ; then
    echo "please provide a root file name"
    exit
fi

outFName="${1%%.root}.txt"

root -l -q -b $1 listHistos.C | tee $outFName
echo "list saved to ${outFName}"
