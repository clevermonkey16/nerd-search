import re 

# To get Degree
def degreeextract(text):
    keyword_list = ""
    # Add keyword list
    keywords = ['Bachelors', 'Masters', 'Doctorates', 'Associates', 'PhD', 'Ph.D.', 'BS', 'BA', 'MS']
    words = text.lower()
    # Replace some words 
    text_replacements = {
    '’':"'",
    "ph.d": 'phd',
    "master's": 'masters',
    "bachelor's": 'bachelors',
    "associate's": 'associates',
    "doctorate's": 'doctorates'
    }

    for key, value in text_replacements.items():
        words = words.replace(key, value)
    
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

    if dollarcount > 1:
        new_list = tokenize
        new_list = re.split(r'\$', tokenize) 
        tokenize = '$' + new_list[1] + ' - ' + '$' + new_list[2]

    #print(tokenize)

    flag = True        
    if len(tokenize) == 0:
        for word in tokenize_list:
            if 'USD' in word and flag == True:
                flag = False
                tokenize += '$' + tokenize_list[tokenize_list.index(word) - 1] + ' - ' + '$' + tokenize_list[tokenize_list.index(word) + 2]
                
      

    if len(tokenize) == 0:
        tokenize = 'NA'

    return tokenize.strip()

def skillsextract(text):
    textlist = text
    text_replacements = {
    'C++': 'Cplusplus',
    'C#': 'Csharp',
    'MS Office': 'MicrosoftOffice',
    'C/C++': 'Cplus and Csharp',
    'Machine Learning': 'ML',
    'Microsoft Word': 'MWord',
    'Sckit-learn': 'Sckitlearn'
    }

    for key, value in text_replacements.items():
        textlist = textlist.replace(key, value)

    #print(textlist)

    textlist = textlist.lower()
    textlist = re.findall(r"\b[\w'-+#]+\b", textlist)
    
    
    skills_keywords = ['R', 'Python', 'SQL', 'Java', 'DBT', 'Leadership', 'Communication', 'Cplusplus', 'C', 'Numpy', 'Pandas',
                     'PowerPoint', 'Excel', 'MicrosoftOffice', 'Tableau', 'Linux', 'Unix', 'Csharp', 'CSS', 'HTML', 'Javascript', 
                     'Reactjs', 'React', 'PHP', 'Ruby', 'Swift', 'TypeScript', 'Ajax', 'JSON', 'MVC', 'Redux', 'API', 'Flask',
                     'ML', 'Django', 'Vue', 'AngularJS', 'NoSQL', 'MongoDB', 'Matlab', 'NodeJS', 'MWord', 'PyTorch', 'SckitLearn'
                     'TensorFlow', 'Snowflake', 'Apache', 'BigQuery', 'Azure', 'Windows', 'IDS', 'IPS', 'QA', 'RDBMS', 'Node'
                     'Unity3D', 'research', 'Maya', 'Unreal', 'UI', 'UX', 'Sketch', 'Figma', 'Adobe', 'Jira', 'Confluence',
                     'BI', 'CAPM', 'PMP', 'CSM', 'GPU', 'Modeling', 'PostgreSQL']
    skills_list = ""
    
    for element in skills_keywords:
        if any(re.search(r"\b{}\b".format(re.escape(element.lower())), word) for word in textlist):
            if element == 'Cplusplus':
                skills_list+='C++\n'
            elif element == 'MicrosoftOffice':
                skills_list+='MS Office\n'
            elif element == 'Csharp':
                skills_list+='C#\n'
            elif element == 'MWord':
                skills_list+='Microsoft Word\n'
            else:
                skills_list+=f'{element}\n'
        
    if len(skills_list) == 0:
        skills_list = 'NA'
    
    return(skills_list).strip()
        

# Testing
if __name__ == "__main__": 
    word = "Master's Degree 16 USD - 88 USD. Our internship hourly rates aren the position and your location, year in school, degree, and experience."
    test = degreeextract(word)
    print(test)
    
 