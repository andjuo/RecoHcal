#!/bin/csh
# ./compile.csh code.cc

set ROOTINC="-I `root-config --incdir`"
set ROOTLIBS="`root-config --libs`"
set CFLAGS="-std=c++11"
set CFLAGS=""
echo "ROOTINC=${ROOTINC}"
echo "ROOTLIBS=${ROOTLIBS}"
set comm="c++ ${1} ${ROOTINC} ${CFLAGS} -o ${1}.exe ${ROOTLIBS}"
echo "${comm}"
${comm}

#c++ ${1} -std=c++11 -I ${ROOTSYS}/include -L ${ROOTSYS}/lib -lCore -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -lTMVA -lMinuit -lXMLIO -lMLP -lTreePlayer -lz -lGui -pthread -lm -ldl 
#mv a.out ${1}.exe
