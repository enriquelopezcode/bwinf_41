#!/usr/bin/env python
# coding: utf-8

def find_lines(line,book = "Alice_im_Wunderland.txt"):
    # line - String mit Namen der Text Datei mit Zeile und Lücken. Beispiel: "line1.txt"
    
    import copy
    
    #Lückenzeile auslesen
    with open(line) as l:
        line = l.readline()
        words = line.split()
        
    #Buch auslesen, alle Sonderzeichen entfernen und Liste mit Wörtern machen  
    with open(book, encoding="utf-8") as b:
        full = ''.join(b.readlines())
        fuller = ""
        for char in full:
            if not char in [",",".","!","?","(",")","[","]","»","«","-","_","*",";"]:
                fuller += char
        fuller = fuller.split()
        for i in range(len(fuller)):
            fuller[i] = fuller[i].lower()
        
        #Zeilenlänge
        length = len(words)
        
        #Erstes verfügbares Wort in Lückenzeile ermitteln
        for i in range(len(words)):
            if words[i] != "_":
                first = i
                break
        
        #Alle Sätze in neue Auswahlliste welche ein gleiches Wort an der richtigen Position und die selbe Länge haben
        selection = []
        for i in range(len(fuller)):
            if fuller[i] == words[first]:
                selection.append(fuller[i-first:i+(length-first)])
        
        #Kopie mit Originalsätzen
        satze = copy.deepcopy(selection)
        
        
        #Positionen der Lücken im Satz ermitteln
        indexes = []
        for i in range(len(words)):
                if words[i] == '_':
                    indexes.append(i)
      
        #Alle Lücken im Lückensatz entfernen
        for i in range(words.count("_")):
            words.remove("_")
            
        #Alle Stellen an denen bei Lückenzeile Lücken waren in Sätzen der Auswahlliste entfernen
        solution = [] 
        for n in range(len(selection)):
            for i in range(length):
    
                if i in indexes:
                    selection[n][i] = "*"
                
            for i in range(selection[n].count("*")):
                selection[n].remove('*')

                
            #Lösungen sind die Sätze, welche die gleichen Wörter wie die Lückenzeile an den passenden Stellen haben
            if selection[n] == words:
                solution.append(" ".join(satze[n]))
        solution = set(solution)
        return solution
        
                   
find_lines(line = input('Dateiname der Lückenzeile: '))                
                
