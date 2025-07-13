from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca = Restaurante('Cantina da Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express','Italiano')

# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 5)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
2
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()