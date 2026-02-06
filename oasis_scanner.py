import math
import random
import sys

# --- CONSTANTES GEOMÉTRICAS ---
PHI = (1 + 5 ** 0.5) / 2
PI = math.pi
EULER = math.e
ROOT2 = 2 ** 0.5

# Colores
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def test_frequency(name, interval, cycles=5000):
    # Aumentamos a 5000 ciclos para eliminar la suerte (Ley de Grandes Números)
    collisions = 0
    # Semilla fija para que la comparación sea justa
    random.seed(42) 
    
    for i in range(cycles):
        noise = random.uniform(0.99, 1.01) # Ruido de sistema real (jitter)
        arrival_time = (i * interval) * noise
        
        # Si cae cerca de un entero, es colisión (Thundering Herd)
        if abs(arrival_time - round(arrival_time)) < 0.05:
            collisions += 1
            
    efficiency = (1 - (collisions / cycles)) * 100
    return efficiency, collisions

print(f"\n{CYAN}>>> INICIANDO ESCANEO DE RESONANCIA DE TU NODO...{RESET}")
print("Buscando la frecuencia perfecta para tu CPU...\n")

candidates = {
    "Clásico (1.0s)   ": 1.0,
    "Oasis A (Pi/Phi) ": PI / PHI,
    "Oasis B (Phi^2)  ": PHI * PHI,
    "Oasis C (Root 2) ": ROOT2,
    "Oasis D (Euler)  ": EULER,
    "Oasis E (Golden) ": PHI
}

best_eff = 0
best_name = ""

for name, interval in candidates.items():
    eff, col = test_frequency(name, interval)
    bar_len = int(eff / 5)
    bar = "█" * bar_len
    
    # Color de la barra
    color = GREEN if eff > 90 else RED
    if eff > 90: print(f"{name} [{interval:.4f}s] | {color}{bar}{RESET} {eff:.2f}% (Colisiones: {col})")
    else:        print(f"{name} [{interval:.4f}s] | {color}{bar}{RESET} {eff:.2f}% (Colisiones: {col})")

    if eff > best_eff:
        best_eff = eff
        best_name = name

print(f"\n{CYAN}============================================{RESET}")
print(f"🏆 FRECUENCIA GANADORA: {GREEN}{best_name}{RESET}")
print(f"🚀 EFICIENCIA MÁXIMA: {best_eff:.2f}%")
print(f"{CYAN}============================================{RESET}")
