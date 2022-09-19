from .video import Video

from typing import  Iterator, List

class VidBean:

    #List with all fetched videos
    vidList : List[Video]
    """List with all fetched videos."""

    #cursor value to know what page we are in
    cursorValue : int 
    """Cursor value to know what page we are in."""

    #to know if there are more videos to fetch
    hasMore : bool
    """To know if there are more videos to fetch."""

    def __init__(self):
        self.vidList = []
        self.hasMore = False
        self.cursorValue = 0

