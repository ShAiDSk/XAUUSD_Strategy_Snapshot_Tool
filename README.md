
<h1 align="center">📊 XAUUSD Strategy Snapshot Tool</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&center=true&vCenter=true&multiline=false&width=600&lines=📈+Trade+Log+Visualizer+for+XAUUSD;⚙️+Entry%2FSL%2FTP+%2B+RR+Calculator;📤+Telegram+Export+%2B+MongoDB+Tracker" alt="Typing animation"/>
</p>

---

<p align="center">
  <img src="https://github.com/ShAiDSk/XAUUSD_Strategy_Snapshot_Tool/blob/main/Trading_GIF__.gif" width="300" alt="Trading chart gif" />
</p>

---

## 🚀 Features

- 📈 Input Entry / SL / TP and auto-calculate RR ratio
- 🖼️ Generate clean annotated strategy chart with zones
- 💾 Save each setup with timestamp to MongoDB
- 📤 Export snapshot directly to Telegram bot
- 📚 Easy journaling and trade documentation
- 🔁 Fully extendable and automation-ready

---

## ⚙️ Tech Stack

| Layer         | Tech                          |
|---------------|-------------------------------|
| Frontend UI   | `Streamlit`                   |
| Chart Engine  | `Matplotlib`                  |
| Backend       | `Python`                      |
| Database      | `MongoDB` via `PyMongo`       |
| Export Tool   | `python-telegram-bot`         |

---

## 📸 Live Demo Snapshots

<table>
<tr>
<td align="center">
  <strong>Trade Entry Form</strong><br>
  <img src="https://via.placeholder.com/350x200.png?text=Form+UI" width="300"/>
</td>
<td align="center">
  <strong>Generated Chart Output</strong><br>
  <img src="https://via.placeholder.com/350x200.png?text=RR+Snapshot+Chart" width="300"/>
</td>
</tr>
</table>

---

## 📥 Installation

```bash
git clone https://github.com/itz-shaidsk-fx/xauusd_ss_tool.git
cd xauusd_ss_tool
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

> ⚠️ MongoDB must be running at `localhost:27017`

---

## 📲 Telegram Integration

1. Create a bot via `@BotFather`  
2. Get your Chat ID via `@userinfobot`  
3. Update `telegram_export.py`:

```python
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
```

4. Uncomment in `app.py`:

```python
send_snapshot_to_telegram(...)
```

---

## 📁 Folder Structure

```
xauusd_ss_tool/
├── app.py
├── chart_generator.py
├── database.py
├── telegram_export.py
├── requirements.txt
└── snapshots/
```

---

## 🌱 Future Enhancements

- 🗃️ Snapshot Journal Page
- ⏰ Daily trade log scheduler
- 🧠 Strategy summary statistics
- 🌐 Streamlit Cloud Deployment

---

## 🙌 Author

Built with 💛 by [Shaid SK](https://github.com/shaidsk)

---

<p align="center">
  <img src="https://github.com/ShAiDSk/XAUUSD_Strategy_Snapshot_Tool/blob/main/download.gif" width="400" alt="Trading glowing chart" />
</p>

<p align="center"><em>“Discipline over emotion. Systems over randomness.”</em></p>
