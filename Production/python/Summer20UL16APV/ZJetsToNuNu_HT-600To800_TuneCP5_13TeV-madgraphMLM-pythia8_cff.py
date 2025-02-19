import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/71DAF64D-8C7A-D547-ADD8-178DDCA974A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/937D8D90-BBD4-8349-969B-2E80BCA7FF1B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/110000/F804914C-C46C-F949-9DF1-6078D0939F67.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/120000/49F07E4E-48D1-5943-AE04-D5C521465946.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/120000/6CB472C3-AA01-B04F-A195-A6CC7D1010C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/130000/12874AA5-0069-934D-B049-6F1DEE8B7F30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/130000/45D32083-FA69-684F-BA12-DD6478227162.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/130000/BD065183-7E96-CA4B-BA55-5AB1F2072531.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/130000/C48A2FB5-11A5-B940-93FD-B84EE052637F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/130000/DEDA5931-5ABC-D34A-A450-3BA2613B97B2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/31DAA3CE-D4F1-EA4A-8AC4-4AAB22D53714.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/B5A91000-A2B8-114B-BA4C-D45294548A1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/96444353-243B-6E43-9676-82F6C775A778.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/176D5B69-CA5F-524D-962B-B7C55C112FA6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/346A4418-45B7-AF4E-B8E7-38E8E97F2E56.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C173C95D-13F0-7A49-908C-A8642355AFF2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/F4BF7C76-2433-9142-B675-DC83C3E508C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/0D6FC374-B055-1049-8157-7196F550A9F6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/2A666C62-8F0E-B449-B397-74B554F8EF6D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/2D41C569-2092-B34B-B4B1-B8D3AF8A7273.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/3239CEFA-BC8F-4241-8754-E2E09D4033EC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/36A0FE8D-C4EA-4A4E-B47A-12DA73695F77.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/39748A2C-953B-AA49-9633-B277BF8FBD80.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/49D6724D-FE8D-864C-BB2F-23CEA42C32C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/84C7D13D-B980-2B4D-8A67-4CD2947CCB17.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/8EA97192-F59E-0A4F-B1B3-8AA5216D176E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/A32FD535-2436-B84C-9594-7E6DD326DE3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/A522983D-145F-4C46-841D-5F932A5279DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/B63B30EE-E982-AD45-8362-C8DD5B2962A0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/CDB421F0-EF26-8044-9631-D66AFA0808EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/CE403086-15C4-ED4B-BD47-891435B19AE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/D051FB24-0270-E84D-A2CD-52B9800020C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/D553CE6B-64C7-6040-B1AE-C7D10D7C0249.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/E78A80FD-9A9B-BE47-AF9F-80FDFDEF7773.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/FE5C5247-2307-F448-96D7-BB5000CDAFA2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/161D6C49-43FE-1041-A07D-3B34F0D4E508.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/407AD821-4D66-8048-AD7F-22039514D45F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/6AAD5FD9-7968-E343-8995-9D93B3B41534.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/76649FE9-E6A7-8A43-ABAF-B5770CF2A896.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/78FB390D-AAD2-C945-811E-89DF358E988B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/8DB62B40-007E-6B46-9EA6-1884E1F5A423.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/A9A9F04A-4A4E-4741-9FBB-428683556346.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/E9064775-6AFF-1848-8050-5B0CFC61D33F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/F4C79393-F44B-CB43-BAB0-1C82E17FA234.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/70000/F7B7B58D-7F6D-CA49-898A-ABFEA8D8A45F.root',
] )
