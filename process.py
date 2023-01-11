import stanza
import csv

rela_dict = {"acomp": "adjectival complement", "advcl": "adverbial clause modifier", "advmod": "adverb modifier",
             "agent": "agent", "amod": "adjectival modifier", \
             "appos": "appositional modifier", "aux": "auxiliary", "auxpass": "passive auxiliary", "cc": "coordination",
             "ccomp": "clausal complement", "conj": "conjunct", \
             "cop": "copula", "csubj": "clausal subject", "csubjpass": "clausal passive subject", "dep": "dependent",
             "det": "determiner", "discourse": "discourse element", \
             "dobj": "direct object", "expl": "expletive", "goeswith": "goes with", "iobj": "indirect object",
             "mark": "marker", "mwe": "multi-word expression", "neg": "negation modifier", \
             "nn": "noun compound modifier", "npadvmod": "noun phrase as adverbial modifier",
             "nsubj": "nominal subject", "nsubjpass": "passive nominal subject", "num": "numeric modifier", \
             "number": "element of compound number", "parataxis": "parataxis", "pcomp": "prepositional complement",
             "pobj": "object of a preposition", "poss": "possession modifier", \
             "possessive": "possessive modifier", "preconj": "preconjunct", "predet": "predeterminer",
             "prep": "prepositional modifier", "prepc": "prepositional clausal modifier",
             "prt": "phrasal verb particle", \
             "punct": "punctuation", "quantmod": "quantifier phrase modifier", "rcmod": "relative clause modifier",
             "ref": "referent", "root": "root", "tmod": "temporal modifier", \
             "vmod": "reduced non - finite verbal modifier", "xcomp": "open clausal complement",
             "xsubj": "controlling subject"
             }
proxies = {'http':'http://10.246.112.38:22','https': 'http://10.246.112.38:22' }
stanza.download('en',proxies=proxies)
nlp = stanza.Pipeline('en')
for data_name in ['test']:
    with open(f'data/{data_name}.csv','r',newline='',encoding='utf-8') as f:
        data = csv.reader(f,delimiter='\t')
        with open(f'data/{data_name}_stanza.csv','w',newline='',encoding='utf-8') as f1:
            writer = csv.writer(f1,delimiter='\t')
            for i in data:
                sent0 = i[5]
                sent1 = i[6]
                doc0 = nlp(sent0)
                text0 = []
                rela0 = ""
                doc1 = nlp(sent1)
                text1 = []
                rela1 = ""
                for word in doc0.sentences[0].words:
                    text0.append(word.text)
                for word in doc0.sentences[0].words:
                    word.deprel = word.deprel.replace(":", "")
                    if word.head == 0:
                        rela0 = rela0 + word.text + ": " + rela_dict[word.deprel] + ", "
                    else:
                        if word.deprel in rela_dict.keys():
                            rela0 = rela0 + word.text + ': ' + rela_dict[word.deprel] + ": " + text0[
                                word.head - 1] + ", "
                        else:
                            rela0 = rela0 + word.text + ': ' + word.deprel + ": " + text0[word.head - 1] + ", "
                    # print(word.text, word.head, word.deprel)
                for word in doc1.sentences[0].words:
                    text1.append(word.text)
                for word in doc1.sentences[0].words:
                    word.deprel = word.deprel.replace(":", "")
                    if word.head == 0:
                        rela1 = rela1 + word.text + ": " + rela_dict[word.deprel] + ", "
                    else:
                        if word.deprel in rela_dict.keys():
                            rela1 = rela1 + word.text + ': ' + rela_dict[word.deprel] + ": " + text1[
                                word.head - 1] + ", "
                        else:
                            rela1 = rela1 + word.text + ': ' + word.deprel + ": " + text1[word.head - 1] + ", "
                    # print(word.text, word.head, word.deprel)
                i0 = f"text:{sent0}, syntax structure:{rela0}"
                i1 = f"text:{sent1}, syntax structure:{rela1}"
                writer.writerow([i[0],i[1],i[2],i[3],i[4],i0,i1])



