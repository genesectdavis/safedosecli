import pytest
import pytest
import sys
import os

sys.path.append(os.path.abspath("src"))

from medication import MedicationManager

def test_add_medication():
    manager = MedicationManager()
    manager.medications = []

    manager.add_medication("Dipirona", "08:00")

    assert len(manager.medications) == 1
    assert manager.medications[0]["name"] == "Dipirona"

def test_invalid_medication():
    manager = MedicationManager()
    manager.medications = []

    with pytest.raises(ValueError):
        manager.add_medication("", "")

def test_mark_taken_invalid_index():
    manager = MedicationManager()
    manager.medications = []

    with pytest.raises(IndexError):
        manager.mark_taken(0)
