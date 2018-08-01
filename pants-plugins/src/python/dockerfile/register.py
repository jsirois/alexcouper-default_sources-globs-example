from pants.build_graph.build_file_aliases import BuildFileAliases

from dockerfile.targets.dockerfile import Dockerfile


def build_file_aliases():
  return BuildFileAliases(
    targets={
      'dockerfile': Dockerfile,
    }
  )

