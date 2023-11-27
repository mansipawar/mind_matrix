from flask import Flask, request, jsonify
from flask_cors import CORS  
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
CORS(app)  

# Load the trained model and other necessary data
csv_file = 'csv1.csv'
df = pd.read_csv(csv_file)
x = df.iloc[:, :-1]
y = df['OUTCOME']
y = y.astype('int')

# Train the Decision Tree Classifier
classifier = DecisionTreeClassifier(random_state=0)
classifier.fit(x, y)

@app.route('/')
def index():
    return "Hello, this is your Flask app!"


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    selected_options = data.get('options', [])

    # Extract the last digit from each option value and store in selected_indices
    selected_indices = [int(option['option'][-1]) for option in selected_options]

    # Predict the outcome based on the selected indices
    prediction = classifier.predict([selected_indices])

    # Append the new data to the DataFrame
    new_data = pd.DataFrame({'Q1': [selected_indices[0]], 'Q2': [selected_indices[1]], 'Q3': [selected_indices[2]], 'Q4': [selected_indices[3]], 'Q5': [selected_indices[4]], 'Q6': [selected_indices[5]], 'Q7': [selected_indices[6]], 'OUTCOME': [int(prediction[0])]})

    global df  # Use the global variable
    df = pd.concat([df, new_data], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    df.to_csv(csv_file, index=False)
   
    # Return a response with the selected indices
    response = {'outcome': int(prediction[0])}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)