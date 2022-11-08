#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt

def hüpfburg(datei,sprünge):
    
    #Directed Graph Objekt wird initialisiert, Pfeile und Felder werden eingelesen
    
        G = nx.DiGraph()
        with open(datei) as f:
            node_values = [[] for i in range(int(f.readline().split()[0]))]
            line = f.readline()
            while line:
                edge = tuple(line.split())
                G.add_edges_from([edge])
                line = f.readline()
        
        #Dieser Code gibt den Parkour visuell aus
        pos = nx.kamada_kawai_layout(G)
        if len(node_values) > 30:
            plt.figure(3,figsize=(12,12)) 
        nx.draw_networkx_nodes(G,pos, node_size = 500,node_color = "green")
        nx.draw_networkx_edges(G,pos, edgelist = G.edges(), edge_color = "black")
        nx.draw_networkx_labels(G,pos)
        plt.show()
        
        #Algorithmusfunktion: Wie viele Sprünge von welchem Feld
        #Positive Werte (1,2,3) werden Nested List hinzugefügt
        
        def add_values_positive(node,number):
            
                for i in list(G.successors(str(node))):
                    node_values[int(i)-1].append(1)
            
                for i in range(number):
                    for b,node in enumerate(node_values):
                        if node.count(1+i) == 1:
                            for n in G.successors(str(b+1)):
                                node_values[int(n)-1].append(2+i)
            
        
        #Die selbe Algorithmusfunktion, aber mit negativen Werten
        def add_values_negative(node,number):
            
                for i in list(G.successors(str(node))):
                    node_values[int(i)-1].append(-1)
            
                for i in range(number):
                    for b,node in enumerate(node_values):
                        if node.count(-1-i) == 1:
                            for n in G.successors(str(b+1)):
                                node_values[int(n)-1].append(-2-i)
            
        
        #Auf welchem Feld treffen sich Sasha und Mika und mit wie vielen Sprüngen
        def find_goal_node(sprünge):
            add_values_positive(1,sprünge)
            add_values_negative(2,sprünge)
            for i in range(1,sprünge+1):
                for node in node_values:
                    if node.count(i) > 0 and node.count(-i) > 0:
                        goal_node = node_values.index(node)+1
                        jumps = i
                        return (goal_node,jumps)
                                
                                
        #Rekonstrunktion des Weges mit Anzahl Sprünge von Feld 1
        def find_path_positive(node,jumps):
            path_sasha = []
            path_sasha.append(str(node))
            current = node
            for n in range(jumps):
                for i in G.predecessors(str(current)):
                    if node_values[int(i)-1].count(jumps-1-n):
                        current = i
                        path_sasha.insert(0,str(current))
                        break
            path_sasha.insert(0,"1")
            return print("Sashas Weg:","->".join(path_sasha),"\n")
        
        #Rekonstrunktion des Weges mit Anzahl Sprünge von Feld 2
        def find_path_negative(node,jumps):
            path_mika = []
            path_mika.append(str(node))
            current = node
            for n in range(jumps):
                for i in G.predecessors(str(current)):
                    if node_values[int(i)-1].count(-jumps+1+n):
                        current = i
                        path_mika.insert(0,str(current))
                        break
            path_mika.insert(0,"2")
            return print("Mikas Weg:","->".join(path_mika))
        
        
                    
            
            
            
        #Wenn mehr als 100000 Sprünge ohne Lösung berechnet wurden gibt es keine (Siehe Dokumentation)   
        try:
            goal_node,jumps = find_goal_node(sprünge)
        except:
            if sprünge >= 1000:
                return print('Nicht lösbar mit dieser Anzahl von Sprüngen \n{} Sprünge bei lediglich {} Feldern und keine Lösung -> Der Parkour ist nicht lösbar'.format(sprünge,len(node_values)))
            else: 
                return print('Nicht lösbar mit dieser Anzahl von Sprüngen. Versuch es mit mehr!')
        print('Erfolgreich absolviert in {} Sprüngen!\n'.format(jumps))   
        find_path_positive(goal_node,jumps)
        find_path_negative(goal_node,jumps)

hüpfburg(input('Dateiname:'),int(input('\nAnzahl der zu berechnenden Sprünge: ')))
        






