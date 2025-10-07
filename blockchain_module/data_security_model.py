"""
SmartCare Health — Blockchain Data Security Model
-------------------------------------------------
This file outlines the prototype logic for secure storage
and verification of patient health data using blockchain.

The code is simplified and will evolve during testing in
local community clinics.

Author: SmartCare Health (Open Source Project)
License: MIT
"""

from hashlib import sha256
import json
from datetime import datetime

# Placeholder patient record (off-chain storage)
patient_record = {
    "patient_id": "12345",
    "name": "Anonymous",
    "dob": "2020-06-05",
    "diagnosis": "Routine check-up",
    "last_updated": str(datetime.utcnow())
}

def generate_record_hash(record: dict) -> str:
    """
    Generates a SHA-256 hash for a patient record.
    Only metadata and summary information are hashed,
    not full medical data (kept off-chain).
    """
    record_string = json.dumps(record, sort_keys=True)
    return sha256(record_string.encode()).hexdigest()

def verify_record_integrity(record: dict, stored_hash: str) -> bool:
    """
    Compares new hash with stored hash to detect tampering.
    """
    current_hash = generate_record_hash(record)
    return current_hash == stored_hash

# Example usage
if __name__ == "__main__":
    record_hash = generate_record_hash(patient_record)
    print(f"Generated record hash: {record_hash}")
    print("Verification:", verify_record_integrity(patient_record, record_hash))
