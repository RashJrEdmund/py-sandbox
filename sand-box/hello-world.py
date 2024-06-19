print("Hello World")

#
## Spreading
#
user = {
  "name" : "rash",
  "email" : "example@gmail.com"
}

others = {
  "avatar": "image.png"
}

print({ **user, **others }) # spreading here is funny
