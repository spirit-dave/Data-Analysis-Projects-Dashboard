import pandas as pd
import matplotlib.pyplot as plt
import os

# File paths
file_path = '/storage/emulated/0/Data Analysis Local Repository/Graduate_Dataset.xlsx'
bar_chart_path = '/storage/emulated/0/Data Analysis Local Repository/Charts/Top_5_Gender_Disparities_BarChart.png'
line_chart_dir = '/storage/emulated/0/Data Analysis Local Repository/Line chart/'
pie_chart_dir = '/storage/emulated/0/Data Analysis Local Repository/Pie_Charts/'
excel_output_path = '/storage/emulated/0/Data Analysis Local Repository/Top_5_Disparities.xlsx'

# Ensure output directories exist
os.makedirs(os.path.dirname(bar_chart_path), exist_ok=True)
os.makedirs(line_chart_dir, exist_ok=True)
os.makedirs(pie_chart_dir, exist_ok=True)

# Load the dataset
df = pd.read_excel(file_path)

# Analyze Gender Representation
def analyze_gender_distribution(dataframe):
    gender_counts = dataframe.groupby(['Field of Study', 'Gender']).size().unstack(fill_value=0)
    gender_counts['Total'] = gender_counts.sum(axis=1)
    gender_counts['Female_Percentage'] = (gender_counts['Female'] / gender_counts['Total']) * 100
    gender_counts['Male_Percentage'] = (gender_counts['Male'] / gender_counts['Total']) * 100
    return gender_counts

# Gender disparity calculation
def calculate_disparity(dataframe):
    gender_distribution = dataframe.groupby(['Field of Study', 'Gender']).size().unstack(fill_value=0)
    gender_distribution['Disparity'] = abs(gender_distribution['Female'] - gender_distribution['Male'])
    return gender_distribution

# Save Top 5 Disparities to Excel
def save_top_5_disparities(disparity_df):
    top_5_disparities = disparity_df.sort_values('Disparity', ascending=False).head(5)
    top_5_disparities.to_excel(excel_output_path, sheet_name='Disparity Analysis')
    return top_5_disparities

# Plot and save bar chart
def plot_bar_chart(top_5):
    ax = top_5[['Female', 'Male']].plot(kind='bar', figsize=(10, 6))
    plt.title('Top 5 Fields with Largest Gender Disparities')
    plt.xlabel('Field of Study')
    plt.ylabel('Number of Graduates')
    plt.xticks(rotation=45)
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.savefig(bar_chart_path)
    plt.close()

# Plot and save line chart
def plot_line_chart(disparity_df):
    disparity_df = disparity_df.reset_index()
    disparity_df['Disparity'].sort_values(ascending=False).plot(
        kind='line', figsize=(10, 6), marker='o', color='b')
    plt.title('Gender Disparities Across Fields of Study')
    plt.xlabel('Field of Study')
    plt.ylabel('Disparity (|Female - Male|)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{line_chart_dir}Gender_Disparities_LineChart.png")
    plt.close()

# Generate and save pie charts
def plot_pie_charts(gender_counts):
    for field, row in gender_counts.iterrows():
        data = [row['Female_Percentage'], row['Male_Percentage']]
        labels = ['Female', 'Male']
        colors = ['pink', 'blue']
        
        plt.figure(figsize=(6, 6))
        plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        plt.title(f"Gender Distribution in {field}")
        plt.savefig(f"{pie_chart_dir}{field}_Gender_Distribution.png")
        plt.close()

# Main Execution
if __name__ == "__main__":
    # Analyze gender distribution
    gender_counts = analyze_gender_distribution(df)
    print("Gender Distribution:")
    print(gender_counts[['Female_Percentage', 'Male_Percentage']])

    # Calculate gender disparities
    gender_disparity = calculate_disparity(df)
    print("\nTop 5 Fields with Largest Disparities:")
    top_5_disparities = save_top_5_disparities(gender_disparity)
    print(top_5_disparities)

    # Generate and save visualizations
    plot_bar_chart(top_5_disparities)
    plot_line_chart(gender_disparity)
    plot_pie_charts(gender_counts)

    print("\nAnalysis complete! Charts and Excel files have been saved.")
