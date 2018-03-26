import RLP
import card
#import numpy as np

GLP=RLP.generateLP()
print("glp:")
print(GLP)
CLP=RLP.adjustLP(GLP)
print("clp:")
print(CLP)
ALP=RLP.allLP(CLP)
print("ALP:")
print(ALP)