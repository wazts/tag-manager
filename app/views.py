"""
    views.py
--------------------------------------------------------------------------------
    The RESTful endpoints for the user manager
--------------------------------------------------------------------------------
    @author Kyle Wagner
    @date 2015
--------------------------------------------------------------------------------
"""

from flask import Flask, request
from flask.ext.restful import Resource, Api, fields, marshal_with, reqparse, abort
from app import api, db
from app.models import Tag

tag_fields = {
    'uri': fields.Url('tag_info'),
}

class TagsInfo(Resource):
    """ Get the info for all tags """
    
    @marshal_with(tag_fields)
    def get(self):
        
        tags = Tag.query.all()
        
        if tags:
            return tags
            
        abort(404, message="No tags exist")
    
    @marshal_with(tag_fields)
    def post(self):
        pass
        
class TagInfo(Resource):
    """ Get the tag """
    
    @marshal_with(tag_fields)
    def get(self, id):
        
        tag = Tag.query.filter_by(id=id).first()
        
        # Make sure we have the user
        if tag:
            return tag
        
        abort(404, message="Tag {} doesn't exist".format(id))

    """ Delete the user
        Delete the user if we have the rights
    """
    def delete(self, user_id):
        pass
        
        
# Register views
api.add_resource(TagsInfo, '/tags/', endpoint='tags_info')
api.add_resource(TagInfo, '/tags/<int:id>', endpoint='tag_info')