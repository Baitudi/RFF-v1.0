from feedback.rff_logger import log_decision

# Simulate a test log entry
log_decision(
    chart_id="Chart4",
    decision="UP",
    confidence=91.2,
    trail_snapshot=[(1000, 650), (1010, 655), (1020, 660)],
    outcome="success"
)

print("Test decision log has been created in 'rff_logs/'.")
