import os
import time
import re

# --- CONSTANTES DE RED OASIS ---
K_VP = 2.3
PING_BASE_HUMANO = 100 # ms (Percepción de instantaneidad)
# El límite es 43ms. Si pasa de ahí, hay "atasco" (bufferbloat).
PING_LIMITE = PING_BASE_HUMANO / K_VP 

def sintonizar_red():
    print(f"📡 OASIS NET WATCHDOG | Límite de Latencia: {PING_LIMITE:.2f} ms")
    
    while True:
        try:
            # Hacemos un ping rápido a Google DNS (8.8.8.8)
            stream = os.popen('ping -c 1 8.8.8.8')
            output = stream.read()
            
            # Buscamos el número de milisegundos en la respuesta
            match = re.search(r'time=([\d.]+)', output)
            
            if match:
                ping_actual = float(match.group(1))
                
                if ping_actual > PING_LIMITE:
                    print(f"\r🔴 LAG DETECTADO ({ping_actual}ms). Aplicando Gravedad...", end="")
                    # AQUÍ LA ACCIÓN: Si hay lag, pausamos descargas pesadas (simulado)
                    # En el futuro podemos integrar comandos 'tc' para limitar ancho de banda real.
                else:
                    print(f"\r🟢 RED FLUIDA ({ping_actual}ms). Todo en orden.", end="")
            
        except Exception as e:
            pass
            
        # Esperamos 2.3 segundos antes de medir otra vez
        time.sleep(K_VP)

if __name__ == "__main__":
    sintonizar_red()
