

![Streamlit notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/e8052bb6-ad89-48c3-b6e9-124f94c1cd01)




# Expense Tracker
This project is designed to help users track their expenses easily and effectively. It allows users to add, categorize, and visualize their expenses over time. With an intuitive interface built using Streamlit, users can quickly input their expenses and see summaries and visualizations of their spending patterns. This project is awesome and helps in managing personal finances efficiently.
## Team members
1. [Aksa Rose](https://github.com/AksaRose)
2. [Adithya Ramesh](https://github.com/Adithya6ramesh)
## Link to product walkthrough
![pic2](https://github.com/AksaRose/Expensetracker/assets/117498997/31ad9006-24b4-4f11-982e-a788ef0326b7)
![pic1](https://github.com/AksaRose/Expensetracker/assets/117498997/fb689505-867e-49fb-934a-4887d95c5598)

[Deployed link](https://expensesstracker.streamlit.app/)

## How it Works ?
The Expense Tracker application is built using Streamlit, a powerful and easy-to-use Python framework for building web applications. Here's a step-by-step explanation of how the project works:

1. **User Input**: Users can input their expense details, including description, amount, category, and date.
2. **Data Storage**: Expenses are temporarily stored in the session state during the user's session. For persistence, an SQLite database can be integrated.
3. **Visualization**: The app provides a summary of total expenses and displays expenses by category in a bar chart.
4. **Feedback**: Users receive immediate feedback upon adding an expense, and the app updates the visualization dynamically.

## Libraries used
- **Streamlit - Version 1.10.0**: For creating the web application.
- **Pandas - Version 1.4.2**: For data manipulation and analysis.
## How to configure
1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
## How to Run
1. **Run the Streamlit Application**:
    ```sh
    streamlit run expense_tracker.py
    ```
2. **Access the Application**:
    - Open your web browser and navigate to `http://localhost:8501`.
3. **Use the Application**:
    - Input your expenses and visualize the data.
