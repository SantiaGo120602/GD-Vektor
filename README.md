# GD-Vektor

**Gauss Data Vektors** o GDV en un lenguaje de dominio específico, cuyo interprete está implementado con antlr4, usando un visitor de python3.
Es un lenguaje pensado para el análisis y procesamiento de datos y su sintáxis es similar a la de javascript y python.

## **Requisitos**
* **python** > 3.11
* **antlr4** > 4.11
* **java** >11 (opcional)
* **make** (opcional)
* **antlr4-python3-runtime**
* **numpy**
* **matplotlib**

## **Instalación**
El código fuente se puede obtener usando git desde la terminal:
```bash
git clone https://github.com/SantiaGo120602/GD-Vektor/
```

## **Make**
Si hace algún cambio al código fuente puede recombilar el proyecto usando:
```bash
make build
```
Antes de esto es recomendado eliminar los archivos finales:
```bash
make clean
```
También puede probar todos los programas de pruebas usando:
```bash
make testAll
```
Adicionalmente puede probar los programas de prueba individualmente con:
```bash
make testCalculadora

make testTangente

make testGraficar
```

## **Sintáxis**
La sintáxis entera del lenguaje se puede encontrar en la gramática "GDV_Grammar.g4". A continuación se presentan algunos ejemplos:

* Declaración de variables
```
variable = 1 + 2;
```

* vectores
```
vector = [[1,2,3],[4,5,6]];
```

* JSON
```
data = {num1 : 1, num2 : 2};
```

* Declaración de variables
```
variable = 1 + 2;
```

* Declaración de funciones
```
function foo(x, y){
    return x*y;
}
```
