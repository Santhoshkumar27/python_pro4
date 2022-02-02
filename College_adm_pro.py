
import csv

def college_w_csv(stu_list):
    with open("students_info.csv",'a',newline='') as csv_file:
        
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["stu_id","Name","Age","Contact_Number","E-mail_ID"])
        writer.writerow(stu_list)
def college_r_csv():
    with open("students_info.csv",'r',newline='') as csv_file:
        
        read = csv.reader(csv_file)
        for x in read:
            print(x)

        #if csv_file.tell()==0:
        #    reader.readline(["stu_id","Name","Age","Contact_Number","E-mail_ID"])
       # .writerow(stu_list) #       

if __name__ =='__main__':
    
    condition =True
    student_num =1

    while(condition):
        student_info = input("Enter student #{} information (stu_id Name Age Contact_Number E-mail_ID):".format(student_num))
        student_info_list = student_info.split(' ')
        print("\n The entered information is -\nstu_id: {} \nName:{}\nAge: {} \nContact_number: {}\nE-mail_id: {}"
                .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))

        cc_check = input("The ABOVE Entered Information is correct  ?(yes/no):")

        if cc_check=="yes":
            college_w_csv(student_info_list)
            con_check =input("Enter another student info (yes/no) :=")
            if con_check == "yes":
                condition=True
                student_num=student-num+1
            elif con_check =="no":
                
                condition =False
        elif cc_check == "no":
            print("\nPlease re-enter the values!")
            
    cond_check =input("Do you want to  Read student info (yes/no) :=")
    if cond_check == "yes":
        college_r_csv()
                
               
    elif cond_check =="no":
        print("THANK YOU")
