# Data Analysis: Gender Disparities Accross Graduate Fields
This repository provides a data analysis pipeline to examine gender representation across various fields of study using a graduate dataset. It identifies the top 5 fields with the largest gender disparities and visualizes these findings through charts. Additionally, it explores potential factors contributing to these disparities and suggests strategies for bridging the gaps.

## Features
1. Data Loading and Preparation: Reads a graduate dataset from an Excel file and processes the data for analysis.
2. Gender Distribution Analysis: Calculates the percentage representation of males and females in each field of study.
3. Gender Disparity Identification:
- Identifies fields with the largest gender disparities.
- Saves the top 5 fields to an Excel file.
4. Visualizations:
- Bar chart for top 5 fields with the largest gender disparities.
- Line chart showing gender disparities across all fields.
- Pie charts illustrating gender distribution in each field.
5. Key Performance Indicators (KPIs):
- Highlights the top 5 fields with the largest gender disparities.
- Examines factors contributing to these disparities.
- Proposes actionable strategies to address the imbalances.

## Directory Structure

Data Analysis Local Repository/
├── Graduate_Dataset.xlsx  # Input dataset

├── Charts/
└── Top_5_Gender_Disparities_BarChart.png  # Bar chart visualization

├── Line chart/
│   └── Gender_Disparities_LineChart.png  # Line chart visualization

├── Pie_Charts/
│   └── [Field Name]_Gender_Distribution.png  # Pie chart for each field

├── Top_5_Disparities.xlsx  # Excel file with top 5 disparities

## Code Overview
Main Functions

- Analyze_gender_distribution(dataframe):
Calculates gender distribution percentages for each field.

- Calculate_disparity(dataframe):
Computes the absolute gender disparity (|Female - Male|) for each field.

- Save_top_5_disparities(disparity_df):
Extracts and saves the top 5 fields with the largest gender disparities to an Excel file.

- Plot_bar_chart(top_5):
Generates a bar chart visualizing gender representation in the top 5 fields.

- Plot_line_chart(disparity_df):
Creates a line chart of gender disparities across all fields.

- Plot_pie_charts(gender_counts):
Produces individual pie charts showing the gender distribution for each field.

## Key Performance Indicators (KPIs)
1. Top 5 Fields with the Largest Gender Disparities

The analysis identifies the fields with the largest differences between male and female representation. These fields are visualized in:

- Bar Chart: Charts/Top_5_Gender_Disparities_BarChart.png

- Excel File: Top_5_Disparities.xlsx

2. Significant Contributing Factors

- Societal Norms: Traditional roles and stereotypes influencing career choices.

- Educational Opportunities: Accessibility to resources and mentorship in underrepresented fields.

- Cultural Biases: Institutional biases affecting enrollment and career encouragement.

3. Potential Strategies for Bridging Disparities

- Promote STEM Outreach: Encourage underrepresented genders in STEM fields through scholarships and mentorship programs.

- Policy Changes: Implement gender quotas or incentives for educational institutions.

- Awareness Campaigns: Challenge stereotypes through community and media efforts.

- Supportive Environments: Create inclusive environments that empower individuals to pursue non-traditional fields.

## How to Run the Analysis
1. Install Dependencies:Ensure you have Python installed with the required libraries:
pip install pandas matplotlib openpyxl

2. Prepare the Dataset:Place your dataset (Graduate_Dataset.xlsx) in the Data Analysis Local Repository directory.

3. Ensure the dataset contains the following columns:

- Field of Study

- Gender

- Count (number of graduates)

4. Run the Script Execute the script in your Python environment:
python gender_analysis.py

5. View Results
Charts are saved in the respective directories under Data Analysis Local Repository/.

The top 5 disparities are saved in Top_5_Disparities.xlsx.

## Sample Outputs
1. Bar Chart
Top 5 fields with the largest gender disparities:
![image](https://github.com/user-attachments/assets/46622eff-a93c-4126-8454-8cf04b9f4f18)


2. Line Chart
Gender disparities across all fields:
![image](https://github.com/user-attachments/assets/dd11cda3-4c31-4b04-99a9-e272a401d49d)


3. Pie Charts
Gender distribution in individual fields, e.g.:
![image](https://github.com/user-attachments/assets/d2274218-d041-4641-8ed1-b3608ba78593)


## Contributions
Contributions are welcome! If you’d like to enhance this project, submit a pull request or create an issue.

# Additional on Dashboard
- Excel Workbook

- DataSet

- Python Code

- MySql Query







