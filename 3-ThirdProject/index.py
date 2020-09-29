from AlgoritmoGenetico import AlgoritmoGenetico

TAXA_CROSSOVER = 1
TAXA_MUTACAO = 0.4
GERACOES = 4
POPULACAO = 10
TAMANHO_CROMOSSOMO = 8

ag = AlgoritmoGenetico(TAXA_CROSSOVER, TAXA_MUTACAO, GERACOES, POPULACAO, TAMANHO_CROMOSSOMO)
ag.executaAG()
ag.populacao.printPopulacao()