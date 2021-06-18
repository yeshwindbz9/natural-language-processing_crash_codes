# regular expressions
# searching basic patterns
text = "My phone number is 911-911-1100. Call soon!"
print("phone" in text)
# using re.search()
import re
pattern = "phone"
# returns a match object if match found
print(re.search(pattern, text))
# returns none if pattern is not found
print(re.search("blahblah!", text))
match = re.search(pattern, text)
print(match.span(), "starts at:", match.start(), "ends at:", match.end())
print()

# using re.findall()
text = "My phone is the worlds best phone."
match = re.findall("phone", text)
print(match)
print(len(match))
# to get actual match
for match in re.finditer("phone", text):
    print(match.span())
print()

# finding complex patterns
# identifiers for characters in patterns
# \d->A digit, \w->Alphanumeric, \s->WhiteSpace
# \D->A non digit, \W->Non-Alphanumeric, \S->Non-WhiteSpace
text = "My phone number is 911-911-1100. Call soon!"
pattern = r"\d\d\d-\d\d\d-\d\d\d\d"
match = re.search(pattern, text)
print(match.group())
# quantifiers to define the quantity of characters
# +->Occurs one or more times, {3}->Occurs exactly 3 times
# {2,4}->Occurs 2 to 4 times, {3,}->Occurs 3 or more
# \*->Occurs zero or more times, ?->Once or none
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
print(match.group())
# finding groups
pattern = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(pattern, text)
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))
print()
# or operator
re.search(r"man|woman","This man was here.")
re.search(r"man|woman","This woman was here.")
print()
# wildcard operator
print(re.findall(r".at","The cat in the hat sat here."))
# finding words ending with at
print(re.findall(r"...at","The bat went splat"))
# but this is matching space too
# one or more non-whitespace that ends with 'at'
print(re.findall(r'\S+at',"The bat went splat"))
# use the ^ to signal starts with, and the $ to signal ends with
print(re.findall(r'\d$','This ends with a number 2'))
print(re.findall(r'^\d','1 is the loneliest number.'))
print()
# exclusion
# to exclude characters, we can use the ^ symbol in conjunction with a set of brackets []
text = "This is a string! But it has punctuation. How can we remove it?"
print(' '.join(re.findall(r'[^!.? ]+',text)))
# grouping with brackets
text = "Only find the hypen-words in this sentence. But you do not know how long-ish they are"
print(re.findall(r"[\w]+-[\w]+", text))
# multiple matches with parentheses
text = 'Hello, would you like some catfish?'
print(re.search(r'cat(fish|nap|claw)',text))
text = "Hello, would you like to take a catnap?"
print(re.search(r'cat(fish|nap|claw)',text))
text = "Hello, have you seen this caterpillar?"
print(re.search(r'cat(fish|nap|claw)',text))