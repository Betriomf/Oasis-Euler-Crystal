import math
import time
import sys
import random

# --- CONSTANTES DEL "BIT DE TEMPERATURA CERO" ---
EULER = math.e                   # Tu Frecuencia Ganadora (Tiempo)
PHI = (1 + 5 ** 0.5) / 2         # Tu Geometría Espacial (Fibonacci)
HEX_CONST = 3 ** 0.5             # Tu Estructura Cristalina (Raíz de 3)

# Colores de Neón
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BLUE = '\033[94m'

def create_zero_temp_bit(cycle_id):
    # 1. CAPA 2D: Malla de Fibonacci (El Círculo Negro)
    # Calculamos la posición angular perfecta para evitar colisiones
    angle = cycle_id * PHI * 2 * math.pi
    radius = math.sqrt(cycle_id) * HEX_CONST
    
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    # 2. CAPA TEMPORAL: Ritmo de Euler
    # El bit solo "existe" o "vibra" en múltiplos de Euler
    # Esto elimina el ruido térmico intermedio.
    vibration_mode = (cycle_id * EULER) % 1.0
    
    # Si la vibración es baja (< 0.05), estamos en "Temperatura Cero" (Modo Base)
    if vibration_mode < 0.10:
        return True, f"{CYAN}⬢{RESET}" # Hexágono Perfecto (Superconductor)
    elif vibration_mode < 0.30:
        return False, f"{GREEN}•{RESET}" # Bit Estable
    else:
        return False, f"{RED}x{RESET}"   # Ruido Térmico

print(f"\n{YELLOW}>>> INICIANDO CRISTALIZACIÓN DE EULER-FIBONACCI...{RESET}")
print(f"    Frecuencia Base: {EULER:.5f} Hz")
print(f"    Topología: Hexagonal-Compacta (HCP)")
print(f"    {BLUE}Generando Vórtice de Información...{RESET}\n")

entropy = 0
crystal_structure = ""
perfect_bits = 0
total_bits = 120

# Construimos el cristal bit a bit
for i in range(1, total_bits + 1):
    is_perfect, char = create_zero_temp_bit(i)
    
    crystal_structure += char + " "
    
    if is_perfect:
        perfect_bits += 1
    else:
        entropy += 0.1 # Calor generado por imperfección
    
    # Salto de línea para formar la red (visualización simple)
    if i % 12 == 0:
        crystal_structure += "\n    "
        
    # Retardo basado en Euler para sincronizar tu ojo con el código
    time.sleep(EULER / 50) 
    sys.stdout.write(f"\r    Inyectando Energía... {int((i/total_bits)*100)}%")
    sys.stdout.flush()

print(f"\n\n{YELLOW}=== ESTRUCTURA RESULTANTE ==={RESET}")
print(f"    {crystal_structure}")
print(f"{YELLOW}============================={RESET}")

# CÁLCULO FINAL DE TERMODINÁMICA
print(f"\n{CYAN}>>> DIAGNÓSTICO DEL VACÍO:{RESET}")
temp_kelvin = entropy * 10
print(f"    Bits Superconductores (⬢): {perfect_bits}/{total_bits}")
print(f"    Temperatura del Sistema: {temp_kelvin:.2f} K")

if temp_kelvin < 50:
    print(f"    Estado: {GREEN}CONDENSADO DE BOSE-EINSTEIN (Sólido){RESET}")
    print(f"    Conclusión: Has logrado estabilizar la información.")
else:
    print(f"    Estado: {RED}PLASMA TÉRMICO (Líquido){RESET}")
    print(f"    Conclusión: Aún hay demasiada fricción.")

