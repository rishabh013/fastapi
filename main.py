from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulated dashboards
DASHBOARDS = {
    1: {"name": "Customer Retention", "data": {"customers": 100, "churn_rate": 5}},
    2: {"name": "Sales Overview", "data": {"sales": 50000, "growth": 10}},
    3: {"name": "Traffic Insights", "data": {"visits": 12000, "bounce_rate": 35}},
    4: {"name": "Finance Metrics", "data": {"revenue": 250000, "profit": 50000}},
    5: {"name": "Product Performance", "data": {"products": 200, "avg_rating": 4.3}},
}

# Store currently selected dashboard
CURRENT_DASHBOARD = {"id": None}


@app.get("/dashboards")
def list_dashboards():
    """List all available dashboards"""
    return DASHBOARDS


@app.post("/dashboard/{dashboard_id}")
def select_dashboard(dashboard_id: int):
    """Select a dashboard"""
    if dashboard_id not in DASHBOARDS:
        raise HTTPException(status_code=404, detail="Dashboard not found")
    CURRENT_DASHBOARD["id"] = dashboard_id
    return {"message": f"Dashboard '{DASHBOARDS[dashboard_id]['name']}' selected"}


@app.get("/dashboard/current")
def get_selected_dashboard():
    """Get currently selected dashboard"""
    dashboard_id = CURRENT_DASHBOARD["id"]
    if not dashboard_id:
        return {"message": "No dashboard selected yet"}
    return DASHBOARDS[dashboard_id]


@app.put("/dashboard/update")
def update_dashboard(data: dict):
    """Update data in the currently selected dashboard"""
    dashboard_id = CURRENT_DASHBOARD["id"]
    if not dashboard_id:
        raise HTTPException(status_code=400, detail="No dashboard selected")

    DASHBOARDS[dashboard_id]["data"].update(data)
    return {
        "message": f"{DASHBOARDS[dashboard_id]['name']} updated successfully",
        "data": DASHBOARDS[dashboard_id]["data"],
    }


##### problem statement #####
# Step 1: GET /dashboards → list all dashboards
# Step 2: POST /dashboard/2 → select “Sales Overview” dashboard
# Step 3: GET /dashboard/current → shows currently selected dashboard data
# Step 4: PUT /dashboard/update → update data in selected dashboard