# ============================================================================
# FILE: mark.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from defx.base.column import Base
from defx.context import Context
from neovim import Nvim


class Column(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'mark'

    def get(self, context: Context, candidate: dict) -> str:
        if candidate.get('is_selected', False):
            return '* '
        elif candidate.get('is_root', False):
            return '- '
        elif candidate['is_directory']:
            return '+ '
        else:
            return '  '
