# [Examination](https://docs.google.com/document/d/1GhqbgG9YW5cOiR0LLWmMTc-s-VmQudBaNxZUxXL6XJk/edit?tab=t.0)
### Programmering med Python

Du ska lösa uppgiften självständigt. När du tar hjälp av AI, eller diskuterar med andra studenter, ska du se till att du förstår vad koden gör.

- Uppgift
  - Version 1 - grundkrav
  - Version 2 - nice to have
  - Version 3 - extra utmaning
- Tips
- Bedömning
- Inlämning

## Uppgift
Din uppgift är att bygga vidare på spelet "Fruit loop". Spelet kan spelas direkt i terminalen, och går ut på att samla frukter.

Börja med att läsa igenom hela uppgiften, sedan hittar du länk till ett kodprojekt längre ner.


### Version 1 - grundkrav
* A. Spelaren ska börja nära mitten av rummet.
* B. Förflyttningar i alla 4 riktningar. (WASD)
* C. Man ska inte kunna gå igenom väggar.
* D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
* E. Inventory - alla saker som man plockar upp ska sparas i en lista.
* F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
* G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
* H. Använd for-loopar för att skapa flera, sammanhängande väggar på kartan. Se till att det inte skapas några rum som man inte kan komma in i. Gör detta i filen grid.py.

### Version 2 - nice to have
* I. Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en fälla ska man förlora 10 poäng. Fällan ska ligga kvar så att man kan falla i den flera gånger.
* J. Spade - en ny sak man kan plocka upp. När man går in i en vägg nästa gång, förbrukas spaden för att ta bort väggen.
* K. Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen. När man går på en ruta med en nyckel plockar man upp den i sitt inventory. Om man kommer till en kista och har minst en nyckel, öppnar man kistan och plockar upp en skatt som är värd 100 poäng. (Nyckeln är förbrukad.)
* L. Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.
* M. Exit - slumpa ett "E" på kartan. När man har plockat upp alla ursprungliga saker, kan man gå till exit för att vinna spelet. Men innan man tagit upp alla har inte Exit någon effekt.
* N. Jump - om man skriver ett "J" innan något av "WASD", ska spelaren hoppa över en ruta. Man förflyttar sig alltså två steg, men kan förstås bara plocka upp eller interagera med saker där man landar. Hoppar man in i en vägg blir det samma effekt som om man hade gått ett steg på vanligt sätt.

### Version 3 - extra utmaning
* O. Grace period - efter man har tagit plockat upp något, kan man gå 5 steg utan att det dras några poäng.
* P. AI-fiender - placera 1-3 fiender på kartan. För varje steg spelaren tar ska ska varje fiende ha en slumpmässig chans att flytta sig ett steg närmare spelaren. Minus 20 poäng om en fiende hinner ifatt. (Inte diagonalt, dvs. samma rörelsemönster som spelaren. Fienderna ska vara lite "långsammare" så att det är lagom svårt att undvika dem.)
* Q. Tryck "B" för att placera en bomb. Efter 3 drag smäller bomben och förstör allt på sin ruta och de åtta som gränsar till den. (fällor, väggar, m.m.) Om spelaren är kvar förlorar man poäng.
* R. Ett nytt kommando ("T" för trap) för att desarmera fällor.

_Tyvärr finns det inget enkelt, plattformsoberoende sätt att läsa in ett tecken från användaren, utan att man måste trycka Enter. Paketet "curses" är ett avancerat och kraftfullt bibliotek för att styra terminalen i detalj. På Windows kan man använda msvcrt.getch() och på Linux/macOS en kombination av tty och termios. Vill du utmana dig själv ytterligare kan du prova någon av de teknikerna._


## Tips
* Det finns flera tips märkta med "TODO" i kodfilerna. Du måste inte göra allt de säger, men flera av dem är tänkta att hjälpa till.
* Du får använda TDD under utvecklingen.
* Undvik att upprepa kod - skapa loopar, funktioner eller klasser i stället.
* 1H: du måste inte slumpa väggarna, det går bra att göra fasta väggar. Men du måste använda loopar och får alltså inte lägga till dem en och en.
* Du får lägga till fler filer, funktioner och ändra fritt i projektet.
* Lägg till en "run configuration" för projektet så kan du testköra det enklare. Så här ser det ut i PyCharm:


## Bedömning
**Godkänt (G):** 
För att få betyget Godkänt (G) ska den studerande ha genomfört kursen och nått alla kursens lärandemål. 

_Genom att uppfylla alla spelets grundkrav (version 1) kan du visa att du nått kursens lärandemål._

**För betyget (VG):**
För att få betyget Väl Godkänt (VG) ska den studerande dels ha genomfört kursen och nått alla kursens lärandemål, dels uppfylla kravet att kunna ta ansvar för och självständigt driva arbetet med att planera och skapa en välstrukturerad och tydlig kod med högre kvalitet än för betyget G.

För att visa den högre nivå som krävs för VG, behöver du arbeta med flera av kraven för version 2. Dessutom behöver du tänka på att koden ska vara tydlig och välstrukturerad. Det ska vara lätt att läsa och förstå din kod.

## Inlämning
Till din hjälp har du ett Git-repository med kod som du ska utgå från: GitHub exam_template.
Observera att du inte kan arbeta i det repot.
Du måste skapa en egen kopia. Klicka på knappen Fork:

Kontrollera att ditt repo är publikt innan du lämnar in. Ladda sedan upp en textfil på LearnPoint:
* skapa filen i PyCharm/VS Code
* filen ska heta "ditt_namn.txt"
* filen ska innehålla länk till ditt GitHub-repo
* och eventuella andra kommentarer

För att bli godkänd måste all kod finnas med i repot och projektet ska gå att köra utan fel.


### Extra
Använder pytest-cov för code coverage, kräver separat installation:
`pip install pytest-cov`
