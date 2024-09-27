import json
import os

class Habit:
    def _init_(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.reminder_done = False  # Track if the habit is completed

    def to_dict(self):
        return {
            'name': self.name,
            'frequency': self.frequency,
            'reminder_done': self.reminder_done
        }

class HabitManager:
    def _init_(self, filename='habits.json', deleted_filename='deleted_habits.json'):
        self.filename = filename
        self.deleted_filename = deleted_filename
        self.habits = self.load_habits()
        self.deleted_habits = self.load_deleted_habits()

    def load_habits(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
               return [Habit(**habit) for habit in json.load(file)]
        return []

    def load_deleted_habits(self):
        if os.path.exists(self.deleted_filename):
            with open(self.deleted_filename, 'r') as file:
                return [Habit(**habit) for habit in json.load(file)]
        return []

    def save_habits(self):
        with open(self.filename, 'w') as file:
            json.dump([habit.to_dict() for habit in self.habits], file)

    def save_deleted_habits(self):
        with open(self.deleted_filename, 'w') as file:
            json.dump([habit.to_dict() for habit in self.deleted_habits], file)

    def add_habit(self, name, frequency):
        new_habit = Habit(name, frequency)
        self.habits.append(new_habit)
        self.save_habits()
        print(f"Habit '{new_habit.name}' added successfully.")

    def view_habits(self):
        if not self.habits:
            print("No current habits found.")
        else:
            print("\nCurrent Habits:")
            for idx, habit in enumerate(self.habits):
                status = "✅ Done" if habit.reminder_done else "❌ Not Done"
                print(f"{idx + 1}: {habit.name} - {habit.frequency} - Status: {status}")

        if not self.deleted_habits:
            print("No deleted habits found.")
        else:
            print("\nDeleted Habits:")
            for idx, habit in enumerate(self.deleted_habits):
                print(f"{idx + 1}: {habit.name} - {habit.frequency}")

    def update_habit(self, index, name, frequency):
        if 0 <= index < len(self.habits):
            self.habits[index].name = name
            self.habits[index].frequency = frequency
            self.save_habits()
            print(f"Habit '{name}' updated successfully.")
        else:
            print("Habit not found.")

    def delete_habit(self, index):
        if 0 <= index < len(self.habits):
            deleted_habit = self.habits[index]
            self.deleted_habits.append(deleted_habit)
            del self.habits[index]
            self.save_habits()
            self.save_deleted_habits()
            print(f"Habit '{deleted_habit.name}' deleted successfully.")
        else:
            print("Habit not found.")

    def mark_habit_done(self, index):
        if 0 <= index < len(self.habits):
            self.habits[index].reminder_done = True
            self.save_habits()
            print(f"Habit '{self.habits[index].name}' marked as done.")
        else:
            print("Habit not found.")

def main():
    manager = HabitManager()

    while True:
        print("\n--- daily or weekly Habit logo---")
        print("1. create Habit")
        print("2. View Habits")
        print("3. Update Habit")
        print("4. Delete Habit")
        print("5. Mark Habit as Done")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter habit name: ")
            frequency = input("Enter habit frequency (daily/weekly): ")
            manager.add_habit(name, frequency)
        elif choice == '2':
            manager.view_habits()
        elif choice == '3':
            index = int(input("Enter habit number to update: ")) - 1
            name = input("Enter new habit name: ")
            frequency = input("Enter new habit frequency: ")
            manager.update_habit(index, name, frequency)
        elif choice == '4':
            index = int(input("Enter habit number to delete: ")) - 1
            manager.delete_habit(index)
        elif choice == '5':
            index = int(input("Enter habit number to mark as done: ")) - 1
            manager.mark_habit_done(index)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()s
