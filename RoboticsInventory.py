import List

class Bin:
  def __init__(self, id:int, location:str, part_id:str, qty_in_bin:int):
    self._id = id
    self._location = location
    self._part_id = part_id
    self._qty_in_bin = qty_in_bin
   
  def get_id(self):
    return self._id
  
  def set_id(self,value:int):
    assert type(value) is int, "The id must be an integer."
    self._id = value
  
  def get_location(self):
    return self._location
  
  def set_location(self,value:str):
    assert type(value) is str, "The location must be a string."
    self._location = value

  def get_part_id(self):
    return self._part_id
  
  def set_part_id(self,value:str):
    assert type(value) is str, "The part id must be a string."
    self._part_id = value
    
  def get_qty_in_bin(self):
    return self._qty_in_bin
  
  def set_qty_in_bin(self,value:int):
    assert type(value) is int, "The quantity in the bin must be an integer."
    assert value>=0, "The quantity in the bin must be 0 or more".
    self._qty_in_bin = value
    
class Part:
  def __init__(self, id:int, name:str, quantity:int, bin_id: int):
    self._id = id
    self._name = name
    self._quantity = quantity
    self._bin_id = bin_id
    
  def get_id(self):
    return self._id
  
  def set_id(self,value:int):
    assert type(value) is int, "The id must be an integer."
    self._id = value
    
  def get_name(self):
    return self._name
  
  def set_name(self,value:str):
    assert type(value) is str, "The part name must be a string."
    self._name = value
    
  def get_quantity(self):
    return self._quantity
  
  def set_quantity(self,value:int):
    assert type(value) is int, "The part quantity must be an integer."
    assert value>=0, "The quantity must be 0 or more."
    self._quantity = value
   
  def get_bin_id(self):
    return self._bin_id
  
  def set_bin_id(self,value:int):
    assert type(value) is int, "The bin id must be an integer."
    self._bin_id = value

class User:
  def __init__(self, email:str, student_num:int):
    self._email = email
    self._student_num = student_num
    
  def get_email(self):
    return self._email
  
  def set_email(self, value:str):
    assert type(value) is str, "The user's email must be a string."
    self._email = value

  def get_student_num(self):
    return self._student_num
  
  def set_student_num(self,value:int):
    assert type(value) is int, "The user's student number must be an integer."
    self._student_num = value
    
class Log:
  def __init__(self, time:str, user_id:int, part_id:int, quantity:int):
    self._time = time
    self._user_id = user_id
    self._part_id = part_id
    self._quantity = quantity
    
  def get_time(self):
    return self._time
  
  def set_time(self, value:str):
    assert type(value) is str, "The log time must be a string."
    self._time = value

  def get_user_id(self):
    return self._user_id
  
  def set_user_id(self,value:int):
    assert type(value) is int, "The user id must be an integer."
    self._user_id = value

  def get_part_id(self):
    return self._part_id
  
  def set_part_id(self,value:int):
    assert type(value) is int, "The part id must be an integer."
    self._part_id = value
    
  def get_quantity(self):
    return self._quantity
  
  def set_quantity(self,value:int):
    assert type(value) is int, "The quantity must be an integer."
    assert value>=0, "The quantity must be 0 or more."
    self._quantity = value
    
class InventoryManager:
  def __init__(self, parts:List[Part], bins:List[Bin], logs:List[Log], users:List[User]):
    self.parts = parts
    self.bins = bins
    self.logs = logs
    self.users = users
