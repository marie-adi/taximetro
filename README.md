# 🚖 **TaxiMeter CLI** 🚖

¡Bienvenido a **TaxiMeter**! Este es un programa de línea de comandos en Python que simula el funcionamiento de un taxímetro, calculando la tarifa en función del tiempo de espera y del tiempo de movimiento del taxi.

## 📜 Descripción

TaxiMeter te permite simular un viaje en taxi con tarifas basadas en dos estados del vehículo:

- **Detenido**: 0.02€ por segundo 🛑
- **En movimiento**: 0.05€ por segundo 🚗💨

### 🛠️ Funcionalidades principales:

- Iniciar un nuevo viaje 🏁
- Cambiar el estado del taxi entre "en movimiento" y "detenido" 🔄
- Ver el estado actual del viaje y la tarifa 💵
- Terminar el viaje y ver el resumen de la tarifa total y la duración del viaje 📝

## 📥 Instalación

Este proyecto está hecho en Python, por lo que necesitarás tener Python 3 instalado en tu máquina.

1. Clona el repositorio o descarga los archivos del proyecto. 🔽
2. No se requieren dependencias externas, ya que el proyecto utiliza bibliotecas estándar de Python.

## 🖥️ Uso

Para iniciar el programa, simplemente ejecuta el archivo principal del proyecto:

```bash
python taximeter.py
```
Una vez que el programa esté en ejecución, podrás interactuar con él a través de una serie de comandos:
📋 Comandos disponibles:

    start: Inicia un nuevo viaje. 🏁
    move: Alterna entre los estados "en movimiento" y "detenido". 🚗↔️🛑
    status: Muestra el estado actual del viaje (en movimiento o detenido) y la tarifa acumulada. 📊
    end: Finaliza el viaje y muestra un resumen con la duración total y la tarifa acumulada. 🏁💰
    quit: Sale del programa. 👋

📌 Ejemplo de uso:
```bash
Enter command (start/move/status/end/quit): start
Trip started. Meter is running. 🚖

Enter command (start/move/status/end/quit): move
Taxi is now moving (Rate: 0.05€/second) 🚗💨

Enter command (start/move/status/end/quit): status
Status: Trip in progress - Taxi is moving
Current fare: 0.15€ 💵

Enter command (start/move/status/end/quit): end
Trip Summary:
-----------------
Duration: 30 seconds ⏱️
Total fare: 1.50€ 💶
-----------------

Enter command (start/move/status/end/quit): quit
Thank you for using TaxiMeter! 🙏
```
🧑‍💻 Estructura del Código

El programa se compone de las siguientes clases y funciones principales:

    TaxiMeter: La clase que maneja la lógica del taxímetro, como iniciar el viaje, cambiar el estado del taxi y calcular la tarifa. ⚙️
    show_welcome_message(): Muestra un mensaje de bienvenida y las instrucciones al inicio del programa. 🎉
    run_cli(): Función principal que gestiona la interacción con el usuario a través de la línea de comandos. 💻

🤝 Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de realizar un fork del repositorio y enviar pull requests con mejoras o correcciones. 🔧


