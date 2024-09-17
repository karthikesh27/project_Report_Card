import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(host='localhost', user = 'root', password = 'Karthi@2706', database = 'karthikesh')
cursor = conn.cursor()

def get_student_report(roll_number):
    try:
        query = "SELECT * FROM Reportcard WHERE Roll_number = %s"
        cursor.execute(query, (roll_number,))
        result = cursor.fetchone()
        if result:
            subjects = [result[1], result[2], result[3], result[4], result[5]]
            average = sum(subjects) / len(subjects)
            headers = ["Roll Number", " Name "," Maths "," Physics "," Chemistry "," Computer ","English ","  Total  ","Average"]
            data = [[result[7], result[0], result[1], result[2], result[3], result[4], result[5], result[6],round(average, 2)]]
            print(tabulate(data, headers=headers, tablefmt="double_grid"))
            if round(average, 2)>=90:
                print("EXCELLENT!!!,YOU ARE ROCKING")
            elif 80<=round(average, 2)<90:
                print("GOOD!,YOU CAN WORK HARD THAN THIS")
            elif 70<=round(average, 2)<80:
                print("BETTER,YOU HAVE TO WORK HARD")
            else:
                print("NEED HARDWORK,DON'T LOOSE YOUR HOPE")
        else:
            print("No Student Report found with the entered roll number.")

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")

roll_number = int(input("Enter roll number: "))
get_student_report(roll_number)
conn.close();


        
