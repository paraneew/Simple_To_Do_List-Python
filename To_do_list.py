def li(st):
  print("Your to list has:")
  for i in range(len(st)):
    print(f"\n{(i+1)}.{st[i]}")

l = []
while True:
  print("\n Select an option \n 1.Show list \n 2.Add item \n 3.Remove item \n 4.Exit the program")
  a = int(input("Select your options:"))
  if a == 4:
    print("Closing the program・・・")
    break
  elif a == 2:
    two = str(input())
    l.append(two)
    print(f"\n\"{two}\" added to the list.")
  elif a == 1:
    li(l)
    if len(l) == 0:
      print("\n No items.")
  elif a == 3:
    if len(l) == 0:
      print("\nThe list is empty.")
    else:
      li(l)
      r = input("\nWhich task do you want to remove:")
      try:
        l.remove(r)
        print(f"\"{r}\" has been removed from the list.\n")
      except:
        print(f"\"{r}\" was not in the list.\n")
  elif a != 1 or a != 2 or a != 3 or a != 4:
    print("\nChoose the numbers above, don't make up your own number.")
