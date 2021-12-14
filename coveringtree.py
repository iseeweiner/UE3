import math
import graph


def extraire_min(F, distance): 
    min_dst = math.inf # la plus petite distance trouvée jusqu'à présent
    min_s = None  # le sommet associé à cette plus petite distance
    for s in F: # on parcourt tous les sommets de la file F
        if distance[s] <= min_dst: # si s a une plus petite distance que tout ceux vu jusqu'à présent, c'est lui qui devient le nouveau min_s
            min_s = s 
            min_dst = distance[s] 
    F.remove(min_s) # on retire le plus petit sommet qu'on a trouvé de la file F
    return min_s 

def prim(G):
    # C dict qui pour chaque sommet u associera la cout de connexion de u a l'arbre
    #C[(0,0)] = 0
    C = {}
    # P dict qui pour chaque sommet u associera le parent de u dans l'arbre généré
    #P[(1,0)] = (0, 0)
    P = {}
    for v in G.nodes():
        C[v] = math.inf
        P[v] = []
    Q = G.nodes()
    while Q:
        u = extraire_min(Q, C)
        Q.discard(u)
        for v in G.successors(u):
            if v in Q and G.weights[(u,v)] < C[v]:
                C[v] = G.weights[(u,v)]
                P[v].append(u)
    return P

 