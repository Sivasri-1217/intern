import pandas as pd
import os
file_path = 'intern (2).xlsx'
df = pd.read_excel(file_path)
df['Request type'] = df['Request type'].str.lower().str.strip()
df['Priority'] = df['Priority'].str.lower().str.strip()
df['Request dept'] = df['Request dept'].str.lower().str.strip()
df['Approver role'] = df['Approver role'].str.lower().str.strip()
df['Status'] = df['Status'].str.lower().str.strip()
print("Missing data before preprocessing:\n", df.isnull().sum())
df['Priority'] = df['Priority'].fillna('medium')
df['Status'] = df['Status'].fillna('pending')
df['Submission Date'] = pd.to_datetime(df['Submission Date'], errors='coerce')
df['Approval Date'] = pd.to_datetime(df['Approval Date'], errors='coerce')
df['Approval Date'] = df['Approval Date'].fillna(df['Submission Date'] + pd.Timedelta(days=7))
df = df.dropna(subset=['Request type', 'Request dept', 'Approver role'])
df['Decision Time (Days)'] = (df['Approval Date'] - df['Submission Date']).dt.days
approval_counts = df.groupby('Request dept')['Status'].apply(lambda x: (x == 'approved').mean() * 100).reset_index()
approval_counts.rename(columns={'Status': 'Approval Rate (%)'}, inplace=True)
df = df.merge(approval_counts, on='Request dept', how='left')
output_path = r'D:\intern\python\cleaned_dataset.xlsx'
os.makedirs(os.path.dirname(output_path), exist_ok=True) 
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to {output_path}")