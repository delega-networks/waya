# WAYA - Where Are You All

[![license](https://shields.io/badge/license-MIT-green)](https://github.com/delega-networks/waya/blob/main/LICENSE)
[![requirements](https://shields.io/badge/requirements-up%20to%20date-brightgreen)](https://github.com/delega-networks/waya)


Este script se crea con la intención de comprobar la seguridad de los nodos en Cosmos y en las redes basadas que usan el SDK-Cosmos, la información recolectada se guardará en el archivo `output.txt`

### Dependencias
```sh
pip install requests
```

### ¿Cómo se usa?

- Se usan dos archivos, uno llamado `input.txt` y otro `output.txt`.

- El archivo `input.txt` tiene la información necesaria para realizar las peticiones, por defecto `localhost 127.0.0.1`. 

- El archivo `output.txt` almacenará la información recolectada como `'nombre' 'IP'` 

Una vez que estamos en la carpeta `waya/` con las dependencias instaladas, damos permisos de ejecución con `chmod +x waya.py` y lo ejecutamos con `./waya.py`. En pocos segundos veremos como empieza a recolectar IPs y nombres _(moniker)_ y la guardará en el archivo `output.json`. Detenemos el script con `ctrnl+c` cuando veamos que no esta almacenando valores y que está dando algunos errores de conexión _(ver TODO)_.


### TODO

[ ] Añadir IDs.

[ ] Pensar una condición final.

[ ] Migrar a Python3.

[ ] Exportar datos a CSV o JSON.
