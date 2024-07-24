import paramiko
import io
import tkinter as tk
from tkinter import messagebox

hostname = "103.84.207.46"
port = 2222
username = "mack"
private_key = """
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAgEA24NwXSVAsXP3rmwWL/TspeKDxYzcK1Z6Q38okkjrZbdw031hSLxR
Yf641jD5nY4BcGdpLmEpNze2OGlsa4Mp9oyAEXX/Bb2CgaXLnmI75qqIAXRj288fXaG54s
GNNbd6B5/ixx5fiGpg3zu11BimYUVfstH75yEtV5eTZagjCwbQVcbv1+EcS5w1pdel223E
FXqvY5m26Cd4jY/6CYvEwoTxQJOLNrAgpVatvR8rBGrWwOuU12VBhP/xGnKHpD3eyr7Awv
eoRQkpE6JOs97Gm+CMEDy7kC8PA9bOp+p1rzxsp/zE30KetvBAuv4K4Pd209HkF3CqCouB
zwYW5SeBBERuYT4QG8SQKrwb0HoqGy/RH8McPzsiY9B3y/rZxnvQKkh5GaR0OuuqYiqaPr
Mo+q0jmgpBKhcnX3wd7bvSHGAlQKGSLyL3mAze6qb1TLaLxE0E/OVMweL9esI1ZEHDZ/w7
4eqMeFf7ok/SySCn4Nmn3dYQDk6hk2h8P2JtQcbjo7NnIMeKpEeXvHrWHuSzFeuFDKj/R0
wKms2imktiOZUYO4V2pyTqTVNMn1yblajra1jf3DKM/sTi/uWNF8TNtUKMAvM4Eg19mYd/
F3B36K9PFaSteI7Bx5lcTL1JQwFofIevl3jl9Zpk9og+YrqUgD5bNZQyKvbXl8Zt9KHL3g
UAAAdQ1zFWCdcxVgkAAAAHc3NoLXJzYQAAAgEA24NwXSVAsXP3rmwWL/TspeKDxYzcK1Z6
Q38okkjrZbdw031hSLxRYf641jD5nY4BcGdpLmEpNze2OGlsa4Mp9oyAEXX/Bb2CgaXLnm
I75qqIAXRj288fXaG54sGNNbd6B5/ixx5fiGpg3zu11BimYUVfstH75yEtV5eTZagjCwbQ
Vcbv1+EcS5w1pdel223EFXqvY5m26Cd4jY/6CYvEwoTxQJOLNrAgpVatvR8rBGrWwOuU12
VBhP/xGnKHpD3eyr7AwveoRQkpE6JOs97Gm+CMEDy7kC8PA9bOp+p1rzxsp/zE30KetvBA
uv4K4Pd209HkF3CqCouBzwYW5SeBBERuYT4QG8SQKrwb0HoqGy/RH8McPzsiY9B3y/rZxn
vQKkh5GaR0OuuqYiqaPrMo+q0jmgpBKhcnX3wd7bvSHGAlQKGSLyL3mAze6qb1TLaLxE0E
/OVMweL9esI1ZEHDZ/w74eqMeFf7ok/SySCn4Nmn3dYQDk6hk2h8P2JtQcbjo7NnIMeKpE
eXvHrWHuSzFeuFDKj/R0wKms2imktiOZUYO4V2pyTqTVNMn1yblajra1jf3DKM/sTi/uWN
F8TNtUKMAvM4Eg19mYd/F3B36K9PFaSteI7Bx5lcTL1JQwFofIevl3jl9Zpk9og+YrqUgD
5bNZQyKvbXl8Zt9KHL3gUAAAADAQABAAACAC13ZMFiOytWLAW8XP8bYZ29VFJJafvu+j17
O8XK5Tjo/S1M8aa9XLTpq9Kvi7Aqztj/jk1dMgp+F1fJXDvLi9hFgyw6rrL7bOnaE5nvWl
1dUnTMrPdFCAfefNA/CzbGVTf5kaDxBVQNxplONovi/Ck3E4qIDD80A756Bn1ejT2WMHYn
0Zs7BN+TUBhU2YVgz6WsRuIgHz6oGEPn/5/VC5DHtOmNdd8CrYxZbvx2VXRhhbApS2eu0R
qRYZi7AqXN69S+HFJ1texwqImoy1jdqnD0WkZtseK8IIXIyv6EJVKBtza3N/bPR2z4R8wD
XPD6SKo4deA2BX5QJXeiGQFnRIUhxN8Z+l4WnFqX5K9v601pGR6IkdhIwDcNXEwZyOHDdK
G9P38rGt1KfURW+QGkUpEUrfIothhGOUxOEXfT/gyL+IdtUniJgh1maECLtKx8tye4epXR
S5Vf4U01Q+fks17wBfYtRq0Pg3daA5/pNfyvDhmMZAi44UIdSBhL/jsfVU6Varw7RFh/2N
Zz9WbSW7lLkjE4bDTHrdyOrp23r/Bs/iP/pyNT/7kqH+nJ1avXpbPar60XmN2HQ+4XLYvO
B4YqiiJ3f+CUvnpSf8r7w9z+T26TwkPnmKMubC7LBDENFkWR/wxbyZtRO5TVh7apH0b76s
DnjVcAMETO06dqYbtxAAABAQDWBP1usHYT/GTE+KY2JE5zW5+Usu8rQSed+Xq2YMk0iXKC
tRaJ4DxQKyM4enGgl9UZ1MO+t9t6k9aGKSVMGGx5iWDYZHyq/zz1fuVMV0UYNzwg+QCPCh
fcmA8eE8Cjm6sSvmKnFBG6i9rgBZB5qxt27jPu4ZNiVf+SUIg9e3Ghb/YI+S8FwKN1mUI4
3+Dw4nwfe77Ao11arz4nhrCpKyk/z4ToHgu30n9WB2DG/0fYvHr6kXTsWNlyszk1mXjtPm
IKnW+Th+ndj5aYFS2fpk5EdBqIIo5EIIDqYippVNc1shEgfnKDkPL+iFBNLx1/6CYeg7T+
+ij5jCgV7QSyQSMYAAABAQDzH+S1tXSzEjzInhCxaTxnBUEi/NdYggmjOCgio0ZHXqPR/w
39S0xwtxEVwOD1+iEH+qKTdblS/1ZzN7sGCQyvvQcJuX4oK7w9t/DDbbqYZlfqPtLDt/Ol
lFbW/U2xfA29lqEIDyrUcRj9bXH5WusosNLmhCCnIvq3VEqpq8y9mZS6DZ2KIC8mug4Y/2
vPid5eknhLmVFFbGXNTI3igvStsN52gh75ojmvEZEefZ6mgJdlnjI5+ASaWsx/62XvzZdq
ntK9o4VRr6Bukc0YX+mOQvn3t3ughZDziEApBvh39oMjEeNYFuRYFD1GHLCF0j4wzUy41o
B/b3A3xst0ml4VAAABAQDnI3FUEBAlzyIujZbizsD9F6v+if3VT9AY8KYZ90iibE6XASUu
hrJqlscVeW6JT7urION1+pzIS2ySVeE17ULHRI8ysmVFCGhuw7iJoM9qxfa+fX6NVdwWhQ
bYlrdRVfOg/l53NiLFQD40tQgUcEfFRWQ3LVjdrqP1rCX2JY4bwi8YtODOJRfLi4xawoAv
pKqqoKZHaOifshz7tlwaYvAAPEP+YUxXHAS6C22jLgP1sPEb060kxk+ED/P9YAvFMxu3RB
15jn6RataUp83KulAsY0hHYh+w18cwRGFPV8Z4RveqxSjuZODlxmPQf8WWSSuXt6OXLpnK
JFdrkOqhE2wxAAAAGXNjcmlwdHNob2d1bkBzY3JpcHRzaG9ndW4B
-----END OPENSSH PRIVATE KEY-----
"""


