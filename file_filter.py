class FileFilter():
	def filterExtensions(self, file_path, extensions, output_excluded, output_including):
		open(output_excluded,"w")
		open(output_including,"w")

		with open(file_path, 'r',encoding='utf-8', errors='ignore') as f:
			for line in f:
				line_contains_illegal = False
				for extension in extensions:
					if extension in line:
						line_contains_illegal = True

				if line_contains_illegal:
					with open(output_excluded,"a") as f:
						f.write(line)
				else:
					with open(output_including,"a") as f:
						f.write(line)

	def filterLeadingName(self, file_path, leading_signs):
		open('docs/illegal_leading_lines.txt',"w")
		open('docs/excluded_illegal_leading_characters.txt',"w")

		with open(file_path, 'r',encoding='utf-8', errors='ignore') as f:
			for line in f:
				line_contains_illegal = False
				for leading_sign in leading_signs:
					if leading_sign in line:
						line_contains_illegal = True

				if line_contains_illegal:
					with open('docs/illegal_leading_lines.txt',"a") as output_f:
						output_f.write(line)
				else:
					with open('docs/excluded_illegal_leading_characters.txt',"a") as output_f:
						output_f.write(line)

	def filterIllegalCharacter(self, file_path, characters, outputfile='docs/excluded_illegal_characters.txt'):
			open(outputfile,"w")
			open('docs/illegal_character_lines.txt',"w")

			with open(file_path, 'r',encoding='utf-8', errors='ignore') as f:
				for line in f:
					line_contains_illegal = False
					for character in characters:
						if character in line:
							line_contains_illegal = True

					if line_contains_illegal:
						with open('docs/illegal_character_lines.txt',"a") as output_f:
							output_f.write(line)
					else:
						with open(outputfile,"a") as output_f:
							output_f.write(line)

if __name__ == '__main__':
	fileFilter = FileFilter()

	#fileFilter.filterExtensions('docs/files2.txt', ['Thumbs.db'], 'docs/excluded_extensions_file_2.txt', 'docs/illegal_extension_lines_file_2.txt')
	#fileFilter.filterExtensions('docs/file2.txt', ['Thumbs.db'])
	
	fileFilter.filterIllegalCharacter('docs/compare_file_filtered_log.txt', [':','*','?','"', '<', '>', '|','{', '}', '|','&','#','~'])
	#fileFilter.filterLeadingName('excluded_illegal_characters.txt', [''])	