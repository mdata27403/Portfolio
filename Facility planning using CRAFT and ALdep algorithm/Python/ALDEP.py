import pandas as pd

table = pd.read_excel('C:/test code python/test code.xlsx', sheet_name='Sheet1', index_col=0)

table = table.astype(object)

for row in table.index:
    for col in table.columns:
        if pd.notna(table.loc[row, col]):
            if int(table.loc[row, col]) > 500:
                table.loc[row, col] = 'A'
            elif int(table.loc[row, col]) > 300:
                table.loc[row, col] = 'E'
            elif int(table.loc[row, col]) > 200:
                table.loc[row, col] = 'I'
            elif int(table.loc[row, col]) > 100:
                table.loc[row, col] = 'O'
            else:
                table.loc[row, col] = 'U'
print(table)
table.to_excel(excel_writer = "Test AEIOU 1.xlsx")
import random
import pandas as pd

table = pd.read_excel('C:/test code python/Test AEIOU 1.xlsx', sheet_name='Sheet1', index_col=0)

class DepartmentPlacement:
    def __init__(self, table):
        self.table = table
        self.departments = list(table)
        self.remaining_departments = self.departments.copy()
        self.placed_departments = []

    def select_department(self):
        if self.remaining_departments: 
            if not self.placed_departments:
                selected_department = random.choice(self.remaining_departments)
            else:
                last_placed_department = self.placed_departments[-1]
                related_departments_A = [dep for dep in self.remaining_departments if self.table.loc[last_placed_department, dep] == 'A']
                related_departments_E = [dep for dep in self.remaining_departments if self.table.loc[last_placed_department, dep] == 'E']
                related_departments_I = [dep for dep in self.remaining_departments if self.table.loc[last_placed_department, dep] == 'I']

                if related_departments_A:
                       selected_department = random.choice(related_departments_A)
                elif related_departments_E:
                       selected_department = random.choice(related_departments_E)
                elif related_departments_I:
                       selected_department = random.choice(related_departments_I)
                else:
                    selected_department = random.choice(self.remaining_departments)
            self.placed_departments.append(selected_department)
            self.remaining_departments.remove(selected_department)
            return selected_department

    def place_all_departments(self):
        for _ in range(1000):
            self.select_department()
            if len(self.placed_departments) == len(self.departments):
                break

department_placement = DepartmentPlacement(table )
department_placement.place_all_departments()

print("Placed departments:", department_placement.placed_departments)