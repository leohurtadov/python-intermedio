# Curso de Python Intermedio
> - Inicio: 09 de Abril del 2021 
> - Plataforma: Platzi 
> - Docente: Facundo Garcia Martoni

## Zen de Python
Referencia: https://www.python.org/dev/peps/pep-0020/

> import this

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one-- and preferably only one --obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!

## Documentacion
https://docs.python.org/3/

python.org/dev/peps/pep-0008/

## Entornos virtuales
> python 3 -m venv {nombre del entorno}

Los entornos virtuales son vesiones especificas de Python que pueden servir para instalar modulos en especificos sin afectar la version de Python que esta instalada en el computador.

Esto es muy bueno cuando se trabajan diferentes proyectos con Python que requieren diversos modulos con versiones especificas.

## PIP
Es el paquete de instalacion de python, como el npm de JavaScript
> pip freeze 

pip freeze muestra la lista de modulos intalados.

> pip freeze > requirements.txt

Este comando permite convertir nuestra lista de modulos y dependencias en un archivo que puede ser ejecutado.

> pip install -r requirements.txt

Asi es como se instalarian todos los modulos, esto es muy util cuando trabajamos en el mismo proyecto mas de una persona, asi el resto del equipo podra instalar exactamente los mismos modulos y versiones necesarios para el proyecto.