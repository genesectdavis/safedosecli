from storage import load_data, save_data

class MedicationManager:
    def __init__(self):
        self.medications = load_data()

    def add_medication(self, name, time):
        if not name or not time:
            raise ValueError("Dados inválidos")

        self.medications.append({
            "name": name,
            "time": time,
            "taken": False
        })
        save_data(self.medications)

    def list_medications(self):
        return self.medications

    def mark_taken(self, index):
        if index < 0 or index >= len(self.medications):
            raise IndexError("Índice inválido")

        self.medications[index]["taken"] = True
        save_data(self.medications)
