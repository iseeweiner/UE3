import math

def extraire_min(F, distance): 
    min_dst = math.inf # la plus petite distance trouvée jusqu'à présent
    min_s = None  # le sommet associé à cette plus petite distance
    for s in F: # on parcourt tous les sommets de la file F
        if distance[s] <= min_dst: # si s a une plus petite distance que tout ceux vu jusqu'à présent, c'est lui qui devient le nouveau min_s
            min_s = s 
            min_dst = distance[s] 
    F.remove(min_s) # on retire le plus petite sommet qu'on a trouvé de la file F
    return min_s 

def prim(G):
    ### TODO ####
    # C dict qui pour chaque sommet u associera la cout de connexion de u a l'arbre
    #C[(0,0)] = 0
    C = {}
    # P dict qui pour chaque sommet u associera le parent de u dans l'arbre généré
    #P[(1,0)] = (0, 0)
    P = {}
    for u in G.nodes():
        C[u] = math.inf
        P[u] = 0
    Q = G.nodes()
    while Q:
        u = extraire_min(Q, C[u])


    # COPY #
    F = G.nodes() # ici, on représente notre file comme un dictionnaire 	 
    distance = {}  # pareil pour les distances (contenant "le plus court chemin vu jusqu'à présent")
    pere = {} # le dictionnaire qui permet de représenter le "parent" de chaque sommet afin de garder quel est le chemin parcourut pour obtenir le plus court chemin
	 
    for u in G.nodes(): # initialision de tous les sommets à une distance infinie
        distance[u] = math.inf
        pere[u] = None     
    distance[s] = 0 
    cpt = 1 # ce compteur permet juste d'afficher quel est l'itération courante 
    while F: # tant que F n'est pas vide
        u = extraire_min(F, distance) #ici, la taille de F diminue à chaque itération
        print("Iteration "+str(cpt) + ":\npere : " , pere, "\nDistance : ",distance) # ATTENTION : à commenter sur les grandes instances (par exemple, pour les tours de Hanoi)
        for v in G.predecessors(u): # pour tous les sommets accessibles à partir de u
            if distance[v] > distance[u] + G.weights[(u,v)]:  # on vérifie si l'ajout de l'arete (u,v) permet de découvrir un nouveau plus court chemin
                distance[v] = distance[u] + G.weights[(u,v)] 
                pere[v]= u # le pere nous permet de savoir quel est le sommet par lequel on est arrivé pour trouver le plus court chemin
        cpt += 1
    return pere

