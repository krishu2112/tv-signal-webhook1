# TradingView Webhook System (with Python)

## 🚀 Features
- Receives TradingView alerts via webhook
- Logs signals with timestamp
- Ready to deploy on Railway
- Placeholder for Angel One integration

## 🔧 Setup
1. Rename `.env.example` to `.env`
2. Add your API keys
3. Deploy using Railway or run locally

## 📩 Webhook Example
Use this JSON in TradingView alerts:

```json
{
  "symbol": "{{ticker}}",
  "price": "{{close}}",
  "signal": "BUY"
}
```

Webhook URL (after deployment):  
`https://your-app-name.up.railway.app/webhook`
