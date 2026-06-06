from datetime import datetime

class AttendanceTracker:
    def __init__(self):
        self._date = None
        self.records = []
    
    @property
    def current_date(self):
        return self._date
    
    @current_date.setter
    def current_date(self, new_date):
        try:
            datetime.strptime(new_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Invalid date format: {new_date}. Use YYYY-MM-DD")
        self._date = new_date

    def add_record(self, member_id, status):
        record = {
            'member_id': member_id,
            'status': status,
            'date': self.current_date
            }           
        self.records.append(record)

    def summary(self, member_id):
        present = 0
        absent = 0
        for record in self.records:
            if record['member_id'] == member_id:
                if record['status'] == 'present':
                    present += 1
                elif record['status'] == 'absent':
                    absent += 1

        total = present + absent
        if total > 0:
            attendance_percentage = (present / total) * 100
        else:
            attendance_percentage = 0.0

        return {
            'member_id': member_id,
            'present': present,
            'absent': absent,
            'attendance_percentage': attendance_percentage
        }
    

# Example usage
tracker = AttendanceTracker()

tracker.current_date = '2024-06-01'

tracker.add_record('member1', 'present')        
tracker.add_record('member1', 'absent')
tracker.add_record('member2', 'present')
tracker.add_record('member2', 'present')


print(tracker.summary('member1'))
print(tracker.summary('member2'))

