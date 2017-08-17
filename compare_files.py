from file_filter import FileFilter

class fileComparer():

    def compareFiles(self, file_path_1, file_path_2, output_file):
        outputSlash1 = "./docs/files1NoSlashes.txt"
        self.convertFileSlashes(file_path_1, outputSlash1)
        outIllegalCharacters_1 = "./docs/files1NoIllegalCharacters.txt"
        self.convertIllegalCharacter(["%","#"],"_", outputSlash1, outIllegalCharacters_1)
        outIllegalCharacters_2 = "./docs/files1NoIllegalCharacters1.txt"
        self.convertIllegalCharacter(["\\."],"\\_", outIllegalCharacters_1, outIllegalCharacters_2)
        outIllegalCharacters_3 = "./docs/files1NoIllegalCharacters3.txt"
        self.convertIllegalCharacter(["...."],"_._.", outIllegalCharacters_2, outIllegalCharacters_3)
        outIllegalCharacters_4 = "./docs/files1NoIllegalCharacters4.txt"
        self.convertIllegalCharacter(["..."],"__.", outIllegalCharacters_3, outIllegalCharacters_4)
        outIllegalCharacters_5 = "./docs/files1NoIllegalCharacters5.txt"
        self.convertIllegalCharacter([".."],"_.", outIllegalCharacters_4, outIllegalCharacters_5)

        outputSlash2 = "./docs/files2NoSlashes.txt"
        self.convertFileSlashes(file_path_2, outputSlash2)

        output_filter_1_excluded = 'docs/excluded_extensions_file_1.txt'
        output_filter_1_included = 'docs/excluding_illegal_extension_file_1.txt'
        FileFilter.filterExtensions(self, outIllegalCharacters_5, ['Thumbs.db'], output_filter_1_excluded, output_filter_1_included)

        output_filter_2_excluded = 'docs/excluded_extensions_file_2.txt'
        output_filter_2_included = 'docs/excluding_illegal_extension_file_2.txt'
        FileFilter.filterExtensions(self, outputSlash2, ['Thumbs.db'], output_filter_2_excluded, output_filter_2_included)

        output_filter_characters_1_excluded = 'docs/excluded_characters_file_1.txt'
        output_filter_characters_1_excluding = 'docs/excluding_characters_file_1.txt'
        #FileFilter.filterIllegalCharacter(output_filter_1_included, ['%'])

        output_file_diff_1_2 = "./docs/file_diff_1_2.txt"
        self.fileDiff(output_filter_1_included, output_filter_2_included, output_file_diff_1_2)

        output_file_diff_2_1 = "./docs/file_diff_2_1.txt"
        self.fileDiff(output_filter_2_included, output_filter_1_included, output_file_diff_2_1)

        output_illegal_excluded = "./docs/filtered_final_excluded_1_2.txt"
        output_illegal_including = "./docs/filtered_final_including_1_2.txt"
        FileFilter.filterIllegalCharacter(self, output_file_diff_1_2, ['~$'], output_illegal_excluded, output_illegal_including)

    def fileDiff(self, file_path_1, file_path_2, output_file_name):
        # compare file logs
        with open(file_path_1, 'r',encoding='iso-8859-1', errors='ignore') as file1:
            with open(file_path_2, 'r',encoding='iso-8859-1', errors='ignore') as file2:
                same = set(file1).difference(file2)

        same.discard('\n')

        with open(output_file_name, 'w',encoding='iso-8859-1', errors='ignore') as file_out:
            for line in same:
                file_out.write(line)

        comparedFile = open(output_file_name, 'r',encoding='iso-8859-1', errors='ignore')
        lines = comparedFile.readlines()
        lines.sort()

        with open(output_file_name, 'w',encoding='iso-8859-1', errors='ignore') as file_out:
        	for line in lines:
        		file_out.write(str(line))
        print("done comparing files. Saved log to %s" % (output_file_name))

    def convertFileSlashes(self, file_path_1, output_file_path_1):
        with open(file_path_1, 'r',encoding='iso-8859-1', errors='ignore') as file_in:
            with open(output_file_path_1, 'w', encoding='iso-8859-1', errors='ignore') as file_out:
                for line in file_in:
                    file_out.write(line.replace("\\","/"))

    def convertIllegalCharacter(self, characters, output_character, file_path, output_file_path):
        with open(file_path, 'r',encoding='iso-8859-1', errors='ignore') as file_in:
            with open(output_file_path, 'w', encoding='iso-8859-1', errors='ignore') as file_out:
                for line in file_in:
                    modified_line = line
                    for character in characters:
                        modified_line = modified_line.replace(character,output_character)
                    file_out.write(modified_line)

    def findMissingFiles(self, file_path_1, file_path_2):


        with open(file_path_1, 'r',encoding='iso-8859-1', errors='ignore') as file1:
            for line in file1:
                split_line = line.split('\\')
                if len(split_line) > 2:
                    print(split_line[1])

        #print("file1: %s, file2: %s " % (sum1, sum2))


if __name__ == '__main__':
    file_path_1 = "./docs/files1.txt"
    file_path_2 = "./docs/files2new.txt"

    fileComparer = fileComparer()

    #fileComparer.findMissingFiles(file_path_filtered_1, file_path_filtered_2)
    #fileComparer.compareFiles(file_path_filtered_1, file_path_filtered_2, 'compare_file_filtered_log.txt')
    fileComparer.compareFiles(file_path_1, file_path_2, './docs/files_diff_log.txt')
    #fileComparer.compareFiles(dirPath1, dirPath2, 'compare_dir_log.txt')
