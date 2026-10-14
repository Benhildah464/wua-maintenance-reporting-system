import unittest
from unittest.mock import patch
from observer_pattern import MaintenanceStaff, MaintenanceSystem


class TestMaintenanceSystem(unittest.TestCase):

    def test_add_observer(self):
        system = MaintenanceSystem()
        staff = MaintenanceStaff()

        system.add_observer(staff)

        self.assertEqual(len(system.observers), 1)

    @patch("builtins.print")
    def test_submit_report(self, mock_print):
        system = MaintenanceSystem()
        staff = MaintenanceStaff()
        system.add_observer(staff)

        system.submit_report("Broken window in the classroom")

        self.assertTrue(
            any(
                "Report submitted: Broken window in the classroom"
                in str(call)
                for call in mock_print.call_args_list
            )
        )

        self.assertTrue(
            any(
                "Maintenance staff notified: Broken window in the classroom"
                in str(call)
                for call in mock_print.call_args_list
            )
        )

    @patch("builtins.print")
    def test_multiple_reports(self, mock_print):
        system = MaintenanceSystem()
        staff = MaintenanceStaff()
        system.add_observer(staff)

        system.submit_report("Broken window")
        system.submit_report("Faulty light")

        notifications = [
            call for call in mock_print.call_args_list
            if "Maintenance staff notified:" in str(call)
        ]

        self.assertEqual(len(notifications), 2)


if __name__ == "__main__":
    unittest.main()