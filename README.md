<p align="center">
  <img src="https://raw.githubusercontent.com/PatterAI/Patter/main/docs/patter-logo-banner.svg" alt="Patter" width="300" />
</p>

# Patter: Outbound Calls

Place outbound calls with answering machine detection (AMD) and voicemail drop.

> Part of the [Patter](https://github.com/PatterAI/Patter) Voice AI SDK.

## Prerequisites

- [Twilio](https://www.twilio.com/) account with a phone number
- [OpenAI](https://platform.openai.com/) API key with Realtime access

## Quick Start

### Python

```bash
cd python
cp ../.env.example .env   # fill in your keys
pip install -r requirements.txt
python main.py
```

### TypeScript

```bash
cd typescript
cp ../.env.example .env   # fill in your keys
npm install
npx tsx main.ts
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | OpenAI API key with Realtime access |
| `TWILIO_ACCOUNT_SID` | Yes | Twilio account SID |
| `TWILIO_AUTH_TOKEN` | Yes | Twilio auth token |
| `TWILIO_PHONE_NUMBER` | Yes | Your Twilio phone number (E.164) |
| `WEBHOOK_URL` | No | Public URL for webhooks (auto-tunneled if omitted) |

## What This Demonstrates

- `phone.call()` for placing outbound calls
- `machineDetection` to detect answering machines via AMD
- `voicemailMessage` to leave a pre-recorded message on voicemail
- Lifecycle callbacks for call events

## Next Steps

- [Inbound Agent](https://github.com/PatterAI/patter-inbound-agent) — answer calls with AI
- [Tool Calling](https://github.com/PatterAI/patter-tool-calling) — add webhook-backed tools
- [Custom Voice](https://github.com/PatterAI/patter-custom-voice) — pipeline mode with Deepgram + ElevenLabs
- [Full documentation](https://docs.getpatter.com)
- [All templates](https://github.com/PatterAI/Patter#templates)

## License

MIT
