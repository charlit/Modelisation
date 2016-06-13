ListeSommetsMarques= [['A','*'],['B',''],['C',''],['D','*']]
Liste= [['A'],['B'],['C'],['D']]
Pile=[]
Graphe1 = [[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]

def Ajouter(Element):
    Pile.append(Element)


def Retirer():
    Element=Pile[0]
    del Pile[0]
    return Element

def EstMarque(Sommet):
    for i in range(0, len(ListeSommetsMarques)):   
        if(ListeSommetsMarques[i][0]==Sommet and ListeSommetsMarques[i][1] == '*'):
            print (ListeSommetsMarques[i][0])
   


def Marquer(Sommet):
    for i in range(0, len(ListeSommetsMarques)):   
         if(ListeSommetsMarques[i][0]==Sommet):
            ListeSommetsMarques[i][1]='*'
            print (ListeSommetsMarques)
    
    

Marquer('B')


