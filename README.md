## README

Kindly check the readme files for installation / set up details:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

## Api Reference

### Getting Started
- After running the backend server locally, you should be able to access all endpoints using the base url ```http://127.0.0.1:5000/api/```
- This version does not required authentication or API Keys.

### Error Handling
Error are returned as JSON objects in the following format:
```json
{
  "success" : False,
  "error" : 400,
  "message" : "bad request"
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Unprocessable


### Endpoints
#### GET /categories
- General
  - Returns a list of cateogy object as key:value pairs, success value and the total number of categories
- Sample ```http://127.0.0.1:5000/api/categories```: 
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true, 
  "total_categories": 6
}
```

#### GET /questions
- General
  - Returns a list of question object, all available categories, current category, success value and total number of questions
  - Results are paginated in groups of 10. Include a request arugment to chose page number, starting from 1
  - optional: include categoryId request arugment to get the questions of that specific category
- Sample ```http://127.0.0.1:5000/api/questions?page=1&categoryId=1```: 
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": "Science", 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Test1", 
      "category": 1, 
      "difficulty": 1, 
      "id": 25, 
      "question": "Test1"
    }
  ], 
  "success": true, 
  "total_questions": 4
}
```


#### POST /questions
- General
  - Option#1: include searchTerm to get the search result.
  - Option#2: include all required fields other than the searchTerm to create a question.
- Sample ```http://127.0.0.1:5000/api/questions```: 
- Option#1 - Request Parameters: 
```json
{
    "question": "Test1",
    "answer" : "Test1",
    "category" : "1",
    "difficulty" : "1"
}
```
- Option#1 - Response body: 
```json
{
    "created": 26,
    "success": true
}
```