ascii_arts = [
    """






                                ,sARRAs,
                                ,ARRRRRs,
                                cARRRRRRRT, ,
                                ,CTARRRRRRRA  ,,,,
                                ,saCARRRRRRRAc  ,,                                ,caas,,
                                ,cscaTRRRRRRRRAsc,,,,,                       ,caCTRRRRRAa
                                ,ccccaTRRRRRRRRRTc,            ,,,,,,,,      cRRRRRRRRRAC
                                ,cccccaTARRRRRac,,,  ,,,,,, ,,,  ,,,,  ,CRRRRRRRRRRRRATTT
                                ,ascccsaTRRRac, ,, , ,       ,,   ,,,ARRRRRRRRRRRRRTaac,,
                                ,CaccccaTRRa, ,,,,,,,           ,,,,cRRRRRRRRRRRRATacc,
                                cRAccccssc,,,,,,,,,,,,,,,,, ,, ,,,,,,,cARRRRRRRACsc,cc,
                                cRRsccccc,,,,,,,,,,,,,,,,,,,,  ,,,,,,,,sARRRRATCsc,,cac
                                ,caCCscc,,ccccc,,,,,,,,,,,,,,,,,,,,,,,,,,cTATCsc,,,,cc,
                                  ,CTscc,cccccc,,,,,,,,,,,,,,,,,,,,,,,,,cccccc,,  cs,
                                  ,aCcc,ccsccc,c,,,,,,,,,,,,,,,,,,,,cccccccc,,,  ,sTs
                                ,cscccaRRC,sAAac,,,,,,,,,,,,,ccccccc,ccccccccc,,cac,
                            caacccc,,,sRRRRRRAac,,,,,,,,,cARRRRRRAscccc,cc,cccaac,
                            sATaccc,,,cRRRRRRTsc,,,,,,,,,cRRRRRRRRTaccc,,,,cccCC,
                            cCCsccccc,  ,TRRCc,    ,   ,,cCRRTTRRRRRc,ccccc,,ccc,
                          ,caCasscccccc,,casc,          ,,cTRRRRRRRAc,ccc,cccccc
                        ,cCATTCCasscccscc,       cTAc     ,,sARCssc,,,,,c,,,ccccc,
                        cCTATTTTCCaaasccc,,,,,,,,cRRs  ,,,,    ,cccccccc,,,,ccccsa,
                         ,sATCTAATTCCCaascc,,,,,,,cc,,,,,,,,,,caCCascccc,,,,c,cccc,
                          aRAAATTTTCCCCCsscccc,cccccc,c,,,,,,,,ccccc,,ccccc,,,,,cccc,
                          cCCaCTTTTCTTTCaaasccccccccccccccc,,,,,,cccccccccc,,,,,,,ccc
                              cCTATATATATTCassccssccccccccccccccsCTTTCsccccccccccccccc,
                                ,TAAARRATTTCCaasaassccccccccccccccccccccccsscccccccc,
                                 cccsARRAATTTCaaaaaaasaassssssssscccccccccccccccccc,
                                     ,sCTAAAATTTTCCTTTTTTTTTTaTTTTTCaasssssssc,,,,
                                       caARRRAAATTTTTTTTTTTTATATTRRTCaaCCaaCCs,
                                  ,CCscccccsaaaTAATaaCaaaTTTTAARRRRRAAAAAa,
                                  ,TACscccccccccaaaasaaaaaCaaac,
                                  ,CACscccccccccccsssssssssascc
                                  ,aCTCsccccc,cccccccccccccccccccsc,
                             ,,,, ,csTTaccc,,,,cccccccccccc,cccccccc,,,
                      ,,, ,,,,,c,,,,cTTCccc,,,,,,,,,,,,,cccccccccccc,cc,
                      caCCscsssccccccCCscc,,,,,,,,,,,,,,,,,cccaCCc,,,,
                     ,cTRRTCTACsssscsCCscc,,,,,,,,,,,,,,,,,ccaTRRs,,,
                     ,TRRRRRRRRATAATTTCcc,,, ,,,, ,,,,,,,,,,ccsscc,,,
                     ,sCaCCTARAsssCTACacc,,,,,,,,,, , ,,,cccccccc,,,
                                  ,CTacc,,,,,, , ,,,,  ,caaasccc,,,
                                cAACscc,,,,,,,,,,,,,,,  cCCCsccccc,
                                ,AACscc,,,,,,,,,,,,,,  ,cATassccccc
                                cTAascc,,,,,,,,,,,,,,  ,cTACCaascc
                                ,TTascc,,,,,,,,,,,,,,, ,cACscccc,
                                ,CTascccccc,,,,,,,,,,,,,sTac,c,
                                ,aCaccccc,,,,,,,,,,,,,,,,,,,ccc
                               ,caCssccccc,,,,,,,,,,,,,,,,,,cc,
                              cAAascccccc,,,,,, ,,, ,,,,,,,c,
                              cTCsc,,,,cc,,,,,,,,,,,,,,,,,cc,
                       ,cCCaasCTCsc,,,,,cc,ccccccc,,,,,,,,,cc,,
                       ,ARRRAAACasc,,,,,,ccsCTTCascc,,,,,,,cccccssscscsscaCc,
                       ,CRAAATTCscc,,,,,,ccCAAATTac,,, ,,,,,,csARRAAAARARRRT,
                          aAAACacc,,, ,,,,csAAAACsc,, ,,,,,cc,sARAAAAAAAAa
                 cARAARAAAAATTCacc,  ,,,,,,caTAACcc,,, ,,,,ccccccccTAAARRs
                 cTTTCCCCCTATTCscc,, ,,,,,ccCARRCcc,,, ,,,,,,ccccccaTAARRTc,c,
                          sTTCasc,,,,,,,,,caARRRTc,,,   ,,,,,,,cccc,csTAAAAAAC,
                     ,CTasCTCCscc,,,,,,,,,caAARAaccc,,  ,,,,,,,,,cccccsssc,,,,
                      ,cCTCscc,,,,,,,,,,c,cARRATCascc,,    ,,,,,,,,,,cccc,
                        sCsc,,,,,,,,,ccccccTRRAAATCascc,,,,,,,,,,,,,,,ccc,
                        sCsc,,,,,,,,cccccccCAAAAAATCasssccccccc,,,,,,,ccc,
                       ,CTs,,,,,,cccccccsRRRRAAAAAAAAAAATasccc,,,,,,,,ccac
                       ,TAacccccccccccsTRAACcCARRARARRRRATCaaasc,,,caaaTAs
                       ,cCTTTTTTTTTTCcsARc   ,sCaCaaaasaTARAARAasssaaCCCCc
                          aRRAAAAARRC                   cRRAAAAARRA,              
                                           
    """,
    """
    



                             ,cCsc,
                            ,aRRRRA,
                            cRRRRRRRRs,   ,
                            sRRRRRRRRRsc,,,
                            cTTARRRRRRRRRs  ,,,,                            ,, ,sARRC
                            ,sssCARRRRRRRRRA  ,,,,,,,,  ,,          ,,,,,  cRRRRRRRRRRs
                            ,sscsTARRRRRRRRRACsc, ,,,,,,,,             ,csCRRRRRRRRRRRa
                            csc,csaTARRRRRRRRRTs,    , ,, ,,,,,,   csaCARRRRRRRRRRTaCRa
                            cCc,ccsaTRRRRRRRCcc,,    ,,,,, , ,,   ,TRRRRRRRRRRRRAAssaAs
                            sRC,,,ccaTAATCsc,,,,,,,,,        ,    ,caRRRRRRRRRRascc,,,
                            CRTc,,,ccaasc,,,,,,,,,,,           ,,,, ,sARRRRRRTsc,,cc,
                            aRTc,,,cssscc,,,,,,,,,,,   ,,  ,,  ,, ,,,,cTRRRAAsc,,,cac
                              cCaccaascc,,,,,,,,,,,,,,,,,,,,,,, ,,,,,,,,csaacc, ,,sCc
                              cATssaascc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccc,,  cscc,
                              ,csaassccc,c,,,,,c,,,,,,,,,,,,,,,,,,,,,,c,,cc,, ,,cc,
                                ,sscccccc,csTCcc,,,,,,,,,,,,,,,,,,,,,,cc,cccccss,
                              ,cssccccccccsRRRCcc,,,,,,,,,,c,,,,,,,,,cc,cccccsCC,
                          sTacccccc,cccsCRRT,aRRCc,,,,,,,,,,,cTRRRRAsccccccccc,
                           ,ccc,,,,,,,,,sRRRRRRAsc,,,,,,,,,,CRRasRRRRRscccc,cccc
                            ,cc,,,,,,,,,cRRRRRTac,,,,,    ,,TRRc CRRRRs,cc,,,css,
                       ,CTCscccccccccc,,, ,,,,,,  ,    ,    cTRRRRCRRR,,,,,,,ccc,
                      csTTCsscccccccccccccc,,,,,            ,caTAscCAs,,,cc,,cccc,,
                      csTTCasassscccccccccc,, ,,,  ,cc,,,,,       ,,ccccccc,,cccss,
                        CATCCCaassssscccccc,,,,,,,,,sCcc,,,,,,,,,,ccssscccc,c,cc,,,
                       ,CAATTCCCaaaaassssssccc,,,,,cccc,,,,,,,,,,,,,,,,,,c,cccc,,,cc,
                           ,sAATTCaCaaaassssccccccccssccccc,c,,c,csaTCCCCascc,cccccs,
                            cCTTTTTTTCaaaassssccccccssccccccccccccsaTTTTTCsccccccccc,
                              cTATTAAAATATACaassccccsasccccccccccccccccccccccccccc,
                                  ,TRRAARAAAAATTaaaaaaasaasaasaaaaaasaaassaCCs,
                                   ,caAARRRARAAAATTaaTAaAaaaAaCCTTATTTTTACc,,,
                                 ,, ,csaAAaAaTAAATAATTTTTAaATAAAAsccccccs,
                                ,ccccccccccccssaaaTAaaaAaaaTTaTAC,
                                 ,cssssccccc,ccccccsssssscssssc
                              , ,,caCCascccccccccccccccccccccccc,
                             ,,,,,,sCCCascccc,,cccccccccccccccccc,
                     ,csccccccc,,,,csTTCscc,,,,,,,,,,,,,,,cc,cccccc,
                      cCTTTTCscccccccCTCscc,,,,,,,,,,,,,,,,c,cccccc
                     ,TRRRRRRRAasascsCCacc,,,,,,,,,,,,,,,,,,ccccc,,,,,,
                     ,csccccaacc,,caCCscc,,, ,,,,, ,,,,,,,,ccccc,,,csasc,
                                  ,aTCscc,,,, ,,,,,,,,,,, ,cc,,,,,caTTsc,
                                cCTCaccc,, ,,,, ,,,,     ,cATc,,cTRAACccc,
                                cAACscc,,,,,,,,,,,,,,, , ,cTCc,csARRTaccc,
                                cCCscc,,,,,,,, ,, ,,,,,,,,csscccsARRACcc,
                              cAACaccc,,,,,,,,,,,,  ,,,,,,cCTCaaCCTRRTc
                              cAACscc,,,,,,,,,,,, , ,,,,,,cTATCCCTTRRs
                              cTTaccc,,,,,,,,,,,,,,,,,,,,,,caTAATc,,,
                              cTTsccc,,,,,,,,,,,,,,,,,,,,,,,ccccc
                              cTTscc,,,,,,,,,,,,,,,,,,,,,,,,,
                              cTTsccc,,,,,,,,,,,,,,,,,,,,,,c,
                              cTCsccc,,,,,,,,,,,,,,,,,,,,,cc,
                             ,cCaccc,,,c,,,,,,,,,,,,,,,,,,,c,
                            sAAacc,,,,,cccccccsssccccc,,,,,,ccc
                            cATscc,,,,,ccccsaCCCasscc,, ,,,,cc,  cCaaaaCCc
                     ,sCasscaTCsc,,,,,,,cccaAAAACCacc,, ,,,,ccc,,TRRRRRRRT,
                     ,ARRRAAATasc,,,,,,,cccCAAAATCasc,,  ,,,,ccccTAAAAAAAa
                        CAATTascc,,,,,,,cccCAAAACCacc,,   ,,,,cccccccCAs
                   cAAAAAAATTasc,,  ,,,,cccaARRRACaccc,,  ,,,,,,,,cccCRRAAARRA,
                   cCARRAAATCCsc,, ,,,,,cccCRRRRACascc,,,  , ,,,,,,,caTTCTTTTa,
                     ,TRATTCCscc,,,,,,,cc,cARRAAAACacccc,,, ,,,,,,,,,cc,
                     ,ARATCCascc,,,,,,cccccTRRARRRACssccc,,,,,,  ,,,,cc,
                 cCATs,caTCscc,,,,,,,,cccccCAAARRRAATCCaascccc,,,,,,,cc,
                 ,csc,  sTacc,, ,,,,,ccccccaAAAAAAAAAATTCssssccc,,,,,csc
                       ,sTscc,, ,,,,cccccccCAAAAAAAAAAATCasssccc,,,,,sCc
                       ,TRCccc,,,,,,,cc,cRRRRAAAAAAAAAAATassccc,cccsaARa
                       ,ARCccccc,cc,ccsTAAATsscCARRAAAAAAATTCaaaCCCTTTac
                        sCCaaCaaaaaasccARc      sCaaaaaaCaCaCCCCCCCCC,
                          aRRAAAAARRT

    """,
    """
    



                         ,                                                ,,cc,
                        cs,                                              ,TRRRRs,
                     ,sARRRRRRa,                                     ,cARRRRRRRT,
                     ,TRRRRRRRRsc,,,                              ,,,sTRRRRRRRRT,
                     ,TRRRRRRRRRRRRc  ,,,,,, ,,,,,,,, ,,,,,,,,,,, ,RRRRRRRRRATTT,
                     ,TTCCTRRRRRRRRRRRTc   ,,,,  ,,, , ,,,,,  ,,CRRRRRRRRRAsssTT,
                     ,TTssCTRRRRRRRRRRRRAc, ,    ,, ,    ,,   cARRRRRRRRRTac,cTAc
                     ,TAsccsCTARRRRRRRRRRT, , ,   ,,   , ,    sRRRRRRRRACs,,,,ss,
                     ,ARscccssTARRRRRRAACc,,,,,,   , , , ,,   ,caTARRRATsc,,,,,
                     cRRac,,,csCTRRATsccc,,,,,     ,  ,,      ,,,,csTTCs,, ,CC,
                      ,casc ,,,saCCsccc,,,,,,,,           ,    ,,,,ccc,,  ,,,,
                        aTc,,,ccsssscc,,,,,,,,,,,, ,      ,    ,,,,,c,,, ,c,
                       ,TAs,,,csssscc,,,,,,,,,,,,, ,,,,,,,,,,,,,,,,,,ccccsTa,
                        cssscccsssscc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccc,
                          ,ccssssssccc,,,,,,,,c,,,,,,,,,,,,,,,,,,,,,ccccc,
                           ,csssscccccccc,,,,,,,,,c,,,,,,,,,,,ccccccccccc,,
                          ,ssscsccccccccc,,,,,,,,,,,,,,,,,,,,ccsssccc,,,ccc,
                        csscccccccccccc,sRRRRRac,,,,,,,,,,,cARRRARRRsccc,cccsc
                     ,caCascc,,,,cccccTRRAcCRRRRc,,,,,,,,,cTTaaARRRRAsc,,,,cas,
                     ,TACscc,,,,,cccccARRT ,ARRRs,,,,,,, ,cTa,cARRRRTsc,,,,css,
                     ,TACscc,,,,,,,,,,,,sRRRRRRR,   ,       sRRRRRTc,,,,cc,cccccss,
                    csCCsscccccccccc,,, ,CRTcsTs,           ,aTATsc,,,ccc,,,,cccss,
                 ,caAACsssccccccccccc,,,cc,,       ,,ccc,,       ,cc,ccccccccc,,,,
                 ,sassCTasssssscccccccccsssc,,,,   ,csssc,,,,,,,,sassscccccsCs,
                     ,CTCassaassssscccccc,,,,,,,,,,,,,,c,,,,,,,,,caTTTaasasaTC,
                     ,TRAATTTCCCaaasssssscsccccc,,ccccccc,cccccc,ccssCCc
                     ,aTTTaaTATTTCaCaaassasssccccccccsscccccccccccccccc,
                            cTATTAATTTTTTCCassssccccssssscccsccssas,
                                cARAARRRRRATTCTCCsasaaasCCCCCTAAT,
                               ,cCTCCCTCTARRAAATTTTTTATTAAa,,,ccc
                             ,cscccccccccsTCCCCCCCCCCCCCTTc
                            ,ccccccccsscccccccccccsccccccccccc,
                          ,c,,,,,cccssscccccccccc,cccccccccccc,
                        csc,,c,,,,csssssccc,,,,,,,,,,,,,,,cccccc,
                       ,aCc,,c,,,,,sssssccc,,,,,,,,,,,,,,,,ccccc,
                        aTasc,,,,cccssascc,,,,,,,,,,,,,,,,,ccccc,
                        CAac,,,,sTTCaasscc,,,,,,,,,,,,,,,,,cccc,,
                        ,c,csTc cARACsscc,,, ,,,,,,,,,,,,,,cc,,,,
                          cCCs, ,TACascc,,,, ,,, , ,,,, ,,,,,,,,,,,
                          CAc   ,TTCsscc,,,,, ,,, , ,,,,,,,cc,,,,,,
                                ,CTasccc,,, ,,,,,,, , ,,,,cCscc,,,,,
                               ,cCCsscc,,, ,,,,,,,,, ,   ,cTTscc,,,,,
                              cAACssccc,,  ,,,,,,,,,,,   ,cCTAATTs,,,
                              cTTassc,,,,,,,,,,,,,,,,,,,,,,,cCARRTc,,
                              cTTssccc,,,,,,,,,,,,,,,,,,,,,,,,ccsscc,
                              cTTsscc,,,,,,,,,,,,,,,, ,,,,,c,    cac,
                              cTCscc,,,, ,,,,,,,,,,,,,,,,,,c,    ,ccc,
                              ,TTsccc,,,,,,,,,,,,,, ,,,,,,,c,      cs,
                            sTATasccc,,,,,,,,,,,,,,,,,,,,,,c,
                            sRATasscc,,,,,,,,,,,,,,,,,,,,,,c,,
                            sATCsccc,,,,cc,cccccscccccc,, ,,,sc
                            sTTssc,,,,,,cccsCTTTCCsscc,,,  ,,cc,
                            cTTscc,,,,,,cccaAAAATCascc,,, ,,,,caCCCTTc
                        csssCTasc,,,,,,,,ccCRRRATCsscc,,,, ,,,csTRRC,
                       ,TRRRACacc,, ,,,,,ccCARAATCsscc,,,,, ,,,,sTAc
               sRRRRRAAARRATTasc,,,,,,,,,ccCARAATCsccc,,,   ,,ccsTRRARRRRT,
                 cARAAAARATTCssc,, ,,,,,,csCARRRRTsccc,,,,,  ,,,sARRRs
                ,sRRRRRAAATTCscc,,,,,,,,cccCARRRRACsccc,,,, ,,,ccsCTC,
               sAATRRRRATTTCssc,,,,,,,,ccccTRRAAAAATCasscc,,,,,c,
                ,, sRRRATTCascc,,,,,,,,,ccsARRAAAAATTaasscc,, ,c,
                    ,sRRACascc,,,,,,,,,,c,cTRRRATTTaasssccc,,,,,cCC,
                      ,sCTCsc,, ,,,,,,cccccaARAAATCasccccc,,,,,,,cc,
                        sTCsc,,,,,,,,,ccccsCARARAATascccc,,,,,,,,
                       ,TRTcc,,,,,,,c,ccsTRRRRRRRRRACccccc,,,,,,,
                       ,ARCcc,,,,,,,,,csTasssTAAsaARATCaaasasas,
                        sCCaassssssssssTa,        cCCCCTCCCTTTs
                          aRRRRRRRRRRRT,

    """,
    """


                                                                      ,,
                                                                 ,caTAAs
                                                               ,CRRRRRRC
                                                           ,  ,RRRRRRRRc
                                                       ,,   cRRRRRRRRTCc
                                                      ,,,, ,TRRRRRRRTCs,
                 CRRRRRTc,,,,,         ,,,,,,,,    ,,,,   TRRRRRRRAaccc,
               cARRRRRRRRRRRa,   ,,,,,,,,,,,,,,   ,,,  ,RRRRRRRRRAac,cc,
               ,sTRRRRRRRRRRRATTs,,,,,,,,,,,, ,  ,,,,, ,CRRRRRRRACs,,cac
                 ,CTARRRRRRRRRRRRRTc,,,,,,, ,,,,  ,  ,    sRRRRACc,,,sAs
                 ,CCCTARRRRRRRRRRRRCc,,,,,,   ,,, ,,,     ,csaCCCc,,,aAa
                 ,asccsCTARRRRRRRRTacc,,,,  ,, ,        , , ,,,cc, ,c,,
                 cACc,,ccaCARRRRTsccc,,,,,, , ,         ,, ,,,,,,,,aTc
                 sRTc,,,ccaTRRAacccc,,,,,,,,,,,  , ,,,,,, , ,,,,,,cCTc
                 sRAs,  ,,csssssccc,,,,,,,,,,,,, ,,,,,,,,,,,,,,,ccc
                 ,sCTa,  ,,ccsccccc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccc,
                   ,aac,,,,ccssccc,,,,,,,,,,,,,,,,,,,,,,,,,,ccc,c,ccc,,
                      cacccsssscccc,,,cccc,,,,,,,,,,,,,,,,sTAARRAac,cccc,
                     ,aCscssssccc,,cccccc,,,,,,,,,c,,,,,,cTRRRRRRAccc,ccsc
                     ,sCscccccccccc,cccccTATscc,,,,,,,,,csccaARRRRcc,,,cccc,
                      saccccccccccc,ccCRRC,CRRsc,,,,,,,,,cTRRRRRRa,,,,,,,cccc,
                     ,saccccccc,,c,ccsARRC CRRCc,,,,    ,,TRRRRRAc,,,,,cc,,,cc
                   ,TTacc,,cccccccccsTRRRRRRTsc,,      ,        ,,ccccccc,
                   ,TTasc,,c,,,,,,,,csCTRRRRsc,,               ,,ccccccssc
                 ,caTCascc,,,,,,,ccc,,,,,sTac,     ,sCc,,,,,,,,ccssccsas,,
                 cAATCacccc,cc,,ccccccc,,,, , ,,,  ,TAa,,,,,,,,,caTCacc,
                 cTTCascccc,,,c,,c,,,,,,,,,,,,,,,,,,ccc,,,,,ccccccaCCc
               cTATTTCCasccccccccccccsssasscc,,,,,cccccccccccccsc,
               cTTaCTTCasccscssccccccssaaaasccccccccccsscccccsccc
                   ,aTCCCCCCCCCCaaassscccccsccccccccsssscssaCCs
                     ,CAATTTTTTTTTTTTTCCaCaaaaaasssaaaCCAAARa
                      cccccc,,aARAAAAAAAATTTTTTTATATATACCCCTc
                              cTTTTTTTTTCCCCCCaTTTCTCCasccccc,,
                          ,,,,c,ccccccccccccccccscsscccccccccsc
                        ,,,,,,c,ccccccccccccccccccccccccccccccc
                        ,c,,,,,,cccccccccccccc,,,,,,,,,,,,,,cc,
                       ,cc,  ,,,,ccccssccccc,,,,,,,,,,,,,,,ccc,
                     ,aCc,, ,,,,,,,csassccc,,,,,,,,,,,,,,,,ccc,c,
                     ,ss,,,,,,,,,,,ccssscc,,,,,,,,,,,,,,,,,cc,,,,
                       ,,,,,,,,,,,,,,sascc,,,,,,,,,,,,,,,,,,,,,,,
                        cascc,,,,,,,,cccc,,,,,,, ,, ,  ,,,,,,,,,,
                       ,sCacc,,,,,,,,ccccc,,,,,,, ,,,,,  ,,,,,,,
                         ,sTCsc,,,,,ccscc,,,, ,,,, ,,,, ,,,,,,,,,
                          ,saCsc,,,ccssc,,,,,,,,, ,,,,,, ,,,,,,,,
                            caTCaccaascc,,, ,,,,,,,,, ,, ,,cc,,,,cc
                              cAATCacccc,,,,,,,,,,,,,,,,,,cCac,,,cc
                              cTATaasccc,,,,,,,,,,,,,,,,,,casc,,,cc,
                              cTTCasccc,,,,,,,,,,,,,,,,  ,,ccc,, ,,
                              cTTCaccc,,,,,,,,, ,,,,,,,, ,,ccc,,
                              cTTasscc,,,,,,,,,,,,,,, ,, ,,csc,,
                              cTTascccc,,,,,,, ,,,,,,,,,,,,csCTTa,
                             ,sTTCssccc,,,,,,,,,,,,,,,,c,,ccscsas,
                            aRATCaccc,,,,ccccccccccccccc,,cc,
                            sATasscc,,,,,ccsCTTTTCacccc,, ,c,
                            cTTascc,,,,,,ccaAAAATCsscc,,,,,c,
                      sassssTTCscc,,,,,,c,cCRRRACasccc,,,,,,,,,
                     ,ARRRRRATCsc,,, ,,,,,caRAATCascc,,,,,,,ccc
             aRRRRARARRARAAATCasc,, ,,,,,ccCAAATCaccc,,,,  ,cARRRRRc
            ,TRRRRRRRRARARATCCsc,,  ,,,,,ccCTAATCsccc,,,,, ,sRA,
             caARRAAARRRRATTCasc,,, ,,,,cccCAAATTascc,,,, ,,sas
              ,aRRRRRARATTTCacc,,, ,,,,,,csCAATATTaacc,,, ,cc,
             sARRRRRRARATTCCacc,, ,,,,,,cccCAATTTTCCscc,, ,caTs,
             ,c,,ccCRRRRTCaacc,  ,,,,,,,cccCATTCCCaasccc, cTRRA,
                    ccccaCac,,,,,,,,,,,ccccTRACassccccc,  sRRs,
                        sCac,,,,,,,,,,cccccTRRTascccc,,, ,sRC
                        sCsc,,,,,,,,ccccsTRRRRRAacccc,,,ARR
                      ,sTTs,,,,,,,,,,,caTaaTRTaaTTCCCCsaRRT
                     ,aACaassscsssssssaCa,      sTTaTCTTs,
                          aRRRRRRRRRRRA,

    """,
    """



                                                            cTCc,
                                                          sRRRRRT,
                                                        ,sRRRRRRC,
                                                       ,RRRRRRATs
                                                     ,,aRRRRRATac
                                                ,,,  cRRRRRRACscc
                                              ,,   ,RRRRRRRRCc,c,
             ,sss,                            ,, ,CRRRRRRRRAs,,,,
            cRRRRRRATasc,,,,,,   ,,,,,,,,, ,,,   cRRRRRRRRAac,,cc
           sARRRRRRRRRRAc,        ,,  ,,,,   ,   ,,c,csTARAsc,,cc
          ,TRRRRRRRRRRRRRRRRRRRAs, ,,,     , ,        ,,ccc,, ,aC,
           ,,sTTARRRRRRRRRRRRRRTc,,,,, ,    ,,    ,,,  ,,,,,,,cTT,
             cCCaTARRRRRRRRRRRRc,,,,,,,,,    ,   ,, ,,,,,,,,,,cCa,
             cacccsCTARRRRRRRsccc,,,,,,,,,,,  ,,,,,,,,,,,,,cccc
             CAacccssCTARRRRCcccc,,,,,,,,,,,,,,,,,,,,,,,,,,,ccc,,
             cCsc,,,,csCTTsscccc,,,,,,,,,,,,,,,,,,,,,,,,,cccccccc,,
               cTs, ,,ccssssccc,,,,,,,,,,,cc,,,,,,,,,,,caRRRRACc,cc,
               CRT,   ,,cssscccc,,,,ccc,ccc,,,,,,,,,,,,sRRRRRRRs,,ccc,
                ,sTs,,ccsssccccc,,cccc,,,,,,,,,c,,,,,,sCc,cRRRRa ,cccc,
                  ,csssssccccccccc,cccCRRRRAc,,,,,,,,,,sTRRRRAs,,csc,,ccc,
                   ,sCssccccccccc,ccsCRRRRRRs,,,,,  ,,,,ARRRRc ,,ssc,,ccc,
                   ,cscccccccc,,,cccARRc aRRRT,    ,          ,CTsc,ccc,
                    csccccccc,cccccsARRRTRRRTc,               ,ssc,saas,
                 ,,cssc,c,ccccccc,ccsTRRRRTc       ,sCc, ,,,,,cccccaTs,,
                 cATsscc,,,,,,,,,,ccc,,,c,,,  , ,, ,TRa,,cc,cccssssc,
                 cTTascc,,,,,,,,ccsaaCCTTac,, ,,,,,,ccc,ccc,cccccss,
                 cTACacc,,,,,,,,,,ccc,,,,,,,,,,,,,,ccsccccccccsCa,
                 sTTCsccc,,,,,,,,,,,ccc,,,,,,,c,,,ccssccccccssaCs,
               sRATassccc,,cccccccccsTTascccccccccccssscsssCCAs
               sTTCCCassscccCATTasccccccccccccccccsssaCTCAARa
               ,c,,saCssssssCTTassssscscssassssssaCCTTAAaccc,
                   ,TATTTTTTTTTCaCCTTTATTTAATAAAATTCTTTTc
                   cTRAAATTTTTTTTTTTARRAAAAAAARRAACaCCassc,
                              sRRRRRAscsssaaaCTCaasscccccccc,
                             ,cssssssccccccccccccccccccccccc,
                            ,cc,cccccccccccccccccccccc,,cccc,
                          ,,,,,ccccccccccccccc,,,,,,,,,,,,cccc,
                          ,,,,,cccccccccccccc,,,,,,,,,,,,,ccc,
                        ,,,  ,,,,,,ccsssscccc,,,,,,,,,,,,,,,,
                        ,c,,   ,,,,ccssssscc,,,,,,,,,,, ,,,,,
                        ccc,, ,,,,,cccsssscc,,,,,,,,,,,,,,,,
                        cs,,       ,,,,,,ccc,,, ,,,,, ,,, ,,,
                        ss, ,       ,,,,,,c,, ,,,,,  ,,   ,,,
                        ,c,,,,,,,,,,,,,,,,,,,,,,,,   , ,,,,,,,
                          cCaascc,,,,,,,,,,, ,,, ,,,,,,,, ,,,,,
                           ,aTTssccc,,,,,,c,,,,,,,,,,, ,, ,,,,,
                            sAATTCassscccc,,,,,,,,,,,,,,,,,,,,,
                            cAATTTasssssc,,,,,,,,,,,,,,,,,,,,
                            cTATTCassccc,,,,,,,,,,,,,,,, ,,,,
                            cAATTassccc,,,,,,  ,, , ,,,,,,,s,
                            cAATTaasccc,,,,,,,, ,,,, ,,,,,,c,
                            sAATCassccc,,,,,,,,,,,,,,,,,,,
                            sATCssccc,,,,,ccccc,ccc,ccccc,,
                            cATCsccc,,,,,,ccssssssccccc,,,,
                      sCasssTATascc,,,,,,,caAATTCssccc,,,ccc,
                     ,ARRRRRATCascc,,,,,,,caRRATCssscc,,,csac
               sRRRRARRRRRARATCscc,,,,,,,,,CRATCscccc,,,,,csARRRT,
      cTRRRRRTARRRARRAARRRATTCascc,, ,,,,,,aATCscccc,,,,,,csc,
      ,TTTTTTRRRRTRARARRAAATTCssc,,,,,,,,,,aATCscccc,,, ,,cc,
             CRRRRRRRRTAATTTCascc,,,,,,,,,cCAACsccc,,,  ,s,
            ,RRRRRRRRARRATTCassc,,, ,,,,,,,aAATsccc,,,  sTs
             ,sccccCRRRAACaascc,,  ,,,,,csTTAATTCscc,,  aRC
                    ,aRRTassc,,,,,,,,,cccsaCTTCasscc,,  csc
                     ,TRTasc,, ,,,,,,cccccssCasscccc,,,,,,,
                        casc,,,,,,,,,cc,sRRRACssccc,,cRRRc,
                      ,sCTsc,,,,,,,,,,csCARTsaRRAACssCRRA,
                     ,CTRACssssssssssaaas,   cRRRRTCCCas,
                        TRRRRRRRRRRRRRA,

    """,
    """


                                                         ,
                                                      ,cTRCc,
                                                     cRRRRRRC
                                                   ,aRRRRRRRa
                                                   cRRRRRRACc
                                                 ,cTRRRRRACs,
                                              ,  aRRRRRRCccc,
                                            ,  sRRRRRRRTs,,c,
                                            ,,,TRRRRRRRCc,,c,
                                   ,,,  ,,,, ,cCRRRRRRAsc,,c,
                            ,,,,  ,,,,,  ,,,   ,,CRRRRTs, ,sc
         ,sRRACs,           ,,,,, ,,,  , ,,       cccccc, cCs
        cRRRRRRRRRRRRRRTsc,  ,,,,,       , ,,        ,,,,,sAs
        cRRRRRRRRRRRRRRRACc,,,,,,,,,,,   ,,,,      ,,,,,,,sCs
        ,TRRRRRRRRRRRRRRRRRRRc,,,,,,,,,  ,   ,,,, ,,,,,,,c,
        ,ARAAARRRRRRRRRRRRRRTc,,,,,,,,,,  ,,,,,,,,,,,,,,,,,,
        ,sTasaCTAARRRRRRRRTscc,,,,,,,,,,,,,,,,,,,,,,,,,,,ccc,,,,,
           sCsc,cssTARRRCsccc,,,,,,,,,,,,,,,,,,,,,,,,csTRRAacccsc
          ,TAs,,,cssCARAaccccc,,,,,,,,,,,,,,c,,,,,,,,cARRRRRaccc,
            ,cc, ,,,csaacccccc,,,,,,,,,c,,,,,,,,,,,cccccTRRRRc,,,,,,,cc,
             TRa,  ,,csssscccc,,,,cc,,,,,,,,,,,,,,,,caARRRRRRc,ccc,cc,
             TRCc,  ,,csssscc,,,,cccccccscc,,,,,,,,,,sRRRRRRCc,ssc,cs,
               sTa,ccsscsccccc,,ccccaRRRRRRa,,,,,,          ,csccccss,
               ,ccssssccccccc,ccccsTTCTRRRRT, ,, ,          ,cccccsc,
                 ,aascccccccccccccTRRRARRRRA   ,       ,  ,,,ccccc,
                 ,ssccccccccccccccCRRRRRARRa     ,,,,,,,,,,,ccaac
                 ,ascc,cccccc,,,,cccccccc,,,    ,,ccc,,,,cccccsss,
               cTTasc,,,,,,,,,c,,,,,,,,cc,,,, ,,,,,cccc,cccccsc,
               aRACssc,,,,,,,,,,,,,,,,,cc,,,,,,,,,,ccsc,cccccsc
               sATCassccc,,,,,,,,,,,,c,,,,,,,,,ccccssascccaCc
               sRACaascc,,,,,,,cc,,,,csaCscccccccccssssaCTARC
               sRTCasccc,,,c,,ccaascccccscccccccccssaCAAs,ccc
               sAACCCsccccssscsaCTCscccccsssssssCCTTTTTTc,
               sTTCTTCsccsaCassssssssssssCCCaCCTAARTTascss,
                   ,TTTCCCCCCCCCCTCTTRRRAAARRACaaaCacccccc,
                       ,TRRRRRRRRRRRACasaaaCaasssssccccccccc,
                        sTTTTTTAAAARTscccsssssscsscccccccccs,
                               ccccscccccccccccccc,c,,,,,,cc,
                             ,ccccccccccccccccc,c,,,,,,,,,,
                            ,cccccccccccccccc,,,,,,,,,,,,,
                            ,,,ccccccccssccc,,,,,,,,,,,,,,
                           ,,,,cc,,,ccsssscc,,,,,,,, ,,,,,
                           ,,, ,,,,,,,ccccc,,,,,,,,, , ,,
                        ,,,,,,    ,,,,,,,,,,,,,,,,,,, ,,,
                       ,sasc,,,  ,,,,   ,,,,,,,,,,,,,,,,,,
                          cascc,,      ,,,,,,,,,cc,  ,,,,
                          sTac,,      ,,,,,,,,,,cc, ,,,,,,
                          aATsc,,,,,,,,,,,,,cccc,,,,,,,,,,
                          aRTCaaaasssaacccccccc,,,,,,,,,,,
                          aRTCTTTCaaaTTsc,,,,,,,,,,,,,,,,,
                          aATaCTTCCssccc,,,,,,,,,,,,,,,,,,
                          aRTCCTTTCacccc,,,,,,,,,,,,,,,,,,
                          cCTTTTTCascccc,,,,,,,,,,,,,,,c,,,
                            cATTCasccc,,,,cccc,,cc,cccc,,,,
                            cAATCascc,,,,,ccccssssccccc,,,cc,
                      saaassTATCCscc,,,,,,,ccaTTCasccc,,,,cac
                     ,ARRRRRATTCascc,,,,,,,ccCATTsccc,,,,,ccc
               sRRRRRRRARRARATTCasc,,,,,,,,,caTTaccc,,,,, ,c,
      cTRAAAAAAARRRARAAARRARATCCscc,,,,,,,,aARTCsccc,,,,,,,c,
     ,aRRRRRRRRRRRARRARRRARAATCCscc,,,,,,,,aRRTTscc,,,,,, ,,,
    cTATTTTARRRRARRAARRRRRATTCaacc,,  ,,,,caRRATCsc,,,,,,,
     ,,,, cTRRRARARARARAATTTTCascc,, ,,,,,caARRACacc,,,,,
          ,TRRRRRRRRRRRRTTTCaacc,,,, ,,,,,caTTTTTTCscc,,,c,
           cccccccccccccCCCscc,,,,,,,,,ccccaCCaaCasscc, cTs
                        sCasc,,,,,,,,,cccccaCCasssccc,,,aRC
                        sCacc,,,,,,,c,,ccsaARTsccc,, ,aRRRa
                      csTTsc,,,,,,,cccccaTTCsaTTCTTTTTTTTac
                     ,aARRTassssssaaaCascCC, ,CTCTRRRRs,
                        CRRRRRRRRRRRRRA,

    """,
    """


                                                    cTac,
                                                  ,CRRRRC,
                                                 cRRRRRARRa
                                                 sRRRRACARa
                                               sRRRRRAacCTc
                                               TRRRRRTs,sCc
                                             ,cRRRRRAsc,cCc
                                   ,,,ccc,,  TRRRRRRCc,,cTc
                                   ,,,ccc,,cCRRRRRRAac,,sTc
                             ,,,,,,   ,,, ,aRRRRRRRTs,, sAa
                        ,,,    ,,,,,,  ,,, ,,csaTTATs,  sAa
                      ,,,,,,,,, ,,,,,    ,,   ,,,ccc,,,,,,
                     ,,,,,,,,,, ,  , , ,,   ,,   ,,,,,cc,
               ,,,,,,,,,  ,,,, , ,,,,, ,,     ,,  ,,,,cs,
      ,aRRRRRRRRRRAacc,,,,,,,,,,,,,  ,,          ,,,,,,ccc,
      cRRRRRRRRRRRRRRRRRRRa,,,,,,,   ,           ,,,,,,,cc,,,c,
      cRRRRRRRRRRRRRRRRRRRTc,,,,,,,           ,,,,,,,,,,cccccsc,,,,
      cARTTTAARRRRRRRRRRTcccc,,,,,,  ,,  ,,,,,,,,,,,,ccssccc,,cssas,
      cRRTaaTTTARRRRRRRTascc,,,,,,,,,,,, ,,,,,,,,,,,,csTCCsc,,,cccc
       ,,cccccsssCTARACasccc,,,,,,,,,,,,,,,,,,,,,,,cRRRRRRRc,,,c,
        ,ARsc,,,ccsaCsscscccc,,,,,,,,,,,,,,,,,,,,,,cRRRRRRRc,cc,ccc,
        cRRCc, ,,cccssssscc,,,,,,,,,,cc,,,,,,,,,,,,cARRRRRA,,ccccaa,
          ,CTs,, ,,csaassccc,,,,,,ccccc,,,,,,,,,,,,cARRRRc,,,ccCa,
           ccas,,,ccsssscccc,,,ccccc,cccc,,,,,,,,, ,cCAAs,,csc,c,
             aACcsaassssccccc,ccccaAAaCARCc,,,,,,         csasc
             aATCasscscccccccccc,cARRATRRAc,, ,     ,,,,,,,,ccc
             aATassccscccccc,ccccsARRTaTAs,,,        ,,,,,cc,
               caacccccccccccccccCRRRRRRRs       ,CTc,,ccccs,
               caacccccccccc,ccccsARRRRRAc    ,  cTTc,,ccccc,
             aATCaccc,,,,,,,,,,,,,,,,,, ,   ,,,,,,ccccccss,
             aATCasccc,,,,,c,,,,csaTTTTCsc,,,,,,ccscsscsTRa
             aAATCasccc,c,ccc,,,,ccccssccc,,,,,cccccsssccc,
             aAATCascccccccc,c,,cccccc,cccccccccssCasscc,
             aAATCsscccccc,cccccccaTCsccccccsccssCTTs,cccc,
             aRATCaaCasccsCTTCassssaaaassaCTTAAAsccccccccccc,
                 sTATTTTTTTAATTTAAAAAAAAAacccccccccccc,,cs,
                 ,aCssaaCaCCTTTTTTAAAAAATaccccc,cccc,,,,cc,
                            ,ssccccccccc,cc,c,,,,,,,,,,,,
                            ,sssscccccccccc,,,,,,,,,,,,,,
                          ,,cccccccccccccc,,,,,,,,,,,,,,
                          ,ccccc,cc,cccc,,,,,,,,,,,,,,,
                          ,ccccc,,,,,,,,,,,,,,,,,,,,,,,,,,
                          ,,,,,,,,,,,, ,,,,,,,,,,,,,,,,,,,
                          ,,,,,   ,,,   ,,,,,,,,c,,,,,,,,,,,
                          ,,,,,,,       ,,,,,,ccc,,,,,,,, csc
                          ccccccc,  ,,,,,,,cssCa,  ,,,,,,,,c,
                           ,cascc,   ,,cccsc,cc,,,,,,,,,,,,,,
                            ,,sas,,ccsaCCsc,,   ,,,,,,,,,,,,
                              cTTssaaasaac,,,,,,,,,,,,,,, ,,
                              cAATCassccc,,, ,,,,,,,,,,,, ,,
                              cAATCassccc,,,,,,,,,,,,,,,,,,,
                              cAATCascccc,,,,,,,,,,,,,,ccc,,,,
                              cTATCascccc,,,,,,,,,cccccc,,,,,cc
                              cTTasccc,,,,cccccccccsccc,,,,,,c,
                            caTTCascc,,,,,cccaCTTCssccc,,,, ,,,
                          caAATTascc,,,,,,,ccCARATaccc,,,,, ,,,,,
                          CRRATCacc,,,,,,,,ccCAAATacc,,,,,,,,,ccc,
               sRRRARRARRARRATCascc,,,,,,,,caTARTTaccc,,,,   ,csc,
        ,TRAAAAARRAARAAARRAATCascc,, ,,,,,,aARARATCacc,,,,,  ,,cc
     ,c,sRRRRRRRAARAAAARAAATTCascc,,  ,,,,cTRRRAAATCsc,,,,,  ,,cc
   ,CRRRRRRAAAAAAAARARAARATTCacc,,,  ,,,,,,RRRATTTATCassc,,  ,,c,
  sTRRRRRRRRAAAAAAAAAARAATTCascc,, ,,,,,,,cRRRACTTTTTCasc,,  ,,,
  ,ccc,c,,cARRRRRRRRRRRRATCascc,,  ,,,,,,,cTRRAACaasassscc, ,,,
           ccsasccccccccaCasc,,,,,,,,,,cc,cARRRTCscccccc,,,,,cc
                        sTacc,,,,,,,,,ccccsRRRRTCsscccc,,,,,cas
                        sCsc,,,,,,,,c,,csTRRRRRRRTsc,,,,,, ,sRA,
                      csCCsc,, ,,,,,,,,saaassCARRRRACaaaassaaac
                     ,aTRACssssccsssssssc       sTRRTCCTCTTTs
                        TRRRRRRRRRRRRRA,

    """,
    """


                                                  casscc,
                                                 sRRRRRRc
                                               cRRRRRRRAc
                                               cRRRRRACa,
                                             cRRRRRRCscc,
                                            ,TRRRRRAaccc,
                                       ,,, ,cRRRRRRac,,,
                                      ,   ,ARRRRRRAac,,,sCc
                                     ,, ,cARRRRRRRAs,,,,cc,
                             ,,,,,   ,  ,TRRRRRRRRCc, ,c
                        ,,, ,,,,,,  ,   ,,c,c,csARCc, ,c,
                  ,, ,  ,,,,,, ,     ,,,  ,    ,,cc, ,cac
    cRRRRRRRRRACcc,      ,,, ,, , ,, ,    ,     ,,,,,,aTc
    TRRRRRRRRRRRAacc,,,,,,,,,,,,   ,,   ,     ,,,,,,,caCc
    aRRRRRRRRRRRRRRRRRRRC,,,,,, ,,   ,,,,,,,,,,,,,,,,,,,csc
    cRRRRRRRRRRRRRRRRRRRsc,,,,,,,      , ,,,,,,,,,,,,,,,ccc,,sc
    cRACCTAARRRRRRRRRRaccc,,,,,,,,,,,,,,,,,,,,,,,,ccccccc,cccas
    cCaccccsaCTARRRRasccc,,,,,,,,,,,,,,,,,,,,,,,,cARRARRTcc,,,,    ,,
      ,ccccccsaaTARAacccc,,,,,,,,,,,,,,,c,,,,,,,cCRRRRRRRsc,,cc,,,ccc,
      cRAc,,,,ccsaassccccc,,,,,,c,c,cc,,,,,,,,,,csAARRRRTc,,,,cc,
       ,sTCc  ,,ccsasccccc,,,,,,,,,,,,,,,,,,,,,,,caARRRac ,ssc,,ccc,
        ,TTc,, ,,ccasccccc,,,cccccccccc,,,,,,,,,,csARRAc,,caaccccss,
          ,aTc,,ccsscccccc,,ccccaTRRRRRs,,,,,,         ,cscccssc,
           ,ccsccsscccccccccc,csaCARRRRa,,, ,          ,,ccsasc,
             cTCsscccccccc,c,cARRRRARRRa      ,,c,,,,,,,,,cCs,
             cCacccccccccc,cccTRRRRRRRAc     ,,ccc,,,,,ccccc,
             cCaccccccccccccccccccsscc,     ,  ,,c,,ccccccsac
             cTaccc,,cccc,,,,,,,,,,,,c,, ,, ,,,cccccccccssc
             cTCsc,,,,,,,,,,,,,,,,,,,cc,,,,,,,,cccccccccaac
             cTCscc,,,,,,cccccc,,ccc,,,,,,,,cc,ccccccssaTAs
             sATCscc,,,,,,,,,,,c,,csssccccccccccccsaCCac,
             sACascc,,,,,,,ccccscccccccccccccccssaTTaasc,,
             sTCassccccccscccssascccccccssaaaCTTCaCaccccccc,
             cTCaaasccccCTaccsscccsssssaaCCTTAAAaccccccccccc,
          ,aARA, ,saaaaaCCCCCTTTTTAAAAARRAaaaasccccccccccccc,
            , ,cTAAAAAAAAAAAARRRTscsssssccccccccccc,c,,,cc,
               cTTCCCCCCCCTRAARACccccccc,ccccccccc,,,,,,cc,
                          sATCssccccccc,,cc,,,,,,,,,,,,,cc,
                          sATaascccccssc,,cc,,,,,,,,,,,,,,
                          sTCssccccccssc,,,,c,,,,,,,,, ,csc
                          cTCsccc,,,ccc,,,,,,, ,,,,,,,,,cc,
                          sTCscc,,,,,cc,,,,,,,,,,,,,,,,,,,
                          sTCcc,,,,csc,,,,,,,,,,,,,,,,,,,,,,,
                          csscc,,,,ssc,,,,,,,,,,,,,,,,,,,,,,,
                            ,cc,,,,ccc,,,,,,,,,,,,,,,,,,, ,,,
                            csccc,,cccccccc,  ,,,, ,,,,,,,,,,cc
                             ,csc,,ccccccc,,,,,,,,,,,,,,,,,,,cc
                               ,caasssasc,,,,,,,,,,,,,,,,, ,,c,
                                ,CTCaascc,,,,,,,,,,,,,,, ,,,,c,
                                ,CTascccc,,,,,,,,,,,,,, ,,,,,c,
                                cTTCsccc,,,,,,,,,,,,,,,,,,,,,c,
                                ,TTCsccc,,,,,,,,,,,,,,,,c,,,,cc,
                                cTCaccccc,,,,,,,,,scccccc,,,,,ccc
                              cAACsccc,,,,cc,ccccsaCscc,,,,,,,,cc
                              cATascc,,,,,c,ccCTAAACscc,,,, ,,,cc
                   ,csssssscccaTCscc,,,,,,,ccaATccssc,,,,,  ,,,ccc,
                   cARRAARARAATTasc,,,,,,,,,cCAC  ,cc,,,,, ,,,,,ccc,
             CRRAAAAAAAAAAAAATCascc,, ,,,,cccaARAACcc,,,,,,  ,,,ccc,
        ,TAAAAAAAAAAAAAAAAAATCascc,, ,,,,,,ccARRRAATscc,,,,  ,,,,cccc,
,,,,,c,,cARRRAAAAAAAAAAAAAATCascc,,,,,,,,,ccaRRRAAAACsccc,,,, ,,,,ccc,
sAATAAATAAAAAAAAAAAAAAAAAATCascc,,  , ,,cccaARRRRAAAATCaaccc,, ,,,,cc,
,,,,,,,,cTRAAAAAAAAAAAAATTCCsscc,, ,,,,,,,cCARRRRRRATTTCasccc,,,,,,cc,
        ,ARRRRRRRRRRRRRATCascc,,, ,,,,,,c,cCAAAARRAATTCaassccc,,,,,cc,
         ccccccccc,cccccaCacc,,,,,,,,,,ccccCAAAAAAAATCCsscccc,,,,,,,,
                        sCacc,,,,,,,,,cccccCAAAAAAAATCCsscccc,,,,,,
                        sasc,,,,,,,,ccccccsTRRARRRRAAATCscc,,,,,,cc,
                       ,CAsc,,,,,,,,,ccccc,csssCAAasARAATCaaaaaaaTC,
                       ,aTascccccccccscc,           cCTCCCCCCCTCCTC,
                          CRRRARRRARRRA,

    """,
    """



                                                       ,,,
                                                    ,cARRAs
                                                   ,ARRRRRs
                                                 ,CRRRRRRAc
                                                 cRRRRRRAac
                                               ,sRRRRRRTscaAC
                                          ,,  ,CRRRRRRTs,,sAs
                                         ,, ,cTRRRRRRAac,,cTs
                                       ,,,,  ARRRRRRRTc,,,cTs
                             ,,   ,    ,,,   ARRRRRRACc, ,cTa
    ,cARRRRRRCc,                 ,,,  , ,,   ,cccaRRAac, ,cTa
    cARRRRRRRRRRRRRRRAacc,,, ,,,   , ,           ,cccc, ,,,,
    cARRRRRRRRRRRRRRRRRCc,,,,,,,    ,        ,,,,,,,,c, ,,,
    cARAAARRRRRRRRRRRRRRAc,,,,, ,      , , ,,,  ,,,,,,ccaCc
    ,csaCCAARRRRRRRRRRRRCc,,,,,, ,,   ,,,,,,,,,,,,,,,,ccsac
      ,ssccsaTAAARRRRRaccc,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccc,
      ,ATc,,cccsaAATasccc,,,,,,,,,,,,,,,,,,,,,,,,ccaARTacccc,  ,,
      cRRs,,,,ccaaTasscc,,,,,,,,,,,,,,,,,,,,,,,,ccaARRRRaccc,,cCa,
        cAAc,,,,ccssccccc,,,,,,,ccc,,,,,,,c,,,,,ccTAARRRRac,,,cccc,
         ,cssc ,,csssscccc,cccccccc,,,,,,,,,,,,,cCRRRRRRRc,,,cc,,,c,,cc,
           sac,,,cssscccccc,cccccsssccc,,,,,,,,,,aRRRRRRT,,,cccc,cc,ccc,
             cscccsscccccccc,csTRRRRRRRc,,,,,            ,caacccccc,
             cTacssccccccccc,cRRRCTRRRRa  , ,           ,cccccccccccc
             aACcccccccccccccsRRRAARRRAc     ,c,, ,  , ,cccccccccsacc,
             cTaccccccccccccccccTRRRA,       cas,,,,,,,,,,cCacc,,cc
             cCsccccc,c,,c,,,,,,,,,,,        ,,,,,,,,,,,ccccssc
             cCscc,,,,,,,,ccsaaaaaaac,,,,,,,,,cccc,cccccccsac,
             cCacc,,,,,,,,ccsaCCCCCac,,,,,,,,ccccccccccccssc,
            ,sTCscc,,,cc,,,,,,,,,,,,,,,,,,,,ccccsscccccaaac
          ,CRTCsccc,,,,,ccc,,csCCacccccccccccccsaassaaTCc
          ,CATasccccc,cccssccccssccccccccccccssaaaaCTTaac,,,,
          ,CAACCsssccccsaCCaccccccsssssssaaaaCTTTTTCCaccccssc
          ,aAAATCasccssssassscssssCTTCCaCCATTAAAAACsccccccccc
               cTATTTTCCaCCCTTTTAAAAAAAAAAACaaaaaccccccccccc,
                     ,TRRRRRRRRRRRRRAAATCCCasscccccccccccccc,
                     ,aTTCTTTTTAATAAATCasssscccccccccccccccc,
                               ,,,cccccccccccccccc,,,,,,cccccc,
                            ,c,,,,,,,,ccccccc,,,,,,,,,,,,cccc,,
                          ,sCTscc,,,,,,ccc,,,,,,,,,,,,,,casc,,
                          CRTsaac,,,,,,,,,,,,,,,,,,,,,,,cCCsc,
                          aACcaCc,,,,,c,,,,,,,,,,,,,,, ,,saCs,
                            csc,,ccc,,,c,,,,,,,,,,,,    ,cccc,
                            ,ac,,cccccccc,,,,,, ,,,,,,  ,,,cc,,
                            cCsccsscccccc,,,,, , ,, ,,,, ,,,,cc
                            caCaaaaassssc,,,,,,,,,,,,,,,,,,,,c,
                             ,cCCaaaasssc,  ,,,,,,,,,,,,,,,,,,,
                               ,caCaCCaas,, ,,,,,,,,,,,,,,,,,,,
                                ,CACCascc,,,,,,,,,,,,,,,,,,,,,,
                                ,TACascc,,,,,,,,,,,,,,, ,,,,,,,
                                ,TACaaccc,,,,,,,,,,,,,,,,,,,,,ccc
                                cTACascccc,,,,,,,,,,,,,,,,,,,,ccc
                                ,TACasccccc,,,,,,,,,,,,,,,,,,,ccc
                                ,TTascc,,c,,,,,,,ccccccc,,,,,,ccc
                                ,TTascc,,,,ccc,cccaaasc,, ,,,,ccc
                   ,cacccaccscccaCCscc,,,,,cccsCTTTCsc,,  ,,,,ccc
                   ,ARRARAARARAATCacc,,, ,,ccsCARRTCcc,, ,,,,,ccc
             aRRAAAAAATAAAAAAAATCasc,,, ,,,,,cTAAACcc,,  ,,,,,,cccccc,
CRRATAAAAAAATAAAAAAAAAAAAARAATTCasc,,, ,,,,,,sAATCssc,,  ,,,,,,,ccccccc,
cTACRRRRRRRRRAAAAAAAAARAAAAAATCascc,,,,,,,,,,aRRRAascc,    ,,,,,,,cccccc
    ,CTCCAAAAAAAAAAAAAAAAAATCCascc,, , ,,,,ccTRRRRAascc,,    ,,,,,,,cccccc
     ,, ,TAAAAAAAAAAAAATATTTCascc,,  ,,,,,,csCARRRACascc,     , ,,,,,,ccc,
      ,aARRRRRRRRRRRRRRRTCaascc,,,, ,,,,,,csTRRRRAAATCCaccc,,,,  ,,,,,ccc,
      ,cc,ccaaac,,,cc,,caCsc,,,,,,,,,,,,cccCARRRAARAAAAATCCasc,,,,,,,,,sCc
                        sCsc,,   ,,,,,,,cccCAAAAAAAAAAAAATTCasc,,,,,,,caAa
                        sacc,,,,,,,,cccccccCARRARAAAAAAAATCssccc,,,,,aTc
                       ,aTc,,,,,,,,,,ccaCTCacacacCARRRARRRRTCCaaaaasaAAa
                        caascccccccccsaCCCC,      cCCCaCARTCCCCCCCCCCCC,
                          CRRAARARRRRRA,

    """,
    """





                                                         ,cc,
                                                      sRRRRRRTc
                                                     cRRRRRRRRT,
                                                ,, cRRRRRRRCTRT,
                                              ,  ,TRRRRRRRCsaRC,
                                               ,,aRRRRRRRTscsAC,
                                         ,,,,,caRRRRRRRRCs,,cas
                                    , ,   ,,,cCRRRRRRRRAac,,cCs
      cRRRRRRRAc         ,        ,,  ,   , , ,TRRRRRRRCc,, cTC,
    caRRRRRRRRRRRRRRRTc,   ,,,, ,  ,           ,sasaARAac, ,cAC,
    cTRRRRRRRRRRRRRRRRAcc,, ,,,,   ,,, ,      ,    ,aTac,  ,cas,
      ,aTTARRRRRRRRRRRRRRRT,,,,, ,,  ,,      ,,,,,,,,,,,, ,c,
      ,aCaaTRRRRRRRRRRRRRRs,,,,, ,          ,,,,,,,,,,,,,,cac
      cATcccsaTARRRRRRRRs,,,,,,,, ,,,,,,,,,,,,,,,,,,,,,ccccc,
      ,CCccc,ccsaTARRAcc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cc,cc,  ,
        ,ccc,,ccsaTCCacc,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccc,,ccc
        cRRc,,,,ccsssccc,,,,,,,cc,,cc,,,,,,,,,,,,CRRRRRRAcccccccc
         ,cTTc,,,csasscccc,,ccc,,,,,,,,,,,,,,,,cssccARRRRsc,,,ccc
           CTsc,ccsassccc,ccccccccccc,,,,,,,,,,csc,,aRRRRsc,,ccc,
             cCacsaascccccccccaARRRRRs,,,,,,,,,,,CRRRRRRC,,,cccc,cccccc,
             ,ccsssssccccccccsARATRRRCc,,,,,    ,cTATCCac,,cccccccccc,,
               ,ssccccccccccCRRRRCARRa,,                ,cccccccccccc,
             ,,cccccc,c,cc,csARRRRRTs,     ,,ccc,,,,,,,,cccccccccccc,,
             cCscccc,,,,,,,,,,ccccc,,     ,,cCRAc, ,,,,,csaCacccccc,
             cCacc,,,,,,,,,cccccccc,,,   ,,,,ccc,,,c,ccccccccccas,
            ,cCacc,,,,,,,,,ccccccccc,,,,,,,,,,cc,cccccccccccccssc,
          ,CRATaccc,,,,,,,,,,,c,,,,,,,,,,,,cccsccccccccccssaaas
          ,CACcccc,,,,,,cc,,ccsaCascccc,ccccccsscccccssaaCAAs
           sTacccc,cccccaCcccccsscccccccccccccssccsssaaaAACc,
         ccTACCsccccccsaCTacccccccccscccccsssaaaaaTTTCaaCTc, ,
        ,CARAATCcsssssasassssssssssaassaasaaaaCCCATAACsccccccc,
            ,aAATTTTCCCCCCCCCCTAATTTTTTAAAAAAARACascccccccccccc,,
                   cARAAAARRRRRRRRRRRAATTTCaaaasccccccccccccccc,,
                   ,aTTCCCCCTTTTTARAAAATTaaassscccccccccccccccc,,
                                ,CTaaaaaasccccccc,,cc,ccccccc,,,,,,
                        cc,,,cccsaascccccccccccc,,,,,,,,ccccc,,,,,,
                        ,cccccaATssccccc,c,,c,,,,,,,,,,,ccccccc,,,,
                          csc,aATscccccc,,,,,,,,,,,,,,,,,ccCsc,,,,
                          csccCRAccccccc,,,,,,,,,,,,,,,,,,sCa,,,,,
                          cacccccccssscc,,,,,,,,,,, ,, ,,,ccsas,,  ,,
                          cCsccccccssccc,,,,,, , ,,,, ,,,,,ccssc,, ,,
                          ccscccccccccccc,,,,,,,,,,,,,,,  ,,,,ccc,,
                            casccccccccccc,,,,,,,,,,,,  ,,,,,,,cc,,
                            cCaccccccccccc,,,,,,,,,   , ,,,,,,,ccc,
                            cTCasccccccccc,,,,,,,,,,,,, ,,,,,,,c,,
                            ,csCCasccccccc,c,,,,,,,,,,,,,,,,,,,,,
                              cCCCssccccccc,,,,,,,,,,,, ,,,,,,,c,
                                  ,CACaacccc,cc,,,,,,,,,,, ,,,,,,cc,
                                  ,CATCaccccccc,,,,,,,,,,,,,,,,,,cc,
                                  ,CATCasccccccc,,,,,,,,,,,,,,,,ccc,
                                  ,CATCacccccc,,,,,cc,ccc,,,,,,,ccc,
                                  ,CACsccc,c,,,,,,ccccscc,,,,,,cccc,
                   ,caaccaccccacccsCCscc,,,,cccccsCCCCsc,,,,,,,cccc,
                   cARRAARAAAARAAACascc,,,,,cccsaTAATacc,,,,,,,cccc,
             aARAAAAAAAAAAAAAAATCCascc,,,,,,,,csAATCacc,,  ,,,,cccc,
CRRARRAAAAAAAAAAAAAAAAAAAAAAATTCasccc,,,,,,,,,csAATasc,,  ,,,,,,ccccc,
cTACCCCCAARRAAAAAAAAAAAAAAAAATCCasccc,,   ,,,,,sAACacc,, , ,,,,,ccccc,
        ,ARRRAAAAAAAAAAAAATTTCCsccc,,, ,,,,,,,caAATCscc,,  ,,,,,,ccccccccc
        cRRRRRAAAAAAAAAAAATTCasscc,,,,,,,,,,,cCAAAATascc,   ,,,,,,,,,cccc,
         cCRRRRRRRRRRRRAACCascc,,,,  ,,,,,,,,sAAARRRAascc,,,,,,,,,,,,,,cc,
           ,ccccccccccccaCscc,,,,,,,,,,,cccsCTAAAARRRTTCCssccc,,,,,,,,,cc,
                        sCsc,, ,,,,,,,cccccTAAAAAAAAAAAAACascc,,,,,,,,cccc
                        sCcc,,,,,,,,cccccccCAAAAAAAAAAAACccccccc,,,,ccsTRa
                       ,CAc,,,,,,,,,,,csTAARRAaccCARRAAAACCCCAACaaaaaTTTac
                       ,cCascccccccccssaCARAac    cCCaaaCCCaTRRCaCCCCCCc
                          aRRAARARRRRRA,

    """,
    """




                                                           ,css,
                                                          cRRRRRs,
                                                    ,,  cRRRRRRRa,
                                                    ,, ,RRRRRRRAs,
                                                  ,, ,RRRRRRRATac
                                              ,,   ,RRRRRRRRTscc,
         caCac,                               ,, ,aRRRRRRRRAac,c,
       ,CRRRRRRRTCCc,,,          ,,,,,,,,,,,,,,  sRRRRRRRRTac,,,,
      ,CRRRRRRRRRRRRs,      ,,,  ,,,,,,, ,,      aRRRRRRRRasc,,cc
        cARRRRRRRRRRRRRRRRTc,,,,,, , ,,   ,,  ,  ,csaTRRRAs,, ,sa,
        ,sTCCARRRRRRRRRRRRRsc,,,,,,  , , ,     ,,,, ,,csscc,  cTT,
        ,sassCTRRRRRRRRRRRRcc,,,,,     ,,       ,,,,,,,ccc,  ,caC,
        ,CCc,csaaARRRRRRAsc,,,,,,, ,,,    ,,,,   ,,,,,,,cc,,,sc
        ,ARs,cccsaARRRRAacc,,,,,,,,,,,  ,,,,,,,,,,,,,,,,,cc,cCs
        ,saac,,,ccsaTCsccc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,c,ccccac
           CAc,,,,csasscc,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccc,,c,,
          ,ARCc,,,,caascccc,,,,,c,,,,,,,c,,,,,,,,,cccscccccccccc,
            ,TAa,cccaasccc,,,,,ccc,,,,,,,,,,,,,,,sRRRARRRacc,,,,c,caCc
              ,sTCasassccc,c,cccccccc,,,,,,,,,,,caAATTRRRRAc,,,,,ccsc,
               cAAaassccccc,ccsasccaac,,,,,,,,,,csCTTARRRRTc,cc,c,,,,
               cCCssscccc,,ccaRRR cRRTc,,,,,,  ,,cCRRRRRC,,,cccc,,,,ccccc,
               cCascccccc,ccCRRRRaCRRa,,, ,      ,csAAAac,,ccccc,,ccc, ,,
             ,csssccccc,,c,caARRRRRAac,                 ,,cccccccccccc,
             sACcc,,,,c,,,,,,,,cTRRac,     ,c,,,,,,,,,,,cccccccccscc,cc,
             cTacc,,,c,c,,,,,,,,,,,,,,    ,cTa,,,,,,,,,ccsaCacccccc,
             cCsccccccccc,,,,,,,cc,,,,,,,,,,ccc,,,ccc,ccccccccsas,
            ,sCsccccccc,,,,,,cccccc,,,,,,,,,,cccc,cccccccccccasac
          ,CATasccccccccccccc,,ccccccc,,,cccccsccccccccccssaCTa
        ,CATCTTCCCssssCTAATasccccccccccccccccsascccsssaCAAac,
         cc,cCATCaaaaCCCTTCssssccccccccccccccsaassaaAAAAAascc,,,,
             ,cCTTTTAATTCCCCCCCCCCCaaaaaaaaaaTAAAaaaaCCCaccccccc,,
               sARAAAAAAAATTTTTAAAACCCCAACTTAAAAAAsccccccccccccc,,,
                       ,TRRRRRRRRRRRRRRRAAAaasccccccc,ccccccccc,,,,,,
                                  ,CAaaasssccccc,ccccc,cccccc,,,,,,,,
                                  ,sCasccccccccc,,cc,,ccccccc,,,,, ,,
                                ,TACsscccccccc,,,,,,,,,cccccccccc,,
                                ,TTasccc,,,,,,,,,,,,,,,,ccsaasscc,,,
                      caTCc,  ,caTTascc,,,,,,,,,,,,,,,,,,ccCTTCcc,,, ,,
                     ,RRRRTaccsCTAATCsc,,,,,,,,,,,,,,,,,,ccsaaacc,,,,,,
                     ,RRCsCTRRCcsTAATCsc,,,,,,,,, , ,,,,,ccccascc,,,,,,
                      csaTTTRRAccccsaTAcc,,,,,,,,,,,,, ,,,,,cccscc,,,,,
                      ,csTARRACcc,,csCTscc,,,,,, ,,,,,, ,,,,,,cccc,,,,,
                        caRRC,,ccccccccsaccc,,,,,,,,,,,,,,,,,,,,cc,,,,,
                        cccccccccccccccsCaccc,,,,,, ,,,,,,,,,,,,ccccc,,,
                         ,cCasccccccc,caaaccc,,,,,,,,,,,,,,,,,,,,ccaCc
                          ,,,,casccccccsaacccc,,,,,,,,,,,,,,,,,,,ccc,,
                              ,,sCCascsaCaccccc,,,,,,,,,,,,,,,,,,cc
                                ,CTCCaCCaascccc,,,, ,,,,,,,,,,,,,cc,
                                    ,CATCCasccc,,,,,,,,,,,,,,,,,,cc,
                                     CATCaascc,,,,,,,,,,,,,,,,,,,cc,
                                    ,CACassccc,,,,,,,,,cc,,,,,,,,cc,
                                    ,saccccccc,ccccsaaascc,,,,,,,,ccc,
                                   csscc,,cccccccsaCTTCac,,, ,,,,,ccc,
                   ,caacaccsccacccsCac,,,,,,ccccaCTAAACsc,,  ,,,,cccc,
                   cARRAARAAARRAAATac,,,,,,,cccssCAAATacc,,  ,,,,cccc,
    cARAAAAAAAAAAAAAAAAAAAAAAAATCasc,, ,,,,,cccsaTAATCsc,,,,,,,,,cccc,
    cRRRAAAAAAAAAAAAAAAAAAAAAATCasc, ,,,,,,ccccsaTAATCsc,,,  ,,,,,ccccc,
    ,CCcCRRAAAAAAAAAAAAAAAAAATCasc,, ,,,,,cccccsCAAATCscc,,  ,,,,,,ccccc
        cRRRAAAAAAAAAAAAAAAATscc,  ,,,,,,,cccccaAAAAAACcc,,,   ,,,,,cccccc
      ,CARRRRRRRRAAAAAAAAAATasc,,  ,,,,,,,cccccaAAARRRAscc,,    ,,,,,cccccc,
       ,,,,,,,,,,aRRRRRRAACac,,,,,,,,,,,cccccaTAAAAARRATTCscccc,,,,,,,,ccccc
                 ,,cc,,cARCc,,,,,,,,,,cccccccaARAAAAAAAAATCascc,,,,,,,,,cc,
                       ,TAacc,,,,,,,,ccccccccCAAAAAAAAAAACaascc,,,,,,,,cc,
                          casc,,,,,ccccccccCARRARAAAAAAACscccccc,,,,,,ccCc
                          sATscc,c,,csCCCCCCaaccsacaARRRACTAACaaaaaaaaCTAa
                          cCCsaCCsccaARTaTC,        cCCaaCARACCCCCCCCCCCCc
                              cARRAARRA,

    """,
    """



                                                               ,,cs
                                                             ,aRRRRT
                                                            cRRRRRRRs,
                                                          aRRRRRRRARAc
                                                     ,,,,cRRRRRRRATAA,
                                      ,  ,,, ,,,,,,,,  cRRRRRRRRCscCCc
          ,RRRRRRRAc,  ,,,,,   ,,,,, ,,,,,,  ,,,,  ,cTRRRRRRRRAac,,sCc
         ,CRRRRRRRRRRTCc,      ,,,,,, ,,,, , ,,,,  cARRRRRRRRACsc,,aTc
        ,sTARRRRRRRRRRRRAaaCsc,,,,,   ,,,    ,,   ,cRRRRRRRRATs,, ,CAc
          ,aTTARRRRRRRRRRRRRRTc,,,,  ,,,  ,  ,, ,  ,caCTRRRRTCc, ,,sTc
           csssCAARRRRRRRRRRRsc,,,,    ,,, ,  ,  , ,,,,csaCCsc, ,cs,
           aTs,cssCTARRRRRRACc,,,,, , , ,          ,,,,,,,csc,  ,CT,
          ,CAsccccsCAARRRRAscc,,,,,,,             ,,,,,,,,ccc,,,cCC,
          ,ARTc,,,cssCTTCsccc,,,,,   ,,       ,,  ,,,,,,,,,cccsTs,
           csTTs,,cccsCCsccc,,,,,,,  ,   ,,, ,,,,,,,,,,,,,cccccss
             csasc,ccssascc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,c,,ccc,
               sACccssaascc,,,,,,,,,,,,,,,,,,,,,,,,,,ccccc,c,,,cccc,,
               aRAasCCCascc,,,,,,,c,,,,,,,,,,,,,,,,,,ccccccc,ccc,ccsc,
                ,sTTCCasccc,cccc,c,,,,,,,,c,,,,,,,,sRRRRRRAccccc,,ccsss,
                 ,TTsssccccccc,csTCsc,,,,,,,,,,,,aRRCcRRRRRs,,,,,ccccccc,,c,
                 cCCssscccccccsaCTTCacc,,,,,,,,,,CRRs CRRRRs,,,ccccc,,,ccccc
               sATsssscccc,ccsRRR ,RRRTc,,,,   ,,,cTRRRRTsc,,,,csc,,,,,cc,
               cTCsccccccccccCRRRTTRRRAc, ,      ,,cTRTsc,cccc,cc,,,cccc,
             ,caCsccccccc,,ccsTRRRRTsss,                ,ccccccccssccssc
             aRTsscccccccccc,,,,cTCsc      ,cc,,,,, ,,,,csssccccsTTs,cc,
             sTCsssscccccssssc,,,,,,,,,    sATac,,,,,,,,,csTCscccss,
          ,sTTTCCaaaasssssssscc,,,,,,,,,,,,,cccc,,cc,,,ccccsssc,
          ,sTCaCTTCCCCaasssssssccsc,,,,,,,,,,,cc,cccccc,cccsscc
               cAATCCTCTTTTTAAAATTCsccccccccccsccccscccccaaTc
               sTTTTTTTTTTTTTCCCCCCaaasassssssssscsssaCTAACscccccc,
               ,cccccc,cTAAATAAATTTTCCaaasssssCCaaCTATCssasscccccc,,
                        csscscccCARAAAAAAAAAAAAAsssCCas,cccscccc,,,,,,
                                cARRAAAAAAAAAARAc,cccccccccccccc,,,,,,,
                                  ,TACsssssccccc,,,,c,,,cccc,,,,,,,,,,,
                                ,aTCCsccccccc,,,,,,,,,ccccccccccc,,,   ,sc
                                cAATasccccc,,,,,,,,,,,,ccccccssscc,,   cCc
                                cTATacc,,,,,,,,,,,,,,,,,ccccsTTCac,,,,,cCs
                                ,AATCscc,,,,,,,,,,,,,,,,,ccssaCCsc,,,,,caac,
                                ,CTAACsc,,,,,,,,,,,,,,,,,cccssssc, ,, ,cCTac
                                 ,caTTCsc,,, ,,,, ,, ,,,,,,cccscc,,,,,,,sc,,
                                   csCTasc,, ,,,,,, ,,,,,,,,,ccsc,,,,,,,c,
                   ,aCCCsssc,,,cc,,cc,csassc,,,,,,,  ,,,,,,,,,css,  ,,,,,,
                   ,CAAACCCCasscccccc,csCascc,,,,,,,  ,,,,,,,,cccc,,,,,,cc
                   ,CARACsTARRTccccccccaTascc,,,,,,,,,,,,,,,,,,,csasscccCs
                   ,aTTCaaCTRRCccccccccaCasccc,,,,,,,,,,,,,,,,,,,,ccccc,
                    ,sARTTTTRRCc,cccccsCTassc,,,,,,, ,,,,,,,,,,,,ccsc,,
                      ccccsCTTCsssCCs,,sTCssc,,,,,,,,,,,,,,,,,,,,ccsc,
                          ,,,,,,cccs,  sTCsscc,,,,,,,,,,,,,,,,,,,cc,,
                                       sTTsscc,,,,,,,, ,,,,,,,,,,cc,
                                       sTCsssc,,,, ,,,,,,,,,,,,,,cccc,
                                       sTCssscc,,,,,,,,,,,,,,,,,,ccsc,
                                      ,cCassscccccaascccc,,,, ,,,,ccc,
                                    ,sCasssssscsaCTTTTTsc,,  ,,,,,ccc,
                                   sCCsscsssccssaCAAATCsc,,, ,,,,,ccc,
                   ,sassssssssssssaATsscccccccssCCTATTCsc,,,, ,,,,ccs,
                   cARRRRRRRRRARRAATCsccccccsccsaCTTTTasc,,  ,,,,,ccc,
    sRRRRRRARRARARAARRAAAARAAAAAARACsscccccccssssCTTTTasc,,,  ,,,,ccccc,
      cARRAAAAARARARAAAAAAARAAAAAATasscccccccsssssARATCasc,  ,,,,,,cccc,
      ,aAARRRRAAAAAAARARARAAAAARAATscccccccccssscsARAATasc,, , ,,,,,ccc,
        ,sARRRRARAAARAAARAAARRAAATscccccccccccsccsARRATCasc,,,  ,,,,,,ccsc
         ,,,cARRRRRAAAAAAAARRRRATscc,cccccccccsccsARAAATTascc,, ,,,,,,cccc
             ,,,,aRRRRRRRRRRRRRRTc,,,,,,cccccccsaCARRAAAATCssc,, ,,,,,,cc,
                 ,ccc,cccccc,,aACc,,,,c,cccccccsTAAAARRAAATCssc,,,,,,,ccc,
                              cTCc,,,,cccccccccsARARAAAAAATCascc,,,,,,ccsc
                              cTCsccc,,cccccssCTRRRRRRRAATCsscc,,,,,,,cTRT
                              cARACsscccssCCTTATasssssTRRAATTCCCassssCCCas
                              ,CTTascccccsCCCTCc      ,CCCCCCCCCTRRTaTCc
                                                                 TRc

    """,
    """




                                                                   ,,cc,
                                                                  ,CRRRRa,
               cCAAc                                           cCRRRRRRRAc
               CRRRRc,                                     ,,,cTRRRRRRRRTc
             sARRRRRRRRRa,,,,,       ,,,,,,,,,,,,,,,,,,,,,  aRRRRRRRRATCac
             CAAAARRRRRRRRRRs   , ,,,,,,  ,,,   ,,,,     ,ARRRRRRRRACcccac
             ,saTTTARRRRRRRRRCCac, ,,,,, ,,, ,,,,,,, ,cCARRRRRRRRRRTcc,cac
               ,cccsCARRRRRRRRRRR, ,,,  , ,,,,   ,,  ,CRRRRRRRRRRACc,,,cTc
               ,scccsCTRRRRRRRRRRc,, ,,, , , ,, ,, , ,,csCRRRRRRATac,,,cTa
               cACc,,csaTARRRRRTc,,    ,   ,,, ,,, ,,,,,,ccaTCTCCcc, ,,,,
               CRAcc,,ccaCARACc,,,,,   , ,,           ,,,,,cccccc,,  cCc
               aRAacc,ccsaTTa,,,,,,,,, , ,,      ,  ,,,,,,,,,cccc,  ,cCc
                 sRRaccccsccc,,,,,,,,          , ,,,,,,,,,,,,,ccc,,cc,
                 ,cCCCccsascc,,,,,,,,,    ,   ,,, ,,,,,,,,,,,,ccc,csa,
                   ,caaCCCsc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccaa,
                     ,CACacc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,c,,,
                     ,CTCsc,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cc,
                   ,aTCCaccccc,,,c,,,,,,,,,,,,,,,,,caTARTccccc,,,,,,,cccc,
                 ,aCCTCasccc,cCRRRRRRa,,,,,,,,,,,sRRc,CRRRRscc,,,,,,,,ccccc,
                 cAACCaaccccccARRRRRRC,,,,,,,,,,,aRRc aRRRRc,c,,,,,,,cccccsc
                 cTTaascccccsTRRRccRRAcc,,, ,  ,,cRRRRRRRRRc ,,,,,,,,,,,,,,ccc
               ,cCTCCscccc,,csRRRRRRRCc,,,,,    ,,sTRRRARAa,,,,cc,,,,,,,,,,,,,
             ,cTAACCCasccccc,,,cTRRTs,              ,csc, ,cc,,cc,,,,,,,,,c,
             caacaTCCCCasascc,,,,,         cac  ,,,     ,,cscc,ccccccccccc,,
                 cTACCCCCCasccaasc,,      ,TRR,  ,,,,,,,,,,c,,caCTTaccccsc
                 cAATTAARRATCasccc,,,,,,,,,csc,,,,,,,,,,ccccccccssaTTc
                 ,CCaCARRRATTCacccc,,,,,,,,,,,,c,ccc,,,ccccssccssccsa,
                     ,aTCCCCTTTCCaassccccccaaaccccccccccccccsaCAC,
                            cAATTTTCCCCasaaCCaaaascccccaaCTACc,,,,,,
                            ,cccsARAAATTCCCCTTCCCTTATTATCcaCac,,,,,,   ,,
                                ,ccccccCCTCCaaaasaaaCaCCscccc,,,,,,,,,,,,,
                                       cCacscccc,,,,,cccccccc,,,,,,,,,,,,,
                                  ,CTassscccccc,,,,,,,,,,cc,,,,,,,,,,,,,,,,,
                                  ,TACacccc,,,,,,,,,,,,,ccc,ccccc,,,,,,,,,,,
                                  ,CACacccc,,,,,,,,,,,,,ccc,cccscc,,, ,,,,,,
                                  ,CATCscc,,,,,,,,,,,,,,,cccccsCCsc,,,,,,,
                                  ,sTATsc,,,,,,,,,,,,,,,,cccccaCCc,,,,,,,,    ,,c,,
                                  ,caCCcc,,,,,,,  ,,,,,,,cccccccc,,,,,,,c,  ,,ccc,
                                  ,caccccc,,,,,,,,,,,,,,,,,,casc,,,,,,,,c,,,cccc,
                                  ,cac,cccc,,, ,,,,,,,,,,,,,cTCc,,,,,,,,,ccccccc,
                                ,cscc,ccacc,,,,,,,   ,,,,,,,,ccccc,,,,,,,,cccc
                                ,ccc,,csacc,,,,,,,  ,,,,,,,,,,,csc,,,,,,,,cccc
                              ,ccccc,ccsacc,,,, ,,,,,,,,,,,,,,,,,ccc,,,cccccc,
                            ,cCARRAscccsasc,,,,,,,,,,,,,,,,,,,,,,ccaCaccccc,
                          ,cCRACTAATaccsascc,,,,,,,,,,,,,,,,,,,,ccccaccccccc
                          cTRRTccaARA,,cCacc,,,,,,,,,,,,,,,,,,,c,ccccccccc,
                          ,cCATCCTCac  ,,ccc,,,,,,,,,,,,,,,,,,,,cccccccc,
                            cTAAAAs      ,scc,,,,,,,,,,,,,,,,,,,ccccccc,
                                       caasccc,,,,,,,,,,,,,,,,,,ccccc,
                                       aTCaccc,,c,,,,,,,,,,,,,,,cccc,
                                       cTCasccccaaaccc,,,,,,,,,,,cc
                                      ,caaasscaaCTATCsc,,,   ,,,,cc,
                                   caaasssccccsaCTAACs,,,,,,,,,,,c,
                 ,casccsscccacscccaARACscccccccccaTTCsc,,,   ,,,,cc,,
                 cARAAAAARAAAAARRAAATasccccccccccaaaaac,,    ,,,,cccc,
          ,CRRAAAAAAAAAAAAAAAAAAAAAATacccccccccccccsCacc,, ,,,,,,,ccc,
            ,RRRAAAAAAAAAAAAAAAAAAAATaccccccccccccccCCsc,,,  ,,,,,,ccccsARRC,
            cRRRAAAAARAAAAAAAAAAATARAaccccccccccccccCCac,,,  ,,,,,,,cccaTAAs,
          ,aACaCaCCCCCCCAAAAAAARRRRRRTccccccccccccccaTCacc,,   ,,,,,,,,cc,
           ,,,,,,,,,,, ,CRAATARRRRRRRTccccccccccccccccCTCcc,,   ,,,,,,,cc,
                       ,TRRRRRRRRRAccCTacccc,,ccccccccCATCasc,,  ,,,,,,cc,
                        ,cc,c,c,cc,  CRacccc,cccccccaaTAATCascc,,,,,,,,cc,
                                    ,CRCcccc,cccccccTAAAATTCacc,,,,,,,,ccc
                                    ,CACcccc,,ccccCRRRRATTCascc,,,,,,,cTRT,
                                    ,TRTCaaaaaCCCTAAATARAATTCCaasccscaCCCc
                                    ,cCARRATaaaaaaac  ,aaaaaaaCARRRTaaC,
                                       aRRAc                   TRRR,

    """,
    """




                         ,sCsc,
                        cTRRRRC
                       ,CRRRRRRRA,
                       ,TRRRRRRRRTc,
                       ,TRTCTRRRRRRAs,,,,                                 ,,c,
                       ,ARacsTRRRRRRRRTc   ,,,,,,,,,,,,,,,,    ,,,,   ,TRRRRRRs
                       ,ARaccaTRRRRRRRRRTc, ,,,,,,,,,,,,,,,,      ,cTARRRRRRRRC,
                       ,ARCcccsCARRRRRRRRs     ,,,,   ,,,,,, ,,saaTRRRRRRRRRRAac,
                       ,ARCccccsARRRRRRA,,    ,  ,,,  ,,,, ,,,sRRRRRRRRRRRRAAa,
                         ,sCc,csTAATCsc,    ,   ,    ,,, ,,,TRRRRRRRRRRRRAascc
                          TRTcccsCsc,,,,    ,,    ,,  ,,,,,,sARRRRRRRRRTas,,cc
                         ,TRTssssssc,,,,,,,, ,     ,,  ,,,,,cccsTRRRRAACc,,,cc
                            cTTasc,,,,,,,,,,,    ,  ,,, ,,,,ccccssaCACac,,,,TC,
                            sATssc,,,,,,,,,,,,  ,,   , ,,,,,,ccccccsasc,, ,cTT,
                            sRTccccccccc,,,,,,,,,,,, ,,,,,,,,,ccccccc,,  ,ssc,
                          ,,sTCscccccccccc,,,,,,,,,,,,,,,,,,,,,ccccccc,,,ssc
                          cTTasssscccccccc,,,,,,,,,,,,,,,,,,,,cccccccccsCc,
                        sTTTCscsARRRAsccccc,,,,,,,,,,,,,,,ccccc,cccccccss,
                        aTTassRRRcsRRTsc,,,,,,,,,ccsCTCsscc,ccc,,cccccccc,
                       ,aTCssaRRRccTRTCc,,,,,,,,,csTTTAATasc,cc,,cccccccsc
                   cTRATTCassccsRRRRRRRs,,,,,,,,cTRRc RRRRAsccccccccc,cccsac
                   ,caTATTasssccCRRATTsc,,,,,,,,,TRRRaRRRRRs,cc,,c,,cccccsas
                     ,CATTCCaaasc,,cc,          ,cTRRRRRRRAc,,,,c,,,,cccccss,
                      caTTATTTTTs,,,,,,  cac       ,TRRTc ,,,cccc,,,,ccc,cccsc
                       ,CAAARATsc,,,,,, ,ART   ,    ,,,,,,,,csscc,,,,ccccccccc
                         ,CARATTsccccc,ccssc,,,,,,,,,,csscccccccc,,,,ccc,,cccccc,
                          cTTaTTTssscccccc,ccc,,,,,,,,sasscccccccccccccc,cccc,cc,
                              ,TTTTCaaCaCTTCssasccc,cccsssssssssssscccccccc,
                                cARAATTTTTTTTCCassccccccccscsssssssssscscssc
                                 caARRAAAAATTCCCssscccccsssssCCCCTTTTs,,,,,,
                                   cssscsTRRAATATTTTTCCCTTAATassasasc,
                                         sRRRRARRRAAAAAAARRRTcccc,,
                                       csssssssscccccccccssscccc,,,,,,,
                                     sTCCscccccc,c,cccccc,ccccccc,,,,,,,,,
                                    ,CATascccccc,,,,,ccccccccccc,, ,,,,,,,
                                    ,CATascc,,,,,,,,,,,ccccccsc, ,,, ,,,,,
                                     aTCssc,,,,,,,,,,,,cccccsssc,c,,,,,,,,
                                     sCascc,,,,,,,,,,,,cccccsasscc,,,,,,           ,,
                                     sTasc,,, ,,,,,,,,,cccsssasc,,,,,cc,       ,,,csc
                                     aTasc,,,,,,,,,,,,,cccsssac,,,,,,,c,      ,sscss,
                                     sassc,,, ,,,,  ,,,,,cccccc, ,,,,,      ccccsc,
                                     cassc,,,,,,,, ,,,,,,,csscc,,,,cc,     ,csscsc,
                                    ,csaac,,,,,,,,,,,,,,,,cCac,,,,,,,    ,csccccss,
                                  ,ssccsscc,,,,,,,,,,,,,,,,,,cc,,,,    ,cssscccsaac
                                   ccsssssc,,,,,,,,,,,,,,,,,,sc,,,,   ,csscsccscc,
                                   ,csCassccc,,,,,,,,,,,,,,,,ccaaccccsssscccsc,
                                   csCCasssccc,,,,,,,,,,,,,,,,csaccCACsscccssc
                                  ,sCCCasscccccc,,,,,,,,,,,,,,,ccccaTascscccsc
                                    ,sTTaasssccccc,,,,,,,,,,,,cccccsssscccsc
                                     csCTCasssscc,c,,,,,,,,,,,cccccccscssc,,
                                       caCCasssscccc,,,,,,,,,,,ccccssc,ccc
                                         cTCssaaTTCsc,,,,  ,,,,ccccaac
                                     cCscaCCsssCTTTCc,,,,,,,,,,,cccc,
                   ,caasasssasasasssCARTaassssasaCTTc,,, ,,,,,,cccc
                   cRRRRRRRRRRRRRRRRRRACsssssssasaCTc,,,  ,,,,,ccsc,
                   cARRARAAAARAAAAARARAassccccsscsCCsc,   ,,,,,cccccc,
                 cRRRRRAARARAAAAAAAARRACssccccssssCTsc,,,,,,,,,,ccccc,
                 cTTCTARRRRRRAAARRRAAAACsccccccscsTTas,,,  ,,,,,,ccsc, ,,c,,c,
                     ,CTTTTTARARRRRRRRRCsccccccccsTTCac,,   ,,,,,ccccccCARAAAT,
                      ,,,, ,CRRAARRRRRRTcccccccccssaCCsc,   ,,,,,,,ccccsscc,,,
                             ,CRRRRRRRRATCssccccccccssCTCscc,,, ,,,,,,ccc,
                              ,ccccsCTRATCssscccccccccssCTCscc,,,,,,,,ccc,
                                     TRATasscccccccccccssCCascc,,,,,,,ccc,
                                    ,TRACssccccccccccsRRRCssccc,,,,,,,ccs,
                                     cCTATTAAACaaTTAARRRRTasscc,,,,caaCTTs
                                       cCCCARACCaTRRRRTassCTTTasssaaCTCTTc
                                                          cARRRRRRRc

    """,
    """



                                 ,
                               ,aRAs,
                              cTRRRRRc
                              cRRRRRRRRc
                              cARRRRRRRA,
                              cCTCTRRRRRRT,
                              cTCsaTRRRRRRRs, ,   ,,,,,,,
                              cATccCARRRRRRRc,,,  ,,,,,, , ,
                              aRRscaCARRRRRRac,  ,,,,,,,,,,,,,,,        ,saTTTac
                              aRRsccaTRRRRRR, ,, ,,,,   ,,,,,,,,,,     cARRRRRRRc
                               ,csscsTAACac,      ,, ,   ,,,,,   ,cRRRRRRRRRRRRRc
                                ,AAacsccc,    , ,   ,,  ,    ,sRRRRRRRRRRRRRRRTs,
                                cRRaccc,,,,,   , ,, ,,,  ,,,,,TRRRRRRRRRRRRRATCs,
                                cRAscccc,,,,,         , ,,,,,cccTRRRRRRRRATCccCC,
                                ,ccccccc,,,,,          ,,,,,,cccaRRRRRRRATac,cCT,
                                 ,,sscccc,,,,, ,,       ,,,,,cccccsTAAACssc,,,cc,
                               ,cCTaascscc,,,,,,,,, ,,,,,,,,,,,ccccccsscc,,,cc
                              cCTCCaasscccc,,,,,,,,,,,,,,,,,,,,cccccsc,,,, ,CT,
                            caTTCCTRRCsccc,,,,,,,,,,,,,,,,,,,,,cccccccc,,,,csc
                          cCTTCCRRRssRRC,,c,,,,,,,,,,,,,,,,cccccccccccssssCCc,
                          aRATCCRRRcsRRT,,c,,,,,,,,c,,c,cccccccccccccccsaCTCc,
                          sTTTCaTRRRRRRT,,,,,,,,ccsaaaaCcc,,cccccc,ccccccccccc
                          aRTTCaaTRRRRRs,,,,,,,ccaTAaaRRRsccc,c,,,,ccccccccccc
                          ,caTTCasaAAac,,,,,  ,,cCRRAARRRAscccc,,c,ccc,ccccsac,
                            cAATCacc,,,,,,     ,,cARRRRRRCscccc,,,,cccccccsaCs,
                            sAATascc,,,,,        ,CRRRRRRc,,,cc,,,,,ccccccsaCa,
                              sAACaaccc,,sCc,     ,,,ccc,,,,,c,,,cccccccccccsc
                              ,CTTCaacc,caTc,,,,       ,,,,,,cc,,cccccccccccc,
                                ,aTTTCCaaccccc,,,,,,caTTTscc,,,cc,,,,cc,,ccccc,
                                  ,CATTTTTCCaasscccccccccc,ccccccccccccc,ccccccc,
                                   ,sTRATTTCCaaasccccccccscssaaCCTTacccccccc, ,,
                                     caTRRAATTTCCaassaaCCCCCTTTARRRTCaaasc,,
                                       CRRRRAAATCCCCCaCCTCCTTCCTTTTTTTCCCc
                                       aACassCRRRRRRAARRRRRRRRRRT,
                                       sTCscccsccccccccssaassssccc,
                                       aTTasccc,,,,,,,ccccccccc,,cc,
                                       sTCsccc,,,,,,,,cccccccc,,,,,,,
                                       ,,cssc,,,,,,,,,cccccc,,,,,,,,,,,
                                         ,cc,,,,,,,,,,cccsccccc,,,,,,,,,
                                         ,cc,,,,,,,,,,csaas,,,,, ,,,,,,,           ,,
                                         ,cc,,,,,,,,,,ccaac   ,  ,,,,,,,          ,s,
                                       casc,,,,     ,,,,,,, ,,,,,,,,,,c,        ,css,
                                       sTsc,, ,,,, ,cc,,,  ,,,,,,,,,,,,,        csss,
                                       sTac,, ,,,, ,aTc, ,,,,ccccc,,,      ,csscsccc,
                                       sCas,,,,,,, ,,c,,,,,ccsaassc      ,csscccsc,
                                       cTssc,,,,,,,,cc,,,,cccccsssc,    ,ccscsscsc,
                                       cCascc,,,,,,,sasccccc,,ccccc   ,cssscsssc,,
                                       cTCsccc,,,,,,csccc,,,,,,cccc,,caaccsccsCa,
                                       cTCsscc,,,,,,,,,,,,,,,,c,cccccsassccccsATc
                                         cassccc,,,,,,,,,,,,,,cccccccsssccccsc,
                                         caascccc,,,,,,,,,,,,,,cccccssssccscc,
                                        ,sTCssssccc,,,,,,,,,,,cccccccsssccc,
                                       sTTaaassaCTCscc,,,,,,,,,,c,csac,csc
                       ,sCCa,          cCassassaTTTCc,,,,,,,,,,ccccaTc  ,
                        CRRRCsssssssscccssccssssCTTTc,,,, ,,,,,,cccc,
                       ,TRRARRRRRRRRATassccccssssCTCsc,,   ,,,,,ccc
                     ,TRRRRAAAAAARRRACssccccccssssCCs,,,  ,,,,,ccccc,
                     cARRRAAARAAAAARAascccccccsssaCTac,  ,,,,,,,ccssc,
                     ,sTARRRRAARAARRRCsccccccccccaTTac,,  ,,,,,,cccss, ,,,c,c,
                        sATTARRAAARRRAascccccccccsCTasc,,  ,,,c,cccccccCRRAARC,
                        ,,,,CRRRRRRRRATsccccccccccsaaac,,  ,,,,,,ccccccsacc,,,
                            ,,c,,,c,cARTssccccccccccsscccsc,,,,,,,,,,cccc,
                                     TRAAassccccccccccaTTTCsc,,,,,,,,,ccc,
                                    ,TRRRTassccccccccsTRACCasc,,,,,,,,ccc,
                                    ,TRRRAasccccccccCARATassccc,,,,,,cccs,
                                     cassTAACTATCCARRRRRATTCacccccccsaaTTs
                                         cCCaARRCTRRTCsCaaTAAATCaCCscaCTCc
                                                          cARRRRRRRc

    """,
    """



                               ,
                             ,aRTc,
                            cTRRRRR,
                             ,TRRRRRR, ,,
                              sRRRRRRT,,,
                              cTRRRRRRRT,,,,
                              cCTCARRRRRRT, ,,,,,,,,,,,,, ,,,,
                              cTTaTARRRRRRTc,,,,,,,,,,, ,,,,,,,        ,sc,
                              aRAasCARRRRRRC, , ,,, ,   ,,,  ,,  ,,sCTARRRRC,
                              aRRasaARRRRRs,, ,,,,,  ,,,,,,,,     cRRRRRRRRR,
                               ,caCaCRRCc,,   ,,,,,,,,,,,   ,,aRRRRRRRRRRRRT,
                                cRRCssc,     ,,,  ,,    ,,,,CRRRRRRRRRRRRATc
                                cRRTsc,,,,   ,,,  ,,, ,,,,,cARRRRRRRRRRRATac
                                   sascc,,,,    ,,   ,,,,,cccsTRRRRRRRATCsc,
                                 ,cssscc,,,,      , ,,,,,,ccccaARRRRRATascc,,
                                ,TTascc,,,,,        ,,,,,,ccccccsCATTasc,casc,
                               ,caCasscc,,,,,,,, ,,,,,,,,,,,ccccccccsc,,,caac,
                              cTTTTasscc,,,,,,,,,,,,,,,,,,,,ccccccsss,,,,cccc,
                              cAACCCassccc,,,,,,,,,,,,,,,,,ccccccccssc,cCac,cc,,
                            ,aTARRRRRTcccccccc,c,,,,,,,cccccccccccccscccsccccccc
                            sAAARRRRRAccscccccccccccc,cccccccccccccccsscccccccc,
                            sTTCRRRRRTcccccccccsaaaassc,c,,,cc,c,cccccccscccccc,
                            sATCARRRRCccccccccsTRRRRRATccccc,cccc,ccccccccccc,,
                            ,caTATTACc,,,,,,,csTRRRRRRRCsccccc,,cc,cccccccscc,
                              cAACsccc,,    ,,,csTRRRRRaccccc,,,,,ccccccccsscc
                              cAATCscc,,       cARRRRRAc,cc,,,,,,,,,ccccccsssc
                                cTTac,cARs   , ,,,,ccc,,,,,,c,,ccccccccccccssc
                                ,TTCsccRRa, ,,,      ,,,,,,cc,cc,,,ccc,cccccsc
                                ,CTTTCacccc,,,,,,,,cCTTCsccc,cc,,,c,c,,cccccc,
                                  ,TAATTTCaassccccccccccccccccccccccccccccc,
                                   csTRRATCCCasssccccssssssssssaaaascsssssc,
                                     csscCAATTTTCCCaCCTTTTTTTTTTAAAATs,,,,,,
                                         aRRAATTTTTTTTTATTAAAAAARRRRAc
                                         cCasTRRRRRRRARRRRTsccccccc,
                                         sACcccccccccccccsccccccccccc,
                                         sTac,,,,,,,,,,,cccccccssscss,
                                           ,cc,,,,,,,,c,ccccccccccccc,
                                         ,,,,,,,,,,,,,,,,cccccccccccc,
                                         csc,,,,,,,c,,casssscc,,ccccc,
                                         ,cc,,,,,c,,,,cccccascc,,,,,,
                                         ,cc,, ,cc,,, ,,,,caasc,,,,,,
                                         csc,, ,cc,,, ,,,,,,, ,  ,,,,,,,        ,cas,
                                        ,ccc,, ,ccc,,,,,,,,     ,  ,,,c,       ,casc,
                                       sTac,,, csCasscc,,,,,,,,,,,,,,,,,   ,csssc,
                                       cCsc,,,,  ,aTCassssssccc,,,ccc, ,csscccsc
                                       casc,,,,, ,cccc,,sTCCCascccsaCc,ccsccccsc,
                                       casc,,,,,,,, ,, ,,cccccccccssassscccssc,,
                                       casccc,,,,,,,,,,,,,,,,,,ccccccscscssc,,
                                       cCscccc,,,,,,,,,,,,,,,,cccccsscscsscc
                                       sTascc,,,,,,,,,,,,,,,,cccccssccccs,
                                       sTTaccccc,,,,,,,,,,,,,,cccssscccc,,
                                      ,caaasccsssccc,,,,,,,,,,,ccsscccc,
                                     sTssccsssaCTTTac,,,,, ,,,,cccsc,,
                                     cssccccssaCTTTCc,,  ,,,,,,cccc,
                        cssssssssssccssccccccsssCCTCc,,,  ,,,,,cccc
                       ,TRRRRRRRRRAATscccccccscssaTCc,,,, ,,,,,ccsc,
                     cARRRRRRAAAARATCssccccccssssaCCsc,   ,,,,,ccccTRs
                       ,ARRRAAAARRARAasccccccssssaCTac,, , ,,,,,cccss,
                        cCARAAAAAARRAasccccccccccaTTas,,   ,,,,,ccccc, ,,cc,
                          sAARRRRARRACsssccccccccsCTCscc,    ,,,,,cccccCARAC,
                           ,TRRRRRRRRCsscccccccccssaCCsc,,   ,,,,,,ccccsasc,
                             c,,,,,,,sCsscccccccccccTATasc,,, ,,,,,,,,,cc,
                                   csCCaccccccccccsCRRRRRCascc,,,,,,,,ccc,
                                  ,ARTCasscccccccsCARRRRRTCCas,,,,,,,,cccc
                                  sRRRCassccc,,sCTAAARAAACCasc,,,,,,,,ccc,
                                  ,ARAATTARRATCTAARRRRRRACCascc,,,,csaCTTs
                                     sCCCARRRATaCaCCaaaaTATTaaasscsARRCCTs
                                                        sRRRRRRRRRRRRs

    """,
    """



                                     ,,
                                    ,ARRCc,
                                    ,RRRRRAc
                                    ,TRRRRRRCc,
                                    ,CRRRRRRRC,
                                     sTARRRRRRc,,,                            ,,
                                     caaCRRRRRRRc,,,,, ,,,,,,,,   ,,,,,,,,,sRRRRRRs
                                     cassARRRRRRc ,,,,, ,,,,,,,,,,,    ,aTARRRRRRRs
                                     cCccCARRRRR,   ,,   , ,,,, ,,,cssaRRRRRRRRRRTc
                                     aTccCTac,c,   , ,   ,       ,cARRRRRRRRRRRRAs,
                                    ,RRTccsc,,,            ,,,,,ccCRRRRRRRRRRACaTTc
                                     ,ccacccc,,,          ,,,,,cccsTRRRRRRRATac,,,
                                       cacccc,,      ,   ,,,,,,cccccCRRRRRATscc,
                                    ,sTascccc,,,,,,,  ,, ,,,,,,ccccccssCATCc,,,,
                                    ,aTCssccc,,,,,,,   ,,,,,,,,,,ccccccsCCcc,,cc,
                                     cTCscccc,,,,,,,,,,,,,,,,,,,,,cccccccc,, ,aCc
                                   ,cARRRCccc,,,,,,,,,,,,,,,,,cccccccccccc,,ccssc,
                                  ,cARRRRRccc,,,,,,,,,,,,,,,cccccccccccccc,csasccc,
                                ,sTAAAARRRccc,,,,,cccsaasccccccccc,ccccccccccccccc,
                                ,TTCARRRRC,,,,,,,csscccaRRRscc,cc,,ccccccccccccccc,
                                cTCsTRRRAc,,,,,,,,aasccCRRRTcc,c,,,ccccccccccccccc,
                              cTATCscccc,,,,,,  ,,caRRRRRRRTsc,cccc,,cccccccccccc,,
                              ,csTTTacc,,,,,    , ,cARRRRRAsc,,ccc,,,ccccccccccccc,
                                cARTTscc,,,,c,,    ,caTAC,,,,,,,cc,,,ccccccccccccc,
                                ,aTTCCscccccsc,,,,,   ,,cccc,,,ccc,cccccccccccccc,
                                  ,CTCCssccccc,,,,,,,,cCCCcccc,ccc,c,,ccc,,ccccc,
                                  ,TRATTTCCCascccccc,,ccccccc,,c,,,cc,,,,,cccccc
                                  ,aTAATTTTTTCassscccccccccccccccccccc,ccc,ccccc,
                                     aAAAAATTTCCCscccccccssaaaTTAAACsccccccccccc,
                                       aRRAARATTTCCCsssssaassssssssssssscccccc
                                       ,cccCRRAAAAATTCCCCTTTCCCCCCCCCCaCaaac,
                                          ,sTTTTTTAAAAAAARRRAAAAAAAAARACccc,
                                         cTTCssssCTAAAARRRRRRRRRRRRRRRRs
                                         cTCsccccccccccccsssasssccc,
                                         sRCc,ccccccccccccccccccccccc,
                                         cTs,,,,c,,ccccc,ccccccccccss,
                                            ,,,,,,,,csc,,,,cccccccccc,
                                          ,,,,,,,,,,sCc,,,,,,ccccccccc,,
                                         ,cc,,,,,,,,cac,,,, ,cccccccccc,
                                         ,cc,,,,  ,,csc,,,,,,cc,,cccc,,       ,,
                                         ,cc,,,,, ,,cscc, ,,,cc,,,ccc,        cc,
                                       sTacc,,,,,  ,sTsc,,,,,,,,,,,cc,    ccccsc,
                                       aATcc,,,,,, ,cascc,,,,,,,,,,,,,   ,cscccc
                                       cCscc,,,,,,,, ,cCacc,,,,,,,,,,cccsccccc
                                       cTcc,,,,,,,,, ,cCCacc,,, ,,,,,ccccccccc
                                       cacc,,,,,,,,,,,,csTCcc,,,  ,,cccccccc,
                                       cacc,,,,,,,,,,, ,,csascc,,,cccccccc,
                                     ,cccccc,,,,,,,,,,,,,,,ccccccccccccc,
                                     aTasccc,,,,,,,,,,,,,,,,,,,cccccccc,
                                    ,aATcccc,,,,,,,,,,,,,,,,,,ccccccc,
                                     sTacccc,ccc,,,,,,,,,,,,,ccccccc,
                                    ,cccccccccssccc,,,,,,,,,,,cccc,
                                  cTTc,,,,ccssaTAACsc,,,,  ,,,,cc
                            cTACTCCCs,,,,,,cccaTAATac,,, ,,,,,cccc,
                             cccaRAsc,,,,,,,ccsaTTTCc,,,   ,,,,cccc
                                cTTsc,,,,,,ccccsCTTCc,,,  ,,,,,cccc,
                       ,TRARRRRAAATscc,,,,,ccccccsCCsc,,,  ,,,,,cccCRRRRRa
                         ,TRRRAAATCscccccc,ccccccsCTacc,,   ,,,,cccccTARRRRC,
                          cCAARAATacccccccccccccccCTacc,,  ,,,,,,cc,ccTARAAa,
                            cTAATsccccccc,ccccccaTARTscc,,   ,,,,,,c,,caAs
                             ,sATscc,,,,cc,ccccCRRRRAasc,,,   ,,,,,,cc,cs,
                              cTTcc,,,,,c,ccc,cCRRRRRRACscc,,,   ,,,,,ccc,
                              cTCccc,,,,,ccccccCRRRRRRRATTCscc,,,,,,,,,cc,
                              cTTsccccc,,ccccccTRRRRRRRAATTCscc,,,,,,,ccc,
                              cRATasccccc,csCRRRRAAAAAAAATTCsccc,,,,,,ccsc
                              cRRAATTTCCCTTTAARAcaAAAARRAAATCccc,,,,,cCTAa
                              cCCCaCCCCCCCCTCc    cCCCaCaCTRATaasccsCCCTCc
                                                          cARRARRRRRRc

    """,
    """





                                     cc
                                    ,RRRRTc,
                                    cRRRRRAs,
                                    ,TRRRRRRRC,                             ,,,,TRa
                                     sTARRRRRRAs,,,,                ,,,,,  cRRRRRRRAc
                                     cCTARRRRRRRCc,,                   ,csTRRRRRRRRAs
                                     csssARRRRRRAs, ,,,,,,, ,,,,, ,,csCARRRRRRRRRACs,
                                     cccsCRRRRs,,,,,,,, ,,,  ,,   ,sARRRRRRRRRRRAC,
                                     csccsTTCc,,,       ,,,,,,,,,,sRRRRRRRRRRRACs,,
                                     aCc,csccc,,,         ,,,,,,cccCRRRRRRRRACs,,,
                                    ,CAsccsscc,,,,  ,   ,,,,,,,,cccccsCARRRATs,,cc,
                                    ,ARTassccc,,,,,,,,, ,,,,,,,,,,cccccCAATac,,,sTc
                                     csaascccc,,,,,,,,,,,,,,,,,,,,,ccccsCCsc,,,,,c,
                                     ,,sCssccc,,,,,,,,,,,,,,,,,,,,,,cccccc,, ,cc
                                     aARRAascc,,,,,,,,,,,cc,ccccccc,cccccc,,,,ssc
                                     sRRRRCcc,,,,,,,,,,cccccc,ccccccccccccccssscc,
                                   cARRRTRRRc,,,,,,,,sRRRRRACccccc,,,cccccccsccccc,
                                ,saaRRRRRRRA,,,,,,,cRRTcARRRRCcccc,cc,c,cccccccccc,
                                cTTaTRRRRRRa,   ,  cRRC aRRRRTcccccccc,,cc,ccccccc,
                                ,TTasscc,,,,,,,,,    cRRRTRRRc,,,ccc,,ccccccccccc,,
                              ,csTTasscc,,,,,,  ,,   ,CRCccCs,,,,cc,cc,c,cccccccc,,
                              sARTTCasscc,,,,,,,,,,,,   ,cccccccc,,,,,,,c,c,cccccc,
                              ,sTAATCsscccccccc,,,,,,,,,csaascccc,,,,,,ccc,,ccccsc,
                                cTATTCassssssscccccc,,,,,,,,c,,,,,,,ccc,,,,,,ccccc,
                                  cTATTCCCCCTCssssscccccccsCTTTTTasccc,cc,,ccccccc,
                                  ,aTATTTCTTTTCCasssccccccsTTTTTTCsccccccccccccccc,
                                     aAAAATAATCCCCssscsccccccccccccccccccccccccc
                                       aRRAAAAAAATTTTCCCCCasasCssssssssscccscc
                                       ,sTRRRAAAAAAATTTTTTTCTTTTTCCaasaaCCCsc
                                         cAATTTAARAAAAAAAAAAARRRRRAAAAACccc,
                                         cCasssTARATAAATTTAARRRRRRRRRRRs
                                       sTCCssssssssaCCCsCCCCCCCsc,
                                       CRTsscccccccccscccccssssccc,
                                       sTCasccccccccccccccccccc,ccc,
                                         cCs,,,,,,ccccccccccc,,,,ccss,
                                         cTs,,,,,,,,,,,,cccc,,,,,,csscc,
                                       ,csac,,,,,,,,,,,,,cc,,,, ,cccsss,
                                      ,cccsc,,,,,,,,,,,,csc,,,, ,cccccc,
                                     ccc,ccc,,,,,,,,,,,,casc,,,,,,ccccc,
                                   ,,,cCTaccc,,  ,,,,,  cCCcc,   ,cccsTCsssc
                                  ,,ccsCTCscc,,,,,,, ,,csCac,,   ,c,csCCssc,
                                ,sCsCTATasscc,,,,,,  ,sATscc,,,,,,,cccccc,
                                ,sTRRATassccc,,,,,,, ,sTTasc,,,,,,,ccsc,
                                 ,cARATCsscc,,,,,,,, ,sATscc, ,cccccsss,
                                   ,cTTassccc,,,,,,,,,ccaTTassccccssc,,
                                     sTCssccc,,,,,,,,,,,,ssssssccccc,
                                     sTCsscc,,, ,,,,,,,,,,,,,,,ccsc,
                                  ,CATassccc,,,,,,,,,,,,,,,,,,,cc
                                  ,TACsscccc,,,,,,,,,,,,,,,,,,cc,
                                  cCTsccccc,,,,,,,,,,,,,,,,,,cccc
                                cAATCsc,,,cccccssscccc,,,,,,,,ccc
                            cTTaTAACacc,,,cccsCCTTCscc,, ,,,,,ccc
                             cCRATTssc,,,,,,csTTAAATsc,,   ,,,,cc,,cs,
                              cTATCscc,,,,,,,cCTAATCsc,,   ,,,ccccsARs
                          TRRAATTCscc,,  ,,,,,csARTCcc,,, ,,,,cccccTRRARRC
                            sTTCsscc,, ,,,,,,,csAATscc,, , ,,,,,cccccRRRRa
                           ,sCCascc,,, ,,,,,,sTARRTacc,,  ,,,,,,cccccTRRRa
                          aATsssc,,,, ,,,,,,,TRRRRACsc,,,  ,,,,,,,ccc,csAs
                          sTCsccc,,, ,,,,,,,,TRRRRACCscc,   ,,,,,,,,ccccsc
                          cCscc,,,, ,,,,,,,,cCRRRRRTTCscc,,,   ,,,,,,,ccccc,
                          sCs,,,,,,,,,,ccccsTAAAAAARRRRTCCsscc,,,,,,,,,cccsc
                          sTs,,,,,,,,,ccccsTARRAAAARRRRAAATCascc,,,,,,,cccc,
                          TRCc,,,,,,,,cccsCTRRRRRAAAAAAAATTascc,,,,,,,,cs,
                          TRACaaaasccccaTTATsasasCARRARRRAATascc,,,csaaCTs
                          cCTCCCTTsc,,csTTC,      cCaaaaaCTRACsasssARAaTTc
                                                          cARRARRRRRRc
                                                          
    """,
]

