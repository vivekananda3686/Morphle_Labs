# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse
# import os
# from datetime import datetime
# import pytz
# import subprocess

# def htop_view(request):
#     name = "Vivekananda Kappatrala" 
#     #username = os.getenv("USER") or os.getenv("USERNAME")
#     username="vivekananda"
    
#     # Get server time in IST
#     ist = pytz.timezone('Asia/Kolkata')
#     server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
#     # Get top command output
#     #top_output = subprocess.getoutput("top -b -n 1")
#     #top_output = subprocess.getoutput("ps aux")
#     top_output = subprocess.getoutput("top -b -n 1 2>&1")


#     # HTML format to display information
#     response_content = f"""
#     <html>
#         <body>
#             <h1>System Information</h1>
#             <p><strong>Name:</strong> {name}</p>
#             <p><strong>Username:</strong> {username}</p>
#             <p><strong>Server Time (IST):</strong> {server_time}</p>
#             <h2>Top Command Output</h2>
#             <pre>{top_output}</pre>
#         </body>
#     </html>
#     """
#     return HttpResponse(response_content)



from django.http import HttpResponse
import os
from datetime import datetime
import pytz
import subprocess
import platform

def htop_view(request):
    name = "Vivekananda Kappatrala" 
    username = "vivekananda"
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Check OS and run appropriate command for process list
    if platform.system() == "Windows":
        # For Windows, use `tasklist`
        top_output = subprocess.getoutput("tasklist")
    else:
        # For Unix-based systems, use `ps aux`
        top_output = subprocess.getoutput("ps aux")

    # HTML format to display information
    response_content = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Process List</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(response_content)
