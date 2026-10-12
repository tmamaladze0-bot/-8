text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
text = text.lower()
print(text)
text = text.replace(",", "")
print(text)
text = text.replace(".", "")
print(text)
words = text.split()
print(words)
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
most_common = ""
highest_count = 0

for word, count in word_count.items():
    if count > highest_count:
        highest_count = count
        most_common = word
        print(f"ყველაზე ხშირი: '{most_common}' ({highest_count}-ჯერ)")
        print(f"სხვადასხვა სიტყვა: {len(word_count)}")