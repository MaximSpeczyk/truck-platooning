import asyncio

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.t = 0
        self.state = "Following"

    async def run(self, leader):
        while True:
            if self.state == "Following" and leader.state == "changingLane":
                self.state = "changingLane"
                self.t = 0
            elif self.state == "changingLane":
                if self.t >= agentLaneChangeDuration:
                    self.state = "laneChanged"
                    self.t = 0
            elif self.state == "laneChanged" and leader.state == "Cruising":
                self.state = "Following"
                self.t = 0
            print(f"{self.name} is {self.state}")
            self.t += 1
            await asyncio.sleep(1)

class LeaderVehicle:
    def __init__(self):
        self.t = 0
        self.state = "Cruising"

    async def run(self):
        while True:
            if self.state == "Cruising":
                if self.t >= timeToChangeLane:
                    self.state = "changingLane"
                    self.t = 0
            elif self.state == "changingLane":
                if self.t >= laneChangeDuration:
                    self.state = "laneChanged"
                    self.t = 0
            elif self.state == "laneChanged":
                # Assume some condition here to return to "Cruising"
                self.state = "Cruising"
                self.t = 0
            print(f"Leader is {self.state}")
            self.t += 1
            await asyncio.sleep(1)

# Constants
N = 4
timeToChangeLane = 30
laneChangeDuration = 10
agentLaneChangeDuration = 12

# Create leader and vehicles
leader = LeaderVehicle()
vehicles = [Vehicle(f"Agent{i}") for i in range(1, N)]

# Run the simulation
async def main():
    await asyncio.gather(
        leader.run(),
        *[vehicle.run(leader) for vehicle in vehicles]
    )

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    loop.close()
