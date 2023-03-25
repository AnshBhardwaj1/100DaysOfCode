import os
def clear(type):
    if type[0]==".":
        pass
    else:
        type='.'+type
    #print(os.getcwd())
    num=len(os.listdir('Project/Clear_the_clutter/Sorted'))
    all_files=os.listdir('Project/Clear_the_clutter/Clutter')
    count=0
    for file in all_files:
        num+=1
        count+=1
        if file[-len(type):]==type:
            os.rename(f'Project/Clear_the_clutter/Clutter/{file}',f"Project/Clear_the_clutter/Sorted/{num}{type}")
            try:
                print(f"{all_files[count]}has been converted to {num}{type}")
            except:
                print ("ALL FILES ARE DONE")
if __name__=="__main__":
    clear('pdf')