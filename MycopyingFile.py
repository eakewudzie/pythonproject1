import shutil

# he shutil model
# copyfile() = copies contents of a file
# copy() =     copyfile() + permission mode + desination can be a directory
# copy2() =    copy() + copies metadata(file's creation and modification times)


shutil.copyfile('test.txt','copiedFile.txt') #source,destination

# desination can be specified to be on desktop or anywhere on your machine...so long as you have the path right
