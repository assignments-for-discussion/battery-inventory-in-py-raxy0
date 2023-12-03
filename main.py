
def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  #to calculate the soh percentage
  for capacity in present_capacities:
        rated_capacity = 120  
        soh_percentage = (capacity / rated_capacity) * 100
        #condition to classify the health of soh percentage
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
  
  print(f"Healthy batteries: {counts['healthy']}")
  print(f"Exchange batteries: {counts['exchange']}")
  print(f"Failed batteries: {counts['failed']}")
  
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
