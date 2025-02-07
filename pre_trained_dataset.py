def send_train_set():
    emotionSet = [{'anger': 0.041226,
                   'disgust': 0.048838,
                   'fear': 0.032088,
                   'joy': 0.640749,
                   'sadness': 0.064078},
                  {'anger': 0.097328,
                   'disgust': 0.056914,
                   'fear': 0.096361,
                   'joy': 0.630668,
                   'sadness': 0.589699},
                  {'anger': 0.112036,
                   'disgust': 0.083707,
                   'fear': 0.452798,
                   'joy': 0.618979,
                   'sadness': 0.501347},
                  {'anger': 0.533945,
                   'disgust': 0.089385,
                   'fear': 0.130332,
                   'joy': 0.620318,
                   'sadness': 0.579353},
                  {'anger': 0.017262,
                   'disgust': 0.009342,
                   'fear': 0.023326,
                   'joy': 0.614321,
                   'sadness': 0.039315},
                  {'anger': 0.520355,
                   'disgust': 0.545665,
                   'fear': 0.116037,
                   'joy': 0.552054,
                   'sadness': 0.526169},
                  {'anger': 0.535949,
                   'disgust': 0.107123,
                   'fear': 0.151824,
                   'joy': 0.487562,
                   'sadness': 0.533195},
                  {'anger': 0.136133,
                   'disgust': 0.054715,
                   'fear': 0.126473,
                   'joy': 0.596397,
                   'sadness': 0.524608},
                  {'anger': 0.12781,
                   'disgust': 0.088902,
                   'fear': 0.117208,
                   'joy': 0.581818,
                   'sadness': 0.541787},
                  {'anger': 0.069431,
                   'disgust': 0.036108,
                   'fear': 0.090421,
                   'joy': 0.679301,
                   'sadness': 0.1436},
                  {'anger': 0.537632,
                   'disgust': 0.076903,
                   'fear': 0.46242,
                   'joy': 0.546807,
                   'sadness': 0.542779},
                  {'anger': 0.089874,
                   'disgust': 0.036779,
                   'fear': 0.106785,
                   'joy': 0.55675,
                   'sadness': 0.530379},
                  {'anger': 0.072773,
                   'disgust': 0.036282,
                   'fear': 0.078925,
                   'joy': 0.629194,
                   'sadness': 0.090839},
                  {'anger': 0.150444,
                   'disgust': 0.124924,
                   'fear': 0.09779,
                   'joy': 0.626831,
                   'sadness': 0.558114},
                  {'anger': 0.557211,
                   'disgust': 0.054175,
                   'fear': 0.107395,
                   'joy': 0.55063,
                   'sadness': 0.459126},
                  {'anger': 0.064043,
                   'disgust': 0.054872,
                   'fear': 0.048699,
                   'joy': 0.619996,
                   'sadness': 0.107458},
                  {'anger': 0.620735,
                   'disgust': 0.039361,
                   'fear': 0.551563,
                   'joy': 0.570263,
                   'sadness': 0.088743},
                  {'anger': 0.528082,
                   'disgust': 0.063732,
                   'fear': 0.082191,
                   'joy': 0.639538,
                   'sadness': 0.540755},
                  {'anger': 0.077684,
                   'disgust': 0.0566,
                   'fear': 0.067829,
                   'joy': 0.672832,
                   'sadness': 0.07786},
                  {'anger': 0.043305,
                   'disgust': 0.028549,
                   'fear': 0.04966,
                   'joy': 0.68175,
                   'sadness': 0.104987},
                  {'anger': 0.551473,
                   'disgust': 0.473876,
                   'fear': 0.519488,
                   'joy': 0.65574,
                   'sadness': 0.494794},
                  {'anger': 0.062897,
                   'disgust': 0.530556,
                   'fear': 0.09313,
                   'joy': 0.623301,
                   'sadness': 0.116718},
                  {'anger': 0.499469,
                   'disgust': 0.153306,
                   'fear': 0.097635,
                   'joy': 0.565208,
                   'sadness': 0.508301},
                  {'anger': 0.548653,
                   'disgust': 0.113904,
                   'fear': 0.086122,
                   'joy': 0.645639,
                   'sadness': 0.503645},
                  {'anger': 0.048966,
                   'disgust': 0.057811,
                   'fear': 0.106422,
                   'joy': 0.63678,
                   'sadness': 0.164226},
                  {'anger': 0.556495,
                   'disgust': 0.133057,
                   'fear': 0.142437,
                   'joy': 0.575018,
                   'sadness': 0.146935},
                  {'anger': 0.484081,
                   'disgust': 0.069207,
                   'fear': 0.479538,
                   'joy': 0.567443,
                   'sadness': 0.555651},
                  {'anger': 0.069786,
                   'disgust': 0.668928,
                   'fear': 0.112381,
                   'joy': 0.647004,
                   'sadness': 0.097025},
                  {'anger': 0.51825,
                   'disgust': 0.083963,
                   'fear': 0.169439,
                   'joy': 0.556046,
                   'sadness': 0.551757},
                  {'anger': 0.643496,
                   'disgust': 0.0849,
                   'fear': 0.202932,
                   'joy': 0.004628,
                   'sadness': 0.565787},
                  {'anger': 0.444715,
                   'disgust': 0.035095,
                   'fear': 0.610423,
                   'joy': 0.665558,
                   'sadness': 0.613082},
                  {'anger': 0.058728,
                   'disgust': 0.042806,
                   'fear': 0.043391,
                   'joy': 0.664077,
                   'sadness': 0.075259},
                  {'anger': 0.594919,
                   'disgust': 0.058995,
                   'fear': 0.112997,
                   'joy': 0.619908,
                   'sadness': 0.602652},
                  {'anger': 0.57233,
                   'disgust': 0.141167,
                   'fear': 0.109165,
                   'joy': 0.592284,
                   'sadness': 0.564946},
                  {'anger': 0.075031,
                   'disgust': 0.028417,
                   'fear': 0.110723,
                   'joy': 0.585322,
                   'sadness': 0.524253},
                  {'anger': 0.548044,
                   'disgust': 0.048809,
                   'fear': 0.135264,
                   'joy': 0.471318,
                   'sadness': 0.495805},
                  {'anger': 0.087791,
                   'disgust': 0.060036,
                   'fear': 0.067796,
                   'joy': 0.69265,
                   'sadness': 0.110671},
                  {'anger': 0.060816,
                   'disgust': 0.042516,
                   'fear': 0.069777,
                   'joy': 0.71779,
                   'sadness': 0.10614},
                  {'anger': 0.10092,
                   'disgust': 0.085246,
                   'fear': 0.081196,
                   'joy': 0.636779,
                   'sadness': 0.135925},
                  {'anger': 0.485332,
                   'disgust': 0.077884,
                   'fear': 0.086972,
                   'joy': 0.665762,
                   'sadness': 0.087845},
                  {'anger': 0.120773,
                   'disgust': 0.074011,
                   'fear': 0.090141,
                   'joy': 0.530177,
                   'sadness': 0.571103},
                  {'anger': 0.073482,
                   'disgust': 0.095967,
                   'fear': 0.087682,
                   'joy': 0.601025,
                   'sadness': 0.110386},
                  {'anger': 0.100001,
                   'disgust': 0.074749,
                   'fear': 0.095777,
                   'joy': 0.662631,
                   'sadness': 0.085776},
                  {'anger': 0.05539,
                   'disgust': 0.036302,
                   'fear': 0.069646,
                   'joy': 0.530548,
                   'sadness': 0.167181},
                  {'anger': 0.09863,
                   'disgust': 0.093252,
                   'fear': 0.135127,
                   'joy': 0.643317,
                   'sadness': 0.600757},
                  {'anger': 0.537177,
                   'disgust': 0.087605,
                   'fear': 0.558914,
                   'joy': 0.557149,
                   'sadness': 0.583528},
                  {'anger': 0.082374,
                   'disgust': 0.02421,
                   'fear': 0.045754,
                   'joy': 0.697878,
                   'sadness': 0.099206},
                  {'anger': 0.094278,
                   'disgust': 0.056642,
                   'fear': 0.074516,
                   'joy': 0.637089,
                   'sadness': 0.124744},
                  {'anger': 0.072268,
                   'disgust': 0.047036,
                   'fear': 0.056772,
                   'joy': 0.605054,
                   'sadness': 0.123598},
                  {'anger': 0.105713,
                   'disgust': 0.035599,
                   'fear': 0.078888,
                   'joy': 0.685446,
                   'sadness': 0.669868},
                  {'anger': 0.091127,
                   'disgust': 0.065476,
                   'fear': 0.097711,
                   'joy': 0.575877,
                   'sadness': 0.159716},
                  {'anger': 0.065062,
                   'disgust': 0.036137,
                   'fear': 0.075211,
                   'joy': 0.627795,
                   'sadness': 0.165926},
                  {'anger': 0.455197,
                   'disgust': 0.152483,
                   'fear': 0.138824,
                   'joy': 0.476845,
                   'sadness': 0.529762},
                  {'anger': 0.021255,
                   'disgust': 0.006069,
                   'fear': 0.039857,
                   'joy': 0.654958,
                   'sadness': 0.639948},
                  {'anger': 0.049087,
                   'disgust': 0.048909,
                   'fear': 0.090237,
                   'joy': 0.654029,
                   'sadness': 0.130154},
                  {'anger': 0.038187,
                   'disgust': 0.02834,
                   'fear': 0.043278,
                   'joy': 0.687827,
                   'sadness': 0.05714},
                  {'anger': 0.095656,
                   'disgust': 0.094251,
                   'fear': 0.090477,
                   'joy': 0.581357,
                   'sadness': 0.555648},
                  {'anger': 0.085498,
                   'disgust': 0.051906,
                   'fear': 0.093419,
                   'joy': 0.566957,
                   'sadness': 0.142832},
                  {'anger': 0.085654,
                   'disgust': 0.050708,
                   'fear': 0.055249,
                   'joy': 0.636486,
                   'sadness': 0.464416},
                  {'anger': 0.09813,
                   'disgust': 0.086422,
                   'fear': 0.073293,
                   'joy': 0.648335,
                   'sadness': 0.145682},
                  {'anger': 0.039986,
                   'disgust': 0.041381,
                   'fear': 0.046356,
                   'joy': 0.671365,
                   'sadness': 0.07195},
                  {'anger': 0.095049,
                   'disgust': 0.056001,
                   'fear': 0.104296,
                   'joy': 0.574782,
                   'sadness': 0.544132},
                  {'anger': 0.055904,
                   'disgust': 0.04444,
                   'fear': 0.074111,
                   'joy': 0.621787,
                   'sadness': 0.58421},
                  {'anger': 0.578869,
                   'disgust': 0.094044,
                   'fear': 0.141643,
                   'joy': 0.580338,
                   'sadness': 0.536761},
                  {'anger': 0.528827,
                   'disgust': 0.064109,
                   'fear': 0.096675,
                   'joy': 0.571473,
                   'sadness': 0.594462},
                  {'anger': 0.05886,
                   'disgust': 0.025725,
                   'fear': 0.474838,
                   'joy': 0.681943,
                   'sadness': 0.435708},
                  {'anger': 0.485395,
                   'disgust': 0.113269,
                   'fear': 0.071767,
                   'joy': 0.669985,
                   'sadness': 0.122037},
                  {'anger': 0.105048,
                   'disgust': 0.060223,
                   'fear': 0.09606,
                   'joy': 0.636427,
                   'sadness': 0.473656},
                  {'anger': 0.60615,
                   'disgust': 0.016444,
                   'fear': 0.097605,
                   'joy': 0.521774,
                   'sadness': 0.44325},
                  {'anger': 0.038762,
                   'disgust': 0.019489,
                   'fear': 0.034039,
                   'joy': 0.612718,
                   'sadness': 0.038509},
                  {'anger': 0.578682,
                   'disgust': 0.072979,
                   'fear': 0.15442,
                   'joy': 0.508638,
                   'sadness': 0.552873},
                  {'anger': 0.095593,
                   'disgust': 0.05505,
                   'fear': 0.087083,
                   'joy': 0.646302,
                   'sadness': 0.149008},
                  {'anger': 0.048422,
                   'disgust': 0.014579,
                   'fear': 0.059854,
                   'joy': 0.611464,
                   'sadness': 0.399268},
                  {'anger': 0.103275,
                   'disgust': 0.031277,
                   'fear': 0.104453,
                   'joy': 0.683698,
                   'sadness': 0.556451},
                  {'anger': 0.084629,
                   'disgust': 0.047265,
                   'fear': 0.074373,
                   'joy': 0.631675,
                   'sadness': 0.109624},
                  {'anger': 0.047536,
                   'disgust': 0.023147,
                   'fear': 0.059125,
                   'joy': 0.58566,
                   'sadness': 0.136765},
                  {'anger': 0.1148,
                   'disgust': 0.073919,
                   'fear': 0.087806,
                   'joy': 0.606881,
                   'sadness': 0.149865},
                  {'anger': 0.059329,
                   'disgust': 0.056612,
                   'fear': 0.045411,
                   'joy': 0.648877,
                   'sadness': 0.093004},
                  {'anger': 0.459376,
                   'disgust': 0.036386,
                   'fear': 0.445285,
                   'joy': 0.565579,
                   'sadness': 0.648972},
                  {'anger': 0.205386,
                   'disgust': 0.511592,
                   'fear': 0.431072,
                   'joy': 0.615432,
                   'sadness': 0.509453},
                  {'anger': 0.089066,
                   'disgust': 0.049783,
                   'fear': 0.087389,
                   'joy': 0.574646,
                   'sadness': 0.588759},
                  {'anger': 0.68086,
                   'disgust': 0.069532,
                   'fear': 0.145723,
                   'joy': 0.014557,
                   'sadness': 0.144065},
                  {'anger': 0.597359,
                   'disgust': 0.054314,
                   'fear': 0.085272,
                   'joy': 0.542152,
                   'sadness': 0.640746},
                  {'anger': 0.065478,
                   'disgust': 0.053467,
                   'fear': 0.087376,
                   'joy': 0.699632,
                   'sadness': 0.10691},
                  {'anger': 0.42679,
                   'disgust': 0.025906,
                   'fear': 0.039089,
                   'joy': 0.618292,
                   'sadness': 0.074416},
                  {'anger': 0.057084,
                   'disgust': 0.054183,
                   'fear': 0.079941,
                   'joy': 0.654311,
                   'sadness': 0.544423},
                  {'anger': 0.059656,
                   'disgust': 0.055757,
                   'fear': 0.082782,
                   'joy': 0.612807,
                   'sadness': 0.142394},
                  {'anger': 0.071206,
                   'disgust': 0.072531,
                   'fear': 0.077101,
                   'joy': 0.5663,
                   'sadness': 0.159371},
                  {'anger': 0.130816,
                   'disgust': 0.494286,
                   'fear': 0.070408,
                   'joy': 0.625425,
                   'sadness': 0.16269},
                  {'anger': 0.520801,
                   'disgust': 0.082638,
                   'fear': 0.12902,
                   'joy': 0.574277,
                   'sadness': 0.55529},
                  {'anger': 0.08277,
                   'disgust': 0.054859,
                   'fear': 0.069364,
                   'joy': 0.589917,
                   'sadness': 0.539475},
                  {'anger': 0.046004,
                   'disgust': 0.040435,
                   'fear': 0.084929,
                   'joy': 0.616951,
                   'sadness': 0.580635},
                  {'anger': 0.077567,
                   'disgust': 0.034768,
                   'fear': 0.095056,
                   'joy': 0.671951,
                   'sadness': 0.569955},
                  {'anger': 0.088673,
                   'disgust': 0.074175,
                   'fear': 0.115823,
                   'joy': 0.626812,
                   'sadness': 0.591473},
                  {'anger': 0.053395,
                   'disgust': 0.07823,
                   'fear': 0.064018,
                   'joy': 0.642092,
                   'sadness': 0.163962},
                  {'anger': 0.392787,
                   'disgust': 0.022475,
                   'fear': 0.107678,
                   'joy': 0.594109,
                   'sadness': 0.081411},
                  {'anger': 0.072973,
                   'disgust': 0.088516,
                   'fear': 0.108199,
                   'joy': 0.579065,
                   'sadness': 0.170818},
                  {'anger': 0.122298,
                   'disgust': 0.150824,
                   'fear': 0.621473,
                   'joy': 0.521803,
                   'sadness': 0.521935},
                  {'anger': 0.130671,
                   'disgust': 0.084794,
                   'fear': 0.074568,
                   'joy': 0.655117,
                   'sadness': 0.556961},
                  {'anger': 0.120595,
                   'disgust': 0.106614,
                   'fear': 0.099073,
                   'joy': 0.561009,
                   'sadness': 0.103373},
                  {'anger': 0.110974,
                   'disgust': 0.06965,
                   'fear': 0.08618,
                   'joy': 0.603771,
                   'sadness': 0.588273},
                  {'anger': 0.608548,
                   'disgust': 0.546023,
                   'fear': 0.16661,
                   'joy': 0.010081,
                   'sadness': 0.175322},
                  {'anger': 0.608653,
                   'disgust': 0.077297,
                   'fear': 0.111498,
                   'joy': 0.574728,
                   'sadness': 0.541468},
                  {'anger': 0.002477,
                   'disgust': 3e-06,
                   'fear': 1.3e-05,
                   'joy': 0.322072,
                   'sadness': 6.1e-05},
                  {'anger': 0.086498,
                   'disgust': 0.040864,
                   'fear': 0.427766,
                   'joy': 0.035076,
                   'sadness': 0.153745},
                  {'anger': 0.426048,
                   'disgust': 0.050772,
                   'fear': 0.115381,
                   'joy': 0.626422,
                   'sadness': 0.57163},
                  {'anger': 0.078236,
                   'disgust': 0.076069,
                   'fear': 0.095503,
                   'joy': 0.511974,
                   'sadness': 0.525498},
                  {'anger': 0.058869,
                   'disgust': 0.02644,
                   'fear': 0.062933,
                   'joy': 0.596991,
                   'sadness': 0.584296},
                  {'anger': 0.582502,
                   'disgust': 0.119904,
                   'fear': 0.172341,
                   'joy': 0.446173,
                   'sadness': 0.094649},
                  {'anger': 0.094209,
                   'disgust': 0.018543,
                   'fear': 0.085793,
                   'joy': 0.70779,
                   'sadness': 0.06923},
                  {'anger': 0.087581,
                   'disgust': 0.05441,
                   'fear': 0.118374,
                   'joy': 0.668214,
                   'sadness': 0.522592},
                  {'anger': 0.461314,
                   'disgust': 0.100507,
                   'fear': 0.129861,
                   'joy': 0.562349,
                   'sadness': 0.565069},
                  {'anger': 0.02696,
                   'disgust': 0.065095,
                   'fear': 0.063774,
                   'joy': 0.645753,
                   'sadness': 0.07277},
                  {'anger': 0.559328,
                   'disgust': 0.085173,
                   'fear': 0.118253,
                   'joy': 0.589639,
                   'sadness': 0.102755},
                  {'anger': 0.091756,
                   'disgust': 0.397735,
                   'fear': 0.057857,
                   'joy': 0.626787,
                   'sadness': 0.587521},
                  {'anger': 0.133095,
                   'disgust': 0.10203,
                   'fear': 0.116609,
                   'joy': 0.600875,
                   'sadness': 0.475253},
                  {'anger': 0.088847,
                   'disgust': 0.037178,
                   'fear': 0.145817,
                   'joy': 0.631274,
                   'sadness': 0.535184},
                  {'anger': 0.083722,
                   'disgust': 0.06237,
                   'fear': 0.05775,
                   'joy': 0.606496,
                   'sadness': 0.475336},
                  {'anger': 0.08513,
                   'disgust': 0.054362,
                   'fear': 0.08451,
                   'joy': 0.679362,
                   'sadness': 0.468126},
                  {'anger': 0.084805,
                   'disgust': 0.024529,
                   'fear': 0.085027,
                   'joy': 0.192286,
                   'sadness': 0.126553},
                  {'anger': 0.102547,
                   'disgust': 0.075168,
                   'fear': 0.098091,
                   'joy': 0.627772,
                   'sadness': 0.513166},
                  {'anger': 0.089224,
                   'disgust': 0.060176,
                   'fear': 0.121146,
                   'joy': 0.577164,
                   'sadness': 0.519942},
                  {'anger': 0.050957,
                   'disgust': 0.029916,
                   'fear': 0.037201,
                   'joy': 0.711438,
                   'sadness': 0.068996},
                  {'anger': 0.496458,
                   'disgust': 0.067885,
                   'fear': 0.564857,
                   'joy': 0.604825,
                   'sadness': 0.548137},
                  {'anger': 0.071379,
                   'disgust': 0.063699,
                   'fear': 0.088767,
                   'joy': 0.648899,
                   'sadness': 0.557124},
                  {'anger': 0.104741,
                   'disgust': 0.038946,
                   'fear': 0.089191,
                   'joy': 0.582942,
                   'sadness': 0.562246},
                  {'anger': 0.030346,
                   'disgust': 0.009639,
                   'fear': 0.039819,
                   'joy': 0.589826,
                   'sadness': 0.619348},
                  {'anger': 0.066379,
                   'disgust': 0.057031,
                   'fear': 0.064518,
                   'joy': 0.701161,
                   'sadness': 0.465365},
                  {'anger': 0.093615,
                   'disgust': 0.028877,
                   'fear': 0.116161,
                   'joy': 0.557654,
                   'sadness': 0.553877},
                  {'anger': 0.555078,
                   'disgust': 0.092257,
                   'fear': 0.500861,
                   'joy': 0.446576,
                   'sadness': 0.547064},
                  {'anger': 0.471913,
                   'disgust': 0.060306,
                   'fear': 0.110427,
                   'joy': 0.628902,
                   'sadness': 0.537844},
                  {'anger': 0.066781,
                   'disgust': 0.087706,
                   'fear': 0.073699,
                   'joy': 0.582005,
                   'sadness': 0.120134},
                  {'anger': 0.505515,
                   'disgust': 0.089861,
                   'fear': 0.123225,
                   'joy': 0.55662,
                   'sadness': 0.127695},
                  {'anger': 0.083788,
                   'disgust': 0.040249,
                   'fear': 0.103659,
                   'joy': 0.607054,
                   'sadness': 0.558264},
                  {'anger': 0.527934,
                   'disgust': 0.503555,
                   'fear': 0.095235,
                   'joy': 0.657727,
                   'sadness': 0.488381},
                  {'anger': 0.56258,
                   'disgust': 0.086332,
                   'fear': 0.124341,
                   'joy': 0.62913,
                   'sadness': 0.552427},
                  {'anger': 0.549277,
                   'disgust': 0.121319,
                   'fear': 0.084164,
                   'joy': 0.616472,
                   'sadness': 0.135158},
                  {'anger': 0.082279,
                   'disgust': 0.027579,
                   'fear': 0.060782,
                   'joy': 0.539864,
                   'sadness': 0.121637},
                  {'anger': 0.062509,
                   'disgust': 0.029881,
                   'fear': 0.059718,
                   'joy': 0.665437,
                   'sadness': 0.138731},
                  {'anger': 0.07965,
                   'disgust': 0.031262,
                   'fear': 0.073163,
                   'joy': 0.64537,
                   'sadness': 0.125684},
                  {'anger': 0.545005,
                   'disgust': 0.083788,
                   'fear': 0.097776,
                   'joy': 0.409109,
                   'sadness': 0.585994},
                  {'anger': 0.45143,
                   'disgust': 0.068987,
                   'fear': 0.044019,
                   'joy': 0.729623,
                   'sadness': 0.088004},
                  {'anger': 0.098564,
                   'disgust': 0.052984,
                   'fear': 0.095457,
                   'joy': 0.654577,
                   'sadness': 0.548666},
                  {'anger': 0.091409,
                   'disgust': 0.048295,
                   'fear': 0.10569,
                   'joy': 0.644297,
                   'sadness': 0.62339},
                  {'anger': 0.495419,
                   'disgust': 0.085376,
                   'fear': 0.09395,
                   'joy': 0.643468,
                   'sadness': 0.485662},
                  {'anger': 0.575126,
                   'disgust': 0.077178,
                   'fear': 0.131259,
                   'joy': 0.602837,
                   'sadness': 0.530144},
                  {'anger': 0.100354,
                   'disgust': 0.083394,
                   'fear': 0.5441,
                   'joy': 0.674651,
                   'sadness': 0.481021},
                  {'anger': 0.493946,
                   'disgust': 0.078047,
                   'fear': 0.0819,
                   'joy': 0.614236,
                   'sadness': 0.541432},
                  {'anger': 0.069187,
                   'disgust': 0.084675,
                   'fear': 0.060981,
                   'joy': 0.60265,
                   'sadness': 0.162792},
                  {'anger': 0.169456,
                   'disgust': 0.47709,
                   'fear': 0.434806,
                   'joy': 0.545836,
                   'sadness': 0.520966},
                  {'anger': 0.070696,
                   'disgust': 0.039695,
                   'fear': 0.053607,
                   'joy': 0.622965,
                   'sadness': 0.119031},
                  {'anger': 0.065834,
                   'disgust': 0.078117,
                   'fear': 0.080079,
                   'joy': 0.56524,
                   'sadness': 0.142492}]
    return emotionSet


