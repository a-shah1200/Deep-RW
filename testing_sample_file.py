# -*- coding: utf-8 -*-
"""

@author: Asfahan
"""


from testing_pipeline import *

read=""  # Path for read file
write="" # Path for write file
link="" # API link. API link can be generated by running api.py file and copying the hosted url.

"""Note it is important to append '/model' to the api link. For example

if the api link is www.model_prediction.com, then instead of this link

use www.model_prediction.com/model

"""

name_class={0:"AESCrypt", 1:"Cerber", 2:"Cerber-largefiles", 3:"Cerber-w10dirs", 4:"Darkside", 5:"Darkside-largefiles", 6:"Darkside-w10dirs",
     7:"Excel", 8:"Firefox", 9:"GandCrab4", 10:"GandCrab4-largefiles", 11:"GandCrab4-w10dirs",
     12:"Ryuk",13:"Ryuk-largefiles",14:"Ryuk-w10dirs",15:"SDelete",16:"Sodinokibi",17:"Sodinokibi-largefiles",18:"Sodinokibi-w10dirs",
     19:"TeslaCrypt",20:"TeslaCrypt-largefiles",21:"TeslaCrypt-w10dirs",22:"WannaCry",
     23:"WannaCry-largefiles",24:"WannaCry-w10dirs",25:"Zip"}


if make_prediction(read,write,link)==None:
    print("There is an error with api. Please check the api module")
else:
    ans=make_prediction(read,write,link)
    if ans in [0,25,7,8,15]:
        print("Benign",name_class[ans])
    else:
        print("Ransomware",name_class[ans])
    