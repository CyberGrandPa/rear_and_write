

from pathlib import Path   
         
def txt_file_analysis(file_names):
    file_path = Path(__file__).parent.absolute()
    file_names = ('1.txt', '2.txt', '3.txt')
    files_all = []
    for file_name in file_names:
        with open(f"{file_path}/{file_name}", 'rt', encoding='UTF-8') as txt_file:
            text = txt_file.readlines()
            len_ = len(text)
            info_file = [len_,file_name, text]
            files_all.append(info_file)
            
    print(files_all)        
  
    
    with open(r'home_work\read_and_write_in_file\Cook_Book\result.txt', 'w', encoding='utf-8') as f:
        for output in sorted(files_all):
             f.write(f'{output[1]} \n{output[0]} \n{" ".join(output[2])} \n')
             f.write(f'\n')
             
                       
file_names = ('1.txt', '2.txt', '3.txt')        
txt_file_analysis(file_names)         

