# Laboratorio de patrones de diseño en Python

Código del laboratorio de Ingeniería de Software II, separado en un archivo
independiente por patrón. Basado en `Laboratorio_Patrones_de_Diseño_1.pdf`,
de los profesores Carlos Sierra y Liliana Olarte.

## Requisitos y ejecución

Python 3.9 o superior. Todos los ejemplos usan solamente la biblioteca estándar;
no es necesario instalar paquetes.

Ejecutar un ejemplo desde esta carpeta:

```bash
python 01_builder.py
```

Ejecutar los 13 ejemplos y guardar nuevamente la salida real:

```bash
python ejecutar_todos.py
```

El archivo `resultados.txt` contiene las salidas de los ejemplos, su estado de
ejecución y el resumen final. Se guarda en UTF-8 junto al código, aunque el
ejecutor se invoque desde otra carpeta.

## Contenido

| Apartado | Patrón | Archivo | Demostración |
| --- | --- | --- | --- |
| 1.1 | Builder | `01_builder.py` | Café personalizado y reutilización del constructor |
| 1.2 | Prototype | `02_prototype.py` | Clonar y personalizar promociones |
| 1.3 | Singleton | `03_singleton.py` | Configuración compartida en una sola instancia |
| 1.4 | Factory Method | `04_factory_method.py` | Crear tres tipos de dulces |
| 2.1 | Adapter | `05_adapter.py` | Adaptar pagos de dólares a centavos |
| 2.2 | Decorator | `06_decorator.py` | Componer notificaciones Email, SMS y Slack |
| 2.3 | Facade | `07_facade.py` | Coordinar un sistema de cine en casa |
| 2.4 | Composite | `08_composite.py` | Sumar tamaños de archivos y carpetas |
| 3.1 | Strategy | `09_strategy.py` | Intercambiar descuentos del carrito |
| 3.2 | Observer | `10_observer.py` | Notificar suscriptores de un canal |
| 3.3 | Command | `11_command.py` | Encender, apagar y deshacer acciones |
| 3.4 | Template Method | `12_template_method.py` | Generar reportes de texto y HTML |
| 3.5 | State | `13_state.py` | Transiciones de un pedido |

## Adaptación del documento

Se conservaron las clases, los ejemplos y el comportamiento del enunciado.
Se corrigió el salto de línea que partía la cadena de `Coffee.__str__` en el
PDF y se reunieron los fragmentos repartidos entre páginas. Cada demostración
está en `main()` con protección `if __name__ == "__main__"`, para poder importar
las clases sin ejecutar el ejemplo automáticamente.

El documento desarrolla los 13 ejemplos y no plantea preguntas ni actividades
adicionales al final. Los resultados se obtuvieron ejecutando el código.

Son ejemplos didácticos: los pagos y las notificaciones solo producen texto en
consola. En Facade, la descripción menciona una pantalla, pero el código del
enunciado únicamente incluye proyector, sonido y reproductor; se conserva ese
alcance. La fábrica conserva el nombre Factory Method del laboratorio, aunque
su implementación corresponde a una fábrica simple con selección por tipo.
