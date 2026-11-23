"""The channel-number sequence review must follow owner-assigned numbers.

Channel numbers are preserved verbatim and need not equal row position, so the
review-only check flags only malformed numbers and order inversions within a
group. Gaps and unnumbered alternate feeds are not sequence errors.
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def row(identity, name, number):
    chno = f' tvg-chno="{number}"' if number else ""
    return (
        f'#EXTINF:-1 tvg-id="{identity}" tvg-name="{name}"{chno} channel-id="{identity}" '
        f'tvg-country="BD" tvg-language="ben" tvg-logo="" group-title="Bangladesh",{name}\n'
        f'https://example.test/{identity}.m3u8\n'
    )


class ChannelNumberSequenceSemanticsTests(unittest.TestCase):
    def audit_section(self, rows):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "logos").mkdir()
            (root / "reports").mkdir()
            (root / "IPTV-Playlist.m3u").write_text(
                '#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Sports","Backup","Review"]\n' + "".join(rows),
                encoding="utf-8",
            )
            env = dict(os.environ, PYTHONPATH=str(ROOT / "scripts"))
            subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "audit_playlist.py")],
                cwd=root, env=env, capture_output=True, text=True,
            )
            report = (root / "reports" / "iptv-playlist-audit.md").read_text(encoding="utf-8")
        head = "## Primary Channel-Number Sequence (Review Only)"
        return report.split(head, 1)[1].split("\n## ", 1)[0]

    def test_gaps_and_unnumbered_rows_are_not_sequence_errors(self):
        section = self.audit_section([
            row("a.bd", "Alpha", "10"), row("b.bd", "Bravo", ""), row("c.bd", "Charlie", "40"),
        ])
        self.assertIn("No sequence discrepancies detected.", section)

    def test_order_inversions_and_malformed_numbers_are_still_reported(self):
        section = self.audit_section([
            row("a.bd", "Alpha", "10"), row("c.bd", "Charlie", "40"),
            row("d.bd", "Delta", "30"), row("e.bd", "Echo", "x7"), row("f.bd", "Foxtrot", "0"),
        ])
        self.assertIn("**Delta**", section)
        self.assertIn("**Echo**", section)
        self.assertIn("**Foxtrot**", section)
        self.assertNotIn("**Alpha**", section)
        self.assertNotIn("**Charlie**", section)


if __name__ == "__main__":
    unittest.main()
