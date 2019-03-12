# coding: utf-8

# In[29]:


train_data=[
("""What Are We Searching for on Mars?
Martians terrified me growing up. I remember watching the 1996 movie Mars Attacks! and fearing that the Red Planet harbored hostile alien neighbors. Though I was only 6 at the time, I was convinced life on Mars meant little green men wielding vaporizer guns. There was a time, not so long ago, when such an assumption about Mars wouldn’t have seemed so far-fetched.
Like a child watching a scary movie, people freaked out after listening to “The War of the Worlds,” the now-infamous 1938 radio drama that many listeners believed was a real report about an invading Martian army. Before humans left Earth, humanity’s sense of what—or who—might be in our galactic neighborhood was, by today’s standards, remarkably optimistic.
""",
"science"),
("""Mountains of Ice are Melting, But Don't Panic (Op-Ed)
If the planet lost the entire West Antarctic ice sheet, global sea level would rise 11 feet, threatening nearly 13 million people worldwide and affecting more than $2 trillion worth of property. 
Ice loss from West Antarctica has been increasing nearly three times faster in the past decade than during the previous one — and much more quickly than scientists predicted.
This unprecedented ice loss is occurring because warm ocean water is rising from below and melting the base of the glaciers, dumping huge volumes of additional water — the equivalent of a Mt. Everest every two years — into the ocean.
""",
"science"),
("""Some scientists think we'll find signs of aliens within our lifetimes. Here's how.
Finding extraterrestrial life is the essence of science fiction. But it's not so far-fetched to predict that we might find evidence of life on a distant planet within a generation.
"With new telescopes coming online within the next five or ten years, we'll really have a chance to figure out whether we're alone in the universe," says Lisa Kaltenegger, an astronomer and director of Cornell's new Institute for Pale Blue Dots, which will search for habitable planets. "For the first time in human history, we might have the capability to do this."
""",
"science"),
("""'Magic' Mushrooms in Royal Garden: What Is Fly Agaric?
Hallucinogenic mushrooms are perhaps the last thing you'd expect to find growing in the Queen of England's garden.
Yet a type of mushroom called Amanita muscaria — commonly known as fly agaric, or fly amanita — was found growing in the gardens of Buckingham Palace by the producers of a television show, the Associated Press reported on Friday (Dec. 12).
A. muscaria is a bright red-and-white mushroom, and the fungus is psychoactive when consumed.
""",
"science"),
("""Upcoming Parks : 'Lost Corner' Finds New Life in Sandy Springs
At the corner of Brandon Mill Road, where Johnson Ferry Road turns into Dalrymple Road, tucked among 24 forested acres, sits an early 20th Century farmhouse. A vestige of Sandy Springs' past, the old home has found new life as the centerpiece of Lost Forest Preserve. While the preserve isn't slated to officially debut until some time next year, the city has opened the hiking trails to the public until construction begins on the permanent parking lot (at the moment the parking lot is a mulched area). The new park space includes community garden plots, a 4,000-foot-long hiking trail and an ADA-accessible trail through the densely wooded site. For Atlantans seeking an alternate escape to serenity (or those who dig local history), it's certainly worth a visit.
""",
"science"),
("""Stargazers across the world got a treat this weekend when the Geminids meteor shower gave the best holiday displays a run for their money.
The meteor shower is called the "Geminids" because they appear as though they are shooting out of the constellation of Gemini. The meteors are thought to be small pieces of an extinct comment called 3200 Phaeton, a dust cloud revolving around the sun. Phaeton is thought to have lost all of its gas and to be slowly breaking apart into small particles.
Earth runs into a stream of debris from 3200 Phaethon every year in mid-December, causing a shower of meteors, which hit its peak over the weekend.
""",
"science"),
("""Envisioning a River of Air
By the classification rules of the world of physics, we all know that the Earth's atmosphere is made of gas (rather than liquid, solid, or plasma). But in the world of flying it's often useful to think
""",
"science"),
("""Following Sunday's 17-7 loss to the Seattle Seahawks, the San Francisco 49ers were officially eliminated from playoff contention, and they have referee Ed Hochuli to blame. OK, so they have a lot of folks to point the finger at for their 7-7 record, but Hochuli's incorrect call is the latest and easiest scapegoat.
"""
,"sport"),
("""Kobe Bryant and his teammates have an odd relationship. That makes sense: Kobe Bryant is an odd guy, and the Los Angeles Lakers are an odd team.
They’re also, for the first time this season, the proud owners of a three-game winning streak. On top of that, you may have heard, Kobe Bryant passed Michael Jordan on Sunday evening to move into third place on the NBA’s all-time scoring list. 
"""
,"sport"),
("""The Patriots continued their divisional dominance and are close to clinching home-field advantage throughout the AFC playoffs. Meanwhile, both the Colts and Broncos again won their division titles with head-to-head wins.The Bills' upset of the Packers delivered a big blow to Green Bay's shot at clinching home-field advantage throughout the NFC playoffs. Detroit seized on the opportunity and now leads the NFC North.
"""
,"sport"),
("""If you thought the Washington Redskins secondary was humbled by another scintillating performance from New Yorks Giants rookie wide receiver sensation Odell Beckham Jr., think again.In what is becoming a weekly occurrence, Beckham led NFL highlight reels on Sunday, collecting 12 catches for 143 yards and three touchdowns in Sunday's 24-13 victory against an NFC East rival. 
"""
,"sport")
,("""That was two touchdowns and 110 total yards for the three running backs. We break down the fantasy implications.The New England Patriots' rushing game has always been tough to handicap. Sunday, all three of the team's primary running backs put up numbers, and all in different ways, but it worked for the team, as the Patriots beat the Miami Dolphins, 41-13.
"""
,"sport"),
("""General Santos (Philippines) (AFP) - Philippine boxing legend Manny Pacquiao vowed to chase Floyd Mayweather into ring submission after his US rival offered to fight him next year in a blockbuster world title face-off. "He (Mayweather) has reached a dead end. He has nowhere to run but to fight me," Pacquiao told AFP late Saturday, hours after the undefeated Mayweather issued the May 2 challenge on US television. The two were long-time rivals as the "best pound-for-pound" boxers of their generation, but the dream fight has never materialised to the disappointment of the boxing world.
"""
,"sport"),
("""When St. John's landed Rysheed Jordan, the consensus was that he would be an excellent starter.
So far, that's half true.
Jordan came off the bench Sunday and tied a career high by scoring 24 points to lead No. 24 St. John's to a 74-53 rout of Fordham in the ECAC Holiday Festival.
''I thought Rysheed played with poise,'' Red Storm coach Steve Lavin said. ''Played with the right pace. Near perfect game.''
"""
,"sport"),
("""Five-time world player of the year Marta scored three goals to lead Brazil to a 3-2 come-from-behind win over the U.S. women's soccer team in the International Tournament of Brasilia on Sunday. Carli Lloyd and Megan Rapinoe scored a goal each in the first 10 minutes to give the U.S. an early lead, but Marta netted in the 19th, 55th and 66th minutes to guarantee the hosts a spot in the final of the four-team competition.
"""
,"sport")
]

