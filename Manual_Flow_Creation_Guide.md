# Manual Power Automate Flow Creation Guide
## Complete Step-by-Step Instructions

### Prerequisites
1. Go to https://flow.microsoft.com
2. Sign in with your Microsoft account
3. Ensure you're in the correct environment (Default environment)

---

## Flow 1: Lead Qualification Automation

### Step 1: Create the Flow
1. Click **"My flows"** → **"New flow"** → **"Automated cloud flow"**
2. **Flow name:** `Lead Qualification Automation`
3. **Choose trigger:** Search for "Microsoft Forms" → Select **"When a new response is submitted"**
4. Click **"Create"**

### Step 2: Configure the Trigger
1. **Form Id:** Select your lead qualification form (or create one first)
2. Click **"New step"**

### Step 3: Add Initialize Variable Action
1. Search for **"Initialize variable"**
2. Configure:
   - **Name:** `LeadScore`
   - **Type:** `Integer`
   - **Value:** `0`

### Step 4: Add Budget Range Scoring (Switch Control)
1. Click **"New step"** → Search for **"Switch"**
2. **On:** Click in the box → **"Dynamic content"** → Select response field for budget range
3. **Case 1:**
   - **Equals:** `$50,000+`
   - **Action:** Search "Increment variable"
   - **Name:** `LeadScore`
   - **Value:** `25`
4. **Case 2:**
   - **Equals:** `$25,000-$49,999`
   - **Action:** "Increment variable"
   - **Name:** `LeadScore`
   - **Value:** `20`
5. **Case 3:**
   - **Equals:** `$10,000-$24,999`
   - **Action:** "Increment variable"
   - **Name:** `LeadScore`
   - **Value:** `15`

### Step 5: Add Industry Scoring
1. After the Switch, click **"New step"** → **"Switch"**
2. **On:** Select industry response field
3. Add cases for different industries with appropriate scores

### Step 6: Add Urgency Scoring
1. Add another **"Switch"** for urgency
2. Configure cases for "Immediate", "This month", "This quarter"

### Step 7: Add High Priority Condition
1. Click **"New step"** → Search for **"Condition"**
2. **Choose a value:** Select `LeadScore` variable
3. **is greater than** `20`

### Step 8: Configure High Priority Actions (Yes branch)
1. In the **"Yes"** branch, add **"Send an email (V2)"**
2. Configure:
   - **To:** `sales@company.com`
   - **Subject:** `🔥 High Priority Lead - Immediate Action Required`
   - **Body:** Include lead details and score

### Step 9: Add CRM Integration (Optional)
1. In the **"Yes"** branch, add another action
2. Search for your CRM connector (Dynamics 365, Salesforce, etc.)
3. Create a new lead record with high priority flag

### Step 10: Save and Test
1. Click **"Save"**
2. Submit a test form response
3. Monitor the flow run in the run history

---

## Flow 2: Client Success Monitoring

### Step 1: Create the Flow
1. **"New flow"** → **"Scheduled cloud flow"**
2. **Flow name:** `Client Success Monitoring`
3. **Repeat:** `Weekly`
4. **Start time:** Monday 9:00 AM

### Step 2: Add Get Client Data Action
1. Click **"New step"** → Search for **"SharePoint"**
2. Select **"Get items"** action
3. Configure:
   - **Site Address:** Your SharePoint site
   - **List Name:** Client data list

### Step 3: Initialize At-Risk Clients Array
1. **"New step"** → **"Initialize variable"**
2. Configure:
   - **Name:** `AtRiskClients`
   - **Type:** `Array`
   - **Value:** Leave empty `[]`

### Step 4: Add Apply to Each Loop
1. **"New step"** → **"Apply to each"**
2. **Select an output:** Choose `value` from SharePoint get items

### Step 5: Add Client Health Check Condition
Inside the loop, add a **"Condition"**:
1. **Choose a value:** `Last Contact Date`
2. **is less than** `addDays(utcnow(), -30)` (30 days ago)
3. **OR** (click "Add" → "Add row")
4. **Satisfaction Score** **is less than** `7`
5. **OR** **Project Status** **is equal to** `Delayed`

