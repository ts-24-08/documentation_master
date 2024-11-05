import os
from datetime import datetime
from mysql import connector

def create_connection():
        connection = connector.connect(
        host='10.0.10.27',
        user='meinbenutzer',
        password='geheimespasswort',
        database='meinedb'  
    )
        return connection

# CREATE funkiton 
def add_task(name, description, due, prio, state):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (name, description, due, prio, state)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, description, due, prio, state))
    conn.commit()
    conn.close()

# READ function
def show_tasks(order_by='prio'):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM tasks ORDER BY {order_by}')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# UPDATE funktion
def update_task(task_id, name=None, description=None, due=None, prio=None, state=None):
    conn = create_connection()
    cursor = conn.cursor()
    query = 'UPDATE tasks SET '
    params = []

    if name:
        query += 'name = ?, '
        params.append(name)
    if description:
        query += 'description = ?, '
        params.append(description)
    if due:
        query += 'due = ?, '
        params.append(due)
    if prio:
        query += 'prio = ?, '
        params.append(prio)
    if state:
        query += 'state = ?, '
        params.append(state)
    
    query = query.rstrip(', ') + ' WHERE id = ?'
    params.append(task_id)

    cursor.execute(query, params)
    conn.commit()
    conn.close()

# DELETE funktion
def delete_task(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Multifunktionale Methode zum senden einer SQL Query
def execute(query:str):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

# Main
def main():
    while True:
        print("\n---------- Aufgabenverwaltung ----------")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe aktualisieren")
        print("4. Aufgabe löschen")
        print("5. Programm beenden")

        choice = input("\nWähle eine Option zwischen 1 und 5: ")

        if choice == '1':
            name = input("Aufgabenbezeichnung: ")
            description = input("Beschreibung: ")
            due = input("Fälligkeitsdatum (TT.MM.JJJJ HH:MM): ")
            due_dt = datetime.strptime(due, "%d.%m.%Y %H:%M").strftime("%Y-%m-%d %H:%M")
            prio = int(input("Priorität (1=Hoch), (2=Mittel), (3=Niedrig): "))
            state = input("Status: ")
            add_task(name, description, due_dt, prio, state)
            print("Aufgabe hinzugefügt.")

        elif choice == '2':
            id = input(
                "Gib die ID ein oder drücke ENTER für alle Datensätze: ")
            tasks = show_tasks(id if id else None)
            print("Aufgaben:")
            for task in tasks:
                task_color = get_status_color(task[6], task[4])
                due_date = format_date(task[4])
                print(
                    f"{RESET}{task_color}ID: {task[0]}, Name: {task[1]}, Beschreibung: {task[2]}, Fällig: {due_date}, Priorität: {task[5]}, Status: {task[6]}{RESET}")
     
        elif choice == '3':
            task_id = int(input("Aufgaben-ID zum Aktualisieren: "))
            name = input("Neuer Aufgabenname (ENTER = beibehalten): ") or None
            description = input("Neue Beschreibung (ENTER = beibehalten): ") or None
            due = input("Neues Fälligkeitsdatum (TT.MM.JJJJ HH:MM) (ENTER = beibehalten): ") or None
            prio = input("Neue Priorität (leave blank to keep current): ") or None
            state = input("Neuer Status (Offen, In Bearbeitung, Abgeschlossen) (ENTER = beibehalten): ") or None

            update_task(task_id,
                        name,
                        description,
                        datetime.strptime(due, "%d.%m.%Y %H:%M").strftime("%Y-%m-%d %H:%M") if due else None,
                        int(prio) if prio else None,
                        state)
            print("Aufgabe aktualisiert.")

        elif choice == '4':
            task_id = int(input("Aufgaben-ID zum Löschen: "))
            delete_task(task_id)
            print("Aufgabe gelöscht.")

        elif choice == '5':
            print("Programm beendet.")
            break

        else:
            print("Ungültige Auswahl. Bitte wähle eine Option zwischen 1 und 5.")

if __name__ == "__main__":
    connection = create_connection()
    cursor = connection.cursor()
    main()
    cursor.close()
    connection.close()