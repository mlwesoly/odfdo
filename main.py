from odfdo import *


def print_hi():
    doc = Document("./Untitled1.odt")
    body = doc.body
    with open("reportAll") as file:
        # print(file.read())
        for line in file.readlines():
            if "Header01" in line:
                paragraph = Paragraph(line, style="Heading 1")
            else:
                paragraph = Paragraph(line)
            body.append(paragraph)
        doc.save("./Untitled1.odt")


def hello():
    doc = Document("./Untitled1.odt")
    body = doc.body
    toc = doc.body.get_toc()
    # print(f"{toc}")

    # header = Header(1, 'HHHH')
    # doc.body.append(header)
    # toc.fill()

    doc.body.replace("XXXXX", "20_24_1.001")  # .*([0-9]{2}.*[0-9]{2}.*[0-9].*[0-9]{3}).*
    # h = doc.body.get_references()
    # for ref in h:
    # ref.update()
    # print(f"{ref.tag}")

    h = doc.body.get_user_defined_list()  # get_reference_marks()
    # h[0].replace("XXXXX","20_24_1.001")
    for ref in h:
        print(f"{ref}")

    # h = doc.body.get_toc().children[0]
    # h.update()
    print(f"{h}")
    doc.save("./output.odt")

def playtoc():
    doc = Document("./onlytoc.odt")
    body = doc.body
    toc = doc.body.get_toc().children
    toc.fill()
    doc.save("./output.odt")

def testexample():
    doc = Document('./document.odt')
    toc = doc.body.get_toc()
    header = Header(1,'HHHH')
    doc.body.append(header)
    header = Header(2,'HHHH')
    doc.body.append(header)
    toc.fill(use_default_styles = True)
    print(toc)  # to print only the end of TOC
    #for header in doc.body.get_headers():
    #    print(f"{header}")
    #    level = header.get_attribute_integer("text:outline-level")
    #    print(f"{level}")
    doc.save('./document.odt')

    #doc = Document('./document1.odt')
    #toc = doc.body.get_toc()
    #toc.fill()
    #doc.save('./document1.odt')



if __name__ == '__main__':
    testexample()
    # hello()
    # playtoc()
    # print_hi()
