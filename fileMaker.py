# to easily switch
sushkov = True

if sushkov:
    read_file = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/all.dta', 'r')
    index_file = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/all.idx', 'r')
    '''file1 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data1.txt', 'w')
    file2 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data2.txt', 'w')
    file3 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data3.txt', 'w')
    file4 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data4.txt', 'w')
    file5 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data5.txt', 'w')
    file123 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data123.txt', 'w')
    file1234 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data1234.txt', 'w')'''
    file123_86of4 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data123_86%of4.txt', 'w')
    file_7of4_1 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data_7%of4(valid).txt', 'w')
    file_7of4_2 = open('/home/msushkov/Dropbox/Caltech/Caltech Classes/CS/CS 156b/data/mu/data_7%of4(aggr).txt', 'w')
else:
    read_file = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\\all.dta', 'r')
    index_file = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\\all.idx', 'r')
    file1 = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\data1.txt', 'w')
    file2 = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\data2.txt', 'w')
    file3 = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\data3.txt', 'w')
    file4 = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\data4.txt', 'w')
    file5 = open('C:\Users\Mike\Documents\Mike\Caltech\\aJunior Fall\CS 156b\um\data5.txt', 'w')

indices = index_file.readlines()

count = 0

for i, line in enumerate(read_file):
    '''if int(indices[i]) == 1:
        file1.write(line)
        file123.write(line)
        file1234.write(line)
    elif int(indices[i]) == 2:
        file2.write(line)
        file123.write(line)
        file1234.write(line)
    elif int(indices[i]) == 3:
        file3.write(line)
        file123.write(line)
        file1234.write(line)'''
    if int(indices[i]) == 4:
        #file4.write(line)
        #file1234.write(line)
        
        # write 86% of data4 into this file, as well as 123
        if count < 1182275:
            file123_86of4.write(line)
            count += 1
        elif count >= 1182275 and count < 1278506:
            file_7of4_1.write(line)
            count += 1
        else:
            file_7of4_2.write(line)
            count += 1
    '''elif int(indices[i]) == 5:
        file5.write(line)'''
        
read_file.close()
index_file.close()
'''file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file123.close()
file1234.close()'''
file123_86of4.close()
file_7of4_1.close()
file_7of4_2.close()
