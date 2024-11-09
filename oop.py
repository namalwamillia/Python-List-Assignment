#start by creating a classes
#Cohort class

    
#Assignment
# add a constructor for thr cohort class
#add a method to the class that prints the cohort name and the total number of students
#create a new instance of the cohort class
    
class Cohort:
# a constructor to initialize cohort name and students count
    def __init__(self, name, num_students):
        self.name = name
        self.num_students = num_students
     
#method to print cohort name and number of students   
        
    def print_Cohort_info(self):
        print(f" Cohort name : {self.name}")
        print(f"Total number of students :{self.num_students}")
        
my_cohort = Cohort("Cohort3",25)  
    
#calling the method to print cohort information
my_cohort.print_Cohort_info()
        
       
