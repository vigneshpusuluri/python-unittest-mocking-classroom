import mysql.connector

class DbHelper:

    def __init__(self):
        self.myconnector = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "password7",
            database = "vigneshdg")
        self.mycursor = self.myconnector.cursor()
    
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table

        '''
        self.mycursor.execute('SELECT MAX(emp_no) FROM employees;')
        return self.mycursor.fetchone()[0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.mycursor.execute('SELECT MIN(emp_no) FROM employees;')
        return self.mycursor.fetchone()[0]

"""if __name__ == "__main__":
db_helper = DbHelper()
min_salary = db_helper.get_minimum_salary()
max_salary = db_helper.get_maximum_salary()
print(max_salary)
print(min_salary)"""