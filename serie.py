class Serie:
    def __init__(self,nome,qntTemporadas,qntEpisodios,tmpMedioEpisodio,notaIMDB,categoria,avaliacoes = None):
        self.nome = nome
        self.qntTemporadas = qntTemporadas
        self.qntEpisodios = qntEpisodios
        self.tmpMedioEpisodio = tmpMedioEpisodio
        self.notaIMDB = notaIMDB
        self.categoria = categoria
        self.avaliacoes = avaliacoes