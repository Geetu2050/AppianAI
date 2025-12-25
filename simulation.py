import numpy as np

def simulate_stage(arrival_rate, service_rate, agents, current_queue, hours=4, runs=1000):
    """
    Monte Carlo simulation to estimate SLA breach probability
    """
    sla_limit = hours
    breach_count = 0
    wait_times = []

    for _ in range(runs):
        arrivals = np.random.poisson(arrival_rate * hours)
        capacity = service_rate * agents * hours
        final_queue = max(0, current_queue + arrivals - capacity)
        wait_time = final_queue / (service_rate * agents + 1e-6)
        wait_times.append(wait_time)

        if wait_time > sla_limit:
            breach_count += 1

    return {
        "avg_wait_time": round(np.mean(wait_times), 2),
        "breach_probability": round((breach_count / runs) * 100, 2)
    }


def simulate_workflow(params):
    results = {}

    for stage, values in params.items():
        results[stage] = simulate_stage(
            arrival_rate=values["arrival_rate"],
            service_rate=values["service_rate"],
            agents=values["agents"],
            current_queue=values["queue"]
        )

    return results
