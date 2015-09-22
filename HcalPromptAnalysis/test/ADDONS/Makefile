

CFLAGS=-std=c++11
INCLUDE=-I ${ROOTSYS}/include
LIBS=-L ${ROOTSYS}/lib -lCore -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -lTMVA -lMinuit -lXMLIO -lMLP -lTreePlayer -lz -lGui -pthread -lm -ldl 

OBJ=ObjClass.o

default: zamt_hf2.exe

zamt_hf.exe: zamt_hf.cc
	c++ ${CFLAGS} $^ -o $@ ${INCLUDE} ${LIBS}

zamt_hf2.exe: zamt_hf2.cc ObjClass.o
	c++ ${CFLAGS} $^ -o $@ ${INCLUDE} ${LIBS}


ObjClass.o: ObjClass.cc ObjClass.h
	c++ ${CFLAGS} $< -c -o $@ ${INCLUDE}
