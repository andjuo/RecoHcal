#!/bin/tcsh

./das_client.py --query="run=256448 | grep run.beam_e,run.bfield,run.nlumis,run.lhcFill,run.delivered_lumi,run.duration,run.start_time,run.end_time" --limit=0>mytmp

set date=`cat tmp | awk '{print $7" "$8}'`
set date_end=`cat tmp | awk '{print $9" "$10}'`
set E=`cat tmp | awk '{print $1}'`
set B=`cat tmp | awk '{print $2}'`
set nL=`cat tmp | awk '{print $3}'`
set Fill=`cat tmp | awk '{print $4}'`
set dLumi=`cat tmp | awk '{print $5}'`
set D=`cat tmp | awk '{print $6}'`
rm tmp
