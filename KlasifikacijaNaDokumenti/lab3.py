"""
За секоја прочитан документ од стандарден влез да се испечатат зборовите кои се употребуваат за класификација,
класата и веројатноста на зборот да е од таа класа (заокружено на 4 децимали), како и тежинската веројатност на
зборот да припаѓа на класата (заокружено на 4 децимали). На крај да се испечати предвидената класа на документот
и логаритам со основа 2 од веројатноста со која се предвидува (заокружено на 4 децимали).

"""

import re
import math

train_data = [
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
     , "sport"),
    ("""Kobe Bryant and his teammates have an odd relationship. That makes sense: Kobe Bryant is an odd guy, and the Los Angeles Lakers are an odd team.
They’re also, for the first time this season, the proud owners of a three-game winning streak. On top of that, you may have heard, Kobe Bryant passed Michael Jordan on Sunday evening to move into third place on the NBA’s all-time scoring list.
"""
     , "sport"),
    ("""The Patriots continued their divisional dominance and are close to clinching home-field advantage throughout the AFC playoffs. Meanwhile, both the Colts and Broncos again won their division titles with head-to-head wins.The Bills' upset of the Packers delivered a big blow to Green Bay's shot at clinching home-field advantage throughout the NFC playoffs. Detroit seized on the opportunity and now leads the NFC North.
"""
     , "sport"),
    ("""If you thought the Washington Redskins secondary was humbled by another scintillating performance from New Yorks Giants rookie wide receiver sensation Odell Beckham Jr., think again.In what is becoming a weekly occurrence, Beckham led NFL highlight reels on Sunday, collecting 12 catches for 143 yards and three touchdowns in Sunday's 24-13 victory against an NFC East rival.
"""
     , "sport")
    , ("""That was two touchdowns and 110 total yards for the three running backs. We break down the fantasy implications.The New England Patriots' rushing game has always been tough to handicap. Sunday, all three of the team's primary running backs put up numbers, and all in different ways, but it worked for the team, as the Patriots beat the Miami Dolphins, 41-13.
"""
       , "sport"),
    ("""General Santos (Philippines) (AFP) - Philippine boxing legend Manny Pacquiao vowed to chase Floyd Mayweather into ring submission after his US rival offered to fight him next year in a blockbuster world title face-off. "He (Mayweather) has reached a dead end. He has nowhere to run but to fight me," Pacquiao told AFP late Saturday, hours after the undefeated Mayweather issued the May 2 challenge on US television. The two were long-time rivals as the "best pound-for-pound" boxers of their generation, but the dream fight has never materialised to the disappointment of the boxing world.
"""
     , "sport"),
    ("""When St. John's landed Rysheed Jordan, the consensus was that he would be an excellent starter.
So far, that's half true.
Jordan came off the bench Sunday and tied a career high by scoring 24 points to lead No. 24 St. John's to a 74-53 rout of Fordham in the ECAC Holiday Festival.
''I thought Rysheed played with poise,'' Red Storm coach Steve Lavin said. ''Played with the right pace. Near perfect game.''
"""
     , "sport"),
    ("""Five-time world player of the year Marta scored three goals to lead Brazil to a 3-2 come-from-behind win over the U.S. women's soccer team in the International Tournament of Brasilia on Sunday. Carli Lloyd and Megan Rapinoe scored a goal each in the first 10 minutes to give the U.S. an early lead, but Marta netted in the 19th, 55th and 66th minutes to guarantee the hosts a spot in the final of the four-team competition.
"""
     , "sport"),
]




splitter = re.compile('\\W')


def getwords(doc):
    words = splitter.split(doc)
    #     retained_words=set([word.lower() for word in words if 20>len(word)>2])
    retained_words = set()
    for word in words:
        if 2 < len(word) < 20:
            retained_words.add(word.lower())
    return retained_words


