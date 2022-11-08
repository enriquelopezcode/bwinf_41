#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
import numpy as np
from PIL import Image
import time


def verzinkt(quantity,resolution = (256,256),sharpness = 3):
    
    #sharpness = How fast does the crystal grow in it's fastest direction compared to the other 3 directions
    
    def create_seeds(quantity,resolution):
    
        #quantity = Menge der Kristallkeime
        #resolution = Tupel mit Bilddimensionen (Beispiel: (720,720)) 
        #sharpness = How fast does the crystal grow in it's fastest direction compared to the other 3 directions
        '''BILD MUSS QUADRAT SEIN -> TUPEL muss 2 mal den gleichen Wert haben'''
        #Bei hohen Bilddimensionen wird die Wartezeit sehr viel länger
    
        #Array gefüllt mit Einsen
        array = np.ones(resolution)
    
        #Kristallkeime erstellen - n mal einen Zufälligen Pixel mit Wert zwischen 100 und 220 (Grautöne) überschreiben
        '''Bei einer sehr hohen Anzahl von Keimen weicht der quantity Wert stark von der Anzahl der überschriebenen Werte ab,
        da gegen Ende der Schleife mit höher Wahrscheinlichkeit bereits überschriebene Werte jochmal überschrieben werden.
       Jedoch ist diese Abweichung von Originalwert für kleinere Werte von quantity bis etwa 1000 vernachlässigbar. Da im 
       Beispielbild weitaus weniger Kristalle zu sehen sind, lässt sich ein solches Bild auch erstellen, ohne die Laufzeit
       der Simulation durch einem Check für jeden Pixel unnötig zu erhöhen.'''
    
        for i in range(quantity):
            array.flat[np.random.choice(np.prod(array.shape),1,replace = False)] = np.random.randint(100,221)
            
        return array
    
    if resolution[0] != resolution[1]:
        return print('ERROR: Bild muss Quadrat sein -> Für Resolution übergebener Tupel muss 2 mal den selben Wert haben')
    if not(0 < sharpness <5) or not(type(sharpness) == int):
        return print('ERROR: Gültige Werte für Sharpness: 1,2,3,4')
    print('Programm startet!')
    start_time = time.time()
    #Kristallkeime erstellen
    vorlage = create_seeds(quantity,resolution)
    kristallmuster = vorlage.copy()
    print('Keime gestreut!')
    
    timer = 1
    #Solange es Werte gibt die nicht ersetzt wurden
    while np.count_nonzero(kristallmuster == 1) != 0:
        
        for i in range(len(vorlage.flat)):
            
            ####################################
            if 100 <= vorlage.flat[i] <= 130:
                
                #Errechnete Array Position könnte out of bounds sein -> Ignorier Error mit try / except
                try:
                    if vorlage.flat[i-1] == 1:
                        kristallmuster.flat[i-1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i+1] == 1:
                        kristallmuster.flat[i+1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i-np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i-np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i+np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i+np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                
                if sharpness > 1:
                    try: 
                        if vorlage.flat[i-2*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i-2*(np.shape(vorlage)[0])] = vorlage.flat[i]
                        
                    except:
                        pass
                
                if sharpness > 2:
                    try: 
                        if vorlage.flat[i-3*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i-3*(np.shape(vorlage)[0])] = vorlage.flat[i]
                    except:
                        pass
                    
                if sharpness > 3:
                    try: 
                        if vorlage.flat[i-4*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i-4*(np.shape(vorlage)[0])] = vorlage.flat[i]
                    except:
                        pass
                
            #################################################
            
            if 131 <= vorlage.flat[i] <= 160:
                try: 
                    if vorlage.flat[i-1] == 1:
                        kristallmuster.flat[i-1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i+1] == 1:
                        kristallmuster.flat[i+1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i-np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i-np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass

                
                try: 
                    if vorlage.flat[i+np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i+np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                 
                if sharpness > 1:
                    try: 
                        if vorlage.flat[i+2] == 1:
                            kristallmuster.flat[i+2] = vorlage.flat[i]
                    except:
                        pass
                
                if sharpness > 2:
                    try: 
                        if vorlage.flat[i+3] == 1:
                            kristallmuster.flat[i+3] = vorlage.flat[i]
                    except:
                        pass
                
                if sharpness > 3:
                    try: 
                        if vorlage.flat[i+4] == 1:
                            kristallmuster.flat[i+4] = vorlage.flat[i]
                    except:
                        pass
                    
            ###############################################
            if 161 <= vorlage.flat[i] <= 190:
                try: 
                    if vorlage.flat[i-1] == 1:
                        kristallmuster.flat[i-1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i+1] == 1:
                        kristallmuster.flat[i+1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i-np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i-np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                
    
                try: 
                    if vorlage.flat[i+np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i+np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                
                if sharpness > 1:
                    try: 
                        if vorlage.flat[i+2*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i+2*(np.shape(vorlage)[0])] = vorlage.flat[i]
                    except:
                        pass
                
                if sharpness > 2:
                    try: 
                        if vorlage.flat[i+3*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i+3*(np.shape(vorlage)[0])] = vorlage.flat[i]
                    except:
                        pass
                
                if sharpness > 3:
                    try: 
                        if vorlage.flat[i+4*(np.shape(vorlage)[0])] == 1:
                            kristallmuster.flat[i+4*(np.shape(vorlage)[0])] = vorlage.flat[i]
                    except:
                        pass
            ##################################################
            if 190 <= vorlage.flat[i] <= 220:
                try: 
                    if vorlage.flat[i-1] == 1:
                        kristallmuster.flat[i-1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i+1] == 1:
                        kristallmuster.flat[i+1] = vorlage.flat[i]
                except:
                    pass
                
                try: 
                    if vorlage.flat[i-np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i-np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass

                
                try: 
                    if vorlage.flat[i+np.shape(vorlage)[0]] == 1:
                        kristallmuster.flat[i+np.shape(vorlage)[0]] = vorlage.flat[i]
                except:
                    pass
                 
                if sharpness > 1:
                    try: 
                        if vorlage.flat[i-2] == 1:
                            kristallmuster.flat[i-2] = vorlage.flat[i]
                    except:
                        pass
                
                if sharpness > 2:
                    try: 
                        if vorlage.flat[i-3] == 1:
                            kristallmuster.flat[i-3] = vorlage.flat[i]
                    except:
                        pass
                    
                if sharpness > 3:
                    try: 
                        if vorlage.flat[i-4] == 1:
                            kristallmuster.flat[i-4] = vorlage.flat[i]
                    except:
                        pass
                    
                    
                    
        print('Iteration',timer)
        timer += 1
        vorlage = kristallmuster.copy()
       
        
    print('Fertig nach %s Sekunden!' % (round(time.time() - start_time)))
    time.sleep(2)
    img = Image.fromarray(np.uint8(kristallmuster))
    img.show()
    

                    
                    
                    
       
    

