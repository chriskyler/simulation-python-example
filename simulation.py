def main():
  # Setup
  random.seed(42)
  num_cashiers, num_servers, num_ushers = get_user_input()

  # Run the simulation
  env = simpy.Environment()
  env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
  env.run(until=90)

  # View the results
  mins, secs = get_average_wait_time(wait_times)
  print(
      "Running simulation...",
      f"\nThe average wait time is {mins} minutes and {secs} seconds.",
  )
