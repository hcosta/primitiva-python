# Simulador sorteo Primitiva

Un pequeño experimento del 2012 escrito en Python con una interfaz en WxPython para visualizar las posibilidades de conseguir un premio de cada categoría en base a un número determinado de intentos.

## Demo

<img src="/docs/demo.gif"/>

## Utilización con Pipenv

```bash
# Instalación de pipenv
pip install pipenv

# Instalación de dependencias
cd primitiva-python/
pipenv install -r requirements.txt

# Ejecución del script
pipenv run python primitiva.py
```

## Nota

Este simulador no está planteado correctamente y tiene varios fallos, como codificar directamente en el fichero de la interfaz o un mal uso (aunque funcional) de los threads. Pero a fin de cuentas forma parte de mi aprendizaje y cuando lo realicé estaba muy orgulloso de él.