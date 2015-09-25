#!/bin/bash
# John Hakala, 9/14/15
# Updated by Andrius Juodagalvis, 9/25/2015
# To use this script, run it like this:
# ./runList.sh <lower limit run number> <upper limit run number>
# Example:
# ./runList.sh 255000 255200
#
# It must be run for the cmsusr network, or a tunnel must be set up to forward the query

# check that the first two are integer numbers
if [ ${#2} -eq 0 ] || [[ ! $1 =~ ^-?[0-9]+$ ]] || [[ ! $2 =~ ^-?[0-9]+$ ]]
then
    echo "use:"
    echo "./runList.sh <lower limit run number> <upper limit run number> [--output myoutputfile] [--uselistfile listfilename]"
    echo "./runList.sh 255000 255200 [--output myoutputfile]"
    echo "If \$listfilename is not provided, this sript creates an intermediate file tmp.sql"
    echo "It may be edited and supplied to this script"
    echo "\$myoutputfile will contain the final collection of info"
    exit
fi

outputfile=`echo "$@" | awk -F '--output' '{printf $2}' | awk -F ' ' '{printf $1}'`
sqlListFile=`echo "$@" | awk -F '--uselistfile' '{printf $2}' | awk -F ' ' '{printf $1}'`

if [ ${#outputfile} -eq 0 ] ; then
    outputfile="info_${1}_${2}.txt"
    echo "auto outputfile=${outputfile}"
fi
echo "outputfile=${outputfile}, sqlListFile=<${sqlListFile}>"

if [ ${#sqlListFile} -eq 0 ] ; then
    sqlListFile=tmp.sql
    echo -e "\nBuilding the intermediate script <${sqlListFile}>"
# Build an sql script for checking whether the run is local or global
echo -n 'SELECT  "STRING_VALUE" FROM "CMS_RUNINFO"."RUNSESSION_PARAMETER" WHERE "RUNNUMBER"=' > checkGlobal.sql
echo -n "'&1'"  >> checkGlobal.sql
echo -n 'AND "NAME" LIKE'  >> checkGlobal.sql
echo  "'%RUN_TYPE';" >> checkGlobal.sql
echo "exit;" >> checkGlobal.sql

# Start building an sql query for dumping the desired info from local runs
# All these first lines are just to make the output pretty
echo 'set linesize 300;' > tmp.sql
echo 'set wrap off;' >> tmp.sql
echo 'set trimout on;' >> tmp.sql
echo 'set tab off;' >> tmp.sql
echo 'column NAME format a30' >> tmp.sql
echo 'column TIME format a50' >> tmp.sql
echo 'column STRING_VALUE format a80' >> tmp.sql

# Loop over user-specified run-number range
for ((run=$1; run<=$2; run++))
do 
	# Use the script for checking if a run is global or local
    echo "run=$run"
	sqlplus cms_hcl_runinfo/run2009info@cms_omds_adg @checkGlobal.sql $run | grep -q GLOBAL
	status="$?"
	echo "got status=${status}"
	# If it's global, then do nothing
	if [ "${status}" = "0" ]; then
		echo -n
        # Otherwise, add the local run number to the query for looking at local runs.
	else
		echo -n 'SELECT  "RUNNUMBER","TIME", "NAME","STRING_VALUE" FROM "CMS_RUNINFO"."RUNSESSION_PARAMETER" WHERE "RUNNUMBER"=' >> tmp.sql
		echo -n $run >> tmp.sql
		echo -n ' AND ("NAME" LIKE' >> tmp.sql
		echo -n " '%FULLPATH'" >> tmp.sql
		echo -n ' OR "NAME" LIKE ' >> tmp.sql
		echo -n "'%TRIGGERS%'" >> tmp.sql
		echo ');' >> tmp.sql
	fi
done
# Finish building the query for all the local runs
echo 'exit;' >> tmp.sql
fi

# Execute the query to dump the desired info for the local runs
echo "executing the query to get info"
echo "@${sqlListFile}" | sqlplus cms_hcl_runinfo/run2009info@cms_omds_adg | grep -v "rows selected" | cat -s  | tee ${outputfile}
echo "script done!! File ${outputfile} created"
