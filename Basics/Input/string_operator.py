# Display Beep's energy levels

print("Please enter the number of lives")

print("Please enter the energy levels")

print("Please enter the shield levels")

lives = int(input())

energy_levels = int(input())

shield_levels = int(input())

hearts = "♥"*lives

energy_levels = "♦"*energy_levels

shield_levels = "♦"*shield_levels

print(f"Lives: {hearts}")

print(f"Energy: {energy_levels}")

print(f"Shield: {shield_levels}")