# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        count = 0

        for i in range(k):
            if street.isDoorOpen():
                street.closeDoor()

            street.moveRight()

        street.openDoor()
        count = 0
        street.moveRight()

        while not street.isDoorOpen():
            count+=1
            street.moveRight()

        return count + 1
