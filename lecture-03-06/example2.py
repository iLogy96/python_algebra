"""U tekstu prebrojite pojavljivanje neke riječi.
Npr Lorem.

https://www.lipsum.com/

"""

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque lacinia placerat imperdiet. Pellentesque purus est, pretium blandit aliquam eget, facilisis quis ligula. In hac habitasse platea dictumst. Integer dapibus sem vitae euismod pellentesque. Etiam elementum nisl in tristique ultricies. Nunc vestibulum libero nisl, at euismod ante mattis vel. Aliquam posuere nibh eget luctus iaculis. Suspendisse vitae eros tincidunt dui posuere faucibus sed non erat. Mauris vestibulum erat non nisi imperdiet, non ullamcorper nisi cursus.

Proin condimentum sit amet leo sit amet sodales. Vestibulum sed augue vitae sem placerat tincidunt. Vivamus ut nulla quis leo posuere laoreet ac a augue. Etiam tristique sagittis nunc, id posuere velit bibendum varius. Donec vestibulum lectus felis, et condimentum augue vestibulum in. Curabitur rutrum, est a auctor tempus, ipsum nulla pharetra neque, quis rutrum orci turpis a arcu. Aenean commodo dolor vel turpis semper eleifend. Proin nec sagittis est, ut ornare magna. Fusce non augue nec tortor lobortis interdum.

Vivamus est ex, ornare in sodales et, condimentum vel risus. Suspendisse vitae convallis dui, id facilisis massa. Quisque scelerisque venenatis justo vel vestibulum. Praesent sit amet erat in velit porttitor pharetra auctor ac nulla. Morbi molestie pulvinar diam, ut volutpat tortor eleifend nec. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Integer mollis, velit semper congue auctor, turpis ex porttitor dui, eget suscipit metus neque sed urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum molestie nisi nec maximus convallis. Phasellus eu sagittis justo. Proin iaculis dapibus massa in interdum. Suspendisse suscipit velit vel nisi euismod pharetra. Donec nec magna vel lacus volutpat lobortis. Praesent scelerisque est et elit maximus, et semper elit eleifend. Praesent facilisis tempus nisi ut iaculis. Maecenas ultrices maximus diam et pellentesque.

Mauris scelerisque orci tempus metus vulputate, ultricies consequat enim sodales. In nulla massa, fringilla id leo eget, consequat ullamcorper justo. In eleifend molestie magna egestas auctor. Curabitur eget neque magna. Donec vulputate, ligula quis euismod convallis, sem dolor feugiat augue, ut pretium enim lectus et tortor. Pellentesque fermentum porttitor fringilla. Nunc rhoncus enim sit amet orci imperdiet faucibus. Nullam et lectus eu purus tincidunt venenatis vitae nec nulla. Nam ac iaculis lacus. Donec mollis tempor consequat. In hac habitasse platea dictumst.

Fusce posuere imperdiet venenatis. Donec pulvinar bibendum ornare. Curabitur convallis orci eu velit tempus, vel dapibus risus bibendum. Sed lacus lectus, vestibulum sed consequat nec, aliquet ut sapien. Morbi fermentum facilisis magna, non aliquam arcu laoreet eget. Aliquam vestibulum augue vel lorem porta, vel feugiat turpis cursus. Aenean varius augue eget ante mattis dictum. Curabitur mollis pulvinar lorem, vitae condimentum nisl dapibus nec. Aenean semper iaculis enim vitae eleifend. Praesent faucibus ullamcorper felis et ornare. Quisque sodales enim malesuada purus efficitur, eu laoreet ex lobortis. Mauris ut ex accumsan, lacinia justo sed, volutpat nisi. Suspendisse id accumsan lacus. Etiam congue diam sed tristique porttitor.

Vivamus tincidunt diam quis dui auctor tempor. Vivamus ut velit eget turpis auctor ornare a vel dolor. Integer dictum et neque eget accumsan. Nam tempus sem a quam condimentum, sit amet auctor nisi varius. Aliquam eu rhoncus orci. Phasellus eu tempus lectus. Vestibulum vitae facilisis nunc. Sed tincidunt posuere justo at facilisis. Vivamus id vehicula enim.

Praesent at convallis urna, ac venenatis neque. Nam rhoncus at dolor lacinia accumsan. In commodo commodo sem, eget tincidunt massa sodales vitae. Donec non mauris id velit posuere faucibus. Vestibulum massa diam, semper quis sollicitudin vel, dapibus eget mi. Donec aliquam nibh sed dapibus fringilla. Morbi porta felis non lacus cursus, sit amet facilisis mauris dapibus. In in consequat sem, at cursus neque. Proin sit amet magna dapibus, pellentesque diam sit amet, vestibulum nibh. Donec semper ante a mi venenatis, non sagittis urna volutpat.

