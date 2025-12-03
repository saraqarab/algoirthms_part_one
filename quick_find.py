class QuickFind:
    def __init__(self, n):
        # Each element starts in its own group
        self.id = list(range(n))
        print(f"original {self.id}")

    def connected(self, p, q):
        connected = self.id[p] == self.id[q]
        print(f"Connected({p}, {q})? {'Yes' if connected else 'No'}")
        return connected

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        changed = []

        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid
                changed.append(i)

        print(f"Union({p},{q}) changed elements: {changed}")
        print(f"Current state: {self.id}\n")

# --- Interactive Demo ---
uf = QuickFind(6)

# Example commands
commands = [
    ("union", 0, 1),
    ("union", 2, 3),
    ("union", 1, 2),
    ("connected", 0, 3),
    ("union", 4, 5),
    ("connected", 0, 5),
]

for cmd in commands:
    if cmd[0] == "union":
        uf.union(cmd[1], cmd[2])
    elif cmd[0] == "connected":
        uf.connected(cmd[1], cmd[2])

# You can now call:
# uf.union(p, q)
# uf.connected(p, q)
# And it will print exactly which elements changed and current state
