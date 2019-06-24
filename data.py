import spacy
from spacy import displacy

nlp=spacy.load('en_core_web_sm')
docx=nlp('''Return Amount. Subject to Paragraphs 4 and 5, upon a demand made by the Obligor on or promptly following a Valuation Date, if the Return Amount for that Valuation Date equals or exceeds the Obligee's Minimum Transfer Amount, then the Obligee will Transfer to the Obligor Posted Credit Support as specified by the Obligor in that demand having a Value as of the date of Transfer as close as practicable to the applicable Return Amount (rounded pursuant to Paragraph 13); provided, however, that where such Posted Credit Support consists of Posted Lending Collateral in the form of securities, the Obligee may Transfer to the Obligor Equivalent Collateral or repay cash equivalent thereof in the currency in which such securities are denominated or in Termination Currency. For this purpose, Transfer of the cash equivalent of any Posted Lending Collateral shall be deemed to be a return of such Posted Lending Collateral. However, solely for the purpose of this Paragraph 3(b), the Obligee's right to repay any cash equivalent is subject to the prior consent of the Obligor. Unless otherwise specified in Paragraph 13, the "Return Amount" applicable to the Obligee for any Valuation Date will equal the amount by which:

the Value as of that Valuation Date of all Posted Credit Support held by the Obligee exceeds the Credit Support Amount.

"Credit Support Amount" means, unless otherwise specified in Paragraph 13, for any Valuation Date
(i) the Obligee's Exposure for that Valuation Date plus (ii) the aggregate of all Independent Amounts applicable to the Obligor, if any, minus (iii) all Independent Amounts applicable to the Obligee, if any, minus (iv) the Obligor's Threshold; provided however, that the Credit Support Amount will be deemed to be zero whenever the calculation of the Credit Support Amount yields a number less than zero.''')
#for i,token in enumerate(docx):
    #print ((i,token,token.pos_))

for sent in docx.sents:
    print(sent)

with docx.retokenize() as retokenizer:
    for np in list(docx.noun_chunks):
        attrs = {
            "tag": np.root.tag_,
            "lemma": np.root.lemma_,
            "ent_type": np.root.ent_type_,
        }
        retokenizer.merge(np, attrs=attrs)
for token in docx:
    print(token.text,token.pos_)

