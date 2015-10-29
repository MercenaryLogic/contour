from predicate import predicate
from rdflib import RDF, OWL


class OwlProperty(predicate):
    """
    OWL Property Type
    """
    name = "ObjectProperty"
    rdf_type = RDF.Property
    pred = OWL.Thing
    inverseOf = None
    range_type = OWL.Thing
    valid_ranges = [OWL.Thing]
    