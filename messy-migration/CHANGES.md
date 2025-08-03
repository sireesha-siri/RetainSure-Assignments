
## 🔍 Issues Identified

- SQL injection risks due to string interpolation
- No input validation or password hashing in the original setup
- Poor separation of concerns (all logic in a single file)
- Responses were plain text instead of JSON
- Missing HTTP status codes and error handling

## ✅ Changes Made

- Separated routes, database logic, and utilities into modular folders
- Used parameterized queries to prevent SQL injection
- Replaced plain string responses with JSON and appropriate status codes
- Added input validation for all POST/PUT endpoints
- Passwords are hashed using bcrypt before storing in the database
- Added basic test cases using `pytest`

## 🧠 Assumptions / Trade-offs

- Assumed that the email field must be unique for user creation
- Passwords are stored securely using hashing
- Returned hashed passwords in GET responses for demonstration purposes (not recommended in real-world apps)

## 🤖 AI Usage

Used ChatGPT to guide:
- Folder structure and modularization best practices
- Secure handling of passwords and inputs
- Error handling patterns and JSON responses
- Refactoring for code clarity and maintainability
