from guillotina.behaviors.properties import ContextProperty
from guillotina.behaviors.instance import AnnotationBehavior
from guillotina.interfaces import IResource
from guillotina import configure, schema
from zope.interface import Interface

class IMarckerBehavior(Interface):
    """Marker interface for content with attachment."""


class IMySocketBehavior(Interface):
    websocket = schema.List()

@configure.behavior(
    title="Socket_Attachmant",
    provides=IMySocketBehavior,
    marker=IMarkerBehavior,
    for_=IResource)
class MySocketBehavior(AnnotationBehavior):
    """If attributes
    """
