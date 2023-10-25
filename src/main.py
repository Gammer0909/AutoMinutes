import datetime
import sys
import yamlconverter as yc
import jsonconverter as jc

def main():
    minutes_data = None
    if sys.argv[1] is not None:
        if sys.argv[1] == "--yaml" or sys.argv[1] == "-y":
            # Convert the yaml file into a minutes data object
            if sys.argv[2] == None:
                print("Error: No yaml file specified.")
                exit(1)
            minutes_data = yc.chunk_yaml(sys.argv[2])
        elif sys.argv[1] == "--json" or sys.argv[1] == "-j":
            # Convert the json file into a minutes data object
            if sys.argv[2] == None:
                print("Error: No json file specified.")
                exit(1)
            minutes_data = jc.chunk_json(sys.argv[2])
        else:
            print("Error: Invalid argument.")
            exit(1)
    else:
        print("Error: No argument specified.")
        exit(1)
    
    if minutes_data == None:
        print("Error: No minutes data object created.")
        exit(1)


    # Write the new file
    with open(f'{datetime.datetime.now()}.md', 'w') as output_file:
        output_file.write("# Borger Youth Advisory Council\n# Meeting Minutes")
        # Meeting Date, Time, and Location
        output_file.write(f"\n\n**Meeting Date: {minutes_data.meeting_date}**")
        output_file.write(f"\n**Meeting Time: {minutes_data.meeting_time}**")
        output_file.write(f"\n**Meeting Location: {minutes_data.meeting_location}**")
        # Attendees
        output_file.write("\n\n**Attendees:**")
        for attendee in minutes_data.attendees:
            output_file.write(f"\n- **{attendee}**")

        # Agenda
        i = 1
        output_file.write("\n\n**Agenda:**")
        for agenda_item in minutes_data.agenda:
            output_file.write(f"\n{i}. {agenda_item}")
            i += 1
        
        output_file.write("\n\n## Meeting Minutes:")

        # Meeting Summary
        output_file.write("\n\n**Meeting Summary:**")
        output_file.write(f"\n{minutes_data.meeting_summary}")

        # Agenda Items
        output_file.write("\n\nAgenda Items:")
        i = 1
        for agenda_item in minutes_data.agenda_items:
            output_file.write(f"\n\n**Agenda Item {i}:")
            output_file.write(f" {agenda_item.title}**")
            output_file.write("\n" + agenda_item.description)
            i += 1

        # Next Meeting
        output_file.write("\n\n**Next Meeting:**")
        output_file.write(f"\n{minutes_data.next_meeting}")

        # Adjournment Time
        output_file.write("\n\n**Adjournment Time:**")
        output_file.write(f"\n{minutes_data.adjournment_time}")
        
        # Signed by the Secretary
        output_file.write(f"*Respectfully Submitted by Kyle Garzon*\n*Tresurer and Secretary*\n*Date: {minutes_data.date}*")

        # Approved by
        output_file.write(f"\n*Approved By: The Chamber*\n*Date: {minutes_data.date}*")
    


if __name__ == "__main__":
    main()