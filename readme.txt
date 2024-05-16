Plan:


Done:
1: lag en lookup table med frekvensen til hver bokstav i det engelske språk

ToDo:

2: Lag en metode som sammenligner frekvensen til bokstavene i en gitt tekst med frekvensen til bokstavene i lookup tabellen
3: la metoden gjøre gjetninger basert på høyest frekvens, så neste i frekvens helt ned til bunn, for så å printe ut et forslag til dekryptert tekst.
	3a: Finn en måte å ta høyde for spesialtegn (!'?) i metoden. 
	3b: finn ut av Stian sin setning
4: Lag et API som heter en tilfeldig setning fra f.eks https://rapidapi.com/bryantech-bryantech-default/api/random-text-generator
5: lagre originalteksten i en variabel før kryptering. Krypter teksten i en egen metode. 
6: La dekrypt-metoden ha flere iterasjoner, der den på slutten av hver iterasjon sammenligner resultatet med originalteksten. Hvis resultatet stemmer, avslutt loopen. 
	6a: prøv å behold karakterer som stemmer etter hver iterasjon. Forsøk bare endringer i posisjoner som ikke stemmer med originaltekst. 