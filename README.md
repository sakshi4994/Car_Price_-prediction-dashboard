# Car_Price_-prediction-dashboard
This project is a machine learning-based web application that estimates the market value of a used car in Lakhs (INR). It provides a clean, user-friendly interface for buyers and sellers to understand pricing based on specific vehicle attributes. 

🌟 Features
Real-time Predictions: Instantly calculates the estimated price based on user input.

Intuitive UI: A modern dark-themed dashboard built for ease of use.

Multiple Input Factors: Takes into account crucial valuation metrics including:

Insurance Validity: (e.g., Comprehensive, Third-party)

Fuel Type: (Petrol, Diesel, CNG, etc.)

Transmission: (Manual vs. Automatic)

Kilometers Driven: Total usage history.

Ownership Status: (First Owner, Second Owner, etc.)

Seating Capacity: Impact of car size on price.

🛠️ Tech Stack
Frontend: Streamlit

Machine Learning: Scikit-learn (Random Forest/Linear Regression/KNN)

Data Processing: Pandas & NumPy

Deployment: Streamlit 

How to Run Locally:

Clone the repository:
Bash
git clone https://github.com/your-username/car-price-prediction.git

Install dependencies:
Bash
pip install -r requirements.txt

Run the application:
Bash
streamlit run app.py
