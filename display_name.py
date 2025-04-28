
import cgi

print("Content-Type: text/html\n")  # HTTP Header

# Get form data
form = cgi.FieldStorage()
first_name = form.getvalue("first_name", "Not provided")
last_name = form.getvalue("last_name", "Not provided")

# Generate the response
print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Display Name</title>
</head>
<body>
    <h2>Submitted Name</h2>
    <p><strong>First Name:</strong> {first_name}</p>
    <p><strong>Last Name:</strong> {last_name}</p>
    <a href="/index.html">Go Back</a>
</body>
</html>
""")
