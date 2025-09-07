# Power Automate Quick Reference Card

## 🚀 Getting Started
1. Go to **https://flow.microsoft.com**
2. Sign in with your Microsoft account
3. Click **"My flows"** → **"New flow"**

## 📋 Flow Types to Create

### Flow 1: Lead Qualification ⭐
- **Type:** Automated cloud flow
- **Trigger:** Microsoft Forms - "When a new response is submitted"
- **Key Actions:**
  - Initialize variable (LeadScore = 0)
  - Switch controls for Budget/Industry/Urgency scoring
  - Condition (if LeadScore > 20)
  - Send high priority email alert

### Flow 2: Client Success Monitoring 📊
- **Type:** Scheduled cloud flow (Weekly, Monday 9 AM)
- **Key Actions:**
  - SharePoint - Get client data
  - Initialize array variable (AtRiskClients)
  - Apply to each client
  - Check conditions (last contact, satisfaction, status)
  - Send alert if at-risk clients found

### Flow 3: Automated Reporting 📈
- **Type:** Scheduled cloud flow (Monthly, 1st day 8 AM)
- **Key Actions:**
  - SQL Server - Execute query for financial data
  - SharePoint - Get client metrics
  - Compose HTML report
  - Send email to executives

## ⚡ Essential Actions Reference

| Action Type | Purpose | Location |
|-------------|---------|----------|
| **Initialize variable** | Create variables | Variables |
| **Increment variable** | Add to number variables | Variables |
| **Append to array variable** | Add items to arrays | Variables |
| **Switch** | Multiple condition branching | Control |
| **Condition** | If/then logic | Control |
| **Apply to each** | Loop through items | Control |
| **Compose** | Create/format data | Data Operations |
| **Send an email (V2)** | Send emails | Office 365 Outlook |

## 🔧 Pro Tips

### Dynamic Content
- Click in any text field to see available dynamic content
- Use **Expression** tab for calculations and functions
- Common expressions:
  - `utcnow()` - Current date/time
  - `formatDateTime(utcnow(), 'yyyy-MM-dd')` - Format dates
  - `add(variables('Score'), 10)` - Math operations
  - `length(variables('Array'))` - Array length

### Variables Best Practices
- Always initialize variables at the top of your flow
- Use descriptive names: `LeadScore`, `AtRiskClients`
- Choose correct types: Integer, String, Array, Boolean

### Testing Flows
- Use **"Test"** button for immediate testing
- Check **"Run history"** for debugging
- Start with simple versions, add complexity gradually

## 🎯 Priority Order
1. **Start with Flow 1 (Lead Qualification)** - Most business impact
2. **Then Flow 2 (Client Success)** - Proactive client management  
3. **Finally Flow 3 (Reporting)** - Executive insights

## 📞 Support Resources
- **Microsoft Docs:** https://docs.microsoft.com/en-us/power-automate/
- **Community:** https://powerusers.microsoft.com/t5/Power-Automate-Community/ct-p/MPACommunity
- **Templates:** Browse existing templates in Power Automate for inspiration

---

**🎉 You're ready to start creating your automated flows!**
Begin with the manual creation guide and refer to this card as needed.
