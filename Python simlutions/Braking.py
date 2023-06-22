import asyncio

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.state = "Following"

    async def run(self, leader):
        while True:
            if self.state == "Following" and leader.state == "Braking":
                self.state = "Braking"
            elif self.state == "Braking" and leader.state == "Cruising":
                self.state = "Following"
            print(f"{self.name} is {self.state}")
            await asyncio.sleep(1)

class LeaderVehicle:
    def __init__(self):
        self.state = "Cruising"
        self.t = 0

    async def run(self):
        while True:
            if self.state == "Cruising":
                if self.t >= timeToBrake:
                    self.state = "Braking"
                    self.t = 0
            elif self.state == "Braking":
                if self.t >= brakingDuration:
                    self.state = "Cruising"
                    self.t = 0
            print(f"Leader is {self.state}")
            self.t += 1
            await asyncio.sleep(1)

# Constants
N = 4
timeToBrake = 15
brakingDuration = 5

# Create leader and vehicles
leader = LeaderVehicle()
vehicles = [Vehicle(f"Agent{i}") for i in range(1, N+1)]

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
