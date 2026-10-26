# """Regras de negocio relacionadas ao calculo de pedidos."""


# def validar_item(item: dict) -> None:
#     """Valida preco e quantidade de um item.

#     Raises:
#         ValueError: se o preco ou a quantidade nao forem positivos.
#     """
#     if item["preco"] <= 0:
#         raise ValueError("O preco deve ser positivo.")

#     if item["quantidade"] <= 0:
#         raise ValueError("A quantidade deve ser positiva.")


# def calcular_total(itens: list[dict]) -> float:
#     """Calcula o total do pedido.

#     Uma lista vazia resulta em total igual a zero.
#     """
#     total = 0

#     for item in itens:
#         validar_item(item)
#         total += item["preco"] * item["quantidade"]

#     return total


# EXERCICIO:
# Implemente com TDD a funcao descrita abaixo.

# Red
# def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
#     if total_pedido >= 100:
#         return 0
#     else:
#         if distancia_km <= 3:
#             return 5
#         else:
#             return 5 + (2*(distancia_km-3))


# green
# def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
#     if distancia_km < 0 or total_pedido < 0:
#         if distancia_km < 0 and total_pedido < 0:
#             raise ValueError("A Distancia e o Real não podem ser negativos.")
#         elif total_pedido < 0:
#             raise ValueError("O Real não pode ser negativo.")
#         else:
#             raise ValueError("A Distancia não pode ser negativa")
#     else:
#         if total_pedido >= 100:
#             return 0
#         else:
#             if distancia_km <= 3:
#                 return 5
#             else:
#                 return 5 + (2*(distancia_km-3))

# Refactor
def calcular_taxa_entrega(distancia_km: float, total_pedido: float) -> float:
    if distancia_km < 0 or total_pedido < 0:
        if distancia_km < 0 and total_pedido < 0:
            raise ValueError("A Distancia e o Real não podem ser negativos.")
        elif total_pedido < 0:
            raise ValueError("O Real não pode ser negativo.")
        else:
            raise ValueError("A Distancia não pode ser negativa")
    else:
        if total_pedido >= 100:
            return 0
        else:
            if distancia_km <= 3:
                return 5
            else:
                vezes = distancia_km-3
                acrescimo = 2*vezes

                return 5 + acrescimo