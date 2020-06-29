
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
An example of how you can transform the rendered card content in Anki 2.1.20.
"""

from typing import Tuple

import sys
from anki import hooks
from anki.template import TemplateRenderContext, TemplateRenderOutput
from anki.sound import SoundOrVideoTag
from aqt import mw
from anki.cards import Card
from anki.notes import Note

def gc(arg, fail=False):
    return mw.addonManager.getConfig(__name__).get(arg, fail)

def on_card_did_render(output: TemplateRenderOutput, context: TemplateRenderContext):

    if context.card().did == gc("deckId") and context.card().ivl > gc("maxLevel"):
        output.question_text += f"<style>#gif, #context {{ display: none; }}</style>"
        output.question_av_tags = [output.answer_av_tags[0]]

    #sys.stderr.write(str(context.card().did))

# register our function to be called when the hook fires
hooks.card_did_render.append(on_card_did_render)