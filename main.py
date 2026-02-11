import database as db
import analytics as anc
import visualization as vs
import sys
from time import sleep
import os
from datetime import datetime


def validate_date(date_string):
    """Validate date format YYYY-MM-DD."""
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_positive_integer(value, min_val=0, max_val=None):
    """Validate integer input is positive and within range."""
    try:
        num = int(value)
        if num < min_val:
            return False, f"Value must be >= {min_val}"
        if max_val is not None and num > max_val:
            return False, f"Value must be <= {max_val}"
        return True, num
    except ValueError:
        return False, "Please enter a valid number"


def validate_float(value, min_val=0, max_val=24):
    """Validate float input is positive and within range."""
    try:
        num = float(value)
        if num < min_val or num > max_val:
            return False, f"Value must be between {min_val} and {max_val}"
        return True, num
    except ValueError:
        return False, "Please enter a valid number"


def main():
    connection = None
    delete_tb = False
    try:
        connection = db.connect_to_db()
        db.create_table(connection)
        print('Database is ready.')
        delete_tb = run_app(connection)
    except Exception as e:
        print("Error: ", e)
    finally:
        if connection:
            connection.close()
        if delete_tb and os.path.exists("productivity.db"):
            os.remove("productivity.db")

 
def run_app(connection):
    while True:
            print("\n" + "═"*45)
            print("        🚀 PERSONAL PRODUCTIVITY MANAGER")
            print("═"*45)
            print("  1  ➜  Add New Entry")
            print("  2  ➜  View All Entries")
            print("  3  ➜  Update Existing Entry")
            print("  4  ➜  Delete Entry")
            print("  5  ➜  View Statistics")
            print("  6  ➜  Delete DataBase")
            print("  0  ➜  Exit Application")
            print("═"*45)
            choice = input("Select an option: ")
            print('')

            if choice == "1":
                while True:
                    date = input("Please Enter Date (YYYY-MM-DD): ")
                    if validate_date(date):
                        break
                    print("❌ Invalid date format. Please use YYYY-MM-DD")

                while True:
                    valid, result = validate_float(input("Enter Your Study Hours (0-24): "), 0, 24)
                    if valid:
                        study_hours = result
                        break
                    print(f"❌ {result}")

                while True:
                    valid, result = validate_float(input("Enter Your Sport Hours (0-24): "), 0, 24)
                    if valid:
                        sport_hours = result
                        break
                    print(f"❌ {result}")
                
                while True:
                    valid, result = validate_positive_integer(input("Enter Your Mood (1-10): "), 1, 10)
                    if valid:
                        mood = result
                        break
                    print(f"❌ {result}")
                
                note = input("Enter Short Note (optional): ")
                try:
                    db.add_entry(connection, date, study_hours, sport_hours, mood, note)
                    print("✅ Information added successfully.")  
                    sleep(2)
                    os.system('cls')              
                except Exception as e:
                    print(f"❌ Error: {e}")
                    sleep(2)


            elif choice == "2":
                rows = db.get_all_entries(connection)
                if rows:
                    for row in rows:
                        print(f"""ID: {row['id']}\nDate: {row['date']}\nStudy hours: {row['study_hours']}\nSport hours: {row['sport_hours']}\nMood: {row["mood"]}\nNote: {row["note"]}\n\n""")
                else:
                    print("📭 No data to display.")
                input("\nPress Enter to continue...")
                os.system('cls')


            elif choice == "3":

                while True:
                    try:
                        entry_id = int(input("Update Existing Entry ID: "))
                        break
                    except ValueError:
                        print("❌ Please enter a valid ID number")

                while True:
                    date = input("Please Enter Date (YYYY-MM-DD): ")
                    if validate_date(date):
                        break
                    print("❌ Invalid date format. Please use YYYY-MM-DD")
                
                while True:
                    valid, result = validate_float(input("Enter Your Study Hours (0-24): "), 0, 24)
                    if valid:
                        study_hours = result
                        break
                    print(f"❌ {result}")
                
                while True:
                    valid, result = validate_float(input("Enter Your Sport Hours (0-24): "), 0, 24)
                    if valid:
                        sport_hours = result
                        break
                    print(f"❌ {result}")
                
                while True:
                    valid, result = validate_positive_integer(input("Enter Your Mood (1-10): "), 1, 10)
                    if valid:
                        mood = result
                        break
                    print(f"❌ {result}")
                
                note = input("Enter Short Note (optional): ")
                try:
                    rows = db.update_entry(connection, entry_id, date, study_hours, sport_hours, mood, note)
                    if rows == 0:
                        print("❌ Entry ID not found.")
                    else:
                        print("✅ Information updated successfully.")
                except Exception as e:
                    print(f"❌ Error: {e}")
                sleep(1)
                os.system('cls')


            elif choice == "4":
                while True:
                    try:
                        entry_id = int(input("Delete Entry ID: "))
                        break
                    except ValueError:
                        print("❌ Please enter a valid ID number")
                
                confirm = input("Are you sure? (y/n): ").lower()
                if confirm in ['y', 'yes']:
                    try:
                        rows = db.delete_entry(connection, entry_id)
                        if rows == 0:
                            print("❌ Entry ID not found.")
                        else:
                            print("✅ Entry deleted successfully.")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                else:
                    print("Cancelled.")
                sleep(1) 
                os.system('cls')            



            elif choice == "5":
                rows = db.get_all_entries(connection)
                if not rows:
                    print("📭 No data available for statistics.")
                    input("\nPress Enter to continue...")
                    os.system('cls')
                    continue
                
                try:
                    total = anc.total_study_time(rows)
                    print(f'\n📊 STATISTICS')
                    print(f'══════════════════════════════════════════')
                    print(f'Total study time: {total} hours')

                    avg = anc.average_study_hours(rows)
                    print(f'Average study hours: {round(avg, 2)} hours')

                    best = anc.best_study_day(rows)
                    if best:
                        date, hours = best
                        print(f'Best study day {date}: {hours} hours')
                    else: 
                        print("No data available")
                    
                    avg_m = anc.average_mood(rows)
                    print(f'Average mood: {round(avg_m, 2)}/10')

                    correlation = anc.correlation(rows)
                    if correlation > 0.7:
                        interpretation = "Strong positive correlation"
                    elif 0.3 < correlation <= 0.7:
                        interpretation = "Moderate positive correlation"
                    elif -0.3 <= correlation <= 0.3:
                        interpretation = "No significant correlation"
                    elif -0.7 <= correlation < -0.3:
                        interpretation = "Moderate negative correlation"
                    elif correlation < -0.7:
                        interpretation = "Strong negative correlation"
                    print(f"Correlation (Study↔Mood): {round(correlation, 3)} - {interpretation}")
                    print(f'══════════════════════════════════════════')

                    visualization = input('\nSee Study Hours vs Mood visualization? (y/n): ').lower()
                    if visualization in ['y', 'yes']:
                        if not rows:
                            print("No data to visualize.")
                        else:
                            vs.plot_study_vs_mood(rows)
                except Exception as e:
                    print(f"Error calculating statistics: {e}")
                
                input("\nPress Enter to continue...")
                os.system('cls')


            elif choice == "6":
                confirm = input("⚠️  Are you sure you want to delete the database? (y/n): ").lower()
                if confirm in ['y', 'yes']:
                    return True
                else:
                    print("Cancelled.")
                    sleep(1)
                    os.system('cls')
            
            elif choice == "0":
                print("\nThank you for using Personal Productivity Manager!👋")
                return False
            
            else:
                print("Invalid option. Please select 0-6.")
                sleep(1)
                os.system('cls')
                

if __name__ == "__main__":
    main()
    
