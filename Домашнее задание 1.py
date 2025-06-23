def total_salary(path):
    try:
        with open (path,"r", encoding="utf-8")as file: 
            lines=file.readlines()
        
        total= 0
        count = 0


        for line in lines:
            parts = line.strip().split(",")
            if len(parts)==2:
                try:
                    salary=int(parts[1])
                    total+=salary
                    count+=1
                except ValueError:
                    continue
        if count==0:
            return 0,0
        averange = total//count
        return total, averange
    except FileNotFoundError:
        print("Файл не знайдено")
        return 0,0
    
#check 

if __name__=="__main__":
    total,average = total_salary("salary.txt")
    print(f"Total salary : {total}, Midle salary: {average}")