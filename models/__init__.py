from models.Match import Match
from models.AllHalfTime import AllHalfTime
from models.AllHighlights import AllHighlights
from models.HighlightsRow import HighlightsRow
from models.Videos import Videos

def factory_models():
    return {"Match": Match(),
            "AllHalfTime":AllHalfTime(),
            "AllHighlights":AllHighlights(),
            "Videos":Videos()}