import re

# In[31]:


p_words = re.compile(r'\w+')


# p_words = re.compile(r'[^\n\r\t\.\:\,\d\!\?; ]+')
# p_words = re.compile(r'[\w\']+')


def parse_line(line):
    words = p_words.findall(line)
    return [w.lower() for w in words]


# ![TF-IDF](4.SNZ_tf-idf.png)

# # Caclulate Document Frequency (DF) and Inverser Document Frequency (IDF)

# In[32]:


import pprint
import math

df = {}
vocab = set()
documents = []
i = 0
for doc_text, label in train_data:
    words = parse_line(doc_text)
    # print(words)
    documents.append(words)
    # print(documents)
    words_set = set(words)
    # print(words_set)
    vocab.update(words_set)  # site zborovi vo korpusot (od site dokumenti)
    for word in words_set:
        # vo kolku dokumenti se srekjava ovoj zbor
        df.setdefault(word, 0)
        df[word] += 1
# pprint.pprint(df)
idf = {}
N = float(len(train_data))
for word, cdf in df.items():
    idf[word] = math.log(N / cdf)
#pprint.pprint(idf)


# # Calculate TF, normalized TF, and TF * IDF

# ## This is the training process

# In[33]:


def calc_vector(cur_tf_idf, vocabular):
    vec = []
    for word in vocab:
        tf_idf = cur_tf_idf.get(word, 0)
        vec.append(tf_idf)
    return vec


