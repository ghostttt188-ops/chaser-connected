from flask import Flask, render_template_string

app = Flask(__name__)

FULL_APP_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ChaserConnect - Live Operations</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white">
    <nav class="navbar navbar-dark bg-black border-bottom border-secondary px-4">
        <span class="navbar-brand fw-bold text-warning">⚡ ChaserConnect 24/7</span>
        <span class="badge bg-success">Status: Online</span>
    </nav>
    <div class="container mt-5 text-center">
        <div class="card bg-secondary text-white p-4 shadow-lg border-0">
            <h2>Welcome to ChaserConnect</h2>
            <p class="text-light">Live tracking, chat, and field coordination network.</p>
            <hr class="border-light">
            <div class="d-flex justify-content-center gap-3 mt-3">
                <a href="#" class="btn btn-warning fw-bold px-4">Login</a>
                <a href="#" class="btn btn-outline-light px-4">Sign Up</a>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(FULL_APP_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
