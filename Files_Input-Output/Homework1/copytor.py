'''Laura V. Bullock
11/4/2024
Week8 - Day1
Homework1-copytor.py

Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file into the second file.

(Note:  we've provided you with the first chapter of Alice's Adventures in Wonderland to give to some sample text to work with.  This is also the text used in the tests.)

copy('story.txt', 'story_copytxt') #None
        #expect the contents of story.txt and story+_copy.txt to be the same.'''

#Write a function called copy
def copy(source, destination):
        #Open the source in read mode
        with open('story.txt', 'r') as source_file:
                lines = source_file.read()

                # for line in lines:
                #         print(line.strip())

        #Open the destination file in write mode
        with open('story_copy.txt', 'w') as destination_file:
                destination_file.write(lines)

#Call the copy function
copy('story.txt', 'story_copy.txt')