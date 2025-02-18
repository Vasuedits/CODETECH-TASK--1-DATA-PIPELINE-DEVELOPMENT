import pandas as pd
from sklearn.preprocessing import StandardScaler

# Step 1: Extract
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)  # Correct method to read a CSV file
        print("Data extracted successfully.")
        return data 
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Step 2: Transform
def transform_data(data):
    # Display initial data info
    print("Initial Data Info:")
    print(data.info())
    
    # Handle missing values
    data.fillna(data.mean(), inplace=True)  # Fill missing values with mean for numerical columns
    print("Missing values handled.")

    # Example transformation: Standardize numerical features
    numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    print("Numerical features standardized.")

    # Display transformed data info
    print("Transformed Data Info:")
    print(data.info())
    
    return data

# Step 3: Load
def load_data(data, output_file_path):
    try:
        data.to_csv(output_file_path, index=False)
        print(f"Data loaded successfully to {output_file_path}.")
    except Exception as e:
        print(f"Error loading data: {e}")

# Main ETL function
def main(input_file_path, output_file_path):
    # Extract
    data = extract_data(input_file_path)
    if data is not None:
        # Transform
        transformed_data = transform_data(data)
        # Load
        load_data(transformed_data, output_file_path)

# Example usage
if __name__ == "__main__":
    input_file = 'input_data.csv'  # Replace with your input file path
    output_file = 'output_data.csv'  # Replace with your desired output file path
    main(input_file, output_file)
