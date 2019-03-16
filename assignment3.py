from typing import List, Dict, Tuple


def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.

    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]),
    200: ('Ariel', [100, 500], [500]),
    300: ('Jasmine', [500], [500, 100]),
    400: ('Elsa', [100, 500], []),
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    # Your code goes here
    f=open(file_name)
    PD:Dict={}
    info:List=f.read().splitlines()
    l1:List
    l2:List
    for i in range(0,len(info),5):
        if (info[i + 2].strip()==""):
            l1=[]
        else:
            l1 = [int(j) for j in info[i + 2].strip().replace(",", "").split(' ')]
        if (info[i + 3].strip()==""):
            l2 = []
        else:
            l2 = [int(j) for j in info[i + 3].strip().replace(",","").split(' ')]
        PD[int(info[i].strip())]=(info[i+1].strip(),l1,l2)
    return PD

def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.

    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400,
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'],
        [100, 200, 300],
        [400, 500]),
    100001: (
        200,
        'Make the ocean great again.',
        [''],
        [],
        [400]),
    100002: (
        500,
        "Help I'm being held captive by a beast!  %OhNoes",
        ['OhNoes'],
        [400],
        [100, 200, 300]),
    100003: (
        500,
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome",
        ['StockholmeSyndrome'],
        [400, 100],
        []),
    100004: (
        300,
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.',
        ['ShowYouTheWorld', 'JustSayNo'],
        [500, 200],
        [400]),
    100005: (
        400,
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan',
        ['StockholmeSyndrome', 'SnowMan'],
        [],
        [200, 300, 100, 500])}
    """
    # Your code goes here
    f = open(file_name)
    CD: Dict = {}
    info: List = f.read().splitlines()
    l1:List
    l2:List
    tg:List
    for i in range(0, len(info), 7):
        tg=[j for j in info[i + 3].strip().replace(",", "").split(' ')]
        if (info[i + 4].strip()==""):
            l1=[]
        else:
            l1 = [int(j) for j in info[i + 4].strip().replace(",", "").split(' ')]
        if (info[i + 5].strip()==""):
            l2 = []
        else:
            l2 = [int(j) for j in info[i + 5].strip().replace(",","").split(' ')]
        CD[int(info[i].strip())] =(int(info[i+1].strip()),info[i+2].strip(),tg,l1,l2)
    return CD

def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int) \
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of th .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(profile_dictionary, chirp_dictionary, 300)
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profiles, chirps, 500 )
    ['Make the ocean great again.',
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.',
    'Does not want to build a %SnowMan %StopAsking']
    """
    # Your code goes here
    chps:List=[]
    for id in profile_dictionary[user_id][2]:
        maxlikes=-1
        chpstr:str=""
        for key in chirp_dictionary:
            if id==chirp_dictionary[key][0]:
                if(len(chirp_dictionary[key][3])>maxlikes):
                    maxlikes=len(chirp_dictionary[key][3])
                    chpstr=chirp_dictionary[key][1]
        if (chpstr!=""):
            chps.append(chpstr)
    return chps


def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.

    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']},
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']},
    '': {
        200: ['Make the ocean great again.']},
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]},
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"],
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']},
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']},
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    # Your code goes here
    TD:Dict={}
    for key in chirp_dictionary:
        for chp in chirp_dictionary[key][2]:
            if chp.strip() not in TD:
                TD[chp.strip()]={}
            if chirp_dictionary[key][0] not in TD[chp.strip()]:
                TD[chp.strip()][chirp_dictionary[key][0]]=[]
            TD[chp.strip()][chirp_dictionary[key][0]].append(chirp_dictionary[key][1])
    return TD


def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking',
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    # Your code goes here
    lol:List=[]
    g=create_tag_dictionary(chirp_dictionary)
    if tag.strip() not in g:
        return[]
    for key in g[tag.strip()]:
        lol.extend(g[tag.strip()][key])
    return lol