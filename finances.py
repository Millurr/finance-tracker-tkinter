import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class Finances(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # data values
        self.income_values = []
        self.expense_values = []

        self.title("Finance Tracker")
        self.geometry(f"{1280}x{720}")

        # configure grid layout
        self.grid_columnconfigure((1,1,1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.create_left_sidebar()

        self.create_middle_area()

        self.create_right_sidebar()

    def create_left_sidebar(self):

        # create sidebar frame with widgets
        self.left_sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, padx=20, pady=20, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Income Per Month", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.add_income_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.add_income, text="Add Income")
        self.add_income_button.grid(row=2, column=0, padx=20, pady=10)
        
        # create scrollable frame
        self.income_list = customtkinter.CTkScrollableFrame(self.left_sidebar_frame, label_text="Listed Incomes")
        self.income_list.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.income_list.grid_columnconfigure(0, weight=1)
        self.income_list_labels = []

    def create_middle_area(self):

        self.middle_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.middle_frame.grid(row=0, column=1, rowspan=4, padx=20, pady=20, sticky="nsew")
        self.middle_frame.grid_columnconfigure((1,1,1), weight=1)
        self.middle_frame.grid_rowconfigure((5,5,5), weight=1)

        self.total_income_label = customtkinter.CTkLabel(self.middle_frame, text="Total Income", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_income_label.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.total_income = customtkinter.CTkLabel(self.middle_frame, text=f"{self.get_total_income()}", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_income.grid(row=2, column=0, padx=20)

        self.net_income_label = customtkinter.CTkLabel(self.middle_frame, text="Net Income", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.net_income_label.grid(row=1, column=1, padx=20, pady=(20, 10))

        self.net_income = customtkinter.CTkLabel(self.middle_frame, text=f"{self.get_net_income()}", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.net_income.grid(row=2, column=1, padx=20)

        self.total_expenses_label = customtkinter.CTkLabel(self.middle_frame, text="Total Expenses", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_expenses_label.grid(row=1, column=2, padx=20, pady=(20, 10))

        self.total_expenses = customtkinter.CTkLabel(self.middle_frame, text=f"{self.get_total_expenses()}", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_expenses.grid(row=2, column=2, padx=20)

    def create_right_sidebar(self):

        # create sidebar frame with widgets
        self.right_sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=4, padx=20, pady=20, sticky="nsew")
        self.right_sidebar_frame.grid_rowconfigure(4, weight=1)

        self.expense_label = customtkinter.CTkLabel(self.right_sidebar_frame, text="Expenses Per Month", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.expense_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.add_expense_button = customtkinter.CTkButton(self.right_sidebar_frame, command=self.add_expense, text="Add Expense")
        self.add_expense_button.grid(row=2, column=0, padx=20, pady=10)

        self.expense_list = customtkinter.CTkScrollableFrame(self.right_sidebar_frame, label_text="Listed Expenses")
        self.expense_list.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.expense_list.grid_columnconfigure(0, weight=1)
        self.expense_list_labels = []

        
    def add_income(self):
        income = customtkinter.CTkInputDialog(text="Type in your income:", title="Income")
        try:
            income = int(income.get_input())
        except:
            return
        self.income_values.append(income)
        for idx, value in enumerate(self.income_values):
            label = customtkinter.CTkLabel(master=self.income_list, text=f"${value}", text_color='green')
            label.grid(row=idx, column=0, padx=10, pady=(0, 20))
            self.income_list_labels.append(label)
            print(f"Income added: ${value}")

        self.net_income.configure(text = f"${self.get_net_income()}")
        self.total_income.configure(text = f"${self.get_total_income()}", text_color='green')

    def add_expense(self):
        expense = customtkinter.CTkInputDialog(text="Type in your expense:", title="Expense")
        try:
            expense = int(expense.get_input())
        except:
            return
        self.expense_values.append(expense)
        for idx, value in enumerate(self.expense_values):
            label = customtkinter.CTkLabel(master=self.expense_list, text=f"${value}", text_color='red')
            label.grid(row=idx, column=0, padx=10, pady=(0, 20))
            self.expense_list_labels.append(label)
            print(f"Expense added: ${value}")

        self.net_income.configure(text = f"${self.get_net_income()}")
        self.total_expenses.configure(text = f"${self.get_total_expenses()}", text_color='red')

    def get_net_income(self):
        return sum(self.income_values) - sum(self.expense_values)
    
    def get_total_income(self):
        return sum(self.income_values)
    
    def get_total_expenses(self):
        return sum(self.expense_values)

if __name__ == '__main__':
    app = Finances()
    app.mainloop()