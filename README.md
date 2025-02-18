# Anti-BadUSB 🛡️💻

### A Python3-based tool to detect and block BadUSB attacks by monitoring keyboard inputs.

---

## 🚨 Overview

BadUSB attacks exploit the USB protocol to emulate malicious devices, often using USB peripherals like keyboards to inject harmful commands. **Anti-BadUSB** is here to help protect you! It detects suspicious keyboard activity and blocks the keyboard temporarily, preventing any further malicious input.

It monitors real-time keyboard events to identify rapid, repeated keystrokes — a common indicator of a BadUSB attack. Once detected, it automatically blocks the keyboard and sends a **real-time notification** to alert you.

---

## ✨ Features

- **Suspicious Activity Detection**: 🕵️‍♂️ Detects rapid or consecutive key presses which are often used in BadUSB attacks.
- **Keyboard Blocking**: ⛔ Automatically blocks keyboard input when an attack is detected.
- **Real-time Notifications**: 📲 Sends desktop notifications when an attack is detected and when the keyboard is unblocked.
- **Configurable Settings**: ⚙️ Customize the number of key presses needed to trigger the blocking mechanism.
- **Cross-Platform**: 💻 Compatible with Windows, macOS, and Linux using `pynput` and `plyer`.

---

## 📦 Requirements

To run **Anti-BadUSB**, you'll need to install the following dependencies:

- `pynput`: For monitoring keyboard and mouse input.
- `keyboard`: For interacting with the keyboard.
- `plyer`: For sending desktop notifications.

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/1Developpeur/Anti-BadUSB.git
cd Anti-BadUSB
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the script:
```bash
python3 main.py
```
```bash
python main.py
```

---

## ⚙️ Configuration

You can adjust the detector’s behavior with the following parameters:

* **max_trigger** : The number of rapid key presses that will trigger the keyboard block. Default is `10`.
* **log** : Enable logging of events by setting this to `True`.

Example configuration:

```py
detector = BadUSBDetector(max_trigger=10, log=True)
```

---

## 💡 How It Works

1. **Key Event Monitoring**: The tool listens to key releases using `pynput` to detect patterns.

2. **Suspicious Activity Detection**: If multiple key releases occur within 30ms, it's considered suspicious.

3. **Blocking**: If the `max_trigger` threshold is exceeded, the tool blocks keyboard input.

4. **Unblocking**: The keyboard is unblocked after 5 seconds, and a notification is sent to the user.

---

## 🖥️ Example Output

When the detector is running, you'll see logs like this:
```pgsql
2025-02-18 04:27:19 | [INFO] BadUSB Detector started !
2025-02-18 04:27:20 | [WARNING] BadUSB Detected, blocking keyboard !
2025-02-18 04:27:20 | [INFO] New notification: BadUSB Detected - Keyboard input blocked !
2025-02-18 04:27:25 | [INFO] Keyboard unblocked !
2025-02-18 04:27:25 | [INFO] New notification: BadUSB - Keyboard unblocked.
```

---

## 📹 Preview Video
Check out this video below to see the **Anti-BadUSB** tool in action!

![poc-gif](https://github.com/user-attachments/assets/77097e04-1bf9-47e2-bd8e-16ce83ad5971)

## ⚠️ Notes

* **Permissions**: On some operating systems, elevated permissions may be required to monitor keyboard inputs. Be sure to run the script with the necessary privileges.

* **Keyboard Layout**: The `key_callback` function is currently inactive due to varying keyboard layouts. You can extend this function to analyze key events for specific needs.

* **Custom Notifications**: Notifications are powered by the `plyer` library, so make sure the appropriate notification backend is installed for your platform.

---

## 🙌 Contributing
Contributions are always welcome! Fork the repo, submit issues, or open pull requests.

---

## 📜 License
This project is licensed under the **MIT License**.
