import asyncio
from collections import deque

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.state = "idle"

    async def run(self, leader):
        while True:
            # Wait for the leader to have enough history
            if len(leader.history) > delay:
                self.state = leader.history.popleft()
            print(f"{self.name} is {self.state}")
            await asyncio.sleep(1)

class LeaderVehicle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.history = deque()  # Store state history of leader so agent can do the same

    async def run(self):
        while True:
            if self.state == "idle":
                self.state = "turnLeft"
            elif self.state == "turnLeft":
                self.state = "turnRight"
            elif self.state == "turnRight":
                self.state = "idle"

            self.history.append(self.state)
            print(f"{self.name} is {self.state}")
            await asyncio.sleep(1)

# Create leader and vehicles
leader = LeaderVehicle("Master")
follower = Vehicle("Slave")

# Set delay
delay = 2

# Run the simulation
async def main():
    await asyncio.gather(
        leader.run(),
        follower.run(leader)
    )

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    loop.close()
