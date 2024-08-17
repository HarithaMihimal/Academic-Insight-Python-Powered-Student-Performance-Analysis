
# 🎓 Student Performance Analysis with Data Visualization

## **Overview**

This project focuses on analyzing student performance data sourced from Kaggle's **"Students Exam Scores: Extended Dataset"**. The goal was to preprocess the dataset, clean missing values, and visualize various aspects of the data to identify patterns and insights.

The dataset includes students' scores in three subjects—Math, Reading, and Writing—alongside socio-economic variables such as gender, parental education, marital status, and more. The dataset contains **over 30,000 rows** and **15 columns**, making it ideal for exploring relationships between different factors and student performance.

## **Dataset**

- **Source**: [Students Exam Scores: Extended Dataset on Kaggle](https://www.kaggle.com/datasets/desalegngeb/students-exam-scores)
- **Description**: Fictional data for educational purposes, including test scores and socio-economic information.

### **Features of the Dataset**
- **Gender**: Gender of the student (male/female)
- **EthnicGroup**: Ethnic group of the student (A to E)
- **ParentEduc**: Parent(s) education background
- **LunchType**: School lunch type (standard or free/reduced)
- **TestPrep**: Test preparation course status (completed or none)
- **ParentMaritalStatus**: Parent(s) marital status (married/single/widowed/divorced)
- **PracticeSport**: How often the student practices sport
- **IsFirstChild**: Whether the child is the first in the family
- **NrSiblings**: Number of siblings the student has
- **TransportMeans**: Means of transport to school
- **WklyStudyHours**: Weekly self-study hours
- **MathScore**: Math test score (0-100)
- **ReadingScore**: Reading test score (0-100)
- **WritingScore**: Writing test score (0-100)

## **Project Structure**

```plaintext
project_folder/
│
├── app.py          # Main Flask app
├── requirements.txt # List of dependencies
│
├── templates/      # HTML Templates
│   └── dashboard.html
│
└── static/         # Static assets (CSS, Images)
    ├── css/
    │   └── style.css
    └── images/
```

## **Tech Stack**

- **Python**: Primary programming language used for analysis and backend logic.
- **Pandas & NumPy**: For data manipulation and preprocessing.
- **Matplotlib & Seaborn**: To create meaningful and aesthetically pleasing visualizations.
- **Flask**: For building a web interface to display visualizations.
- **HTML & CSS**: To structure and style the user interface.

## **Data Analysis & Visualization**

### **1. Data Cleaning & Preprocessing**
- Removed unnecessary columns like `Unnamed: 0`.
- Dealt with missing values and inconsistencies in the dataset (e.g., cleaned up the `WklyStudyHours` column).

### **2. Visualization Techniques**
- **Bar Charts**: Gender distribution.
- **Heatmaps**: To compare student scores across different parent education levels and marital status.
- **Boxplots**: To display the distribution of Math, Reading, and Writing scores.
- **Pie Charts**: To show the distribution of ethnic groups.

## **Installation Instructions**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/student-performance-analysis.git
   ```

2. **Install Dependencies**

   Navigate to the project directory and run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   Start the Flask app by running:

   ```bash
   python app.py
   ```

4. **View the Dashboard**

   Visit `http://127.0.0.1:5000/` in your browser to access the dashboard.

## **Key Insights**

- **Gender Distribution**: Female students are slightly more represented in the dataset.
- **Parent Education & Scores**: Students with parents having higher education levels tend to score better in all subjects.
- **Ethnic Group Distribution**: Group C had the highest representation in the dataset, and this group showed a balanced performance across the subjects.

## **Future Improvements**

- **Interactive Visualizations**: Consider using Plotly for more interactive charts.
- **Machine Learning Models**: Build predictive models to forecast student scores based on socio-economic factors.
- **Deeper Analysis**: Explore correlations and statistical tests to validate the relationships observed in the dataset.

## **Contributing**

Feel free to fork the repository and submit pull requests for any improvements or new features.

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.