def send_sentiment_set():
    sentiment = [0.357852,
                 -0.157514,
                 -0.111215,
                 -0.378024,
                 0.58955,
                 -0.16719,
                 -0.247307,
                 -0.229478,
                 0.0278044,
                 0.645001,
                 -0.379016,
                 -0.0304929,
                 0.673765,
                 -0.0443651,
                 -0.226988,
                 0.00400686,
                 0.0882047,
                 0.111658,
                 0.654789,
                 0.647383,
                 -0.526251,
                 0.470136,
                 0.0267508,
                 0.0713389,
                 0.48571,
                 -0.700785,
                 -0.27412,
                 0.283754,
                 -0.190706,
                 -0.57715,
                 0.493909,
                 0.660603,
                 0.111839,
                 -0.50206,
                 -0.283865,
                 -0.665398,
                 0.584792,
                 0.529634,
                 0.120251,
                 0.523138,
                 0.115594,
                 0.106258,
                 0.511018,
                 0.593729,
                 0.344867,
                 -0.266151,
                 0.852798,
                 0.474458,
                 0.00262443,
                 0.041373,
                 0.0281017,
                 0.542082,
                 -0.12884,
                 0.762576,
                 0.483421,
                 0.739952,
                 0.242786,
                 0.354471,
                 0.255258,
                 0.447064,
                 0.275543,
                 0.11617,
                 0.456418,
                 -0.338093,
                 -0.0647984,
                 0.769926,
                 0.585943,
                 0.181172,
                 0.0904864,
                 0.569891,
                 -0.393268,
                 0.221764,
                 0.266078,
                 -0.144117,
                 0.369766,
                 0.590877,
                 0.110727,
                 0.588868,
                 -0.255175,
                 -0.631732,
                 0.452118,
                 -0.192969,
                 -0.36189,
                 0.305406,
                 0.488904,
                 0.468183,
                 0.500045,
                 0.0405676,
                 0.586822,
                 -0.449712,
                 0.103881,
                 0.0478925,
                 0.144926,
                 0.0495007,
                 0.394912,
                 0.147029,
                 0.231447,
                 -0.443005,
                 0.0625252,
                 0.123312,
                 0.245093,
                 -0.760349,
                 -0.0523897,
                 0.67631,
                 -0.687131,
                 0.0974531,
                 -0.109981,
                 0.434493,
                 -0.352558,
                 0.501157,
                 0.394763,
                 -0.280682,
                 0.375647,
                 0.0818479,
                 0.181566,
                 0.0290395,
                 0.090112,
                 0.242246,
                 0.349013,
                 0.488378,
                 0.343372,
                 0.159707,
                 0.38191,
                 -0.222327,
                 0.504782,
                 0.190235,
                 0.365129,
                 0.438006,
                 -0.303491,
                 -0.451219,
                 0.0818928,
                 -0.0321105,
                 -0.0986306,
                 -0.0666249,
                 0.347952,
                 -0.450371,
                 0.0392294,
                 0.555097,
                 0.440592,
                 0.68772,
                 -0.490737,
                 0.858379,
                 0.0966485,
                 -0.0311169,
                 0.213617,
                 -0.208065,
                 0.38859,
                 0.0316181,
                 0.398718,
                 -0.629862,
                 0.555394,
                 -0.213485]
    return sentiment
