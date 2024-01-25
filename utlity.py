import pandas as pd

# Path to your Excel file containing questions
QUESTIONS_FILE = 'questions.xlsx'

def read_questions_from_excel():
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(QUESTIONS_FILE)
        return df
    except FileNotFoundError:
        # Handle file not found error
        print(f"File '{QUESTIONS_FILE}' not found.")
        return None

def add_new_question_to_excel(question_data):
    try:
        # Read the existing questions from Excel
        df = read_questions_from_excel() or pd.DataFrame(columns=['question', 'subject', 'correct', 'use', 'responseA', 'responseB', 'responseC', 'responseD', 'remark'])

        # Append the new question to the DataFrame
        new_row = pd.Series(question_data)
        df = df.append(new_row, ignore_index=True)

        # Write the updated DataFrame back to the Excel file
        df.to_excel(QUESTIONS_FILE, index=False)
        print("New question added to the Excel file.")
        return True
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An error occurred while adding the question: {e}")
        return False
