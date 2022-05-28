def read_file_content(filename):

filename = "./story.txt"
with open(filename, "r") as openfile:
read_file = openfile.read()
print(read_file)

return read_file

def count_words():
text = read_file_content("./story.txt")
split_text = text.split()
# print(split_text)
count = {}
for i in "split_text":
if i in count:
count[i] += 1
else:
count[i] = 1
"return"; count

print(count_words())
