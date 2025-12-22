from numpy import array
def saisir():
    N = int(input("N = "))
    while not (1 <= N < 200):
        print("Erreur : doit être entre 1 et 199")
        N = int(input("N = "))
    return N
def remplir(t, n):
    for i in range(n):
        t[i] = int(input("t["+str(i)+"] = "))

def tri_shell(T,N):
    N = len(T)
    p = 0
    
    # Calcul du pas maximal (séquence de Knuth)
    while p < N:
        p = 3 * p + 1
    
    while p != 0:
        p = p // 3  # division entière comme "p div 3"
        
        # Tri par insertion avec pas p
        for i in range(p, N):
            v = T[i]
            j = i
            
            # Décalage des éléments
            while j >= p and T[j - p] > v:
                T[j] = T[j - p]
                j -= p
            
            T[j] = v
def affichage(t, n):
    for i in range(n):
        print(t[i], end=" | ")
    print("\n")
n=saisir()
t=array([int]*n)
remplir(t,n)
tri_shell(t,n)
affichage(t,n)

