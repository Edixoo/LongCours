import socket
import threading
from world import world
import pickle

monde = world()

IP = "127.0.0.1"  
PORT = 5555  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

clients = []

# fonction pour gérer la connexion d'un client
def handle_client(conn, addr):
    print(f"Nouvelle connexion établie : {addr}")

    # réception du nom du client
    conn.send("NOM".encode())
    name = conn.recv(1024).decode()
    
    conn.send("COLOR".encode())
    colors = conn.recv(1024).decode()
    clients.append({ "connexion": conn, "nom": name, "couleur": colors, 'index': threading.active_count()-2})
    print("hello " + name + "\n"+ colors)

    broadcast(f"{name} vient de rejoindre la partie".encode())

    # création des joueurs et envoi des données aux clients
    # monde.definirjoueurs()
    joueurs = []
    monde.creer_joueur(threading.active_count()-1, name,colors)

    while True:
        try:
            while(monde.jeuon==True):
                for jou in monde.listejoueur:
                    for client in clients:
                        if client['nom']==jou.pseudo:
                            message = conn.recv(1024)
                            monde= pickle.loads(message)
                            broadcast(message)
                            if client['index']==monde.nbtour%6:
                                client['connexion'].send(pickle.dumps(monde))
                    if(len(jou.listecartes)==0):
                        print("Joueur",jou.id+1,"vous n'avez plus de carte à jouer, vous avez donc perdu")
                        del monde.listejoueur[jou.id]
                if(len(monde.listejoueur)==1):
                    print("Joueur",monde.listejoueur[0].id+1,"BRAVO ! Vous avez gagné avec",monde.listejoueur[0].monnaie,"$")
                    monde.actuclass(monde.listejoueur[0].pseudo)
                    monde.jeuon=False
                    monde.afficher_table_classement()
                monde.inflation
        except:
            conn.close()
            for d in clients:
                if d['connexion']==conn:
                    clients.remove(d)
            broadcast(f"{name} vient de quitter le jeu.".encode())
            break

# def distribuercarte():
    

# fonction pour diffuser un message à tous les clients
def broadcast(message):
    for client in clients:
        client['connexion'].send(message)

def start():
    server.listen()
    print(f"Serveur en écoute sur {IP}:{PORT}...")

    # les connexions clients
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Nombre de connexions actives : {threading.active_count() - 1}")

print("Démarrage du jeu...")
start()

