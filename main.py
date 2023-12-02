from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from email_validator import validate_email, EmailNotValidError
from disposable_email_domains import blocklist
import time

from config import PORT, ENVIRONMENT, API_PREFIX
from middleware import validate_api_key

app = FastAPI()

emailValidationRouterV1 = APIRouter(
    prefix="/v1/validate-emails", tags=["email_validator_v1"], dependencies=[Depends(validate_api_key)]
)


class BulkEmailValidator(BaseModel):
    emails: list[EmailStr]


def validate_email_data(email: str):
    """
    Validates the given email data against general email rules and a disposable email blocklist.

    Parameters:
        email (str): The email address to be validated.

    Returns:
        dict: A dictionary containing the validated email address and a message indicating its validity.
        The dictionary has the following keys:
            - email (str): The validated email address.
            - message (str): A message indicating the validity of the email.

    Raises:
        HTTPException: If the email address is found in the disposable email blocklist.

    """
    try:
        # Validate against general email rules
        v = validate_email(email, check_deliverability=True)

        # Check if the domain is in the disposable email blocklist
        domain = email.split("@")[1]
        if domain in blocklist:
            raise HTTPException(
                status_code=400,
                detail=f"Disposable email addresses are not allowed: {email}",
            )

        return {"email": email, "message": "Email is valid"}
    except EmailNotValidError as e:
        return {"email": email, "message": str(e)}
    except Exception as e:
        return {"email": email, "message": str(e)}


@emailValidationRouterV1.post("/:email")
async def validate_email_handler(email: EmailStr):
    # start timer
    start_time = time.time()
    try:
        validation_result = validate_email_data(email)

        # end timer
        end_time = time.time()
        return {"result": validation_result, "time_taken": end_time - start_time}
    except Exception as e:
        # end timer
        end_time = time.time()
        return {"result": str(e), "time_taken": end_time - start_time}


@emailValidationRouterV1.post("/")
async def validate_bulk_emails_handler(emails: BulkEmailValidator):
    # start timer
    start_time = time.time()
    try:
        validation_results = [
            validate_email_data(email) for email in bulk_email_validator.emails
        ]
        # end timer
        end_time = time.time()
        return {"results": validation_results, "time_taken": end_time - start_time}
    except Exception as e:
        # end timer
        end_time = time.time()
        return {"results": str(e), "time_taken": end_time - start_time}


app.include_router(
    emailValidationRouterV1,
    prefix=API_PREFIX,
)

# To run this application:
# uvicorn app:app --reload --port 8000
