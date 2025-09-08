class TV:
    
    def __init__(self, tamanho):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, trocar_canal):
        self.canal = trocar_canal
        print('Canal trocado para {}'.format(trocar_canal))
    
tv_sala = TV(55)
tv_quarto = TV(76)

tv_sala.mudar_canal('HBO')
tv_quarto.mudar_canal('Discovery Channel')

print(tv_quarto.tamanho)
print(tv_sala.tamanho)

