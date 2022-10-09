url="assets/story.txt"

def read_template(url):
    """
    this function takes the file path then read the content
    and return the content
    """
    data=""

    try:
        with open(url) as file:
            data= file.read()
            
    except FileNotFoundError:
        raise FileNotFoundError
    return data

read=read_template(url)
   
def parse_template(data):

    """
    this function  takes string return the tuple contains the str without the content inside curly practice and tuple with the content  inside curly practice
    """
    r2=data
    array=[]
 
    indecies1=[index for index in range(len(data)) if data.startswith("{",index)]
    indecies2=[index for index in range(len(data)) if data.startswith("}",index)]


    for i in range(len(indecies1)):
        array.append(data[indecies1[i]+1:indecies2[i]])
        r2=r2.replace(data[indecies1[i]+1:indecies2[i]], "")
        
    

    
    return (r2,tuple(array))

string,arr=parse_template(read)
    
def merge(str,tuple):
    """
    this function takse 2 arguments the first one is a string the other one is tuple and it return string that made by puting the tuple content inside curly practice inside that string 

    """
    result=str.format(*tuple)
    return result
    
def inputs(str,tuple):
    array=[]
    for i in range(len(tuple)):
        array.append(input("please inter "+tuple[i]+":"))
    
    result=str.format(*array)
    return result

result=inputs(string,arr)

def write_story(result):
    try:
        with open('assets/reponse.txt', 'w') as f:
            data= f.write(result)
    except:
        raise "err"
    return data

story=write_story(result)
def read_story():
    try:
        with open("assets/reponse.txt") as file:
            data= file.read()
            
    except :
        raise "err"
    return data
print(read_story())
