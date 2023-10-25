# Module docstring
"""This module contains the jsonconverter package."""

import json
import os
import sys
import datetime

"""Abstraction for the minutes data."""
class MinutesData:
    meeting_date = None # Date
    meeting_time = None # String
    meeting_location = None # String
    attendees = [] # List of Strings
    agenda = [] # List of Strings
    meeting_summary = None # String
    agenda_items = [] # List of AgendaItem
    next_meeting = None # String
    adjournment_time = None # Time
    date = datetime.datetime.today() # DateTime.now
    
    def __init__(self):
        pass

"""Abstraction for an agenda item."""
class AgendaItem:
    title = None # String
    description = None # String

"""Converts a json file to a MinutesData object."""
def chunk_json(json_path) -> MinutesData:
    # Take a json file and dump it into a MinutesData object
    
    # Open the file
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Create the MinutesData object
    minutes_data = MinutesData()

    # Dump the data into the MinutesData object
    minutes_data.meeting_date = json_data['meeting_date']
    minutes_data.meeting_time = json_data['meeting_time']
    minutes_data.meeting_location = json_data['meeting_location']
    minutes_data.attendees = json_data['attendees']
    minutes_data.agenda = json_data['agenda']
    minutes_data.meeting_summary = json_data['meeting_summary']
    # Oh, convert each item in the agenda_items list to an AgendaItem object, then dump it into the minutes_data object
    for agenda_item in json_data['agenda_items']:
        new_agenda_item = AgendaItem()
        new_agenda_item.title = agenda_item['title']
        new_agenda_item.description = agenda_item['description']
        minutes_data.agenda_items.append(new_agenda_item)
    minutes_data.next_meeting = json_data['next_meeting']
    minutes_data.adjournment_time = json_data['adjournment_time']

    # Return minutes_data
    return minutes_data