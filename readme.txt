Plan:


Done:
1: lag en lookup table med frekvensen til hver bokstav i det engelske spr�k

ToDo:

2: Lag en metode som sammenligner frekvensen til bokstavene i en gitt tekst med frekvensen til bokstavene i lookup tabellen
3: la metoden gj�re gjetninger basert p� h�yest frekvens, s� neste i frekvens helt ned til bunn, for s� � printe ut et forslag til dekryptert tekst.
	3a: Finn en m�te � ta h�yde for spesialtegn (!'?) i metoden. 
	3b: finn ut av Stian sin setning
4: Lag et API som heter en tilfeldig setning fra f.eks https://rapidapi.com/bryantech-bryantech-default/api/random-text-generator
5: lagre originalteksten i en variabel f�r kryptering. Krypter teksten i en egen metode. 
6: La dekrypt-metoden ha flere iterasjoner, der den p� slutten av hver iterasjon sammenligner resultatet med originalteksten. Hvis resultatet stemmer, avslutt loopen. 
	6a: pr�v � behold karakterer som stemmer etter hver iterasjon. Fors�k bare endringer i posisjoner som ikke stemmer med originaltekst. 