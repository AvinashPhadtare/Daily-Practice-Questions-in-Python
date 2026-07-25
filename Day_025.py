class MemberRoster:
    def __init__(self):
        self.members = []

    def add(self, member_id, name, plan):
        member = {
            "id": member_id,
            "name": name,
            "plan": plan
        }
        self.members.append(member)

    def remove(self, name):
        for member in self.members:
            if member["name"] == name:
                self.members.remove(member)
                return
        raise ValueError("Member not found")

    def __len__(self):
        return len(self.members)

    def __contains__(self, name):
        for member in self.members:
            if member["name"] == name:
                return True
        return False

    def __iter__(self):
        return iter(self.members)

    def __getitem__(self, index):
        return self.members[index]


roster = MemberRoster()

roster.add(101, "Avinash", "Gold")
roster.add(102, "Rahul", "Basic")
roster.add(103, "Priya", "Premium")
roster.add(104, "Amit", "Gold")

for member in roster:
    print(member)

roster.remove("Rahul")

print(len(roster))