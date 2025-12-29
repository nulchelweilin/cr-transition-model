"""
Modelo energético de Costa Rica.
Simula la mezcla de generación eléctrica y calcula emisiones de CO2.
"""

# Capacidades instaladas en kW
hydro_capacity_kw = 2000000
wind_capacity_kw = 1200000
solar_capacity_kw = 800000
geothermal_capacity_kw = 1000000
diesel_generator_backup_capacity_kw = 0  # capacidad de respaldo diésel eliminada
biomass_capacity_kw = 300000

# Factores de emisión (kg CO2/kWh)
emission_factors = {
    'hydro': 0.0,
    'wind': 0.0,
    'solar': 0.0,
    'geothermal': 0.0,
    'diesel': 0.8,
    'biomass': 0.1
}

# Demanda máxima en kW
peak_demand_kw = 4000000

def calcular_emisiones(horas=8760):
    """
    Calcula emisiones anuales basadas en la capacidad y factores.
    Asume que el diésel se usa solo cuando la demanda excede la capacidad renovable.
    """
    capacidad_renovable = hydro_capacity_kw + wind_capacity_kw + solar_capacity_kw + geothermal_capacity_kw + biomass_capacity_kw
    if capacidad_renovable >= peak_demand_kw:
        uso_diesel = 0
    else:
        deficit = peak_demand_kw - capacidad_renovable
        uso_diesel = min(deficit, diesel_generator_backup_capacity_kw)
    
    emisiones_diesel = uso_diesel * horas * emission_factors['diesel']
    emisiones_biomass = biomass_capacity_kw * horas * emission_factors['biomass']
    total = emisiones_diesel + emisiones_biomass
    return total

if __name__ == "__main__":
    emisiones = calcular_emisiones()
    print(f"Emisiones anuales estimadas: {emisiones / 1e6:.2f} millones de kg CO2")
    print(f"Capacidad de respaldo diésel: {diesel_generator_backup_capacity_kw} kW")