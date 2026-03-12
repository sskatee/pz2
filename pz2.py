import numpy as np
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w", encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

costs = np.array([
    [6, 12, 20, 24],   # Стратегия 1
    [9, 7, 9, 28],     # Стратегия 2
    [23, 18, 15, 19],  # Стратегия 3
    [27, 24, 21, 15],  # Стратегия 4
])

risks = np.array([
    [0, 5, 11, 9],     # Стратегия 1
    [3, 0, 0, 13],     # Стратегия 2
    [17, 11, 6, 4],    # Стратегия 3
    [21, 17, 12, 0],   # Стратегия 4
])
#Вальд
max_losses = costs.max(axis=1)
logging.info(f'Максимальные потери по стратегиям (Вальда): {max_losses}')
strategy_wald = np.argmin(max_losses)
logging.info(f'Выбранная стратегия по Вальду: {strategy_wald + 1} (индекс {strategy_wald})')

#Сэвидж
max_per_scenario = risks.max(axis=1)
logging.info(f'Максимальные потери по сценариям для каждой стратегии (Сэвидж): {max_per_scenario}')
strategy_savage = np.argmin(max_per_scenario)
logging.info(f'Выбранная стратегия по Сэвиджу: {strategy_savage + 1} (индекс {strategy_savage})')
#Гурвиц
p = 0.6
min_losses = costs.min(axis=1)
max_losses = costs.max(axis=1)
gurrvicz_values = p * max_losses + (1 - p) * min_losses
logging.info(f'Значения по Гурвицу для стратегий: {gurrvicz_values}')
strategy_gurvica = np.argmin(gurrvicz_values)
logging.info(f'Выбранная стратегия по Гурвица: {strategy_gurvica + 1} (индекс {strategy_gurvica})')

print(f"Стратегия по Вальду: {strategy_wald + 1}")
print(f"Стратегия по Сэвиджу: {strategy_savage + 1}")
print(f"Стратегия по Гурвицу: {strategy_gurvica + 1}")