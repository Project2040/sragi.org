# 🧭 SRAGI Ethical Contact Protocol

**File:** `/docs/core/ETHICAL-CONTACT-PROTOCOL.md`  
**Status:** CORE DOCTRINE
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0  
**Last Updated:** December 2025  
**License:** CC BY-SA 4.0 via SRL

---

## 🌿 Purpose

The SRAGI Contact Form embodies our commitment to **ethical communication** and **data minimalism**.  
It demonstrates that meaningful digital interaction can occur **without surveillance, storage, or exploitation**.

This document defines how the contact form on [SRAGI.org/contact](https://sragi.org/contact) operates technically and ethically.

---

## 🧩 Overview

| Principle | Implementation |
|------------|----------------|
| **Data minimization** | Only collects what is necessary for response (name, email, message). |
| **Explicit consent** | Checkbox confirms whether data may be temporarily stored. |
| **No default consent** | Consent must be actively given; otherwise, no data is retained after sending. |
| **Transparency** | Every outgoing email clearly states consent status. |
| **No logging** | No submissions stored in database (Bricks `saveSubmissions` = false). |
| **No cookies or tracking** | The form operates entirely client-side without analytics scripts. |
| **Plaintext delivery** | Messages are sent as standard email — no third-party processing or AI ingestion. |
| **Ethical fallback** | If consent not given, the system marks it explicitly as “No” in the message body. |

---

## 💌 Example Message Structure

### Incoming (to SRAGI team)

When a user submits the form, the system generates a plaintext email formatted for immediate clarity regarding data rights.

```text
Subject: [SRAGI Contact] Message from Ola Nordmann
From: no-reply@sragi.org (Verified Sender)
Reply-To: ola.nordmann@example.com

--- MESSAGE START ---

From: Ola Nordmann
Email: ola.nordmann@example.com
Context: General Inquiry

Message:
"Hei, I would like to inquire about the SRAGI framework..."

--- DATA GOVERNANCE ---

⚠️ CONSENT STATUS: [ GRANTED ] 
(User checked: "I consent to SRAGI storing this message for the duration of our correspondence.")

Action: You may reply and archive this thread normally.

---------------------------------------------------
System: SRAGI Ethical Mailer v1.0
Timestamp: 2025-12-09 14:00:00 UTC
````

**If Consent is DENIED:**

Plaintext

```
🛑 CONSENT STATUS: [ DENIED ]
(User did NOT check the storage consent box.)

Action: READ AND DESTROY.
1. Read the message.
2. Reply immediately if necessary.
3. DELETE this email chain once the query is resolved.
4. Do NOT add this contact to any CRM or mailing list.
```

---

## **🛠️ Technical Implementation**

### **1\. WordPress / Bricks Configuration**

We use the native Bricks Form element, but with strict overrides to prevent data leakage.

* **Action:** Custom (PHP)  
* **Database Storage:** Disabled (Critical\!)  
* **Email Service:** WP Mail (SMTP) via secure relay (Postmark/Brevo).

### **2\. The Sanitzation Layer (PHP)**

Before wp\_mail() is called, the following logic applies:

PHP

```
// Pseudo-code logic for the form handler
$consent = $_POST['form-field-consent'] ? 'GRANTED' : 'DENIED';
$message = sanitize_textarea_field($_POST['form-field-message']);

// Prevent database logging hooks
remove_all_actions('bricks/form/submit/save_submission');

// Construct headers
$headers[] = 'Content-Type: text/plain; charset=UTF-8';
$headers[] = 'X-SRAGI-Ethical-Protocol: Active';
```

---

## **🤖 AI & LLM Safety Policy**

Since SRAGI uses AI heavily internally, we must protect external correspondents.

**Rule:** Incoming contact messages are **Toxic to Latent Space** until proven otherwise.

1. **No Direct Copy-Paste:** Never paste a raw contact email into ChatGPT/Claude without anonymizing PII (Personally Identifiable Information).  
2. **No Training:** These emails exist outside the "SRAGI Knowledge Graph". They are private human-to-human communications.  
3. **The "Air Gap":** The contact form system is physically separate from the Loom Engine and Refinery. No automation touches these messages.

---

## **🔐 Compliance & Verification**

| Check | Frequency | Method |
| :---- | :---- | :---- |
| **No DB Rows** | Monthly | Check wp\_postmeta and custom tables for leaked entries. |
| **SMTP Logs** | Weekly | Ensure logs (in Postmark/Brevo) retention is set to min (e.g., 7 days). |
| **Consent UX** | Per Release | Verify checkbox is unchecked by default. |

---

**© 2025 Rune Solberg / Neptunia Media AS** Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL).

See SRL-LICENSE.yaml for details.

