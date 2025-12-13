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
<!-- ```
/postman -->

  Correct post response:

  ![Alt Text](images\post-links-201-success-picture1.png)
  ![Alt Text](images\post-links-201-success-picture2.png)

  Incorrect post response:

  ![Alt Text](images\post-links-422-invalid-url.png)

  Correct get all url response:

  ![Alt Text](images\get-links-200-success-picture1.png)
  ![Alt Text](images\get-links-200-success-picture2.png)

  inCorrect get all url response:
  because we wrote url instead of urls which is incorrect and raise error.

  ![Alt Text](images\get-code-404-not-found-picture2.png)

  Correct specific url response:

  ![Alt Text](images\get-code-302-redirect.png)

  incorrect specific url response:

  ![Alt Text](images\get-code-404-not-found-picture1.png)

  correct delete respose:

  ![Alt Text](images\delete-code-200-success.png)

  incorrect delete respose:

  ![Alt Text](images\delete-code-404-not-found.png)

  using scheduler:

  As you can see we have this url

  ![Alt Text](images\scheduler-before-expiration-time.png)

  but when the time ends scheduler delete’s it

  ![Alt Text](images\scheduler-after-expiration-time.png)











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


