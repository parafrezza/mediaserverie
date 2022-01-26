import os
os.system('clear')

un_minuto_frames                     = 25 * 60
un_ora_di_frames                     = un_minuto_frames * 60
un_ora_di_amore_ti_vorrei            = " solo un'ora "
quante_ore_questo_me_vo_fa_calcolare = 0
frameRate                            = 60
lista_di_framerates_tipici           = [24, 25, 30, 50, 60] 

def dimme_quanti_frame_in_ore (quante_ore, a_che_framerate):
    un_minuto_frames          = a_che_framerate * 60
    un_ora_di_frames          = un_minuto_frames * 60
    return (f"in un {quante_ore} ore ci sono  {un_ora_di_frames * quante_ore} frame")
def saluto_glorioso_al_sole ():
    # si è scelta questa formula di saluto per gli orientamenti religiosi vigenti
    print ("ué")
def chiedi_quante_ore_vuole():
    global quante_ore_questo_me_vo_fa_calcolare
    quante_ore_questo_me_vo_fa_calcolare_in_lettere =  input("dimmi un po', quante ore di frame vuoi che calcoli (in numeri)?\n")
    if (   quante_ore_questo_me_vo_fa_calcolare_in_lettere.isdigit()  ):
        quante_ore_questo_me_vo_fa_calcolare = int(quante_ore_questo_me_vo_fa_calcolare_in_lettere)  # questa parte di codice viene eseguita se isdigit() == True 
    else:
        os.system('clear')
        print("io non so davvero come fare con te, mi serve un numero intero")                       # questa parte di codice viene eseguita se isdigit() == False
        chiedi_quante_ore_vuole()
def chiedi_il_frameRate():
    global frameRate
    print ("\nVa bene, maschio, grazie. Ma, a che framerate? (premi invio per il default a 25)")

    for ognitipicoFramerate in lista_di_framerates_tipici:
        print(f"Vuoi forse andare a {ognitipicoFramerate} per secondo?") # istruzione eseguita una volta per ogni elemento della lista

    frameRate_letterale =  input("\nDimme un po'.\n")

    if frameRate_letterale != "":
        global frameRate
        frameRate = int(frameRate_letterale)
        try:
            fr = lista_di_framerates_tipici.index(frameRate)
        except:
            print("Occhio, maschio. Perché questo framerate non è tipico.")

    if (frameRate <= 0):
        print('no, ok, grazie, ma che ci faccio?')
        chiedi_il_frameRate()


 
saluto_glorioso_al_sole()
chiedi_quante_ore_vuole()
chiedi_il_frameRate()
frame_ritornati = dimme_quanti_frame_in_ore(quante_ore_questo_me_vo_fa_calcolare, frameRate)
print(frame_ritornati) 






# le parentesi quadre si inseriscono con alt(dx) + è

# le parentesi graffe si inseriscono con alt(dx) + SHIFT + è

# "juve merda"                -> str

# 25  (numero intero)        ->  int

# 25.1 (numero frazionario)  ->  float

# print ("juve mmerda")

