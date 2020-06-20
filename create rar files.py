import shutil

for i in range(250): shutil.copy("c:/teste/zips/vvv.zip", "c:/teste/zips/vvv" + str(i + 1) + ".zip")
