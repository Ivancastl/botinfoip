# 📡 VisitorLoggerBot – Flask + Telegram Bot

Este bot registra automáticamente las visitas a tu sitio web y envía información detallada de cada visitante a tu bot de Telegram. Utiliza la API de ipinfo.io para obtener datos geográficos, IP, proveedor de internet, y más. 

## 🚀 ¿Qué hace este bot?

- Muestra una página web.
- Detecta automáticamente la IP del visitante.
- Consulta datos de IP usando la API de [ipinfo.io](https://ipinfo.io).
- Envía los datos al bot de Telegram (sin usar librerías externas).

## 🛠️ Requisitos

- Python
- Flask
- requests
- Token de ipinfo.io
- Bot de Telegram y tu `chat_id`

## Instalación

### **Paso 1:**
Clona este repositorio
```bash
git clone https://github.com/Ivancastl/botinfoip.git
```

### **Paso 2:**
Accede al directorio del proyecto
```bash
cd botinfoip
```

### **Paso 3:**
Instala los requisitos del proyecto:
```bash
pip install -r requirements.txt
```

### **Paso 4:**
Ejecuta el sistema
```bash
Python flask_app.py
```


### **Paso 5:**
Ahora ya puedes dirigirte a tu navegador para su funcionamiento 
```bash
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.70:5000
```


