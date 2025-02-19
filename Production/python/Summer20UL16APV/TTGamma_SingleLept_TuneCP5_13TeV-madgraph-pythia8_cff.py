import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/02C6FEC6-D0A1-7847-90AD-525DF336EF6E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0D908A74-6A79-CC4F-850B-C8015AF971AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1CD10A04-3106-CF43-8EDA-B5AE7639EC82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/215D4B20-10AA-C943-88CB-0866D41D2B82.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3A5AE1AA-B78D-EC4E-9981-ADD9D246AA4D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/49424294-CBEE-9643-A425-A03255CDB243.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/621AC2BA-78AC-C84B-A8C1-495067FC7542.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/7A31C1C2-C179-754C-8E26-DE8207CDEFE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8DAE8CA3-5308-2046-897A-992B2D29D934.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/94450E92-EC0B-E646-9F61-C7233216C778.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/AC66DDEE-871D-194F-9F4C-057FC12C77FD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B160ECF2-CDAE-8145-AFD7-B82E2218C41C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B3D84CA9-FE1A-2A42-9E7D-727CFCE6FA3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/B66A73CC-0B15-2F42-8A78-0F21C0643723.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C8414AE3-4609-6D41-8673-994BF1C0B7CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/CEE1EC3E-1817-214F-9221-436699F788E9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E36EC456-DC5D-F748-9A46-CDD3DF41C69D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F5C7F55E-95A2-0E4D-8A3A-2143D0904D30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/06CB8962-A4EB-A94D-9480-6306BC359765.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/14A21D06-97CD-8846-BEDD-0CFE46146DAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/16B4D69E-D32D-684B-8F0D-515BF87A05FE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1868FE17-40B7-B64C-9106-01184733C714.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1E513995-147D-B649-854B-F24CE9FC8120.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/23EBEAB9-C885-E74A-A0A0-E305780D9B07.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3500B2F6-83F5-2645-8724-2ED1C195EAC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/37D3F0FA-30E7-6148-8A95-A76C2120C0F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3D91F002-7A95-AC4C-B536-6085B4B3F746.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/452B66D7-00E8-0241-9799-8588F1D8EAC5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/487B93DC-98E0-8A49-A34B-855E7581118F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4A03E671-C5AE-AA48-B71C-1931C69C9DB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4B21E642-208F-2840-87B8-1FC35D7AE483.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/54898C55-8D8C-FA4A-BFB4-D918039FBA95.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/55D5244E-4064-D64C-972D-325A3C86CF63.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/5AD8F8FC-A489-0D47-8FCC-8ACD2A4481B8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/61742318-FD29-B04E-AAF8-55FE0333A4C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/659F3D63-2A58-7A46-9FB2-F5CDD0E61F8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/699CF933-E5CD-9C48-B72E-F70BE4C489A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6D32F65E-BE37-F540-B11F-19BE13A1C016.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6DE0583D-10BC-F041-85DD-CA8093349B6C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/71944A18-40D1-EB43-A4E8-36C070E1141A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/76F2D609-2EF9-A64C-B290-0E7E60CFD107.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/7B00966E-D5B0-174C-BB0A-7242E2D5A8F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/82E3516A-D29A-3245-81E7-288EEBD48B66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/877CDC06-DFE2-D442-895D-4A3968CCE29D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8A1A788E-8FCA-ED48-B50E-07C780B09F34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9397F2D1-7D94-324A-8445-DC369B721ACC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/97718CB7-0B7C-B140-B148-EDD188755884.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B2D2A61C-BFEA-804B-BF4F-35B96A42DC6F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B51FA88E-FC90-5F40-845E-B75A98F63129.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B9814E81-B7EF-C646-AB2F-EE4F643C1DB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/BC932546-497A-8945-8CB8-7A11176D3A96.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C513CCE1-3D04-BA44-9AB7-1FBC44280AF3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CAF2A3C8-AA0E-E248-86A7-101E4553B38E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CF508EA4-7CD6-6F4C-BE30-CBC44622B96B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CF8CD3E0-AFFB-3741-B908-FBEBF2EA4394.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CF9BC422-F091-0C44-AFF4-2BAFACEBA7AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D817FB10-1CD8-0446-B19F-F37B60FF2E09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DBCD08CB-E404-A64B-B8F0-40C7B8E2A709.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E49885D8-E0DF-B348-8569-842584A43918.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E8738AAC-E7FC-6A4F-A116-D2138FE2D3BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E8DFBECB-186A-0F45-807B-E3C66BAC6CA0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F458BC7B-CF5C-B54B-A3F8-F4D643778351.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F562AE21-095C-2D43-BCE3-ABB99DACEAAE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F68DC72E-F1CE-FA48-B264-F6A84E20B266.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/0CB820C4-127D-3842-9757-657047E61BC9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/234830BF-4A41-7949-BB22-386254C09943.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5900CDD6-88B3-8F4A-9FB9-BFEBE9C36062.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/706FB1A7-50BC-D547-BCCA-C4F162CC5B5C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/79D94878-B807-034C-97EB-F0A32E1A0227.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/890910DB-2C1E-F64F-AEBF-D73411AC56A2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8C0B2ECB-5E74-624A-9802-18C25078520C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/96C67326-AC11-3D4A-B296-2EE6069875AB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A19D0DB8-C853-D342-8C88-63D3B976AE9C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A1F28E53-D521-DD40-BFC2-FD8EFF6B08E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A31B5590-ADE4-7745-A97E-F789D5B5C6A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B772562D-3839-6142-B750-CDF59676CDBA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D95A1976-E00D-8947-BDCD-10153E71CF97.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD476FC5-8B02-7042-B6BC-AE46A1E682C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DE855888-AB2C-0A45-AA00-7047629EB587.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E6C614A4-8AF4-3C40-AF0A-48CFA293F23B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/07DB5AA1-A7AC-2C4E-ADFF-506C860352B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0F6DAFF9-0DB7-044C-9140-2B325BC3A3FF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/135BB230-7DEC-EB44-AF5E-297F2320D27B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/17CFC88A-857C-F241-9FE5-56EF25D3F9C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1953014E-C112-A64C-A69E-5BA065053067.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1FA64386-3B5B-FA4D-889B-D404103960E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/257B067B-E1C5-8D47-B5E4-F1D4E02256A8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3A0B87D4-8C1F-B747-9605-B87738F2DD87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/412C8EE2-B36A-5B4E-AB73-18821459DE38.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/4C78E4DF-19D1-C84B-9496-61B3D6E225FB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/50A1C340-1EFB-9F46-9A01-E95B7C5B5B52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/57D0549D-A30A-E64A-8FD5-F3C1967D8814.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5DAFA1C6-2A0F-914F-A2CD-B8E61E6741FD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5DE42FFB-8A66-3449-B5D1-CFAAD11D5FD4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5FAC993F-B198-F842-B092-8CC9527CF063.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/67030A30-D163-CA45-AB03-AF0321C292C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/679172D8-C7A1-4144-B44C-31DA79274DB5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/68C4E06E-78F0-314D-835F-57C549E8F208.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6B9588FF-CDA6-294F-9623-BDFC79E5012F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/6C664846-4BE8-EE4D-B46C-FBC1832DE5FC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/70BC200C-10A7-B043-A163-FBCCE5080263.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/772B6A84-BB56-394A-9E24-15B25747E75A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/79AD09A7-49BB-3540-B169-57BB6295FA87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7D31DE87-2AFA-6241-B8A8-7DDB3ECB26CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/846D0F61-BE6B-C341-8712-A2D08D798EB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9366E641-E827-2944-90BC-D05CAEBCA458.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/98CF58F9-44F2-AF4D-8F77-564CFBBA5130.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9A8E820A-5ADD-C341-BB0A-0952E2D41ACF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9D964754-F445-DD41-9FA0-7B30398B5B47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A2A5A2C1-0EDA-8A48-A0FA-DC1F2A752874.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A3B15F24-5484-9D48-ACDB-98141A5CCBA7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A87B1717-2024-3F41-93F8-D93C913A9248.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/ABE2E81D-D6E9-1249-AFF0-AEC10D1CF1C0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AEA0FFDD-79C5-1540-9C2C-3CA64F8375CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B2DD21CB-D475-F142-8E30-03B460AF5BB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B690B19D-44DE-AE47-98E2-7394DD3DA5C2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/B69CC09F-42CC-8146-951F-A94170AC0DBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BC6962CE-D89B-AC4E-B95D-B552205D1E7D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C3B6821C-3C7D-BA4B-A67D-20886DCF00D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C475AFC2-1EDB-B842-A323-AE9DB5559E0C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C5DDC9AC-D092-7A4D-A46C-EEE32B9D2821.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D1C6F615-22B6-674D-81DA-5C9CC469D708.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/DC8117C9-EB04-1944-970C-DA6AD09CF5E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/DEE30F07-BDD1-474F-9697-D403FCEE1A05.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/DFB11793-1939-A34E-B8EF-B350618177EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E02A35EE-CF95-1B49-B73F-08F24AB72FE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E0756023-A0BB-9B41-B1DC-186341C10715.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E5ABF34D-2CD7-3745-92E5-B342C68F071D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/E9796240-CF1E-8343-B889-F2DCDF49558F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EA9A79E8-35EB-C346-BFB9-3187FCB4EB10.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EC264A4D-7A91-C84A-B8DD-406447DE1E54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/EF553D95-A324-4D41-920D-040E52E76E01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F2960A41-4DEE-4742-85A1-1769C607BCE7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F2EB0E54-D896-D04D-8F89-AC90970DE2CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F537B3CF-1953-B347-8667-557C27F0D845.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/FA512CF9-EC7B-3042-BDB2-D3E5FBFD3FDE.root',
] )
