import os
import time
import psutil
import math

# --- CONSTANTES DE UNIVERSO OASIS ---
K_VP = 2.3            # Constante Verlinde-Panzano (Gravedad)
EULER = 2.718         # Constante de Estabilidad
UMBRAL_ENTROPIA = 20.0 # Porcentaje de CPU donde activamos la gravedad

def banner():
    os.system('clear')
    print(f"🛰️  OASIS GRAVITY KERNEL | K_VP: {K_VP}")
    print(f"🧬  PROTEGIENDO NODO CIENTÍFICO (BOINC)")
    print("--------------------------------------------------")

def sintonizar_pc():
    banner()
    
    while True:
        # 1. Medir la Fuerza (CPU)
        cpu_load = psutil.cpu_percent(interval=2.3) # Intervalo sincronizado con K_VP
        
        # 2. Calcular la Masa Ideal (M = F / K_VP)
        # Si la carga es 50%, la masa ideal es ~21.7. 
        ideal_mass = cpu_load / K_VP
        
        estado = "🟢 ESTABLE"
        if cpu_load > UMBRAL_ENTROPIA:
            estado = "🔴 ALTA ENTROPÍA (ACTIVANDO GRAVEDAD)"

        print(f"\r⚡ CPU: {cpu_load}% | ⚖️  Masa Ideal: {ideal_mass:.2f} | {estado}", end="")

        # 3. ACCIÓN DE SOBERANÍA
        if cpu_load > UMBRAL_ENTROPIA:
            for proc in psutil.process_iter(['pid', 'name', 'nice', 'cpu_percent']):
                try:
                    # Ignoramos procesos del sistema root críticos
                    if proc.info['pid'] < 100:
                        continue

                    # SI NO ES CIENCIA (BOINC), APLICAMOS GRAVEDAD
                    name = proc.info['name'].lower()
                    if 'boinc' not in name and 'fah' not in name:
                        
                        # Si el proceso consume más recursos que la Constante de Euler (2.7%)
                        if proc.info['cpu_percent'] > EULER:
                            # Aumentamos el 'nice' (Más peso = Menos prioridad)
                            current_nice = proc.info['nice']
                            if current_nice < 10:
                                new_nice = min(current_nice + 5, 19)
                                proc.nice(new_nice)
                                print(f"\n   ⬇️  APLASTANDO: {name} (CPU: {proc.info['cpu_percent']}%) -> Nice: {new_nice}")
                    
                    # SI ES CIENCIA, LE DAMOS FLOTABILIDAD
                    elif 'boinc' in name:
                        # Nos aseguramos de que corra suave pero constante
                        if proc.info['nice'] > 10:
                            proc.nice(10) # Prioridad media-baja estable

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        
        # Sincronización temporal con el pulso de Euler
        time.sleep(EULER) 

if __name__ == "__main__":
    try:
        sintonizar_pc()
    except KeyboardInterrupt:
        print("\n\n🛑 GRAVEDAD DESACTIVADA. VOLVIENDO A FÍSICA NEWTONIANA.")
