import csv

def ouvrir_csv(fp):
    pokemons = {}
    with open(fp, 'r', encoding='utf-8') as fpokemon:
        lecteur_csv = csv.reader(fpokemon)
        for i in lecteur_csv:
            nom = i[0]
            stats = list(map(int, i[1:]))
            pokemons[nom] = stats
    return pokemons

fpkmn = ouvrir_csv('./pokemon.csv')

for nom, stats in fpkmn.items():
    print(f'{nom}: {stats}')

print(isinstance(fpkmn, dict))
print(isinstance(fpkmn['Pikachu'], list))
print(isinstance(fpkmn['Pikachu'][0], int))
