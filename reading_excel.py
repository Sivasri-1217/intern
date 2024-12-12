import pandas as pd

# Load the Excel file
df = pd.read_excel(r'D:\intern\intern (2).xlsx')

# Display the first few rows to understand the structure
print(df.head())
# Count requests by status
status_counts = df['Status'].value_counts()
print(status_counts)

# Calculate average decision time
df['Decision Time'] = (pd.to_datetime(df['Approval Date']) - pd.to_datetime(df['Submission Date'])).dt.days
avg_decision_time = df.groupby('Approver role')['Decision Time'].mean()
print(avg_decision_time)
# Filter pending requests
pending_requests = df[df['Status'] == 'Pending']
print(pending_requests)

# Filter recent requests (last 30 days)
recent_requests = df[pd.to_datetime(df['Submission Date']) >= '2024-11-01']
print(recent_requests)
# Save to Excel
pending_requests.to_excel('/content/pending_requests.xlsx', index=False)
