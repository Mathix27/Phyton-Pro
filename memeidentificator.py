
meme_dict = {
    "LOL":"Una respuesta a algo gracioso",
    "CRINGE":"Algo raro o embarazoso",
    "ROFL":"Una respuesta a una broma",
    "SHEESH":"Ligera desaprobación",
    "CREEPY":"Aterrador, siniestro",
    "AGGRO":"Ponerse agresivo/enojado"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("Esta palabra significa:", meme_dict[word])
else:
    print("Esta palabra no la conosco")
