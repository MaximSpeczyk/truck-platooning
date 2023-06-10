import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
random.seed(42)

# Generate random integer values
def create_random_numbers(number_of_cars, random_min, random_max):
    return [random.randint(random_min, random_max) for _ in range(number_of_cars)]

# Generate random data
number_of_cars = 100000
leader_vehicle = create_random_numbers(number_of_cars, 0, 1)
distance_route = create_random_numbers(number_of_cars, 500, 1000)
max_route_match = create_random_numbers(number_of_cars, 0, 100)
fuel_consumption = create_random_numbers(number_of_cars, 30, 400)
body_characteristics = create_random_numbers(number_of_cars, 1200, 4000)
equipment_sensors = create_random_numbers(number_of_cars, 3, 100)

# Create the DataFrame
data = pd.DataFrame({
    'distance_route': distance_route,
    'max_route_match': max_route_match,
    'fuel_consumption': fuel_consumption,
    'body_characteristics': body_characteristics,
    'equipment_sensors': equipment_sensors,
    'leader_vehicle': leader_vehicle
})

# Define features and target
x = data.drop(['leader_vehicle'],axis=1)
y = data.leader_vehicle

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Create a DecisionTreeClassifier and fit it to the training data
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
clf = clf.fit(x_train,y_train)

# Predict the test set results
y_pred = clf.predict(x_test)

# Print the accuracy of the model
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(15,15))
clf = DecisionTreeClassifier(max_depth = 3).fit(x, y)
plot_tree(clf, filled=True, fontsize=9)
plt.show()
