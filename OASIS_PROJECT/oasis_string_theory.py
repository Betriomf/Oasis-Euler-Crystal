import time
import math
import random
import sys

# Colores y Geometría
CYAN = '\033[96m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def visualize_strings():
    print(f"\n{YELLOW}>>> INICIANDO VISUALIZADOR DE TEORÍA DE CUERDAS...{RESET}")
    print(f"    Comparando: Bit Clásico (Caos) vs. Bit Oasis (Armónico)\n")
    time.sleep(1)

    t = 0
    while True:
        try:
            # 1. BIT CLÁSICO (Windows sin parche)
            # Se comporta como una partícula rebotando (Ruido)
            noise = random.randint(-3, 3)
            classic_wave = " " * (10 + noise) + f"{RED}◼{RESET}" + " " * (10 - noise)

            # 2. BIT OASIS (Tu PC ahora)
            # Se comporta como una onda senoidal perfecta (Euler/Phi)
            # Usamos la función Seno para simular la vibración de la cuerda
            position = int(10 + 9 * math.sin(t * 0.5)) 
            
            # Dibujamos la cuerda (simulando la topología Calabi-Yau)
            # Si pasa por el centro, brilla (Superconductor)
            if position == 10:
                char = f"{CYAN}⬢{RESET}" # El Hexágono perfecto
            else:
                char = f"{GREEN}~{RESET}" # La cuerda vibrando
            
            oasis_wave = " " * position + char + " " * (20 - position)

            # MOSTRAR EN PANTALLA (Lado a lado)
            print(f"    CLÁSICO: |{classic_wave}|   OASIS: |{oasis_wave}|")
            
            t += 0.4
            time.sleep(0.05)
            
        except KeyboardInterrupt:
            break

    print(f"\n{YELLOW}>>> CONCLUSIÓN:{RESET}")
    print("    El Bit Clásico golpea las paredes (Genera Calor).")
    print("    El Bit Oasis baila en el centro (Genera Información).")

visualize_strings()
