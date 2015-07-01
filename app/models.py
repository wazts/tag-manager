"""
    views.py
--------------------------------------------------------------------------------
    The model for tag manager
--------------------------------------------------------------------------------
    @author Kyle Wagner
    @date 2015
--------------------------------------------------------------------------------
"""

from app import db
from flask.ext.sqlalchemy import SQLAlchemy
import requests

class Tag(db.Model):
    """ The tag model
        The tag system for the beacon project
    """
    id = db.Column(db.Integer, primary_key=True)
    
    # The beacon we are tagging. We will get this id from the database.
    beacon_id = db.Column(db.Integer, nullable=False)
    
    # The distance to the beacon in meters
    distance = db.Column(db.Float(), nullable=False)
    
    # The owner of this tag. This owner is the overall user of the system and
    # not the sub user.
    owner_id = db.Column(db.Integer, nullable=False)
    
    # The unique session this tag belongs to. This can be an event such as 
    # conference.
    session_id = db.Column(db.Integer, nullable=False)
    
    # The unique string that the owner sends for us to track individuals. 
    creator_id = db.Column(db.String(64))
    
    # The date the tag was created.
    created_on = db.Column(db.DateTime, server_default=db.func.now())


    def __init__(self, uuid, major, minor, distance, creator_id, session_id, owner_id=None):
        """ 
        Init the tag with the beacon info. We will look up this info rather 
        rely on the user input.
        """
        self.creator_id = creator_id
        self.session_id = session_id
        self.owner_id = owner_id
        
        # Look up the beacon.
        pass

    def __repr__(self):
        return '<User %r>' % self.id