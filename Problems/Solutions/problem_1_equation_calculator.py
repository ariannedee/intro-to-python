"""
Calculate the gravitational force between Earth and Venus
"""

G = 6.67e-11  # Gravitational constant

mass_1 = 6e24  # in kg (mass of Earth)
mass_2 = 4.9e24  # in kg (mass of Venus)
distance = 4.1e10  # in m (distance between Earth and Venus)

force = (G * mass_1 * mass_2) / (distance**2)

print(force)
