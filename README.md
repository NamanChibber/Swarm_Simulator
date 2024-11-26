# **ATCommWrapper Library**

The `ATCommWrapper` library facilitates communication between nodes using AT commands. It supports message parsing, serialization, multi-threaded communication, and logging for debugging.

---

## **Table of Contents**
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Message Types](#message-types)
5. [How To Use](#how-to-use)

---

## **Installation**
Clone the repository:
   ```bash
   git clone https://github.com/BhavyaMehta2/ATCommWrapper.git
   ```
## **Usage**
1. Create `Agent` instances for nodes.
2. Use the `Modem` class for socket communication.
3. Parse messages with the `parser` function.
4. Leverage logging for debugging.

## **Features**
* Message Parsing: Parse AT command responses.
* Serialization: Convert messages to/from JSON format.
* Multi-threading: Handle multiple nodes concurrently.
* Debug Logging: Log communication for debugging.

## **Message Types**
* OK: Success response.
* BUSY: Indicates a busy state.
* ERROR: Error response.
* RECVIM: Instant message with various parameters (length, source, destination, etc.).
* RECVIMS: Scheduled instant message.
* RECVPBM: Phone book message.
* DELIVEREDIM: Delivery acknowledgment.
* *TODO: ADD SUPPORT FOR MORE MESSAGE TYPES*
* *TODO: ADD SUPPORT FOR SERIAL COMMUNICATION WITH MODEM*

## **How To Use**
1. Connect to the DMACE emulator or the acoustic modem over WiFi or LAN (Follow instructions in emulator documentation).
2. Create a Network Agent similar to the template given in `simulation.py`.
3. Add logic for all the different nodes.
4. Run it as you would a normal python script. (≥Python 3.8)

Note: For additional information about the functions and their details, refer to the manual that came along with the emulator/modem.
