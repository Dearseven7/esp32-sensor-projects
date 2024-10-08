# 🏠 Smart Monitoring Projects
Welcome to my collection of smart monitoring projects. These projects utilize various sensors and displays to monitor environmental conditions and make adjustments accordingly.

## 🌡️ Temperature and Humidity Monitoring

Track temperature and humidity levels with real-time data on an OLED display. This project features:
- **DHT11 Sensor** for measuring temperature and humidity.
- **OLED Display** to show real-time readings.
- **PWM Control** to adjust device settings based on temperature.
<img src="images/temperature_humidity.jpeg" alt="Temperature and Humidity" width="500"/>

---

## 🌫️ PM2.5 Detection

Monitor air quality by measuring PM2.5 levels and assessing the air quality index. This project includes:
- **PM2.5 Sensor** for detecting particulate matter.
- **OLED Display** to show PM2.5 concentration and air quality.
- **LED Indicator** to provide visual feedback based on air quality.
<img src="images/pm25_detection.jpeg" alt="PM2.5 Detection" width="500"/>
---

## 💡 Light Intensity Monitoring

Measure light intensity and adjust LED brightness based on light levels. This project involves:
- **Light Sensor** for detecting light intensity.
- **LED Control** to adjust brightness.
- **OLED Display** to show light intensity readings.
<img src="images/light_intensity.jpeg" alt="Light Intensity Monitoring" width="500"/>
---

Feel free to explore each project and see how these technologies work together to create a smart monitoring system!

## Hardware Components
- **DHT11 Sensor:** Measures temperature and humidity.
<img src="images/Temperature&Humidity_Sensor.jpeg" alt="Temperature Humidity Sensor" width="300"/>

- **PM2.5 Sensor:** Measures particulate matter concentration.
<img src="images/PM2.5_Sensor.jpeg" alt="PM2.5 Sensor" width="300"/>

- **Light Sensor (ADC):** Measures ambient light intensity.
<img src="images/Touch_Sensor&Light_Sensor.jpeg" alt="Touch Sensor and Light Sensor" width="300"/>

- **SSD1306 OLED Display:** 128x64 pixel display for data visualization.
<img src="images/OLED_Display.jpeg" alt="OLED Display" width="300"/>

- **PWM-Driven Actuator:** Controls LED brightness based on light intensity and PM2.5 levels.
- **Microcontroller (e.g., ESP32 or similar):** Manages sensor data, display, and PWM control.

## Hardware Setup

1. **DHT11 Sensor:**
   - Connect data pin to GPIO 21.
   - VCC to 3.3V, GND to GND.

2. **PM2.5 Sensor:**
   - Connect the sensor's output (VO) to GPIO 36.
   - VCC to 3.3V, GND to GND.

3. **Light Sensor:**
   - Connect the sensor's output (ADC) to GPIO 35.
   - VCC to 3.3V, GND to GND.

4. **OLED Display:**
   - Connect SCL to GPIO 23.
   - Connect SDA to GPIO 19.
   - VCC to 3.3V, GND to GND.

5. **PWM-Driven Actuator:**
   - Connect PWM pin to GPIO 4.
   - Control LED or similar device based on sensor readings.

## Software Installation

1. **MicroPython:**
   - Install MicroPython on your microcontroller.

2. **Library Installation:**
   - Ensure the `ssd1306` and `dht` libraries are installed for OLED and DHT11 functionality.
   - Install any additional libraries required for PWM and ADC control.

## Code Overview

### Temperature and Humidity Monitoring

- Reads temperature and humidity from the DHT11 sensor.
- Displays data on the OLED screen.
- Logs data to `sensor_data.txt` with a timestamp.

### PM2.5 Detection

- Reads PM2.5 concentration from the sensor.
- Converts ADC readings to µg/m³.
- Categorizes air quality and displays it on the OLED screen.
- Logs data to `PM25_data.txt` with a timestamp and air quality category.

### Light Intensity Monitoring

- Reads light intensity from the light sensor.
- Adjusts LED brightness based on light levels.
- Displays light intensity on the OLED screen.
- Logs data to `light_data.txt` with a timestamp.

