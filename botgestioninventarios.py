# -*- coding: utf-8 -*-
"""botGestionInventarios.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lr7Qlfr8NmMa7O-0xeWb3XLTx90L8Jvl
"""



# Procedimientos de menú.

# 1. ---------------- Añadir producto ----------------
def anadir_producto (inventario):
  nombre_producto = input("Ingrese el producto: ").strip().lower();
  if(nombre_producto in inventario):
    print(f"El {nombre_producto} ya se encuentra registrado en el inventario");
  else:
    # Cantidad
    while True:
      try:
        cantidad = int(input("Ingrese la cantidad inicial: "));
        if(cantidad < 0 ):
          print("La cantidad no puede ser menor a 0. Vuelva a intentar.");
        else:
          break;
      except ValueError:
        print("Entrada inválida, por favor ingrese un valor entero.");

    # Precio
    while True:
      try:
        precio = float(input("Ingrese el precio unitario: "))
        if(precio < 0):
          print("El precio no puede ser menor a 0. Vuelva a intentar.");
        else:
          break;
      except ValueError:
        print("Entrada inválida, por favor ingrese un valor flotante.");
  inventario[nombre_producto] = {'cantidad': cantidad, 'precio': precio}
  return inventario;

# 2. ---------------- Actualizar stock ----------------
def actualiza_producto(inventario):
  print("\n -- Actualizar stock del producto --");
  nombre_a_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip().lower();
  if(nombre_a_actualizar not in inventario):
    print(f"El producto {nombre_a_actualizar} no se encuentra en el inventario.");
  else:
    print(f"Producto: {nombre_a_actualizar}");
    print(f"Cantidad actual: {inventario[nombre_a_actualizar]['cantidad']}");
    # Cantidad
    while True:
      try:
        nueva_cantidad = int(input(f"Ingrese la nueva cantidad para el producto {nombre_a_actualizar}: "));
        if(nueva_cantidad<0):
          print("La cantidad no puede ser menor a 0.");
        else:
          break;
      except ValueError:
        print("Entrada inválida, por favor ingrese un valor entero.");

    # Precio
    while True:
      try:
        nuevo_precio = float(input(f"Ingrese el nuevo precio unitario para el producto {nombre_a_actualizar}: "))
        if(nuevo_precio < 0):
          print("El precio no puede ser menor a 0. Vuelva a intentar.");
        else:
          break;
      except ValueError:
        print("Entrada inválida, por favor ingrese un valor flotante.");

  inventario[nombre_a_actualizar] = {'cantidad': nueva_cantidad, 'precio': nuevo_precio}
  return inventario;

# 3. ---------------- Eliminar Producto ----------------
def eliminar_producto(inventario):
  print("\n -- Eliminar el producto --");
  nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip().lower();
  if(nombre_producto not in inventario):
    print(f"El producto {nombre_producto} no se encuentra en el inventario.");
  else:
    confirmacion = input(f"¿Está seguro de eliminar el producto {nombre_producto}? s/n : ").strip().lower();
    if(confirmacion == 's'):
      del inventario[nombre_producto];
      print(f"Producto: {nombre_producto} eliminado.");
    else:
      print("Eliminación cancelada.");
  return inventario;

# 4. ---------------- Ver Inventario ----------------
def ver_inventario(inventario):
  print("\n -- Ver Inventario --");
  if not inventario:
    print("No existe inventario a mostrar.");
  else:
    for nombre, detalles in inventario.items():
      print ( f" Nombre : { nombre } , Cantidad : {detalles ['cantidad']} , Precio : ${ detalles ['precio']:.2f}");

# 5. ---------------- Buscar Producto ----------------
def buscar_producto(inventario):
  print("\n -- Buscar Producto --");
  termino_busqueda = input (" Ingrese el nombre o parte del nombre del producto a buscar : ").strip().lower();
  productos_encontrados = [];
  for nombre, detalles in inventario.items():
    if termino_busqueda in nombre.lower():
      productos_encontrados.append((nombre, detalles));

  if productos_encontrados:
    print("\n -- Resultado de la búsqueda --");
    for nombre, detalles in inventario.items():
      print ( f" Nombre : { nombre } , Cantidad : {detalles ['cantidad']} , Precio : ${ detalles ['precio']:.2f}");
  else:
    print ( f"No se encontraron productos que coincidan con '{ termino_busqueda }'.");

# 6. ---------------- Resumen de inventario ----------------
def resumen_inventario(inventario):
  print("\n -- Resumen Inventario --");
  valor_total_inventario = 0
  for detalles in inventario.values():
    valor_total_inventario += detalles ['cantidad'] * detalles ['precio'];
    print ( f" Valor Total del Inventario : ${valor_total_inventario :.2f}")

  umbral_bajo_stock = 5;
  productos_bajo_stock = []

  for nombre, detalles in inventario.items():
    if detalles ['cantidad'] < umbral_bajo_stock:
      productos_bajo_stock.append (nombre);

    if productos_bajo_stock:
      print ("Productos con bajo stock ( cantidad <{}):".format( umbral_bajo_stock ));
      for p in productos_bajo_stock:
        print ( f"- {p} ( Cantidad : { inventario [p]['cantidad']})");
    else:
      print ("No hay productos con bajo stock.");

  algun_producto_agotado = any(detalles['cantidad'] == 0 for detalles in inventario.values())
  if algun_producto_agotado:
    print (" Advertencia ! Hay al menos unproducto agotado en el inventario .")
  else:
    print ("No hay productos agotados en el inventario.");

# 7. ---------------- Salir ----------------
def salir():
  print("Saliendo del programa. ¡Hasta pronto!");

# ----------------- MAIN -------------------------------------------------------

# Base de Datos de Inventario.
inventario = {
  'manzana'  : { 'cantidad': 2, 'precio': 2.4 },
  'leche'  : { 'cantidad': 1, 'precio': 5.7 },
  'pan'  : { 'cantidad': 5, 'precio': 0.50 },
}

# Menú de Gestion de Inventarios.
while True:
  print("\n--- Menú de Gestión de Inventarios --- ");
  print("1. Añadir producto: ");
  print("2. Actualizar stock: ");
  print("3. Eliminar producto: ");
  print("4. Ver inventario: ");
  print("5. Buscar producto: ");
  print("6. Resumen de inventario: ");
  print("7. Salir: ");

  opcion = input("\n ** Selecciona una opción **: ");
  if opcion == '1':
    inventario = anadir_producto(inventario);
  elif opcion == '2':
    inventario = actualiza_producto(inventario);
  elif opcion == '3':
    inventario = eliminar_producto(inventario);
  elif opcion == '4':
    ver_inventario(inventario);
  elif opcion == '5':
    buscar_producto(inventario);
  elif opcion == '6':
    resumen_inventario(inventario);
  elif opcion == '7':
    salir();
    break;