# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Reconstruction.py -s RAW2DIGI,RECO --filein file:gensimraw.root --eventcontent RECO --datatier RECO --conditions FrontierConditions_GlobalTag,auto:upgradePLS1 -n 10 --data --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('OKRECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('RecoLocalCalo.Configuration.hcalLocalReco_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/0CAAF9B9-C70A-E511-8343-02163E01438B.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/0E551221-BE0A-E511-A607-02163E01424A.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/0EFC0ECE-BD0A-E511-8D83-02163E014569.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/1847400E-A20A-E511-9F5D-02163E012069.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/1C533E9E-8B0A-E511-B399-02163E014117.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/1EEB378D-C70A-E511-8C73-02163E014569.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/20C2BD6F-C70A-E511-A1F6-02163E013907.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/20C73BA1-8B0A-E511-B149-02163E012069.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/20D5C6A8-BD0A-E511-A8C6-02163E014100.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/2658D86D-C70A-E511-9197-02163E0141CC.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/28DBB5B0-8B0A-E511-845B-02163E01456E.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/2AD6B927-E10A-E511-A017-02163E0145BA.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/32F856AC-8B0A-E511-ABBF-02163E014281.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/345A6ED1-BD0A-E511-8DC4-02163E0128A1.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/348E946D-C70A-E511-8EC9-02163E01460E.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/36D6F0A8-BD0A-E511-AB9E-02163E0145BD.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/3AB7046F-C70A-E511-A474-02163E013775.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/5A06DB6F-C70A-E511-8336-02163E0138C6.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/766BC8C9-BD0A-E511-BA65-02163E012069.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/7A0917CA-8B0A-E511-BF15-02163E014374.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/7C158FAD-A40A-E511-ACB1-02163E0145B0.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/7C76059F-8B0A-E511-BE6B-02163E0139DE.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/7E13580A-A20A-E511-B3DC-02163E0145BD.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/7E50E8A3-8B0A-E511-B332-02163E0140E8.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/80F79CA0-8B0A-E511-A1B7-02163E011850.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/8266BE6D-C70A-E511-A426-02163E014166.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/8291B69F-8B0A-E511-AA8A-02163E01461C.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/82ECF172-C70A-E511-B81B-02163E0140E8.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/84297706-A20A-E511-9052-02163E01461C.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/88BDAC9F-8B0A-E511-AEA7-02163E0137F0.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/8A2B5039-A20A-E511-87DA-02163E014569.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/96DDFB9F-8B0A-E511-BE7E-02163E0138F6.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/A49A549F-8B0A-E511-86FA-02163E0145C6.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/AA09C5A0-8B0A-E511-B602-02163E012028.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/AC713221-A20A-E511-9584-02163E014374.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/B2F6E5B2-BD0A-E511-B586-02163E0144C3.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/B42BAA05-A20A-E511-8B36-02163E014147.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/B65DEDC4-DE0A-E511-A165-02163E014569.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/B8998210-A20A-E511-B66D-02163E0146AD.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/BA40676C-C70A-E511-B297-02163E011B58.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/BA82A7A8-BD0A-E511-9C40-02163E0141D2.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/C0D0AF6F-C70A-E511-9AC4-02163E01424D.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/C207D6AB-BD0A-E511-A4E9-02163E0138F6.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/C66205A0-8B0A-E511-B01B-02163E0136B3.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/C6E63B9F-8B0A-E511-AA4D-02163E013979.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/CC641BA0-8B0A-E511-A28F-02163E01369F.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/D82BC69F-8B0A-E511-B576-02163E0143CB.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/D854ED9F-8B0A-E511-B8B0-02163E014300.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/DA4723CF-8B0A-E511-B44B-02163E01463F.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/E019D973-C70A-E511-A325-02163E01288E.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/E0BC170D-A20A-E511-96B3-02163E014338.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/E4E74D9A-BE0A-E511-9A2B-02163E01460E.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/E8FF8FBA-8B0A-E511-B52E-02163E011911.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/EEC0E80B-A20A-E511-84E0-02163E014601.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/F6ADDEA0-8B0A-E511-A632-02163E0133EB.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/FAA3C4B6-BD0A-E511-A9D6-02163E0126EB.root',
'/store/data/Run2015A/Commissioning/RAW/v1/000/246/951/00000/FE672C6E-C70A-E511-9DE1-02163E0145BD.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
#        SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Reconstruction.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)
###########################################################################################################3
process.Analyzer = cms.EDAnalyzer("VeRawAnalyzer",
                                  #
                                  Verbosity = cms.untracked.int32(0),
                                  #Verbosity = cms.untracked.int32(1),
                                  #Verbosity = cms.untracked.int32(-10234),
                                  ##Verbosity = cms.untracked.int32(-91),
                                  #Verbosity = cms.untracked.int32(-51),
                                  #
                                  MapCreation = cms.untracked.int32(1),
                                  #
                                  recordNtuples = cms.untracked.bool(False),
                                  #recordNtuples = cms.untracked.bool(True),
                                  maxNeventsInNtuple = cms.int32(100),
                                  #
                                  #recordHistoes = cms.untracked.bool(False),
                                  recordHistoes = cms.untracked.bool(True),
                                  #
                                  ##scripts: zRunRatio34.C, zRunNbadchan.C
                                  studyRunDependenceHist = cms.untracked.bool(True),
                                  #studyRunDependenceHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zerrors.C
                                  studyCapIDErrorsHist = cms.untracked.bool(True),
                                  #studyCapIDErrorsHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zrms.C
                                  studyRMSshapeHist = cms.untracked.bool(True),
                                  #studyRMSshapeHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zratio34.C
                                  studyRatioShapeHist = cms.untracked.bool(True),
                                  #studyRatioShapeHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zadcamplitude.C
                                  studyADCAmplHist = cms.untracked.bool(True),
                                  #studyADCAmplHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: ztsmean.C
                                  studyTSmeanShapeHist = cms.untracked.bool(True),
                                  #studyTSmeanShapeHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: ztsmaxa.C
                                  studyTSmaxShapeHist = cms.untracked.bool(True),
                                  #studyTSmaxShapeHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zcalib....C
                                  studyCalibCellsHist = cms.untracked.bool(True),
                                  #studyCalibCellsHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zdifampl.C
                                  studyDiffAmplHist = cms.untracked.bool(True),
                                  #studyDiffAmplHist = cms.untracked.bool(False),
                                  #
                                  ##scripts: zadcamplitude.C
                                  studyPedestalsHist = cms.untracked.bool(True),
                                  #studyPedestalsHist = cms.untracked.bool(False),
                                  #
                                  #
                                  ##scripts: zamplpedcorr.C
                                  studyPedestalCorrelations = cms.untracked.bool(True),
                                  #studyPedestalsHist = cms.untracked.bool(False),
                                  #
                                  #
                                  ##DigiCollectionLabel = cms.untracked.InputTag("hcalDigis"),
                                  #Verbosity = cms.untracked.int32(-54),
                                  #Verbosity = cms.untracked.int32(-22),
                                  #Verbosity = cms.untracked.int32(-11),
                                  #Verbosity = cms.untracked.int32(-12),
                                  #Verbosity = cms.untracked.int32(-13),
                                  #Verbosity = cms.untracked.int32(-51),
                                  #Verbosity = cms.untracked.int32(-24),
                                  #Verbosity = cms.untracked.int32(-244),
                                  #Verbosity = cms.untracked.int32(-233),
                                  #
                                  # Verbosity = cms.untracked.int32(-78),
                                  #
                                  #
                                  #         Normal channels:
                                  #
                                  # -53 for  BAD HBHEHF channels from study on shape Ratio
                                  #Verbosity = cms.untracked.int32(-53),
                                  ratioHBMin = cms.double(0.10),
                                  ratioHBMax = cms.double(0.85),
                                  ratioHEMin = cms.double(0.10),
                                  ratioHEMax = cms.double(0.85),
                                  ratioHFMin = cms.double(0.10),
                                  ratioHFMax = cms.double(0.98),
                                  ratioHOMin = cms.double(0.10),
                                  ratioHOMax = cms.double(0.85),
                                  # -54 for  BAD HBHEHF channels from study on RMS of shapes
                                  #Verbosity = cms.untracked.int32(-54),
                                  rmsHBMin = cms.double(2.0),
                                  rmsHBMax = cms.double(4.5),
                                  rmsHEMin = cms.double(1.8),
                                  rmsHEMax = cms.double(4.5),
                                  rmsHFMin = cms.double(0.2),
                                  rmsHFMax = cms.double(3.8),
                                  rmsHOMin = cms.double(2.2),
                                  rmsHOMax = cms.double(3.8),
                                  # -55 for  BAD HBHEHF channels from study on TSmean of shapes
                                  #Verbosity = cms.untracked.int32(-55),
                                  TSmeanHBMin = cms.double(2.2),
                                  TSmeanHBMax = cms.double(6.5),
                                  TSmeanHEMin = cms.double(2.2),
                                  TSmeanHEMax = cms.double(6.5),
                                  TSmeanHFMin = cms.double(0.5),
                                  TSmeanHFMax = cms.double(6.5),
                                  TSmeanHOMin = cms.double(2.2),
                                  TSmeanHOMax = cms.double(6.5),
                                  # -55 for  BAD HBHEHF channels from study on TSmax of shapes
                                  #Verbosity = cms.untracked.int32(-55),
                                  TSpeakHBMin = cms.double(-0.5),
                                  TSpeakHBMax = cms.double(6.5),
                                  TSpeakHEMin = cms.double(-0.5),
                                  TSpeakHEMax = cms.double(6.5),
                                  TSpeakHFMin = cms.double(-0.5),
                                  TSpeakHFMax = cms.double(6.5),
                                  TSpeakHOMin = cms.double(-0.5),
                                  TSpeakHOMax = cms.double(6.5),
                                  # -56 for  BAD HBHEHOHF channels from study on ADC Amplitude
                                  #Verbosity = cms.untracked.int32(-56),
                                  ADCAmplHBMin = cms.double(0.),
                                  ADCAmplHBMax = cms.double(2000.),
                                  ADCAmplHEMin = cms.double(0.),
                                  ADCAmplHEMax = cms.double(1500.),
                                  ADCAmplHFMin = cms.double(0.),
                                  ADCAmplHFMax = cms.double(1000.),
                                  ADCAmplHOMin = cms.double(0.),
                                  ADCAmplHOMax = cms.double(9000.),
                                  #
                                  #
                                  # to see channels for pedestal tails (& < 1.0 hardcoded)
                                  pedestalHBMax = cms.double(0.2),
                                  pedestalHEMax = cms.double(0.9),
                                  pedestalHFMax = cms.double(0.1),
                                  pedestalHOMax = cms.double(0.2),
#                                  pedestalHBMax = cms.double(5.2),
#                                  pedestalHEMax = cms.double(5.4),
#                                  pedestalHFMax = cms.double(14.0),
#                                  pedestalHOMax = cms.double(14.0),
                                  #
                                  # to see channels w/ PedestalSigma > mean+5RMS(& < 0.10 hardcoded)
                                  #Verbosity = cms.untracked.int32(-57),
                                  #Verbosity = cms.untracked.int32(-57),
                                  pedestalwHBMax = cms.double(0.2),
                                  pedestalwHEMax = cms.double(0.2),
                                  pedestalwHFMax = cms.double(0.1),
                                  pedestalwHOMax = cms.double(0.16),
#                                  pedestalwHBMax = cms.double(1.20),
#                                  pedestalwHEMax = cms.double(1.50),
#                                  pedestalwHFMax = cms.double(1.30),
#                                  pedestalwHOMax = cms.double(0.80),
                                  #
                                  #
                                  #
                                   #             CALIBRATION channels:
                                  #
                                  # for  BAD HBHEHOHF CALIBRATION channels from study on ADC amplitude
                                  # cuts for Laser runs:
                                  #calibrADCHBMin = cms.double(15.0),
                                  #calibrADCHEMin = cms.double(15.0),
                                  #calibrADCHOMin = cms.double(15.0),
                                  #calibrADCHFMin = cms.double(15.0),
                                  # cuts for LED runs:
                                  calibrADCHBMin = cms.double(120.),
                                  calibrADCHEMin = cms.double(120.),
                                  calibrADCHOMin = cms.double(120.),
                                  calibrADCHFMin = cms.double(60.),
                                  calibrADCHBMax = cms.double(3000.),
                                  calibrADCHEMax = cms.double(3000.),
                                  calibrADCHOMax = cms.double(3000.),
                                  calibrADCHFMax = cms.double(3000.),
                                  # for  BAD HBHEHOHF CALIBRATION channels from study on shape Ratio
                                  calibrRatioHBMin = cms.double(0.60),
                                  calibrRatioHEMin = cms.double(0.64),
                                  calibrRatioHOMin = cms.double(0.25),
                                  calibrRatioHFMin = cms.double(0.25),
                                  calibrRatioHBMax = cms.double(0.99),
                                  calibrRatioHEMax = cms.double(0.99),
                                  calibrRatioHOMax = cms.double(0.99),
                                  calibrRatioHFMax = cms.double(0.99),
                                  # for  BAD HBHEHOHF CALIBRATION channels from study on TSmax
                                  calibrTSmaxHBMin = cms.double(0.50),
                                  calibrTSmaxHBMax = cms.double(8.50),
                                  calibrTSmaxHEMin = cms.double(0.50),
                                  calibrTSmaxHEMax = cms.double(8.50),
                                  calibrTSmaxHOMin = cms.double(0.50),
                                  calibrTSmaxHOMax = cms.double(8.50),
                                  calibrTSmaxHFMin = cms.double(0.50),
                                  calibrTSmaxHFMax = cms.double(9.50),
                                  # for  BAD HBHEHOHF CALIBRATION channels from study on TSmean
                                  calibrTSmeanHBMin = cms.double(1.00),
                                  calibrTSmeanHBMax = cms.double(5.50),
                                  calibrTSmeanHEMin = cms.double(1.00),
                                  calibrTSmeanHEMax = cms.double(5.50),
                                  calibrTSmeanHOMin = cms.double(1.00),
                                  calibrTSmeanHOMax = cms.double(3.50),
                                  calibrTSmeanHFMin = cms.double(1.00),
                                  calibrTSmeanHFMax = cms.double(5.20),
                                  # for  BAD HBHEHOHF CALIBRATION channels from study on Width
                                  calibrWidthHBMin = cms.double(1.00),
                                  calibrWidthHBMax = cms.double(2.30),
                                  calibrWidthHEMin = cms.double(1.00),
                                  calibrWidthHEMax = cms.double(2.30),
                                  calibrWidthHOMin = cms.double(0.50),
                                  calibrWidthHOMax = cms.double(3.00),
                                  calibrWidthHFMin = cms.double(0.20),
                                  calibrWidthHFMax = cms.double(2.30),
                                  #
                                  # Special task of run or LS quality:
                                  #
                                  # flag for ask runs of LSs:
                                  #=0-runs, =1-LSs
                                  flagtoaskrunsorls = cms.int32(1),
                                  #
                                  # flag for choise of criterion of bad channels:
                                  #=0-CapIdErr, =1-Ratio, =2-Width, =3-TSmax, =4-TSmean, =5-adcAmplitud
                                  flagtodefinebadchannel = cms.int32(0),
                                  #how many bins you want on the plots:better to choice (#LS+1)
                                  howmanybinsonplots = cms.int32(80),
                                  #howmanybinsonplots = cms.int32(2600),
                                  #
                                  #
                                  flagabortgaprejected = cms.int32(1),
                                  bcnrejectedlow = cms.int32(3446),
                                  bcnrejectedhigh= cms.int32(3564),
                                  #
                                  # cuts on Nbadchannels to see LS dependences:
                                  # Verbosity = cms.untracked.int32(-77),
                                  # to select abnormal events,for which Nbcs > this limits
                                  lsdep_cut1_peak_HBdepth1 = cms.int32(20),
                                  lsdep_cut1_peak_HBdepth2 = cms.int32(7),
                                  lsdep_cut1_peak_HEdepth1 = cms.int32(16),
                                  lsdep_cut1_peak_HEdepth2 = cms.int32(13),
                                  lsdep_cut1_peak_HEdepth3 = cms.int32(4),
                                  lsdep_cut1_peak_HFdepth1 = cms.int32(10),
                                  lsdep_cut1_peak_HFdepth2 = cms.int32(5),
                                  lsdep_cut1_peak_HOdepth4 = cms.int32(45),
                                  # to select events with Nbcs > this limits
                                  lsdep_cut3_max_HBdepth1 = cms.int32(19),
                                  lsdep_cut3_max_HBdepth2 = cms.int32(6),
                                  lsdep_cut3_max_HEdepth1 = cms.int32(15),
                                  lsdep_cut3_max_HEdepth2 = cms.int32(12),
                                  lsdep_cut3_max_HEdepth3 = cms.int32(3),
                                  lsdep_cut3_max_HFdepth1 = cms.int32(9),
                                  lsdep_cut3_max_HFdepth2 = cms.int32(4),
                                  lsdep_cut3_max_HOdepth4 = cms.int32(40),
                                  #
                                  #old was for runs:
                                  #                                  nbadchannels1 = cms.int32(7),
                                  #                                  nbadchannels2 = cms.int32(12),
                                  #                                  nbadchannels3 = cms.int32(50),
                                  # to see signal & pedestal in HB TSs
                                  # Verbosity = cms.untracked.int32(-80),
                                  #Verbosity = cms.untracked.int32(-79),
                                  # cuts on Estimator1 to see bcs & LS dependences:
                                  lsdep_estimator1_HBdepth1 = cms.double(0.),
                                  lsdep_estimator1_HBdepth2 = cms.double(0.),
                                  lsdep_estimator1_HEdepth1 = cms.double(0.),
                                  lsdep_estimator1_HEdepth2 = cms.double(0.),
                                  lsdep_estimator1_HEdepth3 = cms.double(0.),
                                  lsdep_estimator1_HFdepth1 = cms.double(0.),
                                  lsdep_estimator1_HFdepth2 = cms.double(0.),
                                  lsdep_estimator1_HOdepth4 = cms.double(0.),
                                  # cuts on Estimator2 to see bcs & LS dependences:
                                  lsdep_estimator2_HBdepth1 = cms.double(0.),
                                  lsdep_estimator2_HBdepth2 = cms.double(0.),
                                  lsdep_estimator2_HEdepth1 = cms.double(0.),
                                  lsdep_estimator2_HEdepth2 = cms.double(0.),
                                  lsdep_estimator2_HEdepth3 = cms.double(0.),
                                  lsdep_estimator2_HFdepth1 = cms.double(0.),
                                  lsdep_estimator2_HFdepth2 = cms.double(0.),
                                  lsdep_estimator2_HOdepth4 = cms.double(0.),
                                  # cuts on Estimator3 to see bcs & LS dependences:
                                  lsdep_estimator3_HBdepth1 = cms.double(0.),
                                  lsdep_estimator3_HBdepth2 = cms.double(0.),
                                  lsdep_estimator3_HEdepth1 = cms.double(0.),
                                  lsdep_estimator3_HEdepth2 = cms.double(0.),
                                  lsdep_estimator3_HEdepth3 = cms.double(0.),
                                  lsdep_estimator3_HFdepth1 = cms.double(0.),
                                  lsdep_estimator3_HFdepth2 = cms.double(0.),
                                  lsdep_estimator3_HOdepth4 = cms.double(0.),
                                  # cuts on Estimator4 to see bcs & LS dependences:
                                  lsdep_estimator4_HBdepth1 = cms.double(0.),
                                  lsdep_estimator4_HBdepth2 = cms.double(0.),
                                  lsdep_estimator4_HEdepth1 = cms.double(0.),
                                  lsdep_estimator4_HEdepth2 = cms.double(0.),
                                  lsdep_estimator4_HEdepth3 = cms.double(0.),
                                  lsdep_estimator4_HFdepth1 = cms.double(0.),
                                  lsdep_estimator4_HFdepth2 = cms.double(0.),
                                  lsdep_estimator4_HOdepth4 = cms.double(0.),
                                  # cuts on Estimator5 to see bcs & LS dependences:
                                  lsdep_estimator5_HBdepth1 = cms.double(0.),
                                  lsdep_estimator5_HBdepth2 = cms.double(0.),
                                  lsdep_estimator5_HEdepth1 = cms.double(0.),
                                  lsdep_estimator5_HEdepth2 = cms.double(0.),
                                  lsdep_estimator5_HEdepth3 = cms.double(0.),
                                  lsdep_estimator5_HFdepth1 = cms.double(0.),
                                  lsdep_estimator5_HFdepth2 = cms.double(0.),
                                  lsdep_estimator5_HOdepth4 = cms.double(0.),
                                  #
                                  # 
                                  #Verbosity = cms.untracked.int32(-81),
                                  #Verbosity = cms.untracked.int32(-82),
                                  #Verbosity = cms.untracked.int32(-83),
                                  # 
                                  # use ADC amplitude:
                                  useADCmassive = cms.untracked.bool(True),
                                  useADCfC = cms.untracked.bool(False),
                                  useADCcounts = cms.untracked.bool(False),
                                  # 
                                  # Pedestals in fC
                                  #usePedestalSubtraction = cms.untracked.bool(True),
                                  usePedestalSubtraction = cms.untracked.bool(False),
                                  #
                                  # for possible ignoring of channels w/o signal, apply same cut for
                                  # HBHEHFHO on Amplitude, usable for all Estimators 1,2,3,4,5:
                                  # forallestimators_amplitude_bigger = cms.double(10.),
                                  forallestimators_amplitude_bigger = cms.double(-100.),
                                  #
                                  #
                                  usecontinuousnumbering = cms.untracked.bool(False),
                                  #usecontinuousnumbering = cms.untracked.bool(True),
                                  #
                                  #
                                  #
                                  hcalCalibDigiCollectionTag = cms.InputTag('hcalDigis'),
                                  hbheDigiCollectionTag = cms.InputTag('hcalDigis'),
                                  hoDigiCollectionTag = cms.InputTag('hcalDigis'),
                                  hfDigiCollectionTag = cms.InputTag('hcalDigis'),
                                  #
                                  #
                                  #
                                  splashesUpperLimit = cms.int32(10000),
                                  #
                                  HistOutFile = cms.untracked.string('Global.root'),
                                  #
                                  MAPOutFile = cms.untracked.string('LogEleMapdb.h')
                                  #
                                  ##OutputFilePath = cms.string('/tmp/zhokin/'),        
                                  ##OutputFileExt = cms.string(''),
                                  #
)		

# Other statements
process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_P_V54', '')

#process.hcalDigis.InputLabel = "hltFEDSelector"

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.ana = cms.Path(process.Analyzer)
process.hcalDigis_step = cms.Path(process.hcalDigis)
process.hcalDigis.FilterDataQuality = cms.bool(False)

# Schedule definition
process.schedule = cms.Schedule(process.hcalDigis_step,process.ana)

process.MessageLogger = cms.Service("MessageLogger",
     categories   = cms.untracked.vstring(''),
     destinations = cms.untracked.vstring('cout'),
     debugModules = cms.untracked.vstring('*'),
     cout = cms.untracked.PSet(
         threshold = cms.untracked.string('WARNING'),
	 WARNING = cms.untracked.PSet(limit = cms.untracked.int32(0))
     )
 )
