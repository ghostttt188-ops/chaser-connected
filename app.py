from flask import Flask, render_template_string

app = Flask(__name__)

# Exact ChaserConnect Dashboard UI Layout from your screenshot
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ChaserConnect</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #121212; color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        .navbar { background-color: #1a1a1a; border-bottom: 1px solid #333; }
        .card, .post-box { background-color: #1e1e1e; border: 1px solid #333; border-radius: 8px; }
        .form-control { background-color: #121212; border: 1px solid #444; color: #fff; }
        .form-control:focus { background-color: #121212; color: #fff; border-color: #ffc107; box-shadow: none; }
        .btn-warning { background-color: #ffc107; border: none; font-weight: bold; }
        .nav-link { color: #ccc !important; font-weight: 500; }
        .nav-link:hover { color: #ffc107 !important; }
        .username { color: #ffc107; font-weight: bold; }
    </style>
</head>
<body>

    <!-- Top Navigation Bar -->
    <nav class="navbar navbar-expand px-4 py-2">
        <a class="navbar-brand fw-bold text-warning fs-4" href="#">⚡ ChaserConnect</a>
        <div class="navbar-nav ms-auto align-items-center gap-4">
            <a class="nav-link d-flex align-items-center gap-1" href="#">🏠 Feed</a>
            <a class="nav-link d-flex align-items-center gap-1" href="#">💬 Field Chat</a>
            <div class="d-flex align-items-center gap-2 text-white bg-dark px-3 py-1 rounded border border-secondary">
                <span class="username">mydadsrecipe</span>
            </div>
            <a href="#" class="btn btn-danger btn-sm px-3 fw-bold">Log Out</a>
        </div>
    </nav>

    <!-- Main Container -->
    <div class="container mt-4" style="max-width: 750px;">
        
        <!-- Create Post Box -->
        <div class="card p-3 mb-4 shadow">
            <div class="d-flex align-items-center gap-2 mb-3">
                <div class="bg-secondary rounded-circle d-flex align-items-center justify-content-center text-white fw-bold" style="width: 35px; height: 35px; font-size: 14px;">MR</div>
                <input type="text" class="form-control rounded-pill px-3" placeholder="What's happening in the field, mydadsrecipe?">
            </div>
            <div class="d-flex justify-content-between align-items-center">
                <div class="d-flex gap-2 w-75">
                    <input type="text" class="form-control form-control-sm" placeholder="📍 Location (e.g. Calera, AL)">
                    <input type="file" class="form-control form-control-sm text-muted">
                </div>
                <button class="btn btn-warning btn-sm px-4">Post</button>
            </div>
        </div>

        <!-- Field News Feed Header -->
        <h5 class="text-warning mb-3">Field News Feed</h5>

        <!-- Feed Item Card -->
        <div class="card p-4 mb-4 shadow">
            <div class="d-flex align-items-center gap-2 mb-2">
                <div class="bg-secondary rounded-circle d-flex align-items-center justify-content-center text-white fw-bold" style="width: 40px; height: 40px;">MR</div>
                <div>
                    <div class="username">mydadsrecipe</div>
                    <div class="text-muted" style="font-size: 12px;">📍 Chelsea, AL</div>
                </div>
            </div>
            
            <p class="mt-2 mb-3">TESTING 123</p>

            <!-- Embedded Image/Card Box -->
            <div class="bg-black p-3 rounded border border-secondary text-center mb-3">
                <span class="text-warning fw-bold">⚡ ChaserConnect</span>
                <div class="card p-3 my-2 bg-dark border-secondary mx-auto" style="max-width: 450px;">
                    <input type="text" class="form-control form-control-sm mb-2" value="" placeholder="Drop a Field Report">
                    <input type="text" class="form-control form-control-sm mb-2" placeholder="Location (e.g. Calera, AL, Sylacauga, AL)">
                    <textarea class="form-control form-control-sm mb-2" rows="2" placeholder="What are you seeing on radar or in the field?"></textarea>
                    <button class="btn btn-warning btn-sm w-100">Publish Report</button>
                </div>
                <div class="text-muted mt-2" style="font-size: 13px;">Active Chase Feed</div>
                <p class="text-muted" style="font-size: 12px;">No chase reports posted yet. Be the first to drop a report from the field!</p>
            </div>

            <!-- Like & Comment Stats -->
            <div class="d-flex justify-content-between text-muted border-top border-bottom border-secondary py-2 mb-3" style="font-size: 14px;">
                <span>⚡ 0 Chasers Liked This</span>
                <span>💬 2 Comments</span>
            </div>

            <!-- Like / Bolt Button -->
            <button class="btn btn-outline-warning w-100 mb-3 fw-bold btn-sm">⚡ Like / Bolt</button>

            <!-- Comments Section -->
            <div class="d-flex flex-column gap-2 mb-3">
                <div class="bg-black p-2 rounded border border-secondary px-3" style="font-size: 14px;">
                    <span class="username">mydadsrecipe:</span> <span class="text-light">SICK!</span>
                </div>
                <div class="bg-black p-2 rounded border border-secondary px-3" style="font-size: 14px;">
                    <span class="username">mydadsrecipe:</span> <span class="text-light">John is gay</span>
                </div>
            </div>

            <!-- Add Comment Input -->
            <div class="input-group">
                <input type="text" class="form-control form-control-sm" placeholder="Write a comment...">
                <button class="btn btn-outline-info btn-sm px-3">Reply</button>
            </div>
        </div>

    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
