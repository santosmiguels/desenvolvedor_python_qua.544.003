paises = ["Brasil",
          "Estados Unidos",
          "Mexico",
          "Argentina",
          "Brasil",
          "Argentina",
          "Arabia Saudita",
          "Irã",
          "Brasil",
          "México",
          "Estados Unidos"
          "Brasil"
          ]


pais = input("Informe o pais a ser pesquisado: ").strip().title()

#Armazenar a quantidade de ocorrência na lista:

quantidade = paises.count(pais)

print(f"O {pais} foi encontrado {quantidade} vezes na lista.")
