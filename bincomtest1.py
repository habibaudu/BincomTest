#answers to test
'''
  Name : Habib Audu
  Bincom Test Answers 1 - 6
  email: auduhabib1990@gmail.com
'''
import re
import psycopg2 #adaptor for postgres and pYthon


def Color():
    fl = open('python_class_question.html','r') #open the page for reading
    f = fl.readlines()                         #make ita list of lines
    numoflines = len(f)                        # number of lines
    dai = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY',]
    colors=[]
    for i in range(numoflines):
        matchstring = re.compile(r'<td>([a-zA-Z,\s])+</td>') # regex to extract colors and daYs
        mobj = matchstring.search(f[i])
        if mobj == None:              
           continue
        else:
               colors.append(mobj.group())

    color1="".join(colors)
    color2 = color1.split('<td>') #removes <td> from the string
    color1="".join(color2)
    color2 = color1.split('</td>') #removes </td> from the string
    color1 =" ".join(color2)
    color2 =color1.split() 
    color3 =[]
    
    for i in color2:
        if i not in dai:     #onlY store colors
            color3.append(i)

    dic ={}                  #create a dictionarY store colors and their frequenci
    numw = len(color3)
    for i in range(numw):
         dic[color3[i]]=dic.get(color3[i],0)+1 

    print(dic)

    """ 
       1.	Which color of shirt is the mean color?
    """
    #mean colors
    sumofvalues = 0
    meancolor =""
    for i in dic.values(): #sum the the total frequenci
        sumofvalues +=i 
    mean = sumofvalues // len(dic)  # divide bY length to get mean
    for i in dic.keys():
        if dic[i]==mean:             
            meancolor = i
    print("Mean color is : "+meancolor) #prints mean color

    """ 
        2.	Which color is mostly worn throughout the week?
    """
    #most worn during the week
    mostWORNcolor = max(dic.values())
    for i in dic.keys():
        if dic[i]==mostWORNcolor:
            mostWORNcolor = i
            break
    print("Most worn color is : "+mostWORNcolor)   #print the Most worn color

    """ 
        3.	Which color is the median?
    """
    #meadean colors
    values = []
    for i in dic.values():
        values.append(i)
    for passnum in range(len(values)-1,0,-1): # sort using bubble sort
        for i in range(passnum):
            if values[i]>values[i+1]:
                temp = values[i]
                values[i] = values[i+1]
                values[i+1] = temp
    
    first = 0
    last = len(values)-1
    mid = (first + last) // 2                   #find the middle index
    medianvalue = values[mid]
    mediancolor =''
    for i in dic.keys():
        if dic[i]==medianvalue:                  # get the color
            mediancolor = i
            break
    print("Median color is : "+mediancolor)   #print the median color


    """ 
       4.	BONUS Get the variance of the colors
    """   

#Get the variance of the colors
#first minus the mean value from all color frequenci values and square them
    varianceV =[] 
    for i in dic.values():
        varianceV.append((i - mean)**2)
#second sum all the values 
    varianceS = 0
    for x in varianceV:
        varianceS +=x
#finally divide by number of item in the dictionary
    variance = str(varianceS / len(dic))

    print("The Variance of the Colors  is : "+variance) #print the variance

    
    """ 
      5.	BONUS if a colour is chosen at random, what is the probability that the color is red?
    """ 

# if a colour is chosen at random, what is the probability that the color is red?
#first sum all the frequencies
    Sum_of_frequenci = 0
    frequency_of_red =0
    for i in dic.values():
        Sum_of_frequenci +=i

#finally divide event by posible outcome i.e total frequency by frequency of red
    frequency_of_red = dic['RED,']
    probability = str(frequency_of_red / Sum_of_frequenci)

    
    print("Probabiliti of picking a red color at random is : "+probability) #print the probability


    """   
         6.	Save the colours and their frequencies in postgresql database
    """

    #inserting into database
    conn = psycopg2.connect(database = "colorsdb", user = "postgres", password = "smirk200", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE colors
      (
      colorID SERIAL PRIMARY KEY,
      color    TEXT    NOT NULL,
      frequenci  int NOT NULL);''')
    print (" Table  created successfully")
    conn.commit()

    sql = """INSERT INTO colors(color,frequenci)
             VALUES(%s,%s);"""

    #extracting from dictionari and inserting into database
    for color,frequenci in dic.items():
      
           cur.execute(sql,(color,frequenci))
           conn.commit()
          
    conn.close()

def select_from_postgres():
    
    conn = psycopg2.connect(database = "colorsdb", user = "postgres", password = "smirk200", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")

    cur = conn.cursor()
    sql1 = """SELECT color,frequenci from colors """

    cur.execute(sql1)
    rows = cur.fetchall()
    for row in rows:

         print ("   Color = ", row[0])
         print ("   Frequenci = ", row[1])
         print()

    print ("Operation done successfully")
    conn.close()



    

Color() #calls or invoke the function
select_from_postgres()

