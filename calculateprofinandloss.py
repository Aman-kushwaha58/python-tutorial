def calculate_profit_or_loss(income, expenses):
    result = income - expenses
    return "Profit: " + str(result) if result > 0 else "Loss: " + str(abs(result)) if result < 0 else "No Profit No Loss"

def main():
    income = float(input("Enter total income: "))
    expenses = float(input("Enter total expenses: "))
    print(calculate_profit_or_loss(income, expenses))

if __name__ == "__main__":
    main()
