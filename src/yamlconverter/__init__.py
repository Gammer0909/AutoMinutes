"""yamlconverter package init file."""
import yaml
import datetime

"""Abstraction for the minutes data."""
class MinutesData:
    meeting_date = None # String
    meeting_time = None # String
    meeting_location = None # String
    attendees = [] # List of Strings
    agenda = [] # List of Strings
    meeting_summary = None # String
    agenda_items = [] # List of AgendaItem
    next_meeting = None # String
    adjournment_time = None # Time
    date = datetime.datetime.now() # DateTime.now
    
    def __init__(self):
        pass

"""Abstraction for an agenda item."""
class AgendaItem:
    title = None # String
    description = None # String

"""Converts a yaml file to a MinutesData object."""
def chunk_yaml(yaml_path) -> MinutesData:
    # Make a new MinutesData object
    minutes_data = MinutesData()

    # Open the yaml file
    with open(yaml_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    # Dump the data into the MinutesData object
    minutes_data.meeting_date = yaml_data['meeting_date']
    minutes_data.meeting_time = yaml_data['meeting_time']
    minutes_data.meeting_location = yaml_data['meeting_location']
    minutes_data.attendees = yaml_data['attendees']
    minutes_data.agenda = yaml_data['agenda']
    minutes_data.meeting_summary = yaml_data['meeting_summary']
    # Oh, convert each item in the agenda_items list to an AgendaItem object, then dump it into the minutes_data object
    for agenda_item in yaml_data['agenda_items']:
        new_agenda_item = AgendaItem()
        new_agenda_item.title = agenda_item['title']
        new_agenda_item.description = agenda_item['description']
        minutes_data.agenda_items.append(new_agenda_item)
    minutes_data.next_meeting = yaml_data['next_meeting']
    minutes_data.adjournment_time = yaml_data['adjournment_time']

    # Return minutes_data
    return minutes_data