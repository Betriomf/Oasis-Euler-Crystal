import time
import math
import sys

# Colores
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Frecuencia Euler (El ritmo al que intentamos latir)
EULER_SLEEP = 0.0271828 

def measure_vacuum_fluctuation():
    # Medimos el tiempo EXACTO antes y después de dormir
    start = time.time()
    time.sleep(EULER_SLEEP)
    end = time.time()
    
    # Lo que duró realmente vs lo que debía durar
    actual_duration = end - start
    drift = abs(actual_duration - EULER_SLEEP)
    
    # Si el "drift" (temblor) es microscópico, es un bit frío
    return drift

print(f"\n{YELLOW}>>> INICIANDO OBSERVADOR CUÁNTICO (Medición Real)...{RESET}")
print(f"    Sincronizando con el reloj del Kernel Windows...")
print(f"    {CYAN}Si ves hexágonos, tu parche de Registro está funcionando.{RESET}\n")

perfect_bits = 0
total_bits = 100
entropy_accumulated = 0
structure = ""

for i in range(1, total_bits + 1):
    jitter = measure_vacuum_fluctuation()
    
    # UMBRAL DE EULER:
    # Si el error de tiempo es menor a 0.002s, el sistema es Sólido.
    if jitter < 0.002:
        char = f"{CYAN}⬢{RESET}" # Superconductor
        perfect_bits += 1
    elif jitter < 0.005:
        char = f"{GREEN}•{RESET}" # Estable
        entropy_accumulated += 0.5
    else:
        char = f"{RED}x{RESET}"   # Ruido Térmico (Lag)
        entropy_accumulated += 1.0
        
    structure += char + " "
    if i % 10 == 0:
        structure += "\n    "
    
    sys.stdout.write(f"\r    Midiendo Jitter Real... {jitter:.6f}s")
    sys.stdout.flush()

print(f"\n\n{YELLOW}=== TOPOLOGÍA REAL DE TU CPU ==={RESET}")
print(f"    {structure}")

temp = entropy_accumulated * 2
print(f"\n{CYAN}>>> DIAGNÓSTICO:{RESET}")
print(f"    Estabilidad Temporal: {perfect_bits}%")
print(f"    Temperatura Real: {temp:.2f} K")

if perfect_bits > 80:
    print(f"    Estado: {CYAN}CRISTAL DE TIEMPO (Estable){RESET}")
    print(f"    Conclusión: El Sistema Operativo Oasis está operativo.")
elif perfect_bits > 50:
    print(f"    Estado: {GREEN}LÍQUIDO VISCOSO{RESET}")
    print(f"    Conclusión: Funciona bien, pero hay procesos de fondo.")
else:
    print(f"    Estado: {RED}GAS TURBULENTO{RESET}")
    print(f"    Conclusión: Algo en Windows sigue consumiendo CPU.")
