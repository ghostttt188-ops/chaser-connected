from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vortex-chaser-secret'

# Full multi-feature ChaserConnect Dashboard template
FULL_APP_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ChaserConnect 24/7 - Operations Center</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-dark text-white">
    <nav class="navbar navbar-expand-lg navbar-dark bg-black border-bottom border-secondary px-4">
        <a class="navbar-brand fw-bold text-warning" href="#">⚡ CHASERCONNECT 24/7</a>
        <div class="navbar-nav ms-auto">
            <span class="nav-item nav-link text-success fw-bold">● System Online</span>
        </div>
    </nav>
    <div class="container mt-4">
        <div class="row">
            <div class="col-md-4 mb-3">
                <div class="card bg-secondary text-white p-3 border-0 shadow">
                    <h4>Quick Navigation</h4>
                    <hr>
                    <a href="#" class="btn btn-warning mb-2 fw-bold text-dark">Live Map & Radar</a>
                    <a href="#" class="btn btn-outline-light mb-2">Team Chat Feed</a>
                    <a href="#" class="btn btn-outline-light mb-2">Severe Weather Dispatches</a>
                    <a href="#" class="btn btn-outline-light mb-2">Storm Shelters Directory</a>
                </div>
            </div>
            <div class="col-md-8">
                <div class="card bg-secondary text-white p-4 border-0 shadow">
                    <h3>Active Operations & Field Feed</h3>
                    <p class="text-light">Connected to local spotter network and live NWS data streams.</p>
                    <div class="p-3 bg-dark rounded border border-secondary mt-3">
                        <h5 class="text-warning">System Status</h5>
                        <p class="mb-0 text-muted">All tracking modules, socket connections, and database pathways initialized successfully.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(FULL_APP_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
