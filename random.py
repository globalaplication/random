#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
SS, BH, KH, BJ = [0,9,1,8,2,7,3,6,4,5], ["A", "B", "C", "D", "E", "F", "G", "X", "H", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z", "Q"],  ["a", "b", "c", "d", "e", "f", "x", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "z", "y", "q"], ["?", "&", "*", "_"]
def rasgele(talimat=""):
  rpass=""
  for t in talimat.split(","):
    if (t == "0"):
      x = random.choice(SS)
      rpass += str(x)
    if (t == "A"):
      x = random.choice(BH)
      rpass += str(x)
    if (t == "a"):
      x = random.choice(KH)
      rpass += str(x)
    if (t == "?"):
      x = random.choice(BJ)
      rpass += str(x)
  return rpass
  
print rasgele("a,A,a,?")
