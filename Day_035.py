# ========================= Question ========================
# Build an UndoableGymLog that records member actions with full undo support.
#
# Actions are strings like:
# "member:1:checked_in"
# "member:2:plan_upgraded"
#
# Requirements:
# • record(action: str) -> log the action
# • undo() -> str
#     Undo the last action and return what was undone.
#     If nothing to undo, return "Nothing to undo"
# • redo() -> str
#     Redo the last undone action.
#     (Use TWO stacks.)
#     If nothing to redo, return "Nothing to redo"
# • history() -> list
#     Return the current log in order.
#
# Simulate:
# • Record 4 actions
# • Undo 2 actions
# • Redo 1 action
# • Print history.
# ==============================================================



# Solution:- 
class UndoableGymLog:
    def __init__(self):
        self.actions = []
        self.undo_stack = []

    def record(self, action):
        self.actions.append(action)
        self.undo_stack.clear()

    def undo(self):
        if not self.actions:
            return "Nothing to undo"

        action = self.actions.pop()
        self.undo_stack.append(action)
        return action

    def redo(self):
        if not self.undo_stack:
            return "Nothing to redo"

        action = self.undo_stack.pop()
        self.actions.append(action)
        return action

    def history(self):
        return self.actions.copy()


# Example usage:-
# Simulation:-
log = UndoableGymLog()

log.record("member:1:checked_in")
log.record("member:2:plan_upgraded")
log.record("member:3:workout_started")
log.record("member:4:checked_out")

print(log.undo())
print(log.undo())

print(log.redo())

print(log.history())
