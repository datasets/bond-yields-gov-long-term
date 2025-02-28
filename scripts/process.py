import os
import csv
import requests
from datetime import datetime, timedelta
from collections import deque

def increment_month(latest_date_str):
    latest_date_dt = datetime.strptime(latest_date_str, "%Y-%m")
    latest_date_dt = latest_date_dt.replace(day=1)

    # Format back to string
    latest_date = latest_date_dt.strftime("%Y-%m-%d")

    # Increment month by adding 32 days (ensures we move to next month)
    next_month_dt = latest_date_dt + timedelta(days=32)
    next_month_dt = next_month_dt.replace(day=1)

    # Get current date
    current_date = datetime.today().strftime("%Y-%m-%d")

    return next_month_dt.strftime("%Y-%m-%d"), current_date
def get_last_row_first_value(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            last_row = deque(csv_reader, maxlen=1)
            if not last_row:
                raise ValueError("CSV file is empty")
            return last_row[0][0]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_csv(url_link):
    try:
        response = requests.get(url_link)
        with open("data/us-10y-temp.csv", 'wb') as file:
            file.write(response.content)

        print("CSV file downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return url_link

def process_final_data():
    # Fill in the missing data as 0 
    # Make it monthly data remove the daily data by combining the dates and dividing the average of each month.
    with open("data/us-10y-temp.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header
        data = list(csv_reader)
        
        # Group data by month
        monthly_data = {}
        for date, value in data:
            if not value:  # Skip missing values
                continue
            month = date[:7]  # Extract YYYY-MM
            if month not in monthly_data:
                monthly_data[month] = []
            monthly_data[month].append(float(value))
        
        # Calculate monthly averages
        final_data = []
        for month, values in monthly_data.items():
            month_avg = sum(values) / len(values)
            final_data.append([month, round(month_avg, 2)])
        
        # Write to final CSV
        with open("data/us-10y-final.csv", 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Date", "Value"])
            csv_writer.writerows(final_data)
        print("Final data processed successfully.")

def combine_and_remove():
    # Combine us-10y.csv and us-10y-final.csv and remove the us-10y-final.csv file
    with open("data/us-10y.csv", 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    with open("data/us-10y-final.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        final_data = list(csv_reader)

    # Combine the data
    combined_data = data + final_data

    with open("data/us-10y.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(combined_data)
        print("Data combined successfully.")

    # Remove the final file
    os.remove("data/us-10y-final.csv")
    os.remove("data/us-10y-temp.csv")
    print("Temporary files removed successfully.")
    
if __name__ == "__main__":
    file_path = "data/us-10y.csv"
    latest_date_str = get_last_row_first_value(file_path)
    
    if latest_date_str:
        try:
            latest_date, current_date = increment_month(latest_date_str)
            print("Latest Date String:", latest_date)
            print("Current Date:", current_date)
            url_link = (
                f"https://fred.stlouisfed.org/graph/fredgraph.csv?"
                f"bgcolor=%23ebf3fb&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&"
                f"mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1320&nt=0&thu=0&trc=0&"
                f"show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DGS10&scale=left&cosd={latest_date}&"
                f"coed=2025-02-26&line_color=%230073e6&link_values=false&line_style=solid&mark_type=none&"
                f"mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily&fam=avg&fgst=lin&fgsnd=2020-02-01&"
                f"line_index=1&transformation=lin&vintage_date=2025-02-28&revision_date={current_date}&nd={latest_date}"
            )
            get_csv(url_link)

            print(f"The latest date in the CSV file is: {latest_date}")

            process_final_data()

            combine_and_remove()
        except ValueError as e:
            print(f"Date conversion error: {e}")
