/**
 * Outbound calls with answering machine detection and voicemail drop.
 * Usage: npx tsx main.ts
 */

import { Patter } from "getpatter";
import dotenv from "dotenv";
dotenv.config({ path: "../.env" });

const phone = new Patter({
  mode: "local",
  openaiKey: process.env.OPENAI_API_KEY!,
  twilioSid: process.env.TWILIO_ACCOUNT_SID!,
  twilioToken: process.env.TWILIO_AUTH_TOKEN!,
  phoneNumber: process.env.TWILIO_PHONE_NUMBER!,
  webhookUrl: process.env.WEBHOOK_URL!,
});

const agent = phone.agent({
  systemPrompt: `You are a polite appointment reminder assistant for Dr. Smith's
dental office. Remind the patient of their upcoming appointment, confirm the date
and time, and ask if they need to reschedule. Keep the call brief and friendly.`,
  voice: "nova",
  firstMessage:
    "Hi! This is a friendly reminder from Dr. Smith's dental office about your upcoming appointment.",
});

async function main(): Promise<void> {
  await phone.call({
    to: "+15551234567",
    agent,
    machineDetection: true,
    voicemailMessage:
      "Hi, this is Dr. Smith's office calling to remind you of your upcoming appointment. Please call us back at your earliest convenience.",
  });
}

main();
