# -*- coding: utf-8 -*-

import json

from serie import Serie

class Main:
    def __init__(self):
        self.listaSeries = []
        self.listaObjetos = []
    
    def salvarDados(self):
        for serie in self.listaSeries:
            objeto = {
                "nome": serie.nome,
                "qntTemporadas": serie.qntTemporadas,
                "qntEpisodios": serie.qntEpisodios, 
                "tmpMedioEpisodio": serie.tmpMedioEpisodio,
                "notaIMDB": serie.notaIMDB,
                "categoria": serie.categoria,
                "avaliacoes": serie.avaliacoes
            }
            self.listaObjetos.append(objeto)
            
        with open('series.json','w',encoding='utf-8') as file:
            json.dump(self.listaObjetos,file)
    
    def lerDados(self):
        with open('series.json',encoding='utf-8') as file:
            self.listaObjetos = json.load(file)
        
        for objeto in self.listaObjetos:
            nome = objeto["nome"]
            qntTemporadas = objeto["qntTemporadas"]
            qntEpisodios = objeto["qntEpisodios"]
            tmpMedioEpisodio = objeto["tmpMedioEpisodio"]
            notaIMDB = objeto["notaIMDB"]
            categoria = objeto["categoria"]
            avaliacoes = objeto["avaliacoes"]
            
            serie = Serie(nome = nome, qntTemporadas = qntTemporadas, qntEpisodios = qntEpisodios, tmpMedioEpisodio = tmpMedioEpisodio, notaIMDB = notaIMDB, 
                                      categoria = categoria, avaliacoes = avaliacoes)
            
            self.listaSeries.append(serie)
           
        del self.listaObjetos[:] 
           
    def menu(self):
        print("1. Menu: exibe informações do sistema\n"+
              "2. Adicionar: adiciona uma série no catálogo\n"+
              "3. Imprimir: imprime lista de séries no catálogo\n"+
              "4. Buscar: busca uma série a partir do nome\n"+
              "5. Mais Bem Avaliada: informações sobre a série mais bem avaliada do catálogo\n"+
              "6. Adiciona uma Review: cadastra a review de uma série no catálogo\n"+
              "7. Por Categoria: exibe séries no catálogo a partir de uma categoria\n"+
              "8. Tempo Total Estimado: retorna o tempo total estimado de uma série, em horas\n"+
              "0. Fecha o programa.\n")
    
    def adicionar(self):
        nome = input("Informe o nome da série: ")
        qntTemporadas = input("Informe a quantidade de temporadas da série: ")
        qntEpisodios = input("Informe a quantidade total de episódios da série: ")
        tmpMedioEpisodio = input("Informe o tempo médio de cada episódio da série (em minutos): ")
        notaIMDB = input("Informe a nota IMDB da série: ")
        categoria = input("Informe a categoria da série: ")
        
        serie = Serie(nome = nome, qntTemporadas = qntTemporadas, qntEpisodios = qntEpisodios, tmpMedioEpisodio = tmpMedioEpisodio, notaIMDB = notaIMDB, 
                                      categoria = categoria)
        self.listaSeries.append(serie)
        
        print(f"{serie.nome} foi adicionada ao catálogo.\n")
        
    def imprimir(self):
        print("Lista de séries no catálogo: \n\n")
        for serie in sorted(self.listaSeries, key = lambda x: x.nome):
            print(serie.nome)
        
        print("\n")
            
    def buscar(self):
        nomeDaSerie = input("Informe o nome da série para a busca: ")
        achou = False
        for serie in self.listaSeries:
            if serie.nome == nomeDaSerie:
                achou = True
                print(f"série {serie.nome}:\n"+
                      f"Quantidade de temporadas: {serie.qntTemporadas}\n"+
                      f"Quantidade de episódios: {serie.qntEpisodios}\n"+
                      f"Tempo médio de cada episódio (em minutos): {serie.tmpMedioEpisodio}\n"+
                      f"Nota IMDB: {serie.notaIMDB}\n"+
                      f"Categoria: {serie.categoria}")
                
                if serie.avaliacoes != None:
                    print(f"Avaliações: {len(serie.avaliacoes)}")
                    for review in serie.avaliacoes:
                        print(review + "\n\n")
                else:
                    print("Avaliações: 0")
                    
                
                 
                
                
        if not achou:
            print("Série não encontrada no catálogo.\n")
                
                
    def maisBemAvaliada(self):
        listaSeriesbyReview = sorted(self.listaSeries, key = lambda x: x.notaIMDB, reverse = True)
        serie = listaSeriesbyReview[0]
        if listaSeriesbyReview:
            print(f"A série mais bem avaliada do catálogo é {serie.nome}.\n\n"+
                    f"Quantidade de temporadas: {serie.qntTemporadas}\n"+
                    f"Quantidade de episódios: {serie.qntEpisodios}\n"+
                    f"Tempo médio de cada episódio (em minutos): {serie.tmpMedioEpisodio}\n"+
                    f"Nota IMDB: {serie.notaIMDB}\n"+
                    f"Categoria: {serie.categoria}")
            if serie.avaliacoes != None:
                print(f"Avaliações: {len(serie.avaliacoes)}")
                for review in serie.avaliacoes:
                    print(review + "\n\n")
            else:
                print("Avaliações: 0")
        else:
            print("Nenhuma série no catálogo.\n")
    
    def newReview(self):
        nomeDaSerie = input("Informe o nome da série para review: ")
        index = -1
        for indice, serie in enumerate(self.listaSeries):
            if serie.nome == nomeDaSerie:
                index = indice
                break
        
        if index>=0:
            review = input("Escreva a review:\n\n")
            self.listaSeries[index].avaliacoes.append(review)
            print("A avaliação foi adicionada. Use a opção 4 para exibir as reviews.\n")
        else:
            print("Série não encontrada.\n")
        
    def porCategoria(self):
        categoriaInformada = input("Informe a categoria: ")
        listaSeriesbyCategoria = [serie.nome for serie in sorted(self.listaSeries, key = lambda x: x.nome) if serie.categoria == categoriaInformada]
        if listaSeriesbyCategoria:
            print("Lista de séries:\n\n")
            for serie in listaSeriesbyCategoria: print(serie)
        else:
            print("Nenhuma série com a categoria informada.\n")
           
    def tempoTotalEstimado(self):
        nomeSerie = input("Informe o nome da série: ")
        tempoMedio = 0
        for serie in self.listaSeries:
            if serie.nome == nomeSerie:
                tempoMedio = serie.tmpMedioEpisodio
                episodios = serie.qntEpisodios
        
        if tempoMedio:
            horasTotais = int(tempoMedio*episodios/60)
            minutosTotais = tempoMedio*episodios%60
            print(f"O tempo total estimado da série é de {horasTotais} horas e {minutosTotais} minutos.\n")
        else:
            print("Série não encontrada.\n")
    
    def run(self):
        self.lerDados()
        print("CATÁLOGO DE SÉRIES\nAutor: Guilherme Reale\n\n")
        opcao = 1
        while (opcao !=0):
            opcao = int(input("Informe a opção desejada (digite 1 para ajuda): "))
            
            if opcao == 1:
                self.menu()
            elif opcao == 2:
                self.adicionar()
            elif opcao == 3:
                self.imprimir()
            elif opcao == 4:
                self.buscar()
            elif opcao == 5:
                self.maisBemAvaliada()
            elif opcao == 6:
                self.newReview()
            elif opcao == 7:
                self.porCategoria()
            elif opcao == 8:
                self.tempoTotalEstimado()
            elif opcao == 0: pass
            else:
                print("Opção inválida")

        self.salvarDados()
        
programa = Main()
programa.run()        