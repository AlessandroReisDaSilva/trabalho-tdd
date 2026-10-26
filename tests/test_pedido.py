import pytest

# from src.pedido import calcular_total

from src.pedido import calcular_taxa_entrega

# def test_calcula_total_de_varios_itens():
#     # Arrange
#     itens = [
#         {"preco": 20, "quantidade": 2},
#         {"preco": 10, "quantidade": 1},
#     ]

#     # Act
#     total = calcular_total(itens)

#     # Assert
#     assert total == 50


# def test_retorna_zero_quando_lista_esta_vazia():
#     # Arrange
#     itens = []

#     # Act
#     total = calcular_total(itens)

#     # Assert
#     assert total == 0


# def test_rejeita_item_com_preco_zero():
#     itens = [{"preco": 0, "quantidade": 1}]

#     with pytest.raises(ValueError, match="preco"):
#         calcular_total(itens)


# def test_rejeita_item_com_quantidade_zero():
#     itens = [{"preco": 20, "quantidade": 0}]

#     with pytest.raises(ValueError, match="quantidade"):
#         calcular_total(itens)


def test_taxa_inicial():
    km = 2
    reais = 50

    resultado = calcular_taxa_entrega(km,reais)
    
    assert resultado == 5

def test_primeiro_km_excedente():
    km = 4
    reais = 50

    resultado = calcular_taxa_entrega(km,reais)
    
    assert resultado == 7

def test_entrega_gratuita():
    km = 5
    reais = 100

    resultado = calcular_taxa_entrega(km,reais)
    
    assert resultado == 0

def test_km_negativo():
    km = -5
    reais = 50

    with pytest.raises(ValueError, match="A Distancia não pode ser negativa"):
        calcular_taxa_entrega(km,reais)

def test_reais_negativo():
    km = 5
    reais = -50

    with pytest.raises(ValueError, match="O Real não pode ser negativo."):
        calcular_taxa_entrega(km,reais)

def test_km_reais_negativo():
    km = -5
    reais = -50

    with pytest.raises(ValueError, match="A Distancia e o Real não podem ser negativos."):
        calcular_taxa_entrega(km,reais)