from medication import MedicationManager

def main():
    manager = MedicationManager()

    while True:
        print("\n=== SafeDose CLI ===")
        print("1. Adicionar medicamento")
        print("2. Listar medicamentos")
        print("3. Marcar como tomado")
        print("4. Sair")

        choice = input("Escolha: ")

        if choice == "1":
            name = input("Nome do medicamento: ")
            time = input("Horário (HH:MM): ")
            manager.add_medication(name, time)

        elif choice == "2":
            meds = manager.list_medications()
            for i, med in enumerate(meds):
                status = "✔" if med["taken"] else "✘"
                print(f"{i} - {med['name']} ({med['time']}) [{status}]")

        elif choice == "3":
            index = int(input("Índice: "))
            manager.mark_taken(index)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
