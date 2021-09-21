# @st.cache
def process_rss(headings):
    nlp = spacy.load("en_core_web_sm")
    for title in headings:
        doc = nlp(title.text)
        # spacy.displacy.render(doc, style='ent', jupyter=True, options={'distance': 120})
        visualize_ner(doc, labels=['ORG', 'PERSON', 'DATE', 'GPE', 'PERCENT'],
                     show_table=False)
        print("Done----------")
    return


def viz_ner():
    with open("./data/History_102.txt") as file:
        text = file.read()
    print(type(text))
    doc = nlp(text)
    visualize_ner(doc, labels=['ORG', 'PERSON', 'DATE', 'GPE', 'PERCENT'],
                    show_table=False)
    return


# txt_file = st.file_uploader("Upload a doc", type=['txt'])

# if txt_file is not None:
#     stringio = StringIO(txt_file.getvalue().decode('utf-8'))
#     string_data = stringio.read()
#     viz_ner()
# else:
#     st.warning("Please upload an image.")
#     st.stop()
    