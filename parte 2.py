import random
import time

def simulate_iot(total_steps=10):
    for step in range(total_steps):
        presence = random.choice([True, False])
        temperature = random.uniform(20, 28)

        lights = "ON" if presence else "OFF"
        ac = "ON" if temperature > 22 else "OFF"

        print(f"Passo {step+1}: Presença={presence}, Temp={temperature:.1f}°C, Luzes={lights}, AC={ac}")
        time.sleep(0.5)

if __name__ == '__main__':
    simulate_iot()