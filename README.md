# 📲 WhatsApp Bulk Message Sender

Automate sending bulk WhatsApp messages to a list of contacts using **Python**, **Selenium**, and **Google Excel (xlsx)**. No WhatsApp Business API required — works directly through **WhatsApp Web** in your browser.

---

## ✨ Features

- Send personalized or identical messages to multiple contacts at once
- Reads contacts directly from an Excel (`.xlsx`) file
- Works with any standard WhatsApp account (no Business API needed)
- Simple to set up and customize

---

## 🛠️ Requirements

Before running the script, make sure you have the following installed:

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Run the script |
| Google Chrome | Browser used for WhatsApp Web automation |
| ChromeDriver | Bridge between Selenium and Chrome |
| pip packages | See `requirements.txt` |

---

## 📦 Installation

### Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
```

### Step 2 — Install Python dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **selenium** — controls Chrome browser automatically
- **pandas** — reads the Excel contact list
- **openpyxl** — engine used by pandas to open `.xlsx` files

### Step 3 — Download ChromeDriver

ChromeDriver must match your installed **Google Chrome version**.

1. Check your Chrome version: open Chrome → go to `chrome://settings/help`
2. Download the matching ChromeDriver from:
   👉 https://googlechromelabs.github.io/chrome-for-testing/
3. Extract the downloaded file
4. Place `chromedriver.exe` (Windows) or `chromedriver` (Mac/Linux) in the **same folder** as `basic_auto.py`

> ⚠️ **Version mismatch will cause the script to fail.** Always match ChromeDriver to your exact Chrome version.

---

## 📋 Preparing Your Contact List

Your Excel file **must follow this exact format**:

| Name | Number |
|------|--------|
| Eshat | 8801609159939 |
| Minahj | 8801830691808 |
| Suchi | 8801302764414 |

### Rules for the Excel file:
- The file must be named `contacts.xlsx`
- It must have **exactly two columns**: `Name` and `Number`
- Phone numbers must include the **country code** (no `+`, no spaces, no dashes)
  - ✅ Correct: `8801609159939` (Bangladesh: 880 + number)
  - ❌ Wrong: `+8801609159939` or `01609159939`
- Place `contacts.xlsx` in the **same folder** as `basic_auto.py`

---

## ✏️ Customizing Your Message

Open `basic_auto.py` and find this line:

```python
message = "Assalamu Alaikum. I love you."
```

Replace it with any message you want to send. For example:

```python
message = "Hi! This is an automated message. Please reply to confirm receipt."
```

> 💡 Currently the same message is sent to all contacts. Personalization per contact (using the Name column) can be added with minor modifications.

---

## 🚀 How to Run

### Step 1 — Update the ChromeDriver path

Open `basic_auto.py` and update this line to match where you placed `chromedriver.exe`:

```python
service = Service(r"E:\Whatsapp_automate\chromedriver.exe")
```

If `chromedriver.exe` is in the **same folder** as the script, change it to:

```python
service = Service("chromedriver.exe")
```

### Step 2 — Run the script

```bash
python basic_auto.py
```

### Step 3 — Scan the QR Code

1. A Chrome browser window will open and load **WhatsApp Web**
2. On your phone, open WhatsApp → tap **⋮ Menu** → **Linked Devices** → **Link a Device**
3. Scan the QR code shown in the browser
4. Go back to your terminal and press **ENTER**

### Step 4 — Watch it work

The script will automatically:
- Open a WhatsApp chat for each number in your Excel file
- Type and send your message
- Wait 6 seconds between messages (to avoid getting flagged)
- Print a success or failure status for each contact in the terminal

---

## 📁 Project Structure

```
whatsapp-bulk-sender/
│
├── basic_auto.py       # Main automation script
├── contacts.xlsx       # Your contact list (Excel file)
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from git
└── README.md           # Project documentation
```

---

## ⚠️ Important Notes

- **Do not spam.** Sending bulk messages to many people in a short time may cause WhatsApp to temporarily or permanently ban your number. Use responsibly.
- **Personal use only.** This tool is intended for legitimate communication (event invites, announcements, etc.), not unsolicited advertising.
- The 6-second delay between messages (`time.sleep(6)`) is intentional — do not reduce it significantly.
- WhatsApp Web UI changes occasionally. If the script stops working, the XPATH selector for the message box may need to be updated.

---

## 🐛 Troubleshooting

| Problem | Solution |
|--------|---------|
| `selenium.common.exceptions.SessionNotCreatedException` | ChromeDriver version doesn't match Chrome. Re-download the correct version. |
| Message box not found / TimeoutException | WhatsApp Web UI may have changed. Try updating the XPATH in the script. |
| Script sends to some but not all numbers | Number format issue — ensure country code is included and no special characters. |
| Chrome opens but immediately closes | ChromeDriver path is wrong. Double-check the path in `Service(...)`. |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Eshat** — [GitHub](https://github.com/Eshat117)

Feel free to fork, improve, and contribute!
