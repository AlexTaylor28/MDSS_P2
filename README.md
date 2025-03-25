
# MDSS_P2

## Diagrama de Clases (Global)
![image](https://github.com/user-attachments/assets/e668bab6-b710-47ff-8854-5ba6dfe9a407)


## Patrones de Diseño Aplicados

### 1. Patrón **State** - Estados del Lote

El patrón **State** se ha aplicado tanto en el lote de materia prima como en el lote de producción de manera idéntica. Cada estado mantiene una referencia a la instancia del lote al que pertenece y delega todas las acciones directamente a la implementación correspondiente en el estado. Esto permite un control más estricto sobre las restricciones de cada acción según el estado en el que se encuentre el lote.

Además, el sistema aprovecha la **búsqueda de métodos (Method Lookup)** para resolver dinámicamente la implementación correcta de cada método. Si un método no está definido en un estado específico, la resolución recae en la clase base, donde se implementan todas las acciones no permitidas, generando un error.

### 2. Patrón **Visitor** - Analizador de Lote de Materia Prima

El patrón **Visitor** se ha aplicado en la relación entre las clases `Producto` y `Analizador`. Este patrón desacopla la lógica de análisis de los productos, permitiendo agregar operaciones a los objetos sin modificar sus clases. 

- `Producto` define una interfaz genérica para los productos (`AceiteDeOliva` y `OlivaDeMesa`), mientras que `Analizador` define operaciones que se aplican a `LotePrima`, dependiendo del tipo de `Producto` para determinar qué método específico utilizar.
- Finalmente, `Producto` delega la lógica de análisis a un `Analizador`, sin conocer su implementación interna.

### 3. Patrón **Strategy** y **Template Method** - Indicador de Calidad de Producto Final

Se ha aplicado el patrón **Strategy** para evaluar la calidad de productos como Aceite de Oliva y Olivas de Mesa. Cada tipo de producto tiene su propia estrategia de evaluación de calidad, lo que permite modificar el comportamiento de la evaluación sin alterar las clases de los productos.

Además, se utiliza el patrón **Template Method** en el método `calcular_calidad` de la clase abstracta `EstrategiaCalidad`. Este método define el esqueleto del algoritmo para calcular la calidad del producto, pero delega los detalles específicos de cómo calcular cada factor a los métodos abstractos definidos en las subclases.

### 4. Patrón **Strategy**  -  Exportador
Se ha aplicado el patrón **Strategy** para el `Exportador`, con la diferencia de que el `LoteProduccion` no mantiene una referencia a un exportador específico. En lugar de eso, el exportador se pasa como parámetro en la llamada al método exportar, permitiendo un control más directo y rápido sobre el tipo de exportación, manteniendo `ExportadorPDF` como valor predeterminado: `exportar(exportador = ExportadorPDF())`


## Diagrama de Secuencia (Estado Lote Materia Prima)
![image](https://github.com/user-attachments/assets/948677b6-ad09-4f00-96b9-bca58be48834)
