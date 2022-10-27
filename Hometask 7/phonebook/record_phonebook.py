


def rec_data(name_file, data: dict):
    with open (name_file, 'a', encoding='utf-8' ) as pb_file:
        for key,val in data.items():
            pb_file.write('{}:{}\n'.format(key,val))
        
        
        

        
        
       

    
        
       
    
       