import sys
from pathlib import Path

from invoke import Collection

# Ensure the repo root (parent of tasks/) is importable so `modules.*` resolves
# regardless of how invoke was invoked.
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from .common import debug, ruff, setup  # noqa: E402  # pylint: disable=wrong-import-position
from .common import main as common_main  # noqa: E402  # pylint: disable=wrong-import-position
from .tests import namespace as tests_namespace  # noqa: E402  # pylint: disable=wrong-import-position

namespace = Collection(auto_dash_names=False)

# `common/` and `tests/` are the only two subpackages here — `tasks/` in this base template is
# deliberately as small as possible (debug/ruff/setup + the fix/test aliases, plus the tests
# themselves), everything project-specific (repo/template sync, AI-agent tooling, versioning)
# lives downstream in template_ai_python instead. Both stay registered at their original
# top-level names (`debug.*`, `ruff.*`, `setup.*`, `tests.*`, plus bare `fix`/`test`) rather than
# nested under `common.*`/`tests.*` prefixes that don't exist — every repo that clones this
# template inherits that exact CLI surface.
namespace.add_collection(debug, name="debug")
namespace.add_collection(ruff, name="ruff")
namespace.add_collection(setup, name="setup")
namespace.add_collection(tests_namespace, name="tests")

namespace.add_task(common_main.fix, name="fix")
namespace.add_task(common_main.test, name="test")
