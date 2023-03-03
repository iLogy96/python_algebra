name = "Ivan"
surname = "Anić"
year = "1994"

# {} - placeholder
# npr. placeholder tekst - Lorem ipsum dolor sit amet
# print("Full person information is: {} - {} {}".format(year, name, surname))
# print(f"Full person information is: {year} - {name} {surname}")
# print(f"Full person information is: {year} - \"{name} {surname}\"")

personal_data = [name, surname, year]
# print(f"Year of birth is: {personal_data[2]}")

personal_data_tuple = (name, surname, year)
# print(f"Year of birth is: {personal_data_tuple[2]}")

personal_data.append("2023-02-23")
print(personal_data)

personal_data_tuple.append("2023-02-23")
