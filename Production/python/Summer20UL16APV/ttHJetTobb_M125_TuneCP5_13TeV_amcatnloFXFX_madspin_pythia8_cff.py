import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/03638CF1-85F7-7947-9D4E-817F5B1D04E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/039B2A34-93A5-6749-BFAE-6B424C321F60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/17A9D02C-82A4-2C4A-9E20-51DB929BFFAB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/28BE1FEF-6410-9845-9C02-2BFF99AC1DBA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/4C715CC0-673E-6646-9303-303A6EE366B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/4D3831F8-2396-9041-99CD-F3F85A4C8524.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/772CDBD5-B568-904F-AAFF-DC1E85B61997.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/81115831-24F8-164C-92DE-2503513DF77D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/9CD438F5-F8DE-804A-A6E6-917B8C3F9CEB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/9E15FF33-61B1-FC49-8774-73BEC945FDC3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/AF5A9936-FBFE-8C41-8217-680BDFDCFF6F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/B44BF96D-96EE-5F42-A5EC-00F0FC202D26.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/C4955FA7-BB35-234C-9A2F-118314AF0827.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/C641988F-23E2-D845-BA21-6A643E88A1C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/FBE7C79F-4E8F-A943-A6D3-34D391B34397.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0B86E0C8-122F-8B48-A724-002608B7E86C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0F6929A0-F45A-1C44-8DC7-75B36C93530C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1837EF4D-15A4-064F-97E0-978B4617DC47.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/564172E1-7476-C047-94B6-92679E3B4E4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/69BEBCF7-C8B1-DA4A-87BC-8CF725F6ED76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8608D94B-9EA2-4640-814E-5B7D225EDAA5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8861E28F-5DD7-D548-8E7B-66DCBC28BC60.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/91EB86C5-4E3E-554D-9CA3-79C069EAFF94.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/98CF2DC1-1935-8449-ADF9-1452F889F0FE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/9B02A0DE-C6B7-434E-A283-BB0EB195DB8F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D17F4E9D-AB1B-9744-A4FC-3FB66C39F57F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D459945B-F9FE-9B4B-852B-99B21EC8E5FA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E88FD722-5139-B44D-9524-FC24573F08B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F87AB6CF-696F-724B-AC08-0C6FFFF9AE5B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/1801090F-B060-A240-A330-69D2401BA505.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3A8ABBFA-6D9A-394E-ACE4-90344127CDC1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3CD45D63-F22D-C445-A89C-C30D17B15369.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3D32DE07-9C67-5E46-A439-1D6F9DCA0DCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/3EDDBCCD-7086-D448-9442-F7BA18481D66.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/450771E9-5155-3941-81F1-048FB95B40C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/59603835-7FEA-CA42-9B36-DD62AE9DD655.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/71372106-0CE6-4A4B-A72E-99C22DFA1B3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7425A6FD-D83D-DB42-AAFF-7B417852C3F8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9CDD7C16-FD50-F544-BE63-9EC0B5E15080.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A4127C1E-139F-AD47-9F13-1F2F0E8694D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B176F011-5BEE-7F42-BE46-D29E663768F0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C1B7AF80-D961-9349-9437-904EB23E0CCB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C52618F8-50E6-7D41-992D-7D0BF160D7B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/C89A7D37-0238-2046-A294-139118685098.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CBCE2460-20F0-D141-984A-7B4B065CB14C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CFC0758B-9796-5648-8CAB-93BA8B023D8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D52AC6CD-1823-6744-88AE-55BA284C055D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/F0FBF771-4338-AA46-9F3B-6A1978A7C03A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0A0FCD47-DB4D-E04E-B733-47EA5A3CBCAA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0A6B9906-AA57-B148-A012-89A6617C6CBE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/130B832D-F247-0949-AA24-2FE53210406B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/1B27BAED-AE0D-9E46-B481-FD7D78739D49.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/23A99348-F3F5-A545-B463-C06D1C15DBFE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/25A2C473-B786-B64D-9883-48920AF53DBF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/27EA2921-008C-CC41-BAEA-3946C8B3EFB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A2ECAD7-C94C-FF4C-AD92-653CD60B1D4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2A5F62E8-D230-7D41-94CA-8D9FAD8B715C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/2ECDAC50-CF6F-8B42-BAEF-19947FBD99B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/37DE6FAA-C9B6-CE44-BE3D-AC3920BA01E2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/41AED2B3-4559-9A48-94F9-DFB0CD877148.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6140178A-FAAC-AA41-AB5F-813D429F03DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/61BADFC0-5120-204D-848F-0D29BEB1713F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/621B7C75-5AC2-2A44-8B99-9FF93A652589.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/6390097D-D0FD-EE4A-BEC3-648F3B1945EB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/72301844-2654-FC40-B9A6-9A4E138E39F5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8BF8176F-A594-8A4A-9297-1AF6F51D4DE6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8D1916C3-A329-D640-A8AF-44FD5B8DA269.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/993994F8-8F51-7E41-AA70-A6E1F32B6391.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/9AAF7969-A48A-8641-8F81-44F911044CBA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A1454138-1E26-A74C-B6D8-0ECADAC12BFB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A36897CC-3D07-A64A-8182-DEA4A165F979.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/A55753F2-8863-4D4F-82A9-8CF9DDBC9E22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B15C613C-711C-1A4F-9221-951FEA6CB4E7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/B3C3773B-4025-224F-B8D0-5213F277A519.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C720E3DF-11FD-CE41-ABAC-E6AD2455B2C7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/C8E19192-F03F-0B42-B881-F5EA39E94DD0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/CBEFE5F3-F7A9-8441-A5F9-CD6DC149215C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D39410C2-7489-CF42-8887-582297DB90E4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/DB63F8E4-FD42-EC44-A81B-B63F5FDF9F09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/E581BA0E-7C16-AD44-B073-7F13AC474E8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/EBBF2D62-9600-BC4B-9282-1C7510B08302.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/ED50F50F-20FE-3A44-866D-1EACABE9A678.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F77E0805-6459-564F-AF68-C747F7896F4F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/F988384E-9B47-204B-AE80-6BA6703162E5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/FC97F60B-7BEE-7C47-9F2F-EEE41BCCCF89.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/15187A07-133A-E843-935A-8AF5576FB6B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/1BC48199-62F3-7F42-A346-D8E075B061AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/1C09D380-D925-2E48-AED5-3D7579366C0B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/1CF3D6B9-FBA5-FE4C-A6FD-E18A04BCE250.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/206824A2-306C-1A43-871F-5975013EACBA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2D76DB22-9293-C540-B1EA-775BC951BFEC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/2F6856C1-204C-9543-91D5-2C45E47C3B30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/32A7980F-5146-EB4C-92B9-29562CD3CA13.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/34B51527-4186-2946-ABC4-43B955A94D0F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/3B2857B8-49BE-674C-9098-2F0E42665783.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/3D8DF8D9-2FF9-F844-B6CF-6C2A4D568FE9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/41A0C97B-9A2D-9040-B3CC-74BBA5D1AF4E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4869A941-178D-0645-81AE-E55B23BCE652.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/48890C59-F93C-BF4F-B668-109B633AC467.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4BDE04C9-3E03-D048-AA74-018F68B0B439.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4DE640AE-FBB5-DD4E-BA2B-4347E995A84D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/54311850-631B-2743-9ECF-6319E7FD1F39.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/573CEB58-45A3-CB43-B9A1-9C2FF150092B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/58FE15BC-C49B-A548-B37C-5FA36E1552DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5F73328A-856C-A24E-B623-62C5E88569CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5F90FCD7-227A-9741-9D4B-68F7E35AC830.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/5FB2FE2E-3141-1F4F-A15E-9F96CF36BBD8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/630E8BBC-24ED-B940-A7F6-A71A1F97C2D7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/75AD92C4-5B26-4941-8608-815D049FD32D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/763E0AE0-764A-E346-BD58-433F2CA71D54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/76AC060D-1F5F-F241-8D5C-A81BFC4FBEB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/85AC8EA2-6C7C-8148-8EDF-E49F87BFF6C9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/868DA413-CE31-4149-9923-19ED0DB71ACB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/8BE99D3A-EE08-7041-AA1C-1435CFAFAE9A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/93852D24-2785-7F41-A91C-B95E22F52624.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/939F2708-A2A2-694E-9978-ADFA9F09B093.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/98868455-05A8-0F42-BC0D-3477D5238C19.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A32B7D68-CFA5-284D-8AD7-99A10AAB91DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/A3AC3553-FE4D-FE4B-BF4E-4206FAECE866.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AAAC1EA0-901C-7F47-A251-E9C11F8ED55F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/ABE73589-0BE3-2A48-81CB-02F973E9327E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AD2B4D1D-A9C2-B44A-90B5-4EEEA6733243.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/AD4B7185-7972-0843-A56C-7C37FE20E151.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B3B69566-08B6-D444-B699-DFDDC48C8A9D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/B74D0986-AE89-6C45-947B-76E5D5B697A6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BA2AC76A-39E1-B949-8B09-602A7731B68E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BC5C4733-F633-B949-82EF-B26457677247.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BCD39FEC-74B2-9F49-912D-17FDE886194D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BD5D2640-BA82-324C-BE03-2C7382C7CA55.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/BE588D04-B61B-384B-B1A1-36027188F1B5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C1B6CAA1-4DD4-7444-B07B-962939D64B1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C3704B95-9E3B-1A44-811F-EBF5C5077724.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C3887B2F-AE9A-EC46-A18C-826EB91C1474.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C61C1D29-461B-F943-AA94-C759D2CD6117.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C89D6702-966C-8A45-A1F5-C4EFD01AED01.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/CE96B29B-B957-5148-B0CD-E15B405AB8B4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D031B7E4-2282-BE4E-99F1-032E4DC54074.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D75E916E-5CEB-E740-8686-4D15F8E0E812.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E644631B-7B55-9D4C-AFEA-62ACFEB7ED21.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/EE7D6323-3EFD-AE40-B494-C307A98BE1EF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/F595C618-7C84-DC44-B2BB-4C8E86A755C5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/076857D7-3D25-8040-989E-9EC8074CFCB7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/0E2C44CF-3812-0A4F-A70C-80DC5AFDADB8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/18136F2B-E289-F84E-8E23-F5627D42D2A5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/1CC698D0-D8AE-5145-ACB2-A953806D4A1D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/29221283-8C99-3949-8B1D-7003A58780A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/335D9544-7E0D-A743-B738-FB075D114040.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/360BE125-5754-5645-AFBA-61BFC25B8156.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/37A89A21-F473-7140-8B3C-1326A81D4664.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3F6FB6B4-FD68-2A47-BEB7-9EF22A7B98CE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/3FD76EA3-AB11-DD40-AF40-D0DE05C1F188.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/4F665191-E5ED-B944-8584-5CC05629B5DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/54063A26-2B3D-1D42-9B2B-1DB9D28E9D62.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/59DCBC8F-4F9A-BF41-9517-9E2154B86D30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/5CDA7B51-C0E4-3145-B510-2B708D60CD3C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/7069B00F-0108-B04F-96E1-843B7359430D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/80BC962A-4E61-AF46-9D92-AA1D6913BE08.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/92610E41-77A5-3148-81EC-1E0AD2B2AD40.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/959906DF-EFEC-1248-8793-81E6BAB8B0E1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/A798165F-3214-904E-B17F-452A72DC7A30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/AC52612F-FB4A-6F45-87A4-0A9A47122BC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/BA6E884D-D354-3340-87B9-D9CFBAA7237F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/C2686827-C099-0344-8D39-A71DC9FC7451.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/CA1AF895-BC1C-0643-94F8-86D6376FFA5C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/CDD5D1F1-75C8-6745-ADE8-72F5601E403F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D1EDDCE4-86FE-4D4A-A752-A48C13D98615.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D4C749B5-FE81-4840-97D9-D3C1899ECB87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D6397576-476A-D04D-8B6A-A16C21101F22.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/DE045B21-EE60-6F40-9E89-5E362E656AC1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/F4296864-0FFC-5F48-90E5-06B36EF0D598.root',
] )
