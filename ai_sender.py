from g4f.client import Client

graficke = open("./data/graficke.txt", 'r').read()
maticne_ploce = open("./data/maticne_ploce.txt", 'r').read()
napajanje = open("./data/napajanje.txt", 'r').read()
procesori = open("./data/procesori.txt", 'r').read()
ram = open("./data/ram.txt", 'r').read()
ssd = open("./data/ssd.txt", 'r').read()
hladjenje = open("./data/kuleri.txt", 'r').read()
kucista = open("./data/kucista.txt", 'r').read()

client = Client()
response = client.chat.completions.create(
    model="gpt-4",
    messages = [
        {"role": "user", "content": "Zdravo, zelim da sastavim kompjuter cija ce cijena biti oko 1400€, zelim da je sto bolja graficka posto zelim da radim machine learning i da igram igrice. Dacu ti spisak: grafickih, maticnih poca, napajanja, procesora, ram, ssd, hladjenja i kucista"},

        {"role": "user", "content": graficke},
        {"role": "user", "content": maticne_ploce},
        {"role": "user", "content": napajanje},
        {"role": "user", "content": procesori},
        {"role": "user", "content": ram},
        {"role": "user", "content": ssd},
        {"role": "user", "content": hladjenje},
        {"role": "user", "content": kucista},


        {"role": "user", "content": "Pa sta mislis, sta da kupim?"},
    ],
)

print(response.choices[0].message.content)
