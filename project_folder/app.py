from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('../Expanded_data_with_more_features.csv')

# Remove unnecessary columns
df = df.drop(columns=['Unnamed: 0'], axis=1)

@app.route('/')
def dashboard():
    # Gender Distribution Plot
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(data=df, x='Gender')
    ax.bar_label(ax.containers[0])
    plt.title('Gender Distribution')
    plt.savefig('static/images/gender_distribution.png')
    plt.close()

    # Parent Education vs Student Score Heatmap
    gp = df.groupby('ParentEduc').agg({"MathScore": "mean", "ReadingScore": "mean", "WritingScore": "mean"})
    plt.figure(figsize=(8, 6))
    sns.heatmap(gp, annot=True, cmap='coolwarm')
    plt.title('Parent Education vs Student Score')
    plt.savefig('static/images/score_comparison.png')
    plt.close()

    # Ethnic Group Distribution Pie Chart
    group_counts = df['EthnicGroup'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(group_counts, labels=group_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Ethnic Group Distribution')
    plt.savefig('static/images/ethnic_distribution.png')
    plt.close()

    # Boxplot for Math Scores
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='MathScore')
    plt.title('Math Scores')
    plt.savefig('static/images/math_score_boxplot.png')
    plt.close()

    # Boxplot for Reading Scores
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='ReadingScore')
    plt.title('Reading Scores')
    plt.savefig('static/images/reading_score_boxplot.png')
    plt.close()

    # Boxplot for Writing Scores
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='WritingScore')
    plt.title('Writing Scores')
    plt.savefig('static/images/writing_score_boxplot.png')
    plt.close()

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
