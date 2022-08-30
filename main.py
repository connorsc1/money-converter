gbp = {
  "usd" : 1.1909052,
  "jpy" : 161.2776,
  "euro" : 1.1685508
}
usd = {
  "gbp" : 0.83960432,
  "jpy" : 135.45448,
  "euro" : 0.98100484,
}
jpy = {
  "gbp" : 0.0061987246,
  "usd" : 0.0073834277,
  "euro" : 0.0072405276,
}
euro = {
  "gbp" : 0.85607774,
  "usd" : 1.0198383,
  "jpy" : 138.1432,
}
signs = {
  "gbp" : "£",
  "usd" : "$",
  "jpy" : "¥",
  "euro" : "€"
}
inp = input("What is your starting currency? (gbp, usd, jpy or euro) ")
num = float(input(f"How many {inp} do you have? "))
if inp.lower() == "gbp":
  currency = input("What Currency would you like to convert to? (usd, jpy, euro) ")
  if currency.lower() in gbp:
    conversion = num * gbp[currency.lower()]
    formatted = "{:.2f}".format(conversion)
    print(f"{signs[inp.lower()]}{num} is {signs[currency.lower()]}{formatted}")
  else: 
    print("Incorrect currency")
elif inp.lower() == "usd":
  currency = input("What Currency would you like to convert to? (gbp, jpy, euro) ")
  if currency.lower() in usd:
    conversion = num * usd[currency.lower()]
    formatted = "{:.2f}".format(conversion)
    print(f"{signs[inp.lower()]}{num} is {signs[currency.lower()]}{formatted}")
  else: 
    print("Incorrect currency")
elif inp.lower() == "jpy":
  currency = input("What Currency would you like to convert to? (gbp, usd, euro) ")
  if currency.lower() in jpy:
    conversion = num * jpy[currency.lower()]
    formatted = "{:.2f}".format(conversion)
    print(f"{signs[inp.lower()]}{num} is {signs[currency.lower()]}{formatted}")
  else: 
    print("Incorrect currency")
elif inp.lower() == "euro":
  currency = input("What Currency would you like to convert to? (gbp, usd, jpy) ")
  if currency.lower() in euro:
    conversion = num * euro[currency.lower()]
    formatted = "{:.2f}".format(conversion)
    print(f"{signs[inp.lower()]}{num} is {signs[currency.lower()]}{formatted}")
  else: 
    print("Incorrect currency")
else:
  print("Incorrect currency")