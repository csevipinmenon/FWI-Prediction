

```markdown
# Algerian Forest Fires - Fire Weather Index (FWI) Prediction

This project is a **Flask web app** that predicts the **Fire Weather Index (FWI)** for Algerian forests using a trained **Ridge Regression model**.  
The app is deployed on **Render** and takes user input through a web form.

---

## Features

- Predicts FWI based on environmental factors:
  - Temperature, Relative Humidity, Wind Speed, Rain
  - FFMC, DMC, DC, ISI, BUI
  - Classes (0 = No Fire, 1 = Fire)
  - Region (0 = Bejaia, 1 = Sidi-Bel Abbes)
- Interactive UI for data input.
- Backend ML model trained with Scikit-learn.

---

## Tech Stack

- **Python** (Flask, Numpy, Pandas, Scikit-learn)
- **HTML, CSS, JavaScript**
- **Deployment:** Render

---

## Project Structure (Single File)

```

forest/
│
├── models/
│   ├── ridge.pkl          # Trained Ridge Regression model
│   └── scaler.pkl         # StandardScaler used for preprocessing
│
├── templates/
│   └── index.html , home.html         # Frontend HTML file
│
├── app.py         # Flask backend
├── requirements.txt       # Python dependencies
└── README.md


````

---

## Installation (Local)

1. Clone this repo:
   ```bash
   git clone <repository-url>
   cd forest
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run Flask app:

   ```bash
   python app.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---



6. Live  [https://fwi-prediction-c051.onrender.com/]

---

## Author

**Vipin Kumar**
📧 Email: [vipinmemon8123@gmail.com](mailto:vipinmemon8123@gmail.com)
💻 GitHub: [vipinmenon](https://github.com/csevipinmenon)

---

## License

Licensed under the MIT License.

```


