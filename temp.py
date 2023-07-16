import os
import re
# try:
import psutil
import tkinter as tk
from tkinter import messagebox

antigo = "SERVER032"
novo = "vhpats4qci.sap.patrimar.com.br"

import itertools

def generate_combinations(word):
    combinations = []
    for i in range(1, len(word) + 1):
        for combo in itertools.product(*zip(word.upper(), word.lower())):
            combinations.append(''.join(combo[:i]) + word[i:])
    return tuple(combinations)
combinacoes = generate_combinations(antigo)
servidor = []
for x in combinacoes:
    servidor.append([x,novo])
print(servidor)
