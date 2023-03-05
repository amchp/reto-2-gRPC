# Installar Controlador

## Descargar repositorio:

```
git clone https://github.com/amchp/reto-2-gRPC.git
cd reto-2-gRPC
```

## Quitar folders innecesarios

```
rm -r FileService
rm -r SearchServicer
rm -r UserService
cd Controller
```

## Installar nodejs:
```
sudo apt update
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
nvm install 18
nvm alias default 18
nvm use 18
nvm install node
```

## Installar dependecias

```
sudo apt install npm
npm install
```

## Cambiar configuraciones
```
vim config.json
```
Cambiar directorio de protros las IPS y PORTS del controllador y de los servicios.

## Correr applicación
```
sudo node index.js
```



