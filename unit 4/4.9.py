#Write a program to read and write data into a file using different file modes.


with open('mdata.txt','w') as f:
    f.write('yuvrajsinh')
    
with open('mdata.txt','r') as f1:
    print(f1.read())
    