### Step 6: Add to At-Risk List (Yes branch)
1. In **"Yes"** branch: **"Append to array variable"**
2. Configure:
   - **Name:** `AtRiskClients`
   - **Value:** Select current item from dynamic content

### Step 7: Send Alert Email
After the loop, add a **"Condition"**:
1. **Choose a value:** `length(variables('AtRiskClients'))`
2. **is greater than** `0`

In the **"Yes"** branch:
1. Add **"Send an email (V2)"**
2. Configure:
   - **To:** `clientsuccess@company.com`
   - **Subject:** `⚠️ Client Health Alert - At-Risk Clients Detected`
   - **Body:** Include count and details of at-risk clients

---

## Flow 3: Automated Reporting Pipeline

### Step 1: Create the Flow
1. **"New flow"** → **"Scheduled cloud flow"**
2. **Flow name:** `Automated Reporting Pipeline`
3. **Repeat:** `Monthly`
4. **Start time:** 1st of month, 8:00 AM

### Step 2: Get Financial Data
1. **"New step"** → Search for **"SQL Server"**
2. Select **"Execute a SQL query"**
3. Configure:
   - **Server name:** Your SQL server
   - **Database name:** Your database
   - **Query:** 
   ```sql
   SELECT 
     SUM(Revenue) as TotalRevenue,
     AVG(ProjectValue) as AvgProjectValue,
     COUNT(*) as ProjectCount 
   FROM Projects 
   WHERE MONTH(CompletedDate) = MONTH(GETDATE()) - 1
   ```

### Step 3: Get Client Metrics
1. **"New step"** → **"SharePoint - Get items"**
2. Configure for your client metrics list

### Step 4: Generate Report HTML
1. **"New step"** → **"Compose"**
2. **Inputs:** Create HTML template with dynamic content:
```html
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    .header { background-color: #2E86AB; color: white; padding: 20px; text-align: center; }
    .metric-card { background: #f8f9fa; padding: 15px; margin: 10px 0; border-left: 4px solid #2E86AB; }
  </style>
</head>
<body>
  <div class="header">
    <h1>Monthly Business Report</h1>
    <p>@{formatDateTime(utcnow(), 'MMMM yyyy')}</p>
  </div>
  <div class="metric-card">
    <h3>Financial Performance</h3>
    <p><strong>Total Revenue:</strong> $@{first(body('Execute_a_SQL_query')?['resultsets'])?['Table1']?[0]?['TotalRevenue']}</p>
  </div>
</body>
</html>
```

### Step 5: Send Monthly Report
1. **"New step"** → **"Send an email (V2)"**
2. Configure:
   - **To:** `executives@company.com;management@company.com`
   - **Subject:** `📊 Monthly Business Report - @{formatDateTime(utcnow(), 'MMMM yyyy')}`
   - **Body:** Select output from Compose action
   - **Importance:** High

---

## Common Configuration Tips

### 1. Setting Up Connections
- First time using a connector, you'll be prompted to create a connection
- Use your work account for business connectors
- Test connections before proceeding

### 2. Dynamic Content
- Click in text fields to see dynamic content panel
- Use expressions for calculations: `add()`, `sub()`, `formatDateTime()`
- Use variables: `variables('VariableName')`

### 3. Error Handling
- Add "Configure run after" for error handling
- Use Try-Catch pattern with Scope actions
- Set up failure notifications

### 4. Testing
- Use "Test" button with manual trigger
- Check run history for debugging
- Use "Peek code" to see JSON structure

### 5. Deployment
- Export flows as solutions for deployment
- Use environment variables for different environments
- Document all custom configurations

---

## Troubleshooting Common Issues

### Connection Issues
- Verify account permissions
- Re-authenticate connections if needed
- Check firewall/network restrictions

### Dynamic Content Not Showing
- Save the flow first
- Refresh the browser
- Use expressions if dynamic content unavailable

### Flow Not Triggering
- Check trigger configuration
- Verify data source has required fields
- Test with manual runs first

### Performance Issues
- Minimize actions in loops
- Use filters in data queries
- Consider batching for large datasets
