import List

class Bin:
  def __init__(self, id:int, location:str, part_id:str, qty_in_bin:int):
    self.id = id
    self.location = location
    self.part_id = part_id
    self.qty_in_bin = qty_in_bin

class Part:
  def __init__(self, id:int, name:str, quantity:int, bin_id: int):
    self.id = id
    self.name = name
    self.quantity = quantity
    self.bin_id = bin_id

class User:
  def __init__(self, email:str, student_num:int):
    self.email = email
    self.student_num = student_num

class Log:
  def __init__(self, time:str, user_id:int, part_id:int, quantity:int):
    self.time = time
    self.user_id = user_id
    self.part_id = part_id
    self.quantity = quantity

class InventoryManager:
  def __init__(self, parts:List[Part], bins:List[Bin], logs:List[Log], users:List[User]):
    self.parts = parts
    self.bins = bins
    self.logs = logs
    self.users = users
