from owslib.csw import CatalogueServiceWeb



def run():
    csw = CatalogueServiceWeb('http://gs.cens.am:8081/geoserver/ows?service=csw&version=2.0.2&request=GetCapabilities')
    csw.identification.type
    print([op.name for op in csw.operations])
    print(dir(csw))


if __name__ == "__main__":
    run()