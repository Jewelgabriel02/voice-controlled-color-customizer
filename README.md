# voice-controlled-color-customizer
Automated voice-controlled paint color mixing system using Raspberry Pi 4, Arduino Nano, Python speech recognition, and peristaltic pumps for custom RGB dye dispensing.

## Overview

The Automatic Paint Colour Mixing Machine is an IoT-based automation system developed to create customized paint colours by accurately mixing different base colours in required proportions.

The project combines embedded systems, Python programming, IoT concepts, and automation techniques to develop a system capable of controlling multiple liquid dispensing units for automated colour preparation.

## Project Description

The system uses a Raspberry Pi 4 as the primary processing unit to handle the main application logic, Python programming, and system-level operations. Three peristaltic pumps are used to dispense different base colours in controlled quantities to achieve the desired colour mixture.

An Arduino Nano was integrated as a dedicated microcontroller for low-level hardware control and actuator management. This allowed separation between high-level processing tasks handled by the Raspberry Pi and real-time hardware operations managed by the Arduino.

A microphone module was also explored to investigate voice-based interaction possibilities for future improvements.

## System Architecture & Design Decision

The use of both Raspberry Pi 4 and Arduino Nano was based on functional requirements rather than duplication of hardware.

### Raspberry Pi 4 Responsibilities:
- Running Python-based control logic
- Managing overall system workflow
- Handling IoT-related functionalities
- Processing user inputs and application-level tasks

### Arduino Nano Responsibilities:
- Controlling hardware-level operations
- Managing pump switching operations
- Providing reliable real-time actuator control
- Acting as an intermediate hardware interface

This modular approach helped in:
- Separating software processing from hardware control
- Improving system reliability
- Simplifying debugging and maintenance
- Creating a scalable architecture for future enhancements

## Features

- Automated paint colour mixing system
- Raspberry Pi 4 based processing
- Arduino Nano based actuator control
- Three-channel peristaltic pump operation
- Python-based automation logic
- IoT-enabled system design
- Voice input exploration using microphone module

## Hardware Components

- Raspberry Pi 4
- Arduino Nano
- Peristaltic Pumps (3 units)
- Motor Driver Module
- Microphone Module
- Paint Containers
- Tubing System
- Power Supply Components

## Software & Technologies

- Python
- Raspberry Pi OS
- Arduino Programming (Embedded C/C++)
- GPIO Interfacing
- Embedded Systems
- IoT Concepts
- Hardware-Software Integration

## Working Principle

1. The user provides the required colour selection.
2. The Raspberry Pi processes the required mixing logic.
3. Control instructions are communicated to the Arduino Nano.
4. The Arduino controls the operation of the peristaltic pumps.
5. The pumps dispense accurate quantities of base colours.
6. The final customized colour is produced through mixing.

## Technical Skills Demonstrated

- Python programming
- Raspberry Pi development
- Arduino-based hardware control
- Embedded systems design
- IoT architecture
- Actuator interfacing
- Automation system development
- Hardware-software integration

## Challenges & Learnings

During development, challenges such as hardware interfacing, pump control accuracy, and communication between multiple controllers were addressed.

The project provided practical experience in designing embedded systems where multiple processing units work together to achieve reliable automation.

## Future Improvements

- Camera-based colour recognition
- Machine learning-based colour prediction
- Mobile application integration
- Cloud-based monitoring
- Flow sensor integration for improved accuracy
- Voice-controlled operation

## Project Gallery
<img width="1678" height="721" alt="Screenshot 2026-07-27 233042" src="https://github.com/user-attachments/assets/a808ce8f-5f71-4123-90e0-01c301f2e8a0" />
<img width="1143" height="757" alt="Screenshot 2026-07-27 233025" src="https://github.com/user-attachments/assets/8144f457-5ebc-4b1a-87bf-5c10be19e91a" />
<img width="1646" height="820" alt="Screenshot 2026-07-27 232853" src="https://github.com/user-attachments/assets/626949c5-1b60-4eee-969e-8affc061a19b" />
<img width="1310" height="812" alt="Screenshot 2026-07-27 232836" src="https://github.com/user-attachments/assets/bfcdbc66-631b-4b75-b892-fb4c527ee6b3" />
<img width="1657" height="951" alt="Screenshot 2026-07-27 232809" src="https://github.com/user-attachments/assets/dc16d341-3596-4b96-af5d-052fef256ab6" />
<img width="1712" height="912" alt="Screenshot 2026-07-27 232738" src="https://github.com/user-attachments/assets/1955dc15-6303-4cdb-983a-c4f542bced97" />
<img width="1770" height="923" alt="Screenshot 2026-07-27 232714" src="https://github.com/user-attachments/assets/93466351-649c-4df1-9c0b-b7ecada17e2d" />
<img width="1671" height="925" alt="Screenshot 2026-07-27 232504" src="https://github.com/user-attachments/assets/544be1d0-1372-4a97-8f75-b03a24f5b73b" />
<img width="1027" height="923" alt="Screenshot 2026-07-27 232441" src="https://github.com/user-attachments/assets/286d4877-0e9d-4387-a5c9-dd2a5448b41e" />
<img width="1040" height="895" alt="Screenshot 2026-07-27 232423" src="https://github.com/user-attachments/assets/6101c1a7-c60b-4338-b897-f04d1e8b409c" />




## Author

**Jewel Gabriel**  
Electronics & Communication Engineering Graduate
