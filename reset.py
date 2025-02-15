#!/usr/bin/env python3
'''
Cursor Trial Reset Tool

This script resets the device IDs in Cursor's configuration file to generate a new random device ID.

Repository: https://github.com/MEAOWSdev/Cursor-Trial-Reset-Tool
Author: MEAOWS DEVELOPER (https://github.com/MEAOWSdev)
Created: 14/Feb/2025
'''

import json
import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path
import platform


def backup_file(file_path: str):
    """Create a timestamped backup of the given file."""
    if os.path.exists(file_path):
        backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(file_path, backup_path)


def get_storage_file():
    """Determine the storage file location based on the operating system."""
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv("APPDATA")) / "Cursor" / "User" / "globalStorage" / "storage.json"
    elif system == "Darwin":  # macOS
        return Path(os.path.expanduser("~")) / "Library" / "Application Support" / "Cursor" / "User" / "globalStorage" / "storage.json"
    elif system == "Linux":
        return Path(os.path.expanduser("~")) / ".config" / "Cursor" / "User" / "globalStorage" / "storage.json"
    else:
        raise OSError(f"Unsupported operating system: {system}")


def reset_cursor_id():
    storage_file = get_storage_file()
    storage_file.parent.mkdir(parents=True, exist_ok=True)
    backup_file(storage_file)

    if not storage_file.exists():
        data = {}
    else:
        with open(storage_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    machine_id = os.urandom(32).hex()
    mac_machine_id = os.urandom(32).hex()
    dev_device_id = str(uuid.uuid4())

    data["telemetry.machineId"] = machine_id
    data["telemetry.macMachineId"] = mac_machine_id
    data["telemetry.devDeviceId"] = dev_device_id

    with open(storage_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print("🔄 Device data has been successfully updated! Here are the new IDs: \n")
    print("----------------------------------------")
    print(f"Machine ID:     {machine_id}")
    print(f"Mac Machine ID: {mac_machine_id}")
    print(f"Device ID:      {dev_device_id}")
    print("----------------------------------------")
    print("\n🙏 Thank you for using the Cursor Trial Reset Tool! Developed with ❤️  by MEAOWS DEVELOPER.\n")


if __name__ == "__main__":
    reset_cursor_id()