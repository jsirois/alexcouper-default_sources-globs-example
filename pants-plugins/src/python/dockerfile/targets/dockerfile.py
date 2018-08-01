from pants.base.payload import Payload
from pants.build_graph.target import Target


class Dockerfile(Target):

    def __init__(self,
                 sources=None,
                 address=None,
                 **kwargs):
        
        payload = Payload()

        payload.add_fields({
            'sources': self.create_sources_field(
                sources, 
                address.spec_path, 
                key_arg='sources'
            )
        })
        super(Dockerfile, self).__init__(
            address=address,
            payload=payload,
            **kwargs
        )

    default_sources_globs = "Dockerfile"
