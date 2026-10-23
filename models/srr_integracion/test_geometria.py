import math
import unittest
from geometria import square_bipyramid, export_obj

class GeometryTests(unittest.TestCase):
    def test_all_unique_edges_have_the_user_length(self):
        vertices, edges = square_bipyramid(0.05)
        self.assertEqual(len(vertices), 6)
        self.assertEqual(len(set(tuple(sorted(e)) for e in edges)), 12)
        for a, b in edges:
            self.assertAlmostEqual(math.dist(vertices[a], vertices[b]), 0.05, places=14)

    def test_square_base_and_common_center(self):
        v, _ = square_bipyramid(0.05)
        self.assertEqual([p[2] for p in v[:4]], [0, 0, 0, 0])
        self.assertAlmostEqual(math.dist(v[0], v[2]), 0.05 * math.sqrt(2))
        self.assertEqual(v[4][:2], (0, 0))
        self.assertEqual(v[5][:2], (0, 0))
        self.assertAlmostEqual(v[4][2], -v[5][2])

    def test_export_units_and_closed_face_topology(self):
        v, e = square_bipyramid(0.05)
        result = export_obj(v, e)
        self.assertEqual(sum(line.startswith("v ") for line in result.splitlines()), 6)
        self.assertEqual(sum(line.startswith("l ") for line in result.splitlines()), 12)
        self.assertIn("units m", result)
        faces = [tuple(int(x) for x in line.split()[1:]) for line in result.splitlines() if line.startswith("f ")]
        self.assertEqual(len(faces), 8)
        uses = {}
        for face in faces:
            for a, b in zip(face, face[1:] + face[:1]):
                key = tuple(sorted((a, b)))
                uses.setdefault(key, []).append((a, b))
        self.assertEqual(len(uses), 12)
        for directions in uses.values():
            self.assertEqual(len(directions), 2)
            self.assertEqual(directions[0], directions[1][::-1])

    def test_invalid_lengths_fail(self):
        for length in (0, -1, float("nan"), float("inf"), True):
            with self.subTest(length=length), self.assertRaises(ValueError):
                square_bipyramid(length)

if __name__ == "__main__":
    unittest.main()
