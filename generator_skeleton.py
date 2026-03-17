"""Maze generation module — core MazeGenerator class."""

from typing import Optional


# Wall bit flags (used in the hex output and internal grid)
NORTH = 0b0001  # bit 0
EAST  = 0b0010  # bit 1
SOUTH = 0b0100  # bit 2
WEST  = 0b1000  # bit 3

# Opposite wall for each direction
OPPOSITE: dict[int, int] = {
    NORTH: SOUTH,
    EAST:  WEST,
    SOUTH: NORTH,
    WEST:  EAST,
}

# (dx, dy) movement for each direction
DIRECTION_DELTA: dict[int, tuple[int, int]] = {
    NORTH: (0, -1),
    EAST:  (1,  0),
    SOUTH: (0,  1),
    WEST:  (-1, 0),
}

# Letter used in the solution path output
DIRECTION_LETTER: dict[int, str] = {
    NORTH: "N",
    EAST:  "E",
    SOUTH: "S",
    WEST:  "W",
}


class MazeGenerator:
    """Generates a random maze and exposes its structure and solution.

    Usage example::

        gen = MazeGenerator(width=20, height=15, seed=42, perfect=True)
        gen.generate()
        print(gen.to_hex_grid())
        print(gen.solution_path())

    Attributes:
        width:   Number of columns.
        height:  Number of rows.
        seed:    RNG seed for reproducibility (None = random).
        perfect: If True, maze has exactly one path between entry and exit.
        entry:   (x, y) entry cell.
        exit:    (x, y) exit cell.
        grid:    2-D list[list[int]] of wall bitmasks, grid[y][x].
                 A set bit means that wall is CLOSED.
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int] = (0, 0),
        exit: tuple[int, int] | None = None,
        seed: Optional[int] = None,
        perfect: bool = True,
    ) -> None:
        """Initialise generator parameters (does not generate yet)."""
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit if exit is not None else (width - 1, height - 1)
        self.seed = seed
        self.perfect = perfect

        # Populated by generate()
        self.grid: list[list[int]] = []
        self._solution: list[str] = []

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def generate(self) -> None:
        """Generate the maze in-place, populating self.grid."""
        self._init_grid()
        self._carve_passages()
        self._embed_42()
        self._solve()

    def cell(self, x: int, y: int) -> int:
        """Return the wall bitmask for cell (x, y)."""
        return self.grid[y][x]

    def is_wall(self, x: int, y: int, direction: int) -> bool:
        """Return True if the given wall of cell (x, y) is closed."""
        return bool(self.grid[y][x] & direction)

    def solution_path(self) -> list[str]:
        """Return the shortest path as a list of direction letters."""
        return list(self._solution)

    def solution_path_str(self) -> str:
        """Return the shortest path as a single string e.g. 'NESSWW'."""
        return "".join(self._solution)

    def to_hex_grid(self) -> list[str]:
        """Return the grid as rows of hex characters (one char per cell)."""
        return [
            "".join(format(self.grid[y][x], "X") for x in range(self.width))
            for y in range(self.height)
        ]

    # ------------------------------------------------------------------
    # Private helpers (stubs — to be implemented)
    # ------------------------------------------------------------------

    def _init_grid(self) -> None:
        """Allocate grid with all walls closed (0xF per cell)."""
        self.grid = [
            [0xF for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def _carve_passages(self) -> None:
        """Carve passages through the grid using the chosen algorithm."""
        # TODO: implement (recursive backtracker)
        raise NotImplementedError

    def _embed_42(self) -> None:
        """Embed the '42' pattern as fully closed cells inside the maze."""
        # TODO: place the '42' glyph; print error if maze is too small
        raise NotImplementedError

    def _solve(self) -> None:
        """Compute shortest path from entry to exit (BFS)."""
        # TODO: BFS over self.grid; store result in self._solution
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Dunder helpers
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        """Short developer representation."""
        return (
            f"MazeGenerator(width={self.width}, height={self.height}, "
            f"seed={self.seed}, perfect={self.perfect})"
        )
