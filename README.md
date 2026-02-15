# Human Machine Interface for Wafer Alignment in Semiconductor Module

## 📌 Project Overview
This project presents an embedded system prototype designed for wafer alignment detection and correction in semiconductor processing modules. The system integrates real-time sensor acquisition, motor control, and industrial-style Human Machine Interface (HMI) monitoring.

The objective is to simulate an industrial semiconductor alignment module using structured firmware architecture and hardware-software integration.

---

## 🛠 Technologies & Hardware
- Raspberry Pi 4
- SPI-based 12-bit ADC
- LDR Sensor (Wafer Edge Detection)
- Motor Driver Module
- DC / Servo Motor for Alignment
- UART Serial Communication
- Node-RED for HMI Dashboard

---

## 🧠 Technical Highlights
- Implemented SPI communication for external ADC data acquisition
- Designed modular firmware architecture (sensor, control, communication layers)
- Developed alignment correction logic using motor control
- Structured UART-based serial protocol for real-time data transmission
- Integrated embedded firmware with Node-RED HMI visualization
- Organized repository following industry-style project structure

---

## ⚙️ System Architecture
![System Architecture](assets/Proteus Schematic.png)

---

## 📊 HMI Dashboard
![Node-RED Dashboard](assets/UI Capture of Node-Red Dashboard.png)

---

## 📁 Repository Structure
firmware/   → Embedded control logic and drivers  
hardware/   → Hardware component documentation  
docs/       → Project reports and technical documentation  
assets/     → System diagrams and screenshots  

---

## 🚀 Key Features
- Real-time wafer edge detection
- Automated motor-based alignment correction
- SPI-based ADC sampling
- Structured serial communication interface
- Industrial monitoring via HMI dashboard

---

## 📄 Documentation
Detailed project reports are available in:
- docs/Final_Report.pdf
- docs/Industrial_Enhancement_Report.pdf

---

## 🎯 Applications
- Semiconductor wafer alignment systems
- Industrial automation prototypes
- Embedded HMI monitoring solutions
- Sensor-based motor control systems

---

## 👨‍💻 Author
Srihari V V  
B.E. Electronics and Communication Engineering  
Embedded Systems & Industrial Automation Enthusiast








# Human Machine Interface for Wafer Alignment in Semiconductor Module

## Project Overview
This project demonstrates an embedded system prototype developed for wafer alignment detection and correction in semiconductor processing modules. The system performs real-time sensor acquisition, motor control, and industrial-style Human Machine Interface (HMI) monitoring using a Raspberry Pi platform.

The objective is to simulate an industrial wafer alignment workflow using structured firmware design and proper hardware–software integration.

---

## Project Highlights
- Modular firmware architecture separating drivers and application logic
- SPI communication with MCP3008 (10-bit ADC)
- Real-time wafer edge detection using LDR sensor
- Threshold-based motor alignment correction
- Emergency stop safety handling mechanism
- 16x2 LCD interface using 4-bit communication mode
- Wafer batch counting system with limit control (0–12)

---

## Technologies & Hardware Used
- Raspberry Pi 4
- MCP3008 (10-bit SPI ADC)
- LDR Sensor
- DC Motor with motor driver
- 16x2 LCD Display (4-bit mode)
- Push Buttons (Wafer Detect, Count, Reset, Emergency Stop)
- Status LEDs (Red & Green)
- Node-RED for HMI dashboard visualization

---

## Technical Implementation
The LDR sensor output is read through the MCP3008 ADC using SPI communication. The firmware continuously monitors the light intensity to determine wafer alignment status.

If the measured value crosses the defined threshold, the motor is activated to perform alignment correction. Once proper alignment is achieved, the motor stops and the LCD updates the system status.

The system also includes:
- Wafer presence detection logic
- Batch counting with maximum limit control
- Reset functionality
- Emergency stop override
- LED-based status indication

The firmware is structured for clarity and scalability, following an industry-style project layout.

---

## System Architecture
![System Architecture](assets/Proteus Schematic.png)

---

## HMI Dashboard
![Node-RED Dashboard](assets/UI Capture of Node-Red Dashboard.png)

---

## Repository Structure
firmware/   → Embedded control logic and drivers  
hardware/   → Hardware component documentation  
docs/       → Project reports and technical documentation  
assets/     → System diagrams and screenshots  

---

## How to Run

### 1. Install Required Libraries
```bash
sudo apt update
sudo apt install python3-spidev
sudo apt install python3-rpi.gpio
2. Enable SPI Interface
sudo raspi-config
Navigate to:
Interface Options → SPI → Enable

Reboot the Raspberry Pi after enabling SPI.

3. Run the Program
cd firmware
python3 main.py
Applications
Semiconductor wafer alignment systems

Industrial automation prototypes

Embedded HMI-based monitoring systems

Sensor-driven motor control applications

Future Enhancements
Implement PWM-based motor speed control

Add ADC signal filtering for noise reduction

Introduce PID control for precise alignment

Port firmware to STM32 microcontroller (C-based implementation)

Author
Srihari V V
B.E. Electronics and Communication Engineering
Focused on Embedded Systems and Industrial Automation
