#!/usr/bin/env python
# coding: utf-8

# In[13]:


def worktime(datei):
    #Erspart einige Dinge wie Durchschnitt von Werten in Array
    import numpy as np
    
    #Für Methode 3
    import random
    
    #Listen für Eingangszeit und Dauer 
    entry = []
    waitlist = []
    with open(datei) as f:
        line = f.readline()
        while line:
            entry.append(int(line.split()[0]))
            waitlist.append(int(line.split()[1]))
            line = f.readline()
            
    #######################################################################
    
    #ERLEDIGUNG IN REIHENFOLGE
    def earlybird(entry,waitlist):
        
    
        #Variable der insgesamt vergangenen Zeit (beginnt um 9 Uhr)
        time = 540
    
        #Variable für verbleibende Zeit am aktuellen Projekt
        currentjob = 0
    
        #Zeitpunkt an dem Marc Feierabend hat
        feierabend = 1020
        
        #Wartedauern aller Aufträge
        wait_times = []
        
        #Äußerer Produktiver Loop
        while True:
        
            #System für Auswahl: Nächster in der Schlange
            if currentjob <= 0:
                
                #Dauer des letzten Auftrags wird berechnet
                if time != 540:
                    wait_times.append(time-currententry)
                    
                
                #Alle Aufträge fertig
                if len(entry) == 0:
                    wait_times = np.array(wait_times)
                    return print('Fertig nach {} Monaten! \n Durchschnittliche Wartezeit: {} Minuten \n Längste Wartezeit: {} Minuten \n Wartezeit Unterschied: {} Minuten \n Median: {} Minuten'.format(round(time * 0.000022816,1),int(round(sum(wait_times) / len(wait_times),0)),max(wait_times),max(wait_times)-min(wait_times),int(round(np.median(wait_times),0))))
                
                #Warteloop auf nächsten Auftrag
                while True:    
                    if entry[0] <= time:
                        currentjob = waitlist[0]
                        currententry = entry[0]
                        del waitlist[0]
                        del entry[0]
                        break
                    else: 
                        time +=1
            
            time += 1
            currentjob -= 1
            
            #Wenn Feierabend ist
            if time == feierabend:
                time += 960
                feierabend += 1440
    ####################################################################### 
    
    def short_is_great(entry,waitlist):
        #Variable der insgesamt vergangenen Zeit (beginnt um 9 Uhr)
        time = 540
    
        #Variable für verbleibende Zeit am aktuellen Projekt
        currentjob = 0
    
        #Zeitpunkt an dem Marc Feierabend hat
        feierabend = 1020
        
        #Wartedauern aller Aufträge
        wait_times = []
        
        #Liste der verfügbaren Aufträge
        waitlist_ready = []
        entry_ready = []
        
        #Äußerer Produktiver Loop
        while True:
                
            if len(entry) != 0:
                if time >= entry[0]:
                    waitlist_ready.append(waitlist[0])
                    entry_ready.append(entry[0])
                    del waitlist[0]
                    del entry[0]
                
                
            #System für Auswahl: Nächster in der Schlange
            if currentjob <= 0:
                
                #Dauer des letzten Auftrags wird berechnet
                if time != 540:
                    wait_times.append(time-currententry)
                    
                    
                
                #Alle Aufträge fertig
                if len(entry_ready) == 0 and len(entry) == 0:
                    wait_times = np.array(wait_times)
                    return print('Fertig nach {} Monaten! \n Durchschnittliche Wartezeit: {} Minuten \n Längste Wartezeit: {} Minuten \n Wartezeit-Unterschied: {} Minuten \n Median: {} Minuten'.format(round(time * 0.000022816,1),int(round(sum(wait_times) / len(wait_times),0)),max(wait_times),max(wait_times)-min(wait_times),int(round(np.median(wait_times),0))))
                
              
                
                #Warteloop auf nächsten Auftrag
                while True:
                    #Index of shortest job
                    if len(waitlist_ready) > 0:
                        min_index = waitlist_ready.index(min(waitlist_ready))
                       
                        
                    
                    
                        
                        
                        currentjob = min(waitlist_ready)
                        currententry = entry_ready[min_index]
                        del waitlist_ready[min_index]
                        del entry_ready[min_index]
                        break
                       
                    else: 
                        time +=1
                        if len(entry) != 0:
                            if time >= entry[0]:
                                waitlist_ready.append(waitlist[0])
                                entry_ready.append(entry[0])
                                del waitlist[0]
                                del entry[0]
            
            time += 1
            currentjob -= 1
            
            #Wenn Feierabend ist
            if time == feierabend:
                time += 960
                feierabend += 1440
    
    
    
    
    def zufällig(entry,waitlist):
        
        #Variable der insgesamt vergangenen Zeit (beginnt um 9 Uhr)
        time = 540
    
        #Variable für verbleibende Zeit am aktuellen Projekt
        currentjob = 0
    
        #Zeitpunkt an dem Marc Feierabend hat
        feierabend = 1020
        
        #Wartedauern aller Aufträge
        wait_times = []
        
        #Liste der verfügbaren Aufträge
        waitlist_ready = []
        entry_ready = []
        
        #Äußerer Produktiver Loop
        while True:
                
            if len(entry) != 0:
                if time >= entry[0]:
                    waitlist_ready.append(waitlist[0])
                    entry_ready.append(entry[0])
                    del waitlist[0]
                    del entry[0]
                
                
            #System für Auswahl: Nächster in der Schlange
            if currentjob <= 0:
                
                #Dauer des letzten Auftrags wird berechnet
                if time != 540:
                    wait_times.append(time-currententry)
                    
                    
                
                #Alle Aufträge fertig
                if len(entry_ready) == 0 and len(entry) == 0:
                    wait_times = np.array(wait_times)
                    return print('Fertig nach {} Monaten! \n Durchschnittliche Wartezeit: {} Minuten \n Längste Wartezeit: {} Minuten \n Wartezeit-Unterschied: {} Minuten \n Median: {} Minuten'.format(round(time * 0.000022816,1),int(round(sum(wait_times) / len(wait_times),0)),max(wait_times),max(wait_times)-min(wait_times),int(round(np.median(wait_times),0))))
                
              
                
                #Warteloop auf nächsten Auftrag
                while True:
                    #Index of random Object
                    if len(waitlist_ready) > 0:
                        random_index = random.randrange(len(waitlist_ready))
                       
                        
                    
                    
                        
                        
                        currentjob = waitlist_ready[random_index]
                        currententry = entry_ready[random_index]
                        del waitlist_ready[random_index]
                        del entry_ready[random_index]
                        break
                       
                    else: 
                        time +=1
                        if len(entry) != 0:
                            if time >= entry[0]:
                                waitlist_ready.append(waitlist[0])
                                entry_ready.append(entry[0])
                                del waitlist[0]
                                del entry[0]
            
            time += 1
            currentjob -= 1
            
            #Wenn Feierabend ist
            if time == feierabend:
                time += 960
                feierabend += 1440
    
    
    def letzter_auftrag(entry,waitlist):
        
        #Variable der insgesamt vergangenen Zeit (beginnt um 9 Uhr)
        time = 540
    
        #Variable für verbleibende Zeit am aktuellen Projekt
        currentjob = 0
    
        #Zeitpunkt an dem Marc Feierabend hat
        feierabend = 1020
        
        #Wartedauern aller Aufträge
        wait_times = []
        
        #Liste der verfügbaren Aufträge
        waitlist_ready = []
        entry_ready = []
        
        #Äußerer Produktiver Loop
        while True:
                
            if len(entry) != 0:
                if time >= entry[0]:
                    waitlist_ready.append(waitlist[0])
                    entry_ready.append(entry[0])
                    del waitlist[0]
                    del entry[0]
                
                
            #System für Auswahl: Nächster in der Schlange
            if currentjob <= 0:
                
                #Dauer des letzten Auftrags wird berechnet
                if time != 540:
                    wait_times.append(time-currententry)
                    
                    
                
                #Alle Aufträge fertig
                if len(entry_ready) == 0 and len(entry) == 0:
                    wait_times = np.array(wait_times)
                    return print('Fertig nach {} Monaten! \n Durchschnittliche Wartezeit: {} Minuten \n Längste Wartezeit: {} Minuten \n Wartezeit-Unterschied: {} Minuten \n Median: {} Minuten'.format(round(time * 0.000022816,1),int(round(sum(wait_times) / len(wait_times),0)),max(wait_times),max(wait_times)-min(wait_times),int(round(np.median(wait_times),0))))
                
              
                
                #Warteloop auf nächsten Auftrag
                while True:
                    #Index of random Object
                    if len(waitlist_ready) > 0:
                        
                        currentjob = waitlist_ready[-1]
                        currententry = entry_ready[-1]
                        del waitlist_ready[-1]
                        del entry_ready[-1]
                        break
                       
                    else: 
                        time +=1
                        if len(entry) != 0:
                            if time >= entry[0]:
                                waitlist_ready.append(waitlist[0])
                                entry_ready.append(entry[0])
                                del waitlist[0]
                                del entry[0]
            
            time += 1
            currentjob -= 1
            
            #Wenn Feierabend ist
            if time == feierabend:
                time += 960
                feierabend += 1440
    
    
    #######################################################################  
    print("\n -------------------------------------------- \n")
    print(' Erste Methode: Erledigung in Reihenfolge \n')
    earlybird(entry.copy(),waitlist.copy())

    print("\n -------------------------------------------- \n")
    
    print('Zweite Methode: Kürzeste Aufträge haben Priorität \n')
    short_is_great(entry.copy(),waitlist.copy())
    
    print("\n -------------------------------------------- \n")
   
    print('Dritte Methode: Zufällige Auswahl aus verfügbaren Aufträgen \n')
    zufällig(entry.copy(),waitlist.copy())
    
    print("\n -------------------------------------------- \n")
    
    print('Vierte Methode: Letzter eingetroffener Auftrag wird bearbeitet')
    letzter_auftrag(entry.copy(),waitlist.copy())
    
worktime(input('Dateiname der Textdatei mit den Auftragsdaten: '))







