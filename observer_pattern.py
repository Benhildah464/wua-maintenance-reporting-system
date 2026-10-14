class MaintenanceStaff:
    def update(self, report):
        print(f"Maintenance staff notified: {report}")


class MaintenanceSystem:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def submit_report(self, report):
        print(f"Report submitted: {report}")
        self.notify_observers(report)

    def notify_observers(self, report):
        for observer in self.observers:
            observer.update(report)


# Create the maintenance system and staff member
system = MaintenanceSystem()
staff = MaintenanceStaff()

# Register the staff member to receive notifications
system.add_observer(staff)

# Submit maintenance reports
system.submit_report("Leaking tap in the hostel")
system.submit_report("Broken window in the classroom")
system.submit_report("Faulty light in the library")
