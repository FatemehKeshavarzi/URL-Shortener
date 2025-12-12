# 📘 README - Midterm Final Checklist
This README **must remain in your repository** and **must be fully
completed** before submitting the midterm.
how to run the code:
```bash
poetry run uvicorn main:app --reload
```
---
## 1. API Test Coverage Table
Fill in the second column with the **name of the student** who implemented
and tested each API.
| # | API Endpoint / Feature | Implemented & Tested By (Student Name) |
|---|------------------------|-----------------------------------------|
| 1 | Create Short Link - **POST /links** | Raha |
| 2 | Redirect to Original URL - **GET /{code}** | Raha |
| 3 | Get All Shortened Links - **GET /links** | Fatemeh |
| 4 | Delete Short Link - **DELETE /links/{code}** | Fatemeh |
---
## 2. Code Generation Method (Section 6.4)
Check the method you used to generate the short code:
- [ ] **1. Random Generation**
- [x] **2. ID → Base62 Conversion**
- [ ] **3. Hash-based Generation**
(Only select the one you actually implemented.)
---
## 3. Bonus User Story: TTL (Expiration Time) for Shortened Links)
If you implemented the bonus user story, mark the box and complete the
required details.
- [x] **TTL Feature Implemented**
**If checked, fill in the following information:**
- **ENV variable or config key used:**
`TTL_TIME = 4 #based on minutes`
You must also ensure this key exists in `.env.example` with a sample value.
- **Location of TTL Logic (File + Function):**
Specify the exact location where TTL expiration is checked and expired
links are detected/removed.
`app/services/url_service.py → delete_expired_links()
`
- **How TTL cleanup is triggered:**
You must write a Command that removes expired links (created_at + TTL <
now()).
Here, write:
- Full file path of the command:
  `app/commands/scheduler.py`
- Command name / execution method:
  `poetry run python -m app.commands.scheduler`
- Scheduler details:
```bash
  Scheduler Technology: schedule (Python schedule library)
  Scheduler Interval: every 60 seconds
  Job: delete_expired_urls() from app.tasks.url_tasks
  Scheduler File: app/commands/scheduler.py
  
  The scheduler runs an infinite loop inside run_scheduler(), executing
  schedule.run_pending() every second.
  
  TTL cleanup is triggered automatically every 60 seconds by calling:
  delete_expired_urls()
  
  The scheduler is started by running:
  poetry run python -m app.commands.scheduler
```
---
## 4. Postman Collection (Required)
A **Postman Collection** has been created and includes all four API routes:
- **POST /links**
- **GET /{code}**
- **GET /links**
- **DELETE /links/{code}**
### Screenshots (included in GitHub)
For each route, two screenshots have been added:
- Successful response (2xx)
- Error-handled response (4xx)
Screenshots are located in:
```
/postman
Correct post response:
<img width="975" height="525" alt="image" src="https://github.com/user-attachments/assets/7d854ba8-f04c-469b-b3b2-99e2e78edd56" />
<img width="975" height="495" alt="image" src="https://github.com/user-attachments/assets/689fa1bf-f79f-451e-b695-96bdb2105954" />
Incorrect post response:
<img width="975" height="524" alt="image" src="https://github.com/user-attachments/assets/f197755b-c6f9-4146-bbc4-267d8d4776f2" />
Correct get all url response:
<img width="975" height="523" alt="image" src="https://github.com/user-attachments/assets/3438b76b-29db-4e23-b7c4-4ce86e1b569e" />
<img width="975" height="518" alt="image" src="https://github.com/user-attachments/assets/24a5c4cd-a7a4-414c-b39c-b34d43bae5d8" />
inCorrect get all url response:
Correct specific url response:
<img width="975" height="520" alt="image" src="https://github.com/user-attachments/assets/c1e346fc-8960-4be4-9edd-d3fb404957b6" />
incorrect specific url response:
<img width="975" height="524" alt="image" src="https://github.com/user-attachments/assets/7a84d8f0-8730-4194-9465-169dd17ecc90" />
correct delete respose:
<img width="975" height="523" alt="image" src="https://github.com/user-attachments/assets/dcfeea8b-c413-4d08-91fb-1bdf2302f294" />
incorrect delete respose:
<img width="975" height="525" alt="image" src="https://github.com/user-attachments/assets/9bb0d2c7-439e-459e-a9da-35b751877b12" />

using scheduler:
As you can see we have this url
 <img width="975" height="524" alt="image" src="https://github.com/user-attachments/assets/dd54a04d-7387-4519-a365-8848f58df7b8" />

but when the time ends scheduler delete’s  it
 <img width="975" height="567" alt="image" src="https://github.com/user-attachments/assets/566fdf01-057c-4b00-95d7-9077ae6df27c" />











```
### Naming Example:
```
postman/
post-links-201-success.png
post-links-400-invalid-url.png
get-code-302-redirect.png
get-code-404-not-found.png
get-links-200-success.png
delete-code-200-success.png
delete-code-404-not-found.png

```
Filenames must clearly show:
- Route
- HTTP status
- Success or error
---
**✔ Make sure this README is fully completed before submission.**

