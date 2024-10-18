# Packaging machine learning models with Python

Packaging Machine Learning models involves saving it and wrapping it with an API. Here’s the process of packaging a Machine Learning model:

- Step 1: Export/Save the Trained Model
- Step 2: Writing a Wrapper Function to Load the Model
- Step 3: Setting Up an API to Serve the Model

## Running the app

```python
  flask --app app run
```

## Testing the app

- Open Postman and create a new POST request.
- Set the URL to <http://127.0.0.1:5000/predict> (Replace the URL with your URL).
- In the Body tab, choose raw and set the data type to JSON.
- Use an object of this format to test the API:

```json
  {
    "input": [0.5, 0.3, 0.7, 0.1]
  }
```
