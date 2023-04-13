import socket
import threading
import pickle
import joueurs
import world

IP = "127.0.0.1" 
PORT = 5555 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024)
            if message.decode() == "NOM":
                client.send(pseudos.encode())
            if message.decode() == "COLOR":
                client.send(colors.encode())
            else:
                messageload=pickle.loads(client.recv(1024))
                if isinstance(messageload, joueurs.joueur):
                    joueur=messageload
                elif isinstance(messageload, world.world):
                    messageload.tourdejeu(joueur)
                    client.send(pickle.dumps(messageload))
        except:
            print("Une erreur est survenue.")
            client.close()
            break

def send():
    while True:
        message = input()
        client.send(message.encode())

pseudos = input("Entrez votre pseudo : ")
colors = input("Entrez votre couleurs : ")


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
