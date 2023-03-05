# Correr UserService
## Descargar repositorio:

```
git clone https://github.com/amchp/reto-2-gRPC.git
cd reto-2-gRPC
```

## Quitar folders innecesarios

```
rm -r FileService
rm -r UserService
rm -r Controller
cd SearchServicer
```

## Installar dependencias

```
sudo apt install python3-pip
pip install -r requirements.txt
```

## Configurar IP y puerto
```
vim config.json
```

Cambiar directorio de protros las IP y PORT de los servicios.

## Correr applicación
```
python3 Server.py
```