class documentClassifier:
    def __init__(self, getfeatures):
        # Broj na parovi atribut/kategorija (feature/category)
        self.featureCountsPerCategory = {}
        # Broj na dokumenti vo sekoja kategorija
        self.categoryCounts = {}
        # funkcija za dobivanje na atributite (zborovite) vo dokumentot
        self.getfeatures = getfeatures

    def incrementFeatureCountsPerCategory(self, currentFeature, currentCategory):
        #         print('incrementFeatureCountsPerCategory',self.featureCountsPerCategory)
        self.featureCountsPerCategory.setdefault(currentFeature, {})
        #         print('incrementFeatureCountsPerCategory',currentFeature, currentCategory)
        self.featureCountsPerCategory[currentFeature].setdefault(currentCategory, 0)
        self.featureCountsPerCategory[currentFeature][currentCategory] += 1

    #         print('incrementFeatureCountsPerCategory',self.featureCountsPerCategory)

    # Zgolemuvanje na brojot na predmeti(dokumenti) vo kategorija
    def incrementCategoryCounts(self, cat):
        self.categoryCounts.setdefault(cat, 0)
        #         print('incrementCategoryCounts',self.categoryCounts)
        self.categoryCounts[cat] += 1

    #         print('incrementCategoryCounts',self.categoryCounts)

    # Dobivanje na brojot kolku pati
    # odreden atribut se ima pojaveno vo odredena kategorija
    def getFeatureCountsPerCategory(self, currentFeature, currentCategory):
        if currentFeature in self.featureCountsPerCategory and currentCategory in self.featureCountsPerCategory[
            currentFeature]:
            v = float(self.featureCountsPerCategory[currentFeature][currentCategory])
        else:
            v = 0.0
        #         print('getFeatureCountsPerCategory',currentFeature, currentCategory, v)
        return v

    # Dobivanje na brojot na predmeti(dokumenti) vo kategorija
    def getCategoryCount(self, currentCategory):
        if currentCategory in self.categoryCounts:
            return float(self.categoryCounts[currentCategory])
        return 0

    # Dobivanje na vkupniot broj na predmeti
    def getTotalCount(self):
        v = sum(self.categoryCounts.values())
        #         print('Dobivanje na vkupniot broj na dokumenti:', v)
        return v

    # Dobivanje na lista na site kategorii
    def categories(self):
        return self.categoryCounts.keys()

    def train(self, item, currentCategory):
        # Se zemaat atributite (zborovite) vo predmetot(dokumentot)
        features = self.getfeatures(item)
        #         print(item, currentCategory)
        #         print(features)
        # Se zgolemuva brojot na sekoj atribut vo ovaa kategorija
        for currentFeature in features:
            self.incrementFeatureCountsPerCategory(currentFeature, currentCategory)

        # Se zgolemuva brojot na predmeti (dokumenti) vo ovaa kategorija
        self.incrementCategoryCounts(currentCategory)

    #         print('incrementCategoryCounts',self.categoryCounts)
    #         print(item, currentCategory, self.featureCountsPerCategory)
    #         print()

    def getFeaturePerCategoryProbability(self, currentFeature, currentCategory):
        if self.getCategoryCount(currentCategory) == 0: return 0
        # Verojatnosta e vkupniot broj na pati koga
        # ovoj atribut f (zbor) se pojavil vo ovaa
        # kategorija podeleno so vkupniot broj na
        # predmeti (dokumenti) vo ovaa kategorija
        return self.getFeatureCountsPerCategory(currentFeature, currentCategory) / self.getCategoryCount(
            currentCategory)

    def weightedprob(self, currentFeature, currentCategory, weight=1.0, ap=0.5):
        # Presmetaj ja osnovnata verojatnost
        basicprob = self.getFeaturePerCategoryProbability(currentFeature, currentCategory)
        # Izbroj kolku pati se ima pojaveno ovoj atribut (zbor)
        # vo site kategorii
        totals = sum([self.getFeatureCountsPerCategory(currentFeature, currentCategory) for currentCategory in
                      self.categories()])
        # Presmetaj ja tezinski usrednetata verojatnost
        bp = ((weight * ap) + (totals * basicprob)) / (weight + totals)
        return bp


class naivebayes(documentClassifier):
    def __init__(self, getfeatures):
        documentClassifier.__init__(self, getfeatures)
        self.thresholds = {}

    def setThreshold(self, currentCategory, threshold):
        self.thresholds[currentCategory] = threshold

    def getThreshold(self, currentCategory):
        if currentCategory not in self.thresholds: return 1.0
        return self.thresholds[currentCategory]

    # ja vrakja verojatnosta na dokumentot da e od klasata cat (cat e odnapred poznata)
    def caclulateDocumentProbabilityInClass(self, item, currentCategory):
        # zemi gi zborovite vo dokumentot item
        features = self.getfeatures(item)
        # pomnozi gi verojatnostite na site zborovi
        p = 1
        for currentFeature in features:
            w = self.weightedprob(currentFeature, currentCategory)
            p *= w
        #             print(currentFeature, currentCategory, w, p)
        #         print(item, currentCategory, p)
        return p

    # Ja vrakja verojatnosta na klasata ako e poznat dokumentot
    def getCategoryProbabilityForDocument(self, item, currentCategory):
        catprob = self.getCategoryCount(currentCategory) / self.getTotalCount()*1.0
        caclulateDocumentProbabilityInClass = self.caclulateDocumentProbabilityInClass(item, currentCategory)
        return caclulateDocumentProbabilityInClass * catprob/(1.0/self.getTotalCount())

    # klasificiranje na dokument
    def classifyDocument(self, item, default=None):
        probs = {}
        # najdi ja kategorijata (klasata)
        # so najgolema verojatnost
        maxp = 0.0
        for cat in self.categories():
            probs[cat] = self.getCategoryProbabilityForDocument(item, cat)
            #print(probs[cat], cat)
            if probs[cat] > maxp:
                maxp = probs[cat]
                best = cat

        # proveri dali verojatnosta e pogolema od
        # threshold*next best (sledna najdobra)
        for cat in probs:
            if cat == best: continue
            if probs[cat] * self.getThreshold(cat) > probs[best]:
                return default

        return best, maxp




if __name__=="__main__":


    m = naivebayes(getwords)
    if len(train_data) > 0:
      for i in train_data:
        m.train(i[0], i[1])

    doc = input()

    zborovi = list(m.getfeatures(doc))
    categorii = m.categoryCounts.keys()
    
    for z in zborovi:
        for c in categorii:
            verojatnost = round(m.getFeaturePerCategoryProbability(z, c), 4)
            tezinskaVero = round(m.weightedprob(z, c), 4)
            print(z, c, verojatnost, tezinskaVero)

    klasa, verojatnost = m.classifyDocument(doc)
    print(klasa, round(math.log(verojatnost,2),4))