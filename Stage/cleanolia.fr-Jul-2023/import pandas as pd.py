import pandas as pd
import os as o
file_path = o.path.join(o.path.dirname(__file__), 'stage.txt')
ip_address = []
timestamp = []
request = []
status_code = []
user_agent = []
with open(file_path, 'r') as file:
    for line in file:
        parts = line.split()
        ip_address.append(parts[0])
        timestamp.append(parts[3][1:] + ' ' + parts[4][:-1])
        request.append(parts[5] + ' ' + parts[6])
        status_code.append(parts[8])
        user_agent.append(' '.join(parts[11:]))
df = pd.DataFrame({
    'IP Address': ip_address,
    'Timestamp': timestamp,
    'Request': request,
    'Status Code': status_code,
    'User Agent': user_agent
})
df.to_csv('log_data.csv', index=False)