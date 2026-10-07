def evaluate(vehicles, signal="RED"):
    violations=[]
    vehicle_present=bool(vehicles)
    motorcycles=[v for v in vehicles if v["class_name"]=="motorcycle"]

    if vehicle_present and signal.upper()=="RED":
        violations.append("Signal Jump")

    # Preserve the original project's heuristic, but make it explicit.
    # A dedicated helmet model should be added before calling this a confirmed helmet violation.
    if motorcycles:
        violations.append("Possible No Helmet")

    return violations or ["No Violation"]
