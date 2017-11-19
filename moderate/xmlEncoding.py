class Attribute(object):
    def __init__(self, tag, vals):
        self.tag = tag
        self.value = vals

    def addVals(self, x):
        self.value.append(x)

class Element(object):
    def __init__(self, tag, attributes, child):
        self.tag = tag
        self.attributes = attributes
        self.children = child

    def addChild(self, child):
        self.children.append(child)

    def addAttributes(self, attr):
        self.attributes.append(attr)

def xmlEncoding(element):
    def xmLEncodingHelper(element):
        res = []
        if not element.tag : #we have only a text child
            res.append(element.children[0])
            return res
        #print(res, element.tag, mapping[element.tag])
        res.append(mapping[element.tag])
        for att in element.attributes :
            tag, val = att.tag, att.value
            res.append(mapping[tag])
            res.append(val)
        res.append(0)
        children = element.children
        for child in children :
            res += xmLEncodingHelper(child)
        res.append(0)
        return res

    mapping = {
        "family": 1, "person": 2, "firstName": 3, "lastName": 4, "state": 5
    }
    res = xmLEncodingHelper(element)
    return " ".join(map(str, res))

if __name__ == "__main__":
    att1 = Attribute("firstName", "Gayle")
    att2 = Attribute("lastName", "McDowell")
    att3 = Attribute("state", "CA")
    att4 = Attribute("firstName", "Julia")
    att5 = Attribute("firstName", "Lucy")
    child1 = Element("person", [att1], [Element(None, None, ["Boy"])])
    child2 = Element("person", [att4], [Element(None, None, ["Girl"])])
    child3 = Element("person", [att5], [Element(None, None, ["Girl"])])
    children = [child3, child1, child2]
    element = Element("family", [att2, att3], children)
    print(xmlEncoding(element))




