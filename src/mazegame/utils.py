#!/usr/bin/env python
# coding=utf-8
class GameWon(Exception):
    """Raised when answer has been guessed."""


class GameLost(Exception):
    """Raised when out of turns."""


class GameOverNotificationComplete(Exception):
    """Raised when controller should break game loop."""
