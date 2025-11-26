class Aadhar:

   def __init__(self,name,aadhar_number,dob,finger_print,retina):
       self.name=name
       self.aadhar_number=aadhar_number
       self.dob=dob
       self._finger_print=finger_print
       self.__retina=retina

   def display_userData(self):
       print(f"finger_print:{self._finger_print}\n retina: {self.__retina}")

   def getRetina(self):
       return self.__retina


var=Aadhar("Shruti",457899,"12-jan-2003", "sdfghjkl","ertyui")
var.display_userData()
retina_var=var.getRetina()
print(retina_var)