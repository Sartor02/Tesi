import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leggi il file CSV
df = pd.read_csv('tesi3.csv')

# Converti tutte le colonne tranne la prima in stringhe e sostituisci le virgole con i punti
for col in df.columns[1:]:
    df[col] = df[col].astype(str).str.replace(',', '.').astype(float)

# Funzione per creare un grafico di sopravvivenza
def create_survival_plot(df, title, filename, log_scale=False):
    plt.figure(figsize=(10, 6))
    for col in df.columns[1:]:
        sorted_times = df[col].sort_values().cumsum()
        plt.plot(range(1, len(sorted_times) + 1), sorted_times.values, label=col)  # Utilizza .values per ottenere un array numpy
    
    plt.xlabel('Number of Solutions')
    plt.ylabel('Cumulative Time (ms)')
    plt.title(title)
    plt.legend()
    if log_scale:
        plt.yscale('log')
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

# Crea il grafico per i primi 25 test
create_survival_plot(df.iloc[:25, :], 'Survival Plot for First 25 Tests', 'survival_plot_25.png', log_scale=True)

# Crea il grafico per tutti i test
create_survival_plot(df, 'Survival Plot for All Tests', 'survival_plot_all.png', log_scale=True)
