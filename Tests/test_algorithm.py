import unittest
from algorithm import RoundRobinScheduler


class TestRoundRobinScheduler(unittest.TestCase):

    def test_single_process(self):
        scheduler = RoundRobinScheduler(
            num_processes=1, quantum=5, arrival_times=[0], burst_times=[10])
        result = scheduler.run_simulation()
        self.assertIn("Process 1 completed at time 10", result)
        self.assertIn("Average return time: 10.0", result)
        self.assertIn("Average wait time: 0.0", result)

    def test_multiple_processes(self):
        scheduler = RoundRobinScheduler(num_processes=3, quantum=4, arrival_times=[
                                        0, 1, 2], burst_times=[5, 9, 6])
        result = scheduler.run_simulation()
        self.assertIn("Process 1 completed at time 13", result)
        self.assertIn("Process 2 completed at time 18", result)
        self.assertIn("Process 3 completed at time 20", result)
        self.assertIn("Average return time: 15.666666666666666", result)
        self.assertIn("Average wait time: 7.666666666666667", result)

    def test_quantum_greater_than_burst(self):
        scheduler = RoundRobinScheduler(num_processes=2, quantum=10, arrival_times=[
                                        0, 2], burst_times=[6, 8])
        result = scheduler.run_simulation()
        self.assertIn("Process 1 completed at time 6", result)
        self.assertIn("Process 2 completed at time 14", result)
        self.assertIn("Average return time: 9.0", result)
        self.assertIn("Average wait time: 3.0", result)

    def test_all_processes_same_arrival(self):
        scheduler = RoundRobinScheduler(num_processes=3, quantum=3, arrival_times=[
                                        0, 0, 0], burst_times=[7, 4, 9])
        result = scheduler.run_simulation()
        self.assertIn("Process 1 completed at time 19", result)
        self.assertIn("Process 2 completed at time 10", result)
        self.assertIn("Process 3 completed at time 22", result)
        self.assertIn("Average return time: 17.0", result)
        self.assertIn("Average wait time: 10.666666666666666", result)

    def test_process_arrives_late(self):
        scheduler = RoundRobinScheduler(num_processes=3, quantum=4, arrival_times=[
                                        0, 5, 8], burst_times=[10, 5, 12])
        result = scheduler.run_simulation()
        self.assertIn("Process 1 completed at time 20", result)
        self.assertIn("Process 2 completed at time 25", result)
        self.assertIn("Process 3 completed at time 29", result)
        self.assertIn("Average return time: 22.666666666666668", result)
        self.assertIn("Average wait time: 13.666666666666666", result)


if __name__ == '__main__':
    unittest.main()
