import os
from shutil import copy

class FileMover():
    def move_files_from_file(self, file_source_path, destination_path):
        open("./error_log_file_mover.txt","w",encoding='iso-8859-1', errors='ignore')
        success = 0
        errors = 0
        with open(file_source_path, 'r',encoding='iso-8859-1') as file:
            for line in file:
                split_line = line.split("/")
                if len(split_line) > 2:
                    destination_folder = destination_path+split_line[-2]
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    copy(line, destination_folder+"/"+split_line[-1])
                    print(destination_folder+"/"+split_line[-1])
                    success = success + 1   
                elif len(split_line) == 1:
                    copy(line, destination_path+"/"+split_line[-1])
                    success = success + 1
                else:
                    with open("./error_log_file_mover.txt","a") as f:
                        f.write(line)
                    errors = errors + 1
                break

        print("completed with %s successes and %s errors" % (success, errors))


if __name__ == '__main__':
    file_mover = FileMover()
    source_file = "./docs/test_location.txt"
    destination_path = "./docs/tmp/"
    file_mover.move_files_from_file(source_file,destination_path)