def get_remote_time():
    try:
        key = paramiko.RSAKey.from_private_key(io.StringIO(private_key))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, pkey=key)
        stdin, stdout, stderr = ssh.exec_command("date")
        time = stdout.read().decode().strip()
        ssh.close()
        return time
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to fetch time: {str(e)}")
        return "Error"

def refresh_time():
    time = get_remote_time()
    time_label.config(text=time)
    
def cycle_ascii_art(index=0):
    art_label.config(text=ascii_arts[index])
    next_index = (index + 1) % len(ascii_arts)
    root.after(100, cycle_ascii_art, next_index)

def create_gui():
    global root, art_label, time_label
    root = tk.Tk()
    root.title("itsabouttime")
    root.configure(background='black')
    
    window_width = 650
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")
    
    title_label = tk.Label(root, text="""
.__  __              _____ ___.                  __    ___________.__                
|__|/  |_  ______   /  _  \\_ |__   ____  __ ___/  |_  \__    ___/|__| _____   ____  
|  \   __\/  ___/  /  /_\  \| __ \ /  _ \|  |  \   __\   |    |   |  |/     \_/ __ \ 
|  ||  |  \___ \  /    |    \ \_\ (  <_> )  |  /|  |     |    |   |  |  Y Y  \  ___/ 
|__||__| /____  > \____|__  /___  /\____/|____/ |__|     |____|   |__|__|_|  /\___  >
              \/          \/    \/                                         \/     \/ 
        """, font=("Courier", 8), justify=tk.LEFT, background="black", foreground="green")
    title_label.pack(pady=10)
    
    art_label = tk.Label(root, text=ascii_arts[0], font=("Courier", 4), justify=tk.CENTER, background="black", foreground="green")
    art_label.pack()

    time_label = tk.Label(root, text="Fetching time...", font=("Helvetica", 14), background="black", foreground="green")
    time_label.pack(pady=10)

    refresh_button = tk.Button(root, text="Refresh Time", command=refresh_time, background="black", foreground="green")
    refresh_button.pack(pady=10)

    # Start cycling ASCII art
    root.after(1, cycle_ascii_art)

    # Fetch initial time
    refresh_time()

    root.mainloop()


if __name__ == "__main__":
    create_gui()
