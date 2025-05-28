# Titanic Data Analysis and Visualization

This project performs exploratory data analysis and visualization on the Titanic dataset using Python libraries like Pandas, NumPy, and Matplotlib.

## 📁 Dataset

The dataset used is the famous **Titanic dataset**, which contains data about passengers aboard the Titanic ship, including whether they survived or not.

- Input File: `../Data/titanic.csv`
- Output File: `../Data/cleaned_titanic_data.csv`

---

## 📊 Features Analyzed

- **Survival by Passenger Class**
- **Passenger Age Distribution**
- **Survival based on Fare and Age**
- **Survival by Sex**

Each feature is visualized using bar charts, histograms, and scatter plots.

---

## 🧼 Data Cleaning Steps

- Filled missing `Age` values with the **mean age**.
- Dropped the `Name` column as it was unnecessary for analysis.
- Converted `Sex` from categorical (`male`, `female`) to numerical (`0`, `1`).

---

## 📂 Output Visualizations

Saved in the `../Results/` directory:

- `Survival_Rates_by_Class.png`
- `Passengers_Age_Distribution.png`
- `Survival_by_Fare_and_Age.png`
- `Survival_Rates_by_Sex.png`

---

## 📌 Requirements

Make sure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib
```
---
## ▶️ How to Run

1. Place the Titanic dataset in the ../Data/ directory with the name titanic.csv.

2. Run the Python script:

```bash
cd scripts
```

```bash
python main.py
```

3. Visualizations and cleaned data will be saved in the appropriate directories.

---

## 📬 Author

### Dhanushka Rathnayaka

Portfolio Website :
https://dhanushkarathnayakaportfolio.vercel.app/

GitHub : https://github.com/Dhanuwa856

---

## 📄 License

Let me know if you want to add badges, more sections like "Future Work," or convert this into a `PDF`.
