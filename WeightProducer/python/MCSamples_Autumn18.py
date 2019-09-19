import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Autumn18
Autumn18samples = [
	# NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
	MCSample('TTJets_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10244307, False, 10234409),
	MCSample('TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 59929205, False, 59872080),
	MCSample('TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 57259880, False, 57205136),
	MCSample('TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 28701360, False, 28674428),
	MCSample('TTJets_SingleLeptFromT_genMET-80_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 84200008, False, 84099728),
	MCSample('TTJets_SingleLeptFromTbar_genMET-80_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 79463720, False, 79369120),
	MCSample('TTJets_DiLept_genMET-80_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 58442000, False, 58374896),
	MCSample('TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 14149394, False, 14065202),
	MCSample('TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10372802, False, 10282774),
	MCSample('TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2779427, False, 2735863),
	MCSample('TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1451104, False, 1376490),
	MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29535000, False),
	MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 25255000, False),
	MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29710000, False),
	MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 41744000, False),
	MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 42459973, False), # subtotal = 17712000, straight subtotal = 17712000
	MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 42459973, False), # subtotal = 24747973, straight subtotal = 24747973
	MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 64061000, False),
	MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 37598000, False),
	MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 18485000, False),
	MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 6928000, False), # subtotal = 2160000, straight subtotal = 2160000
	MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 6928000, False), # subtotal = 4768000, straight subtotal = 4768000
	MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4017800, False), # subtotal = 1445800, straight subtotal = 1445800
	MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4017800, False), # subtotal = 2572000, straight subtotal = 2572000
	MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2394000, False), # subtotal = 1440000, straight subtotal = 1440000
	MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 2394000, False), # subtotal = 954000, straight subtotal = 954000
	MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 800000, False),
	MCSample('QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 4576065, False),
	MCSample('QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v4', 'RunIIAutumn18MiniAOD', 'Constant', 30612338, False),
	MCSample('QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 29884616, False),
	MCSample('QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 20268872, False),
	MCSample('QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 612919, False),
	MCSample('QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 633668, False),
	MCSample('QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 35978539, False),
	MCSample('QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 492418, False),
        MCSample('QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 20495750, False), # subtotal = 492716
        MCSample('QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 20495750, False), # subtotal = 20003034
	MCSample('QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 16618977, False),
        MCSample('QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext3-v2', 'RunIIAutumn18MiniAOD', 'Constant', 16749914, False),
	MCSample('QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10719790, False),
	MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19996995, False),
	MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', 'HEM_102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 18688995, False),
	MCSample('QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 54289442, False, 54251666),
	MCSample('QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 54661579, False, 54600685),
	MCSample('QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 55152960, False, 55056202),
	MCSample('QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 48158738, False, 48038740),
	MCSample('QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 15466225, False, 15407797),
	MCSample('QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10955087, False, 10887751),
	MCSample('QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5475677, False, 5414545),
	MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 11530510, False, 11518130),
	MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 427051, False, 415713),
	MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 11225887, False, 11206441),
	MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 9643184, False, 9616642),
	MCSample('DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 8862104, False, 8828622),
	MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 3138129, False, 3121975),
	MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 100194597, False, 100114408),
	MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 507624, False, 503192),
	MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29521158, False, 29488310),
	MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 25468933, False, 25423156),
	MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 3273980, False, 3191612),
	MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5932701, False, 5915969),
	MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19771294, False, 19699782),
	MCSample('WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 28084244, False, 28060304),
	MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 8402687, False, 8362227),
	MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 7633949, False, 7571583),
        MCSample('WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10071273, False, 10050037),
        MCSample('WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 15298056, False, 15253718),
        MCSample('WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 14627242, False, 14561238),
	MCSample('ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 359639, False, 350333),
	MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 23702894, False, 23678782),
	MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 23276346, False, 23236674),
	MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2707156, False, 2699566),
	MCSample('ZJetsToNuNu_HT-600To800_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5748975, False, 5728007),
	MCSample('ZJetsToNuNu_HT-800To1200_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2066798, False, 2056362),
	MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 343198, False, 340302),
	MCSample('GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '4cores5k_102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 9798176, False, 9796870),
	MCSample('GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19062809, False, 19055655),
	MCSample('GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4655985, False, 4652345),
	MCSample('GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4981121, False, 4971983),
	MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 15424758, False, 15423022),
	MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 49457520, False, 49438028),
	MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 13717985, False, 13705653),
	MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 12456593, False, 12431845),
	MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v3', 'RunIIAutumn18MiniAOD', 'Constant', 19965000, False, 12458638),
        MCSample('ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 9706000, False, 6052124),
	MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1086487, False, 1081535),
	MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1085847, False, 1080939),
	MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 7623000, False, 7588180),
	MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 9598000, False, 9553912),
        MCSample('ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 154307600, False, 144094800),
        MCSample('ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 79090800, False, 74227136),
	MCSample('tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4977000, False, 1287198),
	MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4683136, False, 2941220),
	MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1690064, False, 920352),
	MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 18901469, False, 11248663),
	MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 56428600, False, 56356040), # subtotal = 8371752, straight subtotal = 8382600
	MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '102X_upgrade2018_realistic_v15_ext2-v2', 'RunIIAutumn18MiniAOD', 'Constant', 56428600, False, 56356040), # subtotal = 47984288, straight subtotal = 48046000
	MCSample('ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 57728992, False, 36452112),
	MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 27900469, False, 17815224),
	MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4691915, False, 1842387),
	MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4911941, False, 2686095),
	MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 835296, False, 458226),
	MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 750000, False, 355226),
	MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 13280000, False, 6274046),
	MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 185000, False, 184094),
	MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 64310000, False, 63791484),
	MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 133808000, False, 132725582),
	MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 101550000, False, 100728760),
	MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 199274),
        MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 199060),
        MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext2-v1', 'RunIIAutumn18MiniAOD', 'Constant', 800000, False, 796064),
        MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 198758),
        MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 199396),
        MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 199358),
        MCSample('TTTJ_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 184000, False, 182650),
        MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 2359420, False, 882074),
        MCSample('TTTW_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 200000, False, 199692),
        MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 240000, False, 210100),
        MCSample('WWZ_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 250000, False, 219910),
        MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 250000, False, 219250),
        MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 250000, False, 214282),
        MCSample('ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 7525991, False, 7368333),
        MCSample('ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 11835999, False, 11590377),
        MCSample('WW_TuneCP5_13TeV-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 7850000, False),
        MCSample('ZZ_TuneCP5_13TeV-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1979000, False),
        MCSample('WZ_TuneCP5_13TeV-pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 3885000, False),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1460344, False, 1459016),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1464311, False, 1461991),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1434483, False, 1432383),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1350168, False, 1348088),
        # stealth/rpv stop signals 
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1534432, False),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1529517, False),
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1506030, False),
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1143261, False),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 634080, False),
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 367440, False),
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 220952, False),
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 155322, False),
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 151839, False),
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 151623, False),
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 78020, False),
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 79130, False),
        MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 82843, False),
]
