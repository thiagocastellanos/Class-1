
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "Representa un emoticono de una cara riendose a carcajadas",
            "ROFL": "Una respuesta a una broma",
            "SHEESH":  "Ligera desaprobación",
            "CREEPY":  "Aterrador, siniestro",
            "AGGRO":  "Ponerse agresivo/enojado"}
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("La respuesta es :")
    print(meme_dict[word])
else:
    print("LA PALABRA NO SE ENCUENTRA EN EL DICCIONARIO")