# In[34]:


def proccess_document(doc, idf, vocabular):
    if isinstance(doc, str):
        words = parse_line(doc)
    else:
        words = doc
    f = {}  # kolku pati se javuva sekoj zbor vo ovoj dokument
    for word in words:
        f.setdefault(word, 0)
        f[word] += 1
    #     pprint.pprint(f)
    max_f = max(f.values())  # kolku pati se javuva najcestiot zbor vo ovoj dokument
    tf_idf = {}
    for word, cnt in f.items():
        #         print(w,cnt)
        ctf = cnt * 1.0 / max_f
        tf_idf[word] = ctf * idf.get(word, 0)
    vec = calc_vector(tf_idf, vocabular)
    return vec


# In[35]:


freq = []
doc_vectors = []
w = []
tf_idfs = []
for words in documents:
    vec = proccess_document(words, idf, vocab)
    doc_vectors.append(vec)
#print(len(vocab))
#print(len(doc_vectors[0]))

# In[37]:


import math


def cosine_similarity(v1, v2):
    """compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"""
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


# # Caclulate the distances between documents

# In[38]:


distances = {}
for i in range(len(train_data) - 1):
    for j in range(i + 1, len(train_data)):
        v1 = doc_vectors[i]
        v2 = doc_vectors[j]
        dist = cosine_similarity(v1, v2)
        distances[(i, j)] = dist

# # Print the most similar document pairs

# In[40]:


sort_dist = sorted(distances.items(), key=lambda x: x[1], reverse=True)


# In[41]:


def proccess_document(doc, idf, vocabular):
    if isinstance(doc, str):
        words = parse_line(doc)
    else:
        words = doc
    f = {}  # kolku pati se javuva sekoj zbor vo ovoj dokument
    for word in words:
        f.setdefault(word, 0)
        f[word] += 1
    #     pprint.pprint(f)
    max_f = max(f.values())  # kolku pati se javuva najcestiot zbor vo ovoj dokument
    tf_idf = {}
    for word, cnt in f.items():
        #         print(w,cnt)
        ctf = cnt * 1.0 / max_f
        tf_idf[word] = ctf * idf.get(word, 0)
    vec = calc_vector(tf_idf, vocabular)
    return vec


# In[42]:


def rank_documents(doc, idf, vocabular, doc_vectors):
    query_vec = proccess_document(doc, idf, vocabular)
    similarities = []
    for i, doc_vec in enumerate(doc_vectors):
        dist = cosine_similarity(query_vec, doc_vec)
        similarities.append((dist, i))
    similarities.sort(reverse=True)
    return similarities


if __name__ == '__main__':
    text="""Upcoming Parks : 'Lost Corner' Finds New Life in Sandy Springs
          At the corner of Brandon Mill Road, where Johnson Ferry Road turns 
          into Dalrymple Road, tucked among 24 forested acres, sits an early 
          20th Century farmhouse. A vestige of Sandy Springs' past, the old home
           has found new life as the centerpiece of Lost Forest Preserve. While the 
           preserve isn't slated to officially debut until some time next year, the 
           city has opened the hiking trails to the public until construction begins on 
           the permanent parking lot (at the moment the parking lot is a mulched area). 
           The new park space includes community garden plots, a 4,000-foot-long hiking 
           trail and an ADA-accessible trail through the densely wooded site. For Atlantans 
           seeking an alternate escape to serenity (or those who dig local history), it's certainly 
           worth a visit."""


    najslicni=rank_documents(text, idf, vocab, doc_vectors)[:3]
    print(najslicni)
    docs=[]
    klasi=[]
    for v,index in najslicni:
        print(train_data[index])
        docs.append((train_data[index][0]))
        klasi.append((train_data[index][1]))

    k1=klasi[0]
    k2=klasi[1]
    k3=klasi[2]

    if k1==k2 or k1==k3:
        print(k1)
    elif k2==k3:
        print(k2)
    elif k1!=k2 and k1!=k3 and k2!=k3:
        print("unknown")


