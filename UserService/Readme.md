# Correr UserService
## Descargar repositorio:

```
git clone https://github.com/amchp/reto-2-gRPC.git
cd reto-2-gRPC
```

## Quitar folders innecesarios

```
rm -r FileService
rm -r SearcherServicer
rm -r Controller
cd UserService
```

## Installar dependencias

```
sudo apt install python3-pip
pip install -r requirements.txt
```

## Configurar IP y puerto
`vim config.json`
Modifique la IP y el PORT al que van a usar.

## Correr applicación
`python3 Server.py`
