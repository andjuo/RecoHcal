#ifndef ShowTimeDep_H
#define ShowTimeDep_H

#include "ObjClass.h"
#include "HistoDef.h"


// --------------------------------------------------------

struct PlotOptions_t;

std::vector<TCanvas*>* MakeTimeDepPlot(HistoDef_t hd,
				       const InputCards_t &ic,
				       const PlotOptions_t &opt);

// --------------------------------------------------------
// --------------------------------------------------------

struct PlotOptions_t {
  int fFixedYRange;
  int fSuppressErrorInPlots;
  TString fOutFigFormat;
  TString fOutDirName;
  TString fLegPlace;   // (not used) Values: default
public:
  PlotOptions_t() :
      fFixedYRange(1),
      fSuppressErrorInPlots(0),
      fOutFigFormat("gif"),
      fOutDirName("dir-figs"),
      fLegPlace("default")
  {}
};

// --------------------------------------------------------

#endif
