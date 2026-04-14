"""Outbound calls with answering machine detection and voicemail drop."""

import asyncio
import os

from dotenv import load_dotenv
load_dotenv()

from patter import Patter

phone = Patter(
    mode="local",
    openai_key=os.getenv("OPENAI_API_KEY"),
    twilio_sid=os.getenv("TWILIO_ACCOUNT_SID"),
    twilio_token=os.getenv("TWILIO_AUTH_TOKEN"),
    phone_number=os.getenv("TWILIO_PHONE_NUMBER"),
    webhook_url=os.getenv("WEBHOOK_URL"),
)

agent = phone.agent(
    system_prompt=(
        "You are calling to remind the patient about their upcoming "
        "dental appointment on Friday at 2:30 PM with Dr. Patel. "
        "Confirm their attendance, offer to reschedule if needed, "
        "and remind them to bring their insurance card."
    ),
    voice="nova",
    first_message=(
        "Hi, this is a friendly reminder from Bright Smile Dental. "
        "You have an appointment this Friday at 2:30 PM with Dr. Patel. "
        "Will you be able to make it?"
    ),
)

if __name__ == "__main__":
    asyncio.run(
        phone.call(
            to="+15551234567",
            agent=agent,
            machine_detection=True,
            voicemail_message=(
                "Hi, this is Bright Smile Dental reminding you about your "
                "appointment this Friday at 2:30 PM. Please call us back "
                "at 555-987-6543 to confirm. Thank you!"
            ),
        )
    )
