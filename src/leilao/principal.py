from dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario("Gui")
roberto = Usuario("Roberto")
paulo = Usuario("Paulo")

lance_do_roberto = Lance(roberto, 100.0)
lance_paulo = Lance(paulo, 122.22)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_roberto)
leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_paulo)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(
    f"O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}")
