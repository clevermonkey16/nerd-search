import re 

# To get Degree
def degreeextract(text):
    keyword_list = ""
    # Add keyword list
    keywords = ['Bachelors', 'Masters', 'Doctorates', 'Associates', 'PhD', 'Ph.D.', 'BS', 'BA', 'MS']
    words = text.lower()
    # Replace some words 
    words = words.replace('’',"'")
    words = words.replace('ph.d', 'phd')
    words = words.replace("master's", 'masters')
    words = words.replace("bachelor's", 'bachelors')
    words = words.replace("associate's", 'associates')
    words = words.replace("doctorate's", 'doctorates')
    # Tokenizes
    words = re.findall(r"\b[\w'-]+\b", words)
    #print(words)
    for keyword in keywords:
        # makes it so BA and bachelors are separate
        if any(re.search(r"\b{}\b".format(re.escape(keyword.lower())), word) for word in words):
            keyword_list+=f'{keyword}\n'

    if len(keyword_list) == 0:
            keyword_list = 'NA'

    return keyword_list

# To get Salary 
def salaryextract(text):
    tokenize = ''
    tokenize_list = re.split(r'\s+|\n', text) 
    #print(tokenize_list)
    dollarcount = 0
    for word in tokenize_list:
        if '$' in word:
           tokenize+=word
           dollarcount += 1
    
    #print(tokenize)
    #print(dollarcount)
    #print(tokenize)
    if dollarcount > 1:
        new_list = tokenize
        new_list = re.split(r'\$', tokenize) 
        tokenize = '$' + new_list[1] + ' - ' + '$' + new_list[2]

    #print(tokenize)
            
    if len(tokenize) == 0:
        tokenize = 'NA'

    return tokenize.strip()

# Testing
if __name__ == "__main__": 
    word = "$17.00 - $98.00"
    salary = salaryextract(word)
    text = degreeextract(word)

    print(salary)
    
 