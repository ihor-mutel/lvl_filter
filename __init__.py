
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

    #TODO lvl == 0; review == 0 -> show word translation
    # f = open("/Users/ihor/Library/Application Support/Anki2/addons21/2055492100/log.txt", "a")
    # f.write(str(context.card()))
    # f.write("\n")
    # f.write(str(context.note()))
    # f.write("\n")
    # f.write(str(context.fields()))
    # f.write("\n")
    # f.write(str(context.fields()))
    # f.write("\n")
    # f.write(str(context.fields()["translation"]))
    # f.write("\n")
    # f.write(str(output))
    # f.write("\n")
    # f.close()
    # word {
    # debug {

    # output.question_text += f"<style>#debug {{ display: block; }}</style>"
    #
    # if context.card().did == gc("deckId") and context.card().ivl < 5 and context.card().reps > 5:
    #     output.question_text += f"<style>#word {{ color: red; }}</style>"
    #
    if context.card().did == gc("deckId") and context.card().reps > 10:
        output.question_text += f"<style>#gif {{ display: none; }}</style>"

    if context.card().did == gc("deckId") and context.card().ivl == 0 and context.card().reps == 0:
        output.question_text += f"<style>.hint {{ display: block; }}</style>"

    if context.card().did == gc("deckId") and context.card().ivl > gc("maxLevel"):
        output.question_text += f"<style>#gif, #context {{ display: none; }}</style>"
        output.question_av_tags = [output.answer_av_tags[0]]

    #todo move (in template) gif audio as third audio in answer, add it to array here
    #sys.stderr.write(str(context.card().did))

# register our function to be called when the hook fires
hooks.card_did_render.append(on_card_did_render)