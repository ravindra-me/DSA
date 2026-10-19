# ---- Generated import header (do not edit) ----
# Runs these tests against ../solutions by default. To test your own code, run
# from the day folder:
#   DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_03.py
import os
import sys
import unittest
from unittest import TestCase  # noqa: F401  (models often use the bare name)

_SOLUTIONS_DIR = os.environ.get("DSA_SOLUTIONS_DIR") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "solutions"
)
sys.path.insert(0, os.path.abspath(_SOLUTIONS_DIR))
from problem_03 import TextEditor  # noqa: E402
# ---- End of generated header ----

class TestTextEditor(TestCase):
    def test_example_1(self) -> None:
        editor = TextEditor()
        editor.type_char('a')
        editor.type_char('b')
        self.assertEqual(editor.get_text(), 'ab')
        editor.delete_char()
        self.assertEqual(editor.get_text(), 'a')
        editor.undo()
        self.assertEqual(editor.get_text(), 'ab')

    def test_example_2(self) -> None:
        editor = TextEditor()
        editor.delete_char()
        editor.undo()
        self.assertEqual(editor.get_text(), '')

    def test_empty_editor_queries_and_undo(self) -> None:
        editor = TextEditor()
        self.assertEqual(editor.get_text(), '')
        editor.undo()
        editor.undo()
        self.assertEqual(editor.get_text(), '')

    def test_single_character_lifecycle(self) -> None:
        editor = TextEditor()
        editor.type_char('x')
        self.assertEqual(editor.get_text(), 'x')
        editor.undo()
        self.assertEqual(editor.get_text(), '')
        editor.undo()
        self.assertEqual(editor.get_text(), '')

    def test_multiple_deletes_and_sequential_undos(self) -> None:
        editor = TextEditor()
        for ch in "hello":
            editor.type_char(ch)
        self.assertEqual(editor.get_text(), "hello")

        editor.delete_char()  # removes 'o'
        editor.delete_char()  # removes 'l'
        self.assertEqual(editor.get_text(), "hel")

        editor.undo()  # restores 'l'
        self.assertEqual(editor.get_text(), "hell")
        editor.undo()  # restores 'o'
        self.assertEqual(editor.get_text(), "hello")

    def test_undo_after_undo_does_not_redo(self) -> None:
        editor = TextEditor()
        editor.type_char('a')
        editor.type_char('b')
        editor.undo()  # removes 'b'
        self.assertEqual(editor.get_text(), 'a')
        editor.undo()  # removes 'a'
        self.assertEqual(editor.get_text(), '')
        editor.undo()  # stack now empty, no-op
        self.assertEqual(editor.get_text(), '')

    def test_noop_delete_does_not_affect_undo_history(self) -> None:
        editor = TextEditor()
        editor.type_char('a')
        editor.delete_char()  # text is now ''
        editor.delete_char()  # no-op
        editor.delete_char()  # no-op
        editor.undo()  # should undo the valid delete_char, restoring 'a'
        self.assertEqual(editor.get_text(), 'a')
        editor.undo()  # should undo the type_char('a')
        self.assertEqual(editor.get_text(), '')

    def test_large_scale_operations(self) -> None:
        import random
        rng = random.Random(42)
        editor = TextEditor()
        expected_chars: list[str] = []
        history_sim: list[tuple] = []

        # Perform 50,000 deterministic operations
        for _ in range(50000):
            op = rng.choice(['type', 'type', 'delete', 'undo'])
            if op == 'type':
                ch = rng.choice('abcdefghijklmnopqrstuvwxyz')
                editor.type_char(ch)
                expected_chars.append(ch)
                history_sim.append(('DEL',))
            elif op == 'delete':
                editor.delete_char()
                if expected_chars:
                    removed = expected_chars.pop()
                    history_sim.append(('ADD', removed))
            elif op == 'undo':
                editor.undo()
                if history_sim:
                    act = history_sim.pop()
                    if act[0] == 'DEL':
                        expected_chars.pop()
                    else:
                        expected_chars.append(act[1])

        self.assertEqual(editor.get_text(), ''.join(expected_chars))
