import pandas as pd
import matplotlib.pyplot as plt

# Funzione per rimuovere separatori di migliaia e convertire in float
def preprocess_value(val):
    try:
        # Rimuove i separatori di migliaia e converte a float
        return float(val.replace('.', '').replace(',', '.'))
    except ValueError:
        return float(val.replace(',', ''))

# Carica il file CSV
data = pd.read_csv('Python/Tesi2.csv')

# Rimuovi separatori di migliaia e converti in float
for algo in ['CBS', 'ICR', 'ICTS', 'ICTS+ID', 'XSTAR']:
    data[algo] = data[algo].apply(preprocess_value)

# Converti il DataFrame in un array NumPy per calcolare il "Virtual Best"
data_numpy = data[['CBS', 'ICR', 'ICTS', 'ICTS+ID', 'XSTAR']].to_numpy()
data['Virtual Best'] = data_numpy.min(axis=1)

# Mappa dei colori per ciascun algoritmo
colors = {
    'CBS': 'red',
    'ICR': 'yellow',
    'ICTS': 'green',
    'ICTS+ID': 'aqua',
    'XSTAR': 'blue'
}

# Funzione per creare scatter plot
def create_scatter_plot(data, x_algo, y_algo):
    # Ordina il DataFrame per XSTAR e poi CBS
    data = data.sort_values(by=[x_algo, y_algo])

    # Aggiungi una colonna per l'indice del test che va da 1 a n
    data['Test'] = range(1, len(data) + 1)
    
    plt.figure(figsize=(10, 6))
    
    # Scatter plot con il nuovo indice del test sull'asse X e il tempo sull'asse Y
    plt.scatter(data['Test'], data[y_algo], alpha=0.5, label=y_algo, color=colors[y_algo])
    plt.scatter(data['Test'], data[x_algo], alpha=0.5, label=x_algo, color=colors[x_algo])
    
    # Converti le serie in array NumPy
    test_array = data['Test'].to_numpy()
    virtual_best_array = data['Virtual Best'].to_numpy()
    
    # Aggiungi la linea Virtual Best
    plt.plot(test_array, virtual_best_array, color='black', linestyle='--', linewidth=1, label='Virtual Best')
    
    plt.title(f'{x_algo} vs {y_algo}')
    plt.xlabel('Test Number')
    plt.ylabel('Time (ms)')
    plt.yscale('log')  # Usa scala logaritmica per migliorare la visualizzazione dei dati
    plt.grid(True)
    
    # Aggiungi la legenda
    plt.legend()
    plt.show()

# Creare scatter plot per XSTAR vs altri algoritmi
for algo in ['CBS', 'ICR', 'ICTS', 'ICTS+ID']:
    create_scatter_plot(data, 'XSTAR', algo)
