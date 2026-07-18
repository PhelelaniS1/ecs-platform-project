from flask import Flask, render_template_string
import os
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Platform Status</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: "Segoe UI", sans-serif; background: #0f1117; color: #e2e8f0; min-height: 100vh; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { margin-bottom: 40px; }
        .header h1 { font-size: 28px; font-weight: 600; color: #fff; }
        .header p { color: #94a3b8; margin-top: 6px; font-size: 14px; }
        .badge { display: inline-block; background: #22c55e22; color: #22c55e; border: 1px solid #22c55e44; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 500; margin-bottom: 16px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px; }
        .card { background: #1e2130; border: 1px solid #2d3148; border-radius: 10px; padding: 20px; }
        .card h3 { font-size: 13px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
        .card p { font-size: 22px; font-weight: 600; color: #fff; }
        .card .sub { font-size: 12px; color: #64748b; margin-top: 4px; }
        .services { background: #1e2130; border: 1px solid #2d3148; border-radius: 10px; padding: 20px; }
        .services h2 { font-size: 15px; font-weight: 600; margin-bottom: 16px; color: #fff; }
        .service-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #2d3148; }
        .service-row:last-child { border-bottom: none; }
        .service-name { font-size: 14px; color: #e2e8f0; }
        .service-meta { font-size: 12px; color: #64748b; margin-top: 2px; }
        .status-dot { width: 8px; height: 8px; border-radius: 50%; background: #22c55e; box-shadow: 0 0 6px #22c55e; display: inline-block; margin-right: 6px; }
        .status-ok { color: #22c55e; font-size: 13px; }
        .footer { margin-top: 24px; text-align: center; font-size: 12px; color: #475569; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="badge">● All Systems Operational</div>
            <h1>Platform Status Dashboard</h1>
            <p>Internal Developer Platform — AWS ECS · Terraform · GitHub Actions</p>
        </div>
        <div class="grid">
            <div class="card"><h3>Environment</h3><p>{{ environment }}</p><div class="sub">Active deployment</div></div>
            <div class="card"><h3>Region</h3><p>{{ region }}</p><div class="sub">AWS Region</div></div>
            <div class="card"><h3>Container</h3><p>{{ hostname }}</p><div class="sub">ECS Task hostname</div></div>
            <div class="card"><h3>Last Checked</h3><p style="font-size:16px;">{{ timestamp }}</p><div class="sub">Server time (UTC)</div></div>
        </div>
        <div class="services">
            <h2>Services</h2>
            <div class="service-row"><div><div class="service-name">Application Load Balancer</div><div class="service-meta">Routing traffic to ECS tasks</div></div><span class="status-ok"><span class="status-dot"></span>Healthy</span></div>
            <div class="service-row"><div><div class="service-name">ECS Service</div><div class="service-meta">Fargate · 1/1 tasks running</div></div><span class="status-ok"><span class="status-dot"></span>Healthy</span></div>
            <div class="service-row"><div><div class="service-name">ECR Image Registry</div><div class="service-meta">Container image storage</div></div><span class="status-ok"><span class="status-dot"></span>Healthy</span></div>
            <div class="service-row"><div><div class="service-name">CI/CD Pipeline</div><div class="service-meta">GitHub Actions · Auto-deploy on push</div></div><span class="status-ok"><span class="status-dot"></span>Healthy</span></div>
        </div>
        <div class="footer">Built by Phelelani Sithole · Platform Engineering Project · AWS ECS + Terraform + GitHub Actions</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML,
        environment=os.environ.get("ENVIRONMENT", "production"),
        region=os.environ.get("AWS_REGION", "us-east-1"),
        hostname=os.environ.get("HOSTNAME", "local"),
        timestamp=datetime.datetime.utcnow().strftime("%H:%M:%S UTC")
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
