student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

def grades_for_students(dict, new_dict):

    for student in dict:
      if dict[student] >= 91:
        new_dict[student]= "Outstanding"
      elif dict[student] >= 81:
        new_dict[student]= "Exceeds Expectations"
      elif dict[student]>= 71 :
        new_dict[student]= "Acceptable"
      elif dict[student] <= 70:
        new_dict[student]= "Fail"


grades_for_students(student_scores, student_grades)
print(student_grades)