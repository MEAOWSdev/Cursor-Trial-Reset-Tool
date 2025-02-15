# Cursor Trial Reset Tool

This script resets the device IDs in Cursor's configuration file to generate a new random device ID.

## Repository

- **Repository:** [Cursor Trial Reset Tool](https://github.com/MEAOWSdev/Cursor-Trial-Reset-Tool)
- **Author:** [MEAOWS DEVELOPER](https://github.com/MEAOWSdev)

## Description

The **Cursor Trial Reset Tool** is a Python script that allows you to reset the device IDs in Cursor's configuration file. This is useful for generating a new random device ID, which may be necessary in certain situations, such as resetting Cursor's trial period.

## How It Works

The script does the following:

1. **File Backup:** Creates a timestamped backup of Cursor's configuration file.
2. **File Location:** Determines the location of the configuration file based on the operating system (Windows, macOS, Linux).
3. **ID Reset:** Generates new random device IDs and saves them to the configuration file.

## How to Use

1. Clone the repository or download the `reset.py` script.
2. Run the script with Python 3:

   ```bash
   python3 reset.py
   The script will reset the device IDs and display the newly generated IDs.

## Requirements

- Python 3.x
- File system access to read and write Cursor's configuration file.

## Usage Example

```bash
$ python3 reset.py
🔄 Device data has been successfully updated! Here are the new IDs:

----------------------------------------
Machine ID:     609ddb0b5550080173d798123062d40b45505d711b165bc6b870c090f4ec287a
Mac Machine ID: 8de0f4093b4fa4404d47873f555e76002ccfda9d636eb081e2b37201b027b855
Device ID:      5f8e72cc-ab62-453c-b06d-44c23ed64807
----------------------------------------

🙏 Thank you for using the Cursor Trial Reset Tool! Developed with ❤️ by MEAOWS DEVELOPER.
