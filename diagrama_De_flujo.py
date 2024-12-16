import graphviz

# Crear un diagrama de flujo para el programa
dot = graphviz.Digraph(comment='Gestor de Recetas')

# Crear los nodos del diagrama
dot.node('A', 'Inicio')
dot.node('B', 'Mostrar menú de opciones')
dot.node('C', 'Opción 1: Agregar receta')
dot.node('D', 'Agregar receta a archivo JSON')
dot.node('E', 'Opción 2: Ver receta')
dot.node('F', 'Mostrar receta desde archivo JSON')
dot.node('G', 'Opción 3: Eliminar receta')
dot.node('H', 'Eliminar receta del archivo')
dot.node('I', 'Opción 4: Listar recetas')
dot.node('J', 'Listar recetas disponibles')
dot.node('K', 'Opción 5: Generar lista de compras')
dot.node('L', 'Generar lista de compras')
dot.node('M', 'Opción 6: Salir')
dot.node('N', 'Fin')

# Conectar los nodos
dot.edge('A', 'B')
dot.edge('B', 'C', label='Opción 1')
dot.edge('C', 'D', label='Agregar receta')
dot.edge('B', 'E', label='Opción 2')
dot.edge('E', 'F', label='Ver receta')
dot.edge('B', 'G', label='Opción 3')
dot.edge('G', 'H', label='Eliminar receta')
dot.edge('B', 'I', label='Opción 4')
dot.edge('I', 'J', label='Listar recetas')
dot.edge('B', 'K', label='Opción 5')
dot.edge('K', 'L', label='Generar lista de compras')
dot.edge('B', 'M', label='Opción 6')
dot.edge('M', 'N', label='Salir')

# Mostrar el diagrama
dot.render('/mnt/data/diagrama_flujo_gestor_recetas', format='png', view=True)
