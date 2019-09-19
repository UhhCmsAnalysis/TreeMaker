import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/29C2DE0A-F874-474F-8DBF-9A5B99143AB9.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/34ACA25E-0750-7C41-B1F3-9C2B6BB9AD7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/3A9094F2-88DF-1F4E-AFE6-5833BB8E1E92.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/3ECA98DC-3D54-8D41-A423-4A4BE9F0F720.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/42A63E59-CFF0-244E-894B-BE34BED02600.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/47876B1C-0E6D-5B41-8830-137588D309C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/4CD613E0-7A9E-8C4F-B0FD-9E2F4B5538E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/4F4A4ADF-106B-2849-917F-FD98A3F00AE0.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/520EC7AD-9B15-6A4A-B64D-01C87C40A4A0.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/5DE8DDCB-CD91-8F43-A117-ACA21C066965.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/5FDEA9D3-9B12-FE47-8E38-3FC2DDCF42D7.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/62510930-4BAD-0740-AC28-C25AD08524C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/632AEB28-7969-0948-9334-13A41B55F96B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/7C037D72-D14D-D543-8A88-9736FA86A233.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/80772B2D-4E8B-024E-BB43-56EBE1F656CD.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/8480B388-A24E-8D4C-982E-854A72559E81.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/854EED46-4E59-A442-87B5-8972B44CC1D0.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/89261A80-005C-A349-B11E-940C6922D441.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/8FED1DC0-32EA-CF44-B71A-DCEA5633306A.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/98E05B95-FE95-464E-89B5-01B8E09F884D.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/A45BDF38-BA60-7E4B-9CBC-E82EE139E2DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/A502A600-2DA9-1F44-A9A5-6348F9162ED5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/A684104F-8334-9E4C-B14A-EA2BEFF72A5A.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/ABBB8509-E223-9247-80F5-0DC4ECC74FE1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/B65A632D-415F-5542-9117-6980F52DFB89.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/CF5E487A-D91B-DA46-8DCB-558D573795A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D23A7846-59A6-4543-8C25-12C4914C6B53.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D2D82EBA-51B2-9E46-B85A-FEDE757BCEC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D5F494A9-BF67-754E-BC29-5DEBF7E14F81.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/D734F0E2-F7C3-174E-8D1D-4FC3A7AB8BC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/DDD16F86-7108-CB40-930B-70BD986E8CE3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E2BB6550-CFB4-D046-BF91-8E06A25DF2C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/E32A9417-44FD-4B4C-AAC2-6437D9199713.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/F71C5633-DCB5-A245-93C7-3276D37AB8C1.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/FAD6DB02-933E-4A45-A1B5-5F0DE9E3ECF3.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/FCB8EBC2-1EC9-C148-8925-72F504193527.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/110000/FE985DAD-B338-CF45-8B64-B27351CA4350.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/146DF528-C876-8642-A498-9B1A67291ECE.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/29C7F609-68D8-1F46-AB1F-F8C355093819.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/336685F3-64C5-BC41-890D-F1154E2D8329.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/3B59FC6E-6570-9641-B3DD-470DB067E98C.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/40BDCBA8-8FD8-0244-A8CB-A59E5205FEA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/52E2CEA9-AD7C-0448-AEB5-EF16160A501A.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/585E616F-A5C5-2A49-9ED8-1F92AADFF0DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/72B169FC-2C00-5F41-BB06-13879C87CBFE.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/8B722E16-1CCC-E440-A21F-9F48AEA0A49B.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/8F9EA222-B019-E14D-990B-74DC59135FB6.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/97F1B5D7-E64A-8F49-871C-4C3321C95D31.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/9D531E15-44F4-4548-9280-0004781A9001.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/A41C4422-AC24-504E-9825-BEBD4BC11EBA.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/A5E87D32-E213-7A42-8E96-3DC8FFCA6983.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/BF1DC274-5046-324A-81F9-5E4A7F1A2517.root',
       '/store/mc/RunIIAutumn18MiniAOD/ZZ_TuneCP5_13TeV-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/80000/C0F0CBF5-E942-F840-8347-B6190D10EF7F.root',
] )
