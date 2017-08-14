import glob, os
import sys



class fileFetcher():
	def exportFileLog(self, root_folder, dir_output, file_output):
		fileCount = 0
		dirCount = 0
		os.chdir(root_folder)

		open(dir_output,"w")
		open(file_output,"w")

		for root, dirs, files in os.walk(".", topdown=True):

			for directory in dirs:
				dirCount = dirCount + 1

			with open(dir_output,"a") as f:
				try:
					f.write(root + "\n")
				except:
					pass

			with open(file_output,"a") as f:
				for file in files:
					fileCount = fileCount + 1

					sys.stdout.flush()
					print(fileCount, end="\r")
					
					try:
						f.write(root + "/" + file + "\n")	
					except:
						pass
					
		print("%s files found" % (fileCount))
		print("%s directories found" % (dirCount))


if __name__ == '__main__':
	fileFetcher = fileFetcher()

	#root_dir_1 = "Y:/"
	#dir_log_1 = "C:/Users/MAB/Desktop/RealDania_document_comparer/directories1.txt"
	#file_log_1 = "C:/Users/MAB/Desktop/RealDania_document_comparer/files1.txt"

	#fileFetcher.exportFileLog(root_dir_1, dir_log_1, file_log_1)
	
	root_dir_2 = "https://arenacphx.sharepoint.com/Sdrev"
	dir_log_2 = "C:/Users/MAB/Desktop/RealDania_document_comparer/directories2.txt"
	file_log_2 = "C:/Users/MAB/Desktop/RealDania_document_comparer/files2.txt"

	fileFetcher.exportFileLog(root_dir_2, dir_log_2, file_log_2)

