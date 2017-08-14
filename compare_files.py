class fileComparer():
    def compareFiles(self, file_path_1, file_path_2, output_file_name='compare_log.txt'):
        # compare file logs
        with open(file_path_1, 'r',encoding='utf-8', errors='ignore') as file1:
            with open(file_path_2, 'r',encoding='utf-8', errors='ignore') as file2:
                same = set(file1).difference(file2)

        same.discard('\n')

        with open(output_file_name, 'w') as file_out:
            for line in same:
                file_out.write(line)

        comparedFile = open(output_file_name, 'r')
        lines = comparedFile.readlines()
        lines.sort()

        with open(output_file_name, 'w') as file_out:
        	for line in lines:
        		file_out.write(str(line))
        print("done comparing files. Saved log to %s" % (output_file_name))


if __name__ == '__main__':
    filePath1 = "/Users/martinmeincke/development/python_document_comparer/files1.txt"
    filePath2 = "/Users/martinmeincke/development/python_document_comparer/files2.txt"

    file_path_filtered_1 = "/Users/martinmeincke/development/python_document_comparer/docs/illegal_extension_lines_file_1.txt"
    file_path_filtered_2 = "/Users/martinmeincke/development/python_document_comparer/docs/illegal_extension_lines_file_2.txt"

    dirPath1 = "/Users/martinmeincke/development/python_document_comparer/directories1.txt"
    dirPath2 = "/Users/martinmeincke/development/python_document_comparer/directories2.txt"
    fileComparer = fileComparer()

    fileComparer.compareFiles(file_path_filtered_1, file_path_filtered_2, 'compare_file_filtered_log.txt')
    #fileComparer.compareFiles(filePath1, filePath2, 'compare_file_log.txt')
    #fileComparer.compareFiles(dirPath1, dirPath2, 'compare_dir_log.txt')
