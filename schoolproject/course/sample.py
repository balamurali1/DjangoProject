st = "big black bug bit a big black dog on his big black nose"

words = st.split()

print(set([word for word in words if words.count(word) > 1]))


