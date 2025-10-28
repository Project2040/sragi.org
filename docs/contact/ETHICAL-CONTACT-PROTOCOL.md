# 🧭 SRAGI Ethical Contact Protocol

**File:** `/docs/contact/ETHICAL-CONTACT-PROTOCOL.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0  
**Last Updated:** October 28, 2025  
**License:** CC BY-SA 4.0 via SRL v1.1

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

