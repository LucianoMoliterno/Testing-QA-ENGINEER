"""
Script de prueba rápida para validar Data-Driven Testing
"""
from utils.datos import DataLoader

print("\n" + "="*60)
print("VALIDACIÓN DE ARCHIVOS DE DATOS")
print("="*60)

# Probar carga de CSV
print("\n[1] Cargando datos desde login.csv...")
login_data = DataLoader.get_login_data()
if login_data:
    print(f"    ✓ {len(login_data)} registros cargados correctamente")
    print(f"    ✓ Primer registro: {login_data[0]}")
else:
    print("    ✗ Error al cargar CSV")

# Probar carga de JSON
print("\n[2] Cargando datos desde productos.json...")
productos_data = DataLoader.get_productos_data()
if productos_data:
    print(f"    ✓ JSON cargado correctamente")
    print(f"    ✓ Productos individuales: {len(productos_data.get('productos_a_comprar', []))}")
    print(f"    ✓ Escenarios de compra múltiple: {len(productos_data.get('compras_multiples', []))}")
    print(f"    ✓ Escenarios de carrito: {len(productos_data.get('escenarios_carrito', []))}")
else:
    print("    ✗ Error al cargar JSON")

print("\n" + "="*60)
print("VALIDACIÓN COMPLETADA")
print("="*60 + "\n")

