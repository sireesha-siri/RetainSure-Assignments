### 🚀 Implemented Features (Core Requirements)

- **POST `/api/shorten`**  
  Accepts a valid long URL in JSON body  
  Validates input and returns 6-character short code with full short URL  
  Stores mapping in a thread-safe in-memory dictionary

- **GET `/<short_code>`**  
  Redirects to original long URL  
  Returns 404 if code is not found  
  Increments click count on each successful redirect

- **GET `/api/stats/<short_code>`**  
  Returns JSON: original URL, total click count, and creation timestamp  
  Returns 404 if short code is invalid

---

### ⚙️ Technical Requirements Met

- ✅ 6-character short code generation using secure random alphanumeric string  
- ✅ Thread-safe in-memory storage using `threading.Lock`  
- ✅ Regex-based URL validation  
- ✅ Proper HTTP error handling (400, 404)  
- ✅ RESTful API design and status codes  
- ✅ No external databases used (in-memory only)  
- ✅ All code modular, well-separated (`utils.py`, `models.py`, `main.py`)

---

### 🧪 Testing

- ✅ `tests/test_basic.py` includes **5 tests** covering:
  - Valid shortening and redirection
  - Analytics endpoint
  - Handling of invalid short codes
  - Invalid URL submission
  - Case sensitivity and duplicate URL behavior

- ✅ All tests pass via:
  ```bash
  python -m pytest


🧱 Project Structure

url-shortener/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # API routes
│   ├── models.py        # Thread-safe in-memory storage
│   └── utils.py         # URL validation and short code generator
│
├── tests/
│   └── test_basic.py    # 5 test cases (functional + edge)
│
├── requirements.txt
├── README.md
└── CHANGES.md


📌 Design Decisions

Used re module for simple and fast URL format validation

Kept everything in memory as required—suitable for this scale

Used uuid4().hex[:6] alternative only if collisions were not resolved (but not needed with current generator)

Separated concerns: utils.py handles validation & code gen, models.py handles storage

Click tracking is atomic (thread-safe)

Minimal external dependencies (only Flask and pytest)

Health check available via / route (already scaffolded)


📖 API Summary

Method	Endpoint	Description
POST	/api/shorten	Shortens a long URL
GET	/<short_code>	Redirects to original long URL
GET	/api/stats/<code>	Returns URL analytics
GET	/	Health check


🤖 AI Usage Declaration

I used ChatGPT to assist with:

Planning overall file structure

Writing boilerplate for routes and storage

Suggesting regex for URL validation

Debugging PowerShell-related curl command issues

Writing this CHANGES.md file in markdown format

All AI-generated code and responses were reviewed, understood, and edited to match my logic and project goals.
No code was blindly copied or used without verification.


✅ Final Notes

All assignment requirements are met

Fully testable via curl, browser, or any REST client

Clean code, well-commented for readability