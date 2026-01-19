# 📱 Cross-Platform Social Media Auto Poster

## 🚀 Overview

Managing multiple social media platforms requires posting the same content repeatedly, which is time-consuming and inefficient for startups, organizations, and marketing teams.

**Cross-Platform Social Media Auto Poster** automates this workflow by allowing users to write a post once and publish it across multiple platforms directly through Android apps using **DroidRun-based UI automation**.

---

## 🎯 Problem Statement

- Teams and organizations manually repost the same content on multiple platforms
- API-based tools are limited, restricted, or frequently change
- Platform APIs require approvals, permissions, and maintenance
- Manual posting wastes time and reduces productivity

---

## ✅ Our Solution

We built a **B2B-focused automation tool** that:

- Accepts post content and hashtags from the user via terminal
- Uses DroidRun to automate Android app interactions
- Publishes posts across multiple platforms automatically
- Bypasses API limitations by automating the real mobile workflow

Each platform is handled by a **separate automation agent**, ensuring reliability and respecting DroidRun’s execution limits.

---

## 🧠 How It Works

1. User runs the Python script
2. User enters:
   - Post content
   - Hashtags
   - Target platforms (LinkedIn, X)
3. For each platform:
   - A new DroidRun agent is created
   - The corresponding Android app is opened
   - The post is created and published
4. The agent exits cleanly after completion

---

## 🧩 Architecture

```
User Input (Terminal)
        ↓
Python Controller Script
        ↓
Platform-wise DroidRun Agents
        ↓
Android App UI Automation
        ↓
Post Published Successfully
```

---

## 🛠 Tech Stack

- Python 3
- DroidRun Framework
- Android Emulator / Physical Android Device
- Google Gemini (via LlamaIndex)
- ADB (Android Debug Bridge)

---

## 📱 Supported Platforms

- LinkedIn
- X (Twitter)

> ⚠️ User must already be logged in on the Android device.

> Note: Only Two platform is added due to heavy load on the framework for demo.

---

## ▶️ Usage

### 1️⃣ Run the script

```bash
python post_automation.py
```

### 2️⃣ Provide inputs

```text
Enter post text:
> Launching our new product today!

Enter hashtags:
> #startup #launch #tech

Select platforms (comma separated):
> linkedin,x
```

### 3️⃣ Automation begins

The system automatically publishes the post on the selected platforms using Android UI automation.

---

## 🔒 Why DroidRun?

- No dependency on platform APIs
- Works even when APIs are restricted or unavailable
- Visual, deterministic automation
- Handles UI changes better than brittle API integrations
- Safe execution with bounded step limits

---

## ⚠️ Limitations

- User must be logged in beforehand
- Image and video posting not included in the current demo
- UI changes in apps may require prompt updates

---

## 🔮 Future Scope

- Image and video post automation
- Scheduled posting
- Support for additional platforms (Instagram, Facebook)
- Team dashboards for organizations
- Analytics and posting logs

---

## 🏢 Target Users (B2B Focus)

- Startups
- Marketing teams
- Social media agencies
- Organizations managing multiple brand accounts

*Secondary users:* individual creators and influencers.

---

## 🏁 Conclusion

This project demonstrates how **device-level automation** can solve real-world productivity problems where traditional API-based solutions fall short. By leveraging DroidRun, we enable scalable, reliable, and practical cross-platform social media automation.


## 👤 Author
Developed by **CodeStrom** during a hackathon.