#ifndef HistoDef_H
#define HistoDef_H

#include "ObjClass.h"
#include <TString.h>

// -------------------------------------------------------------

struct HistoDef_t;
TCanvas *MakePlotHD(HistoDef_t hd, const InputCards_t &ic);


// -------------------------------------------------------------

  //     1-  Amp,  2 - TSn,  3 - TSx,  4 - Width,        5-Ratio,
  //     6-  <A>,    7-<TSn>,      8-<TSx>,      9-<W>,     10-<R>,
  //    11- <P0>,   12-<P1>,      13-<P2>,      14-<P3>,
  //    15-<PW0>,   16-<PW1>,     17-<PW2>,     18-<PW3>,
  //    19-  no,     20-no,
  //    21-A_calib, 22-TSn_calib, 23-TSx_calib, 24-W_calib, 25-R_calib,

typedef enum {
  _calcNone=0, _calcAmp, _calcTSn, _calcTSx, _calcWidth, _calcRatio,
  _calcAvgAmp, _calcAvgTSn, _calcAvgTSx, _calcAvgWidth, _calcAvgRatio,
  _calcAvgP0, _calcAvgP1, _calcAvgP2, _calcAvgP3,
  _calcAvgPW0, _calcAvgPW1, _calcAvgPW2, _calcAvgPW3,
  _calcACalib, _calcTSnCalib, _calcTSxCalib, _calcWCalib, _calcRCalib,
  _calcLast,
  _calcUnknown
} TMethod_t;

typedef enum { _histo0, _histo1F, _histo1D, _histo2F, _histo2D } THistoDim_t;

typedef enum { _getNone, _getHisto, _getMean, _getLast, _getUnknown }
  TAction_t;

// -------------------------------------------------------------

// define dictionaries ( enum <-> TString )

TString GetMethodName(TMethod_t method, int shortVersion=0);
TMethod_t GetMethod(TString str);
void ListMethods(int shortVersion=0);
void CheckMethodConversion(int shortVersion=0);

TString GetHistoDimName(THistoDim_t hd);
THistoDim_t GetHistoDim(TString str);

TString GetActionName(TAction_t a);
TAction_t GetAction(TString str);

// -------------------------------------------------------------

inline TMethod_t nextMethod(TMethod_t m) {
  if (m<_calcLast) m=TMethod_t(int(m)+1);
  return m;
}

inline void next(TMethod_t &m) { m=nextMethod(m); }

// -------------------------------------------------------------

struct HistoDef_t {
  TString fCalibType;
  TMethod_t fMethod;
  int fDepth;
  TString fPlotTitle;
  TString fInpHistoName, fInpHistoName2;
  THistoDim_t fHistoDim;
  //TAction_t fAction;
  TH1F *fH1F;
  TH2F *fH2F, *fH2F_2, *fH2F_ratio;
public:
  HistoDef_t(TString set_calibtype="LED", TMethod_t set_method=_calcNone, int set_depth=-1);
  HistoDef_t(const HistoDef_t &d, TString cloneTag="");

  TString calibType() const { return fCalibType; }
  TMethod_t method() const { return fMethod; }
  THistoDim_t histoDim() const { return fHistoDim; }
  int depth() const { return fDepth; }
  TString plotTitle() const { return fPlotTitle; }
  TH1F *getHisto() { return fH1F; }
  TH2F *getHisto2F() { return fH2F; }
  TH2F *getHisto2F_2() { return fH2F_2; }
  TH2F *getHisto2F_ratio() { return fH2F_ratio; }

  // Main methods that initialize the histogram names and the types
  int setMethod(TMethod_t set_method, int set_depth);
  int setMethod(TString reset_calibtype, TMethod_t set_method, int set_depth); // calls setMethod

  // Load histograms from a file and put them in the TH1F or TH2F fields
  int loadHisto(TFile &f, TString setTag="");

  Float_t getMean() const {
    if (fH1F) return fH1F->GetMean();
    std::cout << "getMean fH1F is not ready (fInpHistoName=" << fInpHistoName
	      << ", fPlotTitle=" << fPlotTitle << ")\n";
    return -999.;
  }

};

// -------------------------------------------------------------
// -------------------------------------------------------------

#endif
