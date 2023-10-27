# mi-scale-automation

**mi-scale-automation** is a Python script that automates the process of retrieving weight data from the Xiaomi Mi Scale 2 without the need to connect to Xiaomi's cloud services. This script is designed for users who want to use the scale with alternative apps, create custom applications, or log their weight privately to their own databases.

It is based on the work of the [Bluetooth repository](https://github.com/wiecosystem/Bluetooth/tree/master), and it allows you to quickly and easily obtain your weight data.

## Requirements

Before using this script, make sure you have the following:

- Python 3.10+ installed on your system.
- A Xiaomi Mi Scale 2.
- A Bluetooth adapter that supports Bluetooth Low Energy (BLE). This can be a built-in Bluetooth adapter or a USB dongle. Some Wi-Fi antennas also support BLE.
- A compatible operating system (Linux is recommended, but it may work on Windows and Mac as well).

## Installation

To set up **mi-scale-automation**, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary Python packages using Poetry:

```bash
poetry install
```

## Usage

Once you've installed the script, you can easily retrieve your weight data by following these steps:
  
1. Ensure your Xiaomi Mi Scale 2 has fresh batteries and is within the Bluetooth range of your computer.
2. Run the script by executing the following command in your terminal:

```bash
poetry run python3 scan.py
```
1. The script will run indefinitely and wait for you to step onto the scale.
2. When you are stable on the scale, the script will print your weight.
3. To stop the script, simply press `Ctrl+C`.

## Troubleshooting

If you encounter issues while trying to connect to the scale, consider the following troubleshooting steps:

- Ensure your Xiaomi Mi Scale 2 has fresh batteries.
- Verify that the scale is in close proximity to your computer.
- Check that your Bluetooth adapter supports BLE and is properly connected.
- Make sure your Bluetooth adapter is enabled and not blocked by rfkill.
- Feel free to reach out if you encounter any issues beyond these troubleshooting steps.

