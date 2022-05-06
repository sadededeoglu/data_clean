import re
import pandas as pd
import numpy as np
from alarm_dataframe import df_alarm

with open("C:\\python\\proje\\raw","r",encoding = "utf-8") as file:
    liste = file.readlines()
    deneme = [re.split(":=",entry,1) for entry in liste]
    
    ondata = []
    for x in deneme:
        
        a= x[0].strip("\"")
        sepet= [""]
        for deger in a:
            
            if deger == " " :
                
                if sepet[-1].isalpha() or sepet[-1] == "&" or sepet[-1] == "-" or sepet[-1] == ":" or sepet[-1] == "_":
                    kelime = deger.replace(" ","_")
                    sepet.append(kelime)
                else:
                    sepet.append(deger)
                    
            else:
                sepet.append(deger)
        b = "".join(sepet)
        pat = re.compile('(?P<key>\w+)\=(?P<value>\S+)')
        dicti = {}
        for m in pat.finditer(b):
            dicti[m.group(1)] = m.group(2)

        ondata.append(dicti)
    
    df_raw= pd.DataFrame(ondata)

duplic=pd.concat([df_alarm,df_raw])
not_alarm=duplic.drop_duplicates(keep=False)
not_alarm.to_excel(r'C:\python\proje\not_alarm.xlsx', index = False)

    
    



    
    
    
    
    
        
          

            

    
   