Sed molestie feugiat nisl in faucibus. Phasellus rhoncus diam a tristique vestibulum. Vivamus pharetra congue laoreet. Sed id metus ultricies, tincidunt tellus non, scelerisque quam. Nullam tincidunt tincidunt lobortis. Nunc in tortor eu tortor bibendum suscipit eget id ex. Donec eu elementum dolor. Vestibulum interdum libero ut tellus ultrices pretium. Aenean mattis, sapien vel pulvinar commodo, est lacus imperdiet magna, vel pretium quam urna lacinia mi. Cras fermentum, ex eu faucibus hendrerit, lorem purus gravida dolor, a ullamcorper leo orci et felis. Nulla velit purus, interdum id ullamcorper vitae, tristique non risus. Phasellus sit amet rhoncus eros, sed ornare sapien. Sed aliquet mi odio, vel molestie quam molestie in. Vestibulum iaculis, purus in varius placerat, sem felis aliquet sem, ut dictum est urna ac metus.

Quisque accumsan tristique urna, fringilla sagittis justo efficitur a. Aliquam erat volutpat. Curabitur in ex sit amet lorem hendrerit tristique. In molestie eleifend elementum. Sed sodales risus sed efficitur finibus. Ut lobortis venenatis lectus non consectetur. Nullam dapibus fringilla consequat. Nunc aliquam, purus vitae mollis hendrerit, justo metus gravida purus, non facilisis diam dui vel odio. Ut sed risus metus.

Curabitur in convallis erat, ut pretium erat. Nam congue quam non fringilla suscipit. In egestas vitae erat malesuada dapibus. Nullam consectetur dolor justo, ut rutrum augue tincidunt vel. Morbi laoreet urna ut tortor hendrerit, venenatis tristique magna fringilla. Quisque vel finibus nulla, sed fermentum massa. Aenean nulla nulla, imperdiet at orci blandit, tempor pretium velit. Proin luctus ultrices fringilla. Nam pharetra consequat leo, sed condimentum ante sollicitudin nec.

Quisque varius sagittis maximus. Vivamus quis eros id mauris fermentum molestie sed tempor dolor. Aenean ornare tristique nisl, ut laoreet magna fringilla ut. Nullam vitae tellus vel libero maximus lacinia vel ut odio. Phasellus faucibus pulvinar velit, eu dictum lorem tempus eget. Donec pretium ipsum sed suscipit suscipit. Nam egestas gravida sapien eget tristique.

Proin nisi purus, auctor sit amet leo ac, condimentum finibus lorem. Mauris vitae finibus velit. Proin libero arcu, vehicula et ultrices id, cursus quis nibh. Maecenas sagittis vehicula malesuada. Proin massa nunc, varius pretium lorem ut, porta imperdiet dui. Sed lacus neque, dictum non erat eu, sagittis mollis quam. Aenean congue ex vel massa mattis, sed dapibus sapien viverra. Nulla semper sit amet erat nec dapibus. Duis non tortor et turpis efficitur mattis. Quisque sagittis mi ac erat pharetra consectetur. Proin interdum venenatis sollicitudin.

Integer tempus felis et felis varius tincidunt. Suspendisse ultricies, nisi placerat pellentesque mollis, justo velit feugiat lectus, in aliquet turpis ante et lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc ex ipsum, maximus sed finibus sed, porta vestibulum justo. Maecenas quis dictum lectus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Integer eu justo eu nunc pharetra ultricies. Morbi hendrerit enim ipsum, in rhoncus est porta ultrices. Sed a velit mollis, porttitor nisi eu, interdum diam. Pellentesque aliquet odio nec nisl hendrerit cursus. Suspendisse elementum dapibus turpis, sit amet porta tellus sollicitudin sed. Nulla efficitur, arcu at imperdiet scelerisque, diam turpis hendrerit lacus, nec dapibus ligula arcu ut metus. Fusce hendrerit metus nunc, vel pulvinar mi elementum ac.

"""

print(text.split())

primjer = "test\
test"
primjer = """test
test
"""

"""
tekst = dohvatimo tekst sa lipsum.com
words = text.split(sep=" ")
search_word = input("Unesi riječ za prebrojavanje") # i.e. Lorem
# for word in text:
# krivo! iteriramo po slovima 
counter = 0
for word in words:
    #1 - Lorem
    if (search_word == word):
        counter = counter + 1
print(broj pojavljivanja je counter)
"""

search_word=input("Unesite rijec koju zelite:")  #primjer je lorem
words=text.split()
counter=0
# print(words)
for word in words:
    if search_word==word:
        counter+=1
print(f'ima ukupno {counter} rijeci {search_word} u ovom textu')

# mogli smo koristiti i
text.count()
