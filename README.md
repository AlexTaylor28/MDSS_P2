# MDSS_P2

Diagrama de Clases (Global):
![image](https://github.com/user-attachments/assets/e8d884ce-9561-4764-803a-ca002433ed28)

Diagrama de Secuencia (Estado Lote Materia Prima)
![image](https://github.com/user-attachments/assets/948677b6-ad09-4f00-96b9-bca58be48834)

Informe:


Estados del Lote:
Se ha aplicado el patrón State tanto en el lote de materia prima como en el lote de producción de manera idéntica. Cada estado mantiene una referencia a la instancia del lote al que pertenece y delega todas las acciones directamente a la implementación correspondiente en el estado. Esto permite un control más estricto sobre las restricciones de cada acción según el estado en el que se encuentre el lote.
Además, el sistema aprovecha la búsqueda de métodos (Method Lookup) para resolver dinámicamente la implementación correcta de cada método. Si un método no está definido en un estado específico, la resolución recae en la clase base, donde se implementan todas las acciones no permitidas generando un error.

Analizador de Lote de Materia Prima:
Se ha aplicado el patrón Visitor en la relación entre las clases Producto y Analizador. Este patrón desacopla la lógica de análisis de los productos, permitiendo agregar operaciones a los objetos sin modificar sus clases. Producto define una interfaz genérica para los productos (AceiteDeOliva y OlivaDeMesa), mientras que Analizador define operaciones que se aplican a LotePrima, dependiendo del tipo de Producto para determinar qué método específico utilizar. Finalmente, Producto delega la lógica de análisis a un Analizador, sin conocer su implementación interna.

Indicador de Calidad de Producto Final:
Se ha aplicado el patrón Stratergy para evaluar la calidad de productos como Aceite de Oliva y Olivas de Mesa. Cada tipo de producto tiene su propia estrategia de evaluación de calidad, lo que permite modificar el comportamiento de la evaluación sin alterar las clases de los productos.
