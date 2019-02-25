# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI paste
the commands and results below.

- Navigate to your home directory
cd ~\

- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder


## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file


## explore advanced CLI

- What is the difference between the two commands > and >>?
> creates a new file
>> appends on the new file

- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
touch hello.txt
echo 'how?!' >> hello.txt
cp hello.txt my_file.txt

 
- Overwrite the content of my_file.txt with "tell me"
echo 'tell me' > my_file.txt