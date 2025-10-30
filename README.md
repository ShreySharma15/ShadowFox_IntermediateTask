🚗 CarValueAI: Intelligent Car Price Prediction Web App

CarValueAI is an interactive machine learning web application that predicts the selling price of used cars based on real-world attributes like current price, kilometers driven, fuel type, seller type, transmission, ownership history, and car age.
Built with Streamlit and powered by a Random Forest Regressor, it delivers fast, accurate, and easy-to-understand predictions.


🎯 Try it live:  https://car-value-ai.streamlit.app/


🚀 Features

✅ Real-time car price prediction using a trained Random Forest ML model
✅ Clean and responsive UI built with Streamlit
✅ Handles multiple car attributes and encodings (fuel type, seller type, transmission)
✅ Instant predictions with clear and user-friendly output
✅ Lightweight & portable — runs locally or on Streamlit Cloud

🛠️ Getting Started (Local Setup)
Prerequisites

Python 3.7+

pip package manager

Installation Steps

Clone the Repository

git clone https://github.com/yourusername/CarValueAI.git
cd CarValueAI


Install Dependencies

pip install -r requirements.txt


Run the App

streamlit run app.py


Open your browser and go to 👉 http://localhost:8501

📁 Project Structure
CarValueAI/
│
├── app.py                  # Main Streamlit app script
├── car_price_model.pkl     # Trained Random Forest model
├── le_fuel_type.pkl        # Label encoder for Fuel Type
├── le_seller_type.pkl      # Label encoder for Seller Type
├── le_transmission.pkl     # Label encoder for Transmission
├── requirements.txt        # List of dependencies
└── car.csv                 # Dataset (optional)

☁️ Deployment

You can easily deploy CarValueAI on Streamlit Cloud, Render, or Heroku.

Deploy on Streamlit Cloud

Push your project to GitHub

Go to Streamlit Cloud

Create a new app and link your repository

Set app.py as the main file
✅ Streamlit Cloud automatically handles setup, build, and hosting!

📦 Dependencies

streamlit

scikit-learn

pandas

numpy

(See requirements.txt for full details)

🤝 Contributing

Contributions, suggestions, and feedback are always welcome!

Open an issue for ideas or bugs 🐛

Submit a pull request for improvements 🚀

🧾 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute it with attribution.

💡 Inspiration

CarValueAI was built to demonstrate how machine learning and simple web interfaces can empower everyday users with data-driven insights — in this case, estimating real-world car prices quickly and reliably.
