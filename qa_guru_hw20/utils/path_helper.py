import os
import qa_guru_hw20
def abs_path_from_project(rel_pat: str):
    return os.path.abspath(os.path.join(os.path.dirname(qa_guru_hw20.__file__),  '..', rel_pat))