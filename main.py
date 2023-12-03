def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }
    
    for capacity in present_capacities:
        rated_capacity = 120  
        soh_percentage = (capacity / rated_capacity) * 100
        
        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1
    
    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    
    # Print counts for each category
    print(f"Healthy batteries: {counts['healthy']}")
    print(f"Exchange batteries: {counts['exchange']}")
    print(f"Failed batteries: {counts['failed']}")
    
    # Assertions to ensure counts match expected values
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")

    present_capacities1 = [113, 116, 80, 95, 92, 70, 120, 0, 60, 48, 121]
    
    counts = classify_batteries(present_capacities1)
    
    # Print counts for each category
    print(f"Healthy batteries: {counts['healthy']}")
    print(f"Exchange batteries: {counts['exchange']}")
    print(f"Failed batteries: {counts['failed']}")
    
    # Assertions for expected counts
    assert counts["healthy"] == 3  # Including 120 Ah, 113 Ah, and 116 Ah
    assert counts["exchange"] == 5  # Including 80 Ah, 95 Ah, 92 Ah, 70 Ah, and 60 Ah
    assert counts["failed"] == 3  # Including 0 Ah, 48 Ah, and 121 Ah
    print("Done counting :)")
    
    # Additional test cases
    # Test with an empty list
    empty_list_counts = classify_batteries([])
    assert empty_list_counts["healthy"] == 0
    assert empty_list_counts["exchange"] == 0
    assert empty_list_counts["failed"] == 0
    print("Done counting :)")
    
    # Test with a single battery near the threshold for each category
    single_battery_counts = classify_batteries([79, 81, 61])
    assert single_battery_counts["healthy"] == 1
    assert single_battery_counts["exchange"] == 1
    assert single_battery_counts["failed"] == 1
    print("Done counting :)")
    
    # Test with various capacities of fully healthy batteries
    fully_healthy_counts = classify_batteries([120, 119, 118, 117])
    assert fully_healthy_counts["healthy"] == 4
    assert fully_healthy_counts["exchange"] == 0
    assert fully_healthy_counts["failed"] == 0
    print("Done counting :)")
    


if __name__ == '__main__':
    test_bucketing_by_health()
