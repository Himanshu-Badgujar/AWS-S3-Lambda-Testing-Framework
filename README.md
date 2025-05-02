
# ☁️ AWS S3-Lambda Testing Framework

This project is a cloud-based test automation framework developed using **Pytest**, **Boto3**, and **AWS services**. It validates end-to-end serverless workflows triggered by **S3 uploads**, ensuring **Lambda functions** are invoked and processed as expected, with full log verification using **CloudWatch**.

---

## 🚀 Features

- **End-to-End Workflow Testing**  
  Uploads test images to S3 and verifies Lambda execution via CloudWatch logs.

- **Modular Test Architecture**  
  Includes `conftest.py` for shared fixtures and a reusable `LambdaTestBase` class.

- **Auto Cleanup**  
  Automatically deletes test files from S3 after execution to keep environments clean.

- **HTML Reporting**  
  Generates detailed test execution reports using `pytest-html`, ideal for CI/CD use.

- **Log-Based Assertions**  
  Parses Lambda logs from CloudWatch to assert expected behavior without mocking.

---

## 🔧 Technologies Used

- **Language:** Python 3.x  
- **Test Framework:** Pytest  
- **AWS SDK:** Boto3  
- **Services:** AWS S3, Lambda, CloudWatch Logs  
- **Reporting Tool:** pytest-html

---

## ⚙️ How to Run

1. Clone the repository  
2. Create a `.env` file with AWS credentials and bucket name  
3. Set up a virtual environment and install dependencies  
4. Run the test using:
```bash
pytest --html=reports/aws_test_report.html --self-contained-html
```

---

## 📌 Notes

- Ensure your AWS credentials have access to S3, Lambda, and CloudWatch Logs.  
- The test uploads a real image to your S3 bucket and verifies actual Lambda execution.  
- Make sure the Lambda function is correctly linked to your S3 bucket via event trigger.  
- Ideal for validating production-like event-driven serverless architectures.

---

## 🧑‍💻 Author

**Himanshu Badgujar**
