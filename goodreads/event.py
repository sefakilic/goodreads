"""Class for GoodreadsEvent"""


class GoodreadsEvent:
    def __init__(self, event_dict):
        self._event_dict = event_dict

    def __repr__(self):
        return self.title

    @property
    def gid(self):
        """ID for the event"""
        return self._event_dict['id']

    @property
    def title(self):
        """Title for the event"""
        return self._event_dict['title']

    @property
    def description(self):
        """Description for the event"""
        return self._event_dict['description']

    @property
    def link(self):
        """Link for the event"""
        return self._event_dict['link']

    @property
    def venue(self):
        """Venue for the event"""
        return self._event_dict['venue']

    @property
    def address(self):
        """Address for the event"""
        return self._event_dict['address']

    @property
    def city(self):
        """City for the event"""
        return self._event_dict['city']

    @property
    def postal_code(self):
        """Postal code for the event"""
        return self._event_dict['postal_code']

    @property
    def state_code(self):
        """State for the event"""
        return self._event_dict['state_code']

    @property
    def country_code(self):
        """Country code for the event"""
        return self._event_dict['country_code']

    @property
    def access(self):
        """Is event public or private?"""
        return self._event_dict['access']

    @property
    def event_type(self):
        """Type of the event"""
        return self._event_dict['event_type']

    @property
    def added_by(self):
        """User id for the event creator"""
        return self._event_dict['user_id']['#text']

    @property
    def image_url(self):
        """Image URL for the event"""
        return self._event_dict['image_url']

    @property
    def created_at(self):
        """Event created at"""
        return self._event_dict['created_at']['#text']

    @property
    def updated_at(self):
        """Event updated at"""
        return self._event_dict['updated_at']['#text']

    @property
    def reminder_at(self):
        """Reminder time for the event"""
        return self._event_dict['reminder_at']['#text']

    @property
    def rsvp_end_at(self):
        """RSVP for the event ends at"""
        return self._event_dict['rsvp_end_at']['#text']

    @property
    def start_at(self):
        """Event starts at"""
        return self._event_dict['start_at']['#text']

    @property
    def end_at(self):
        """Event ends at"""
        return self._event_dict['end_at']['#text']

    @property
    def attending_count(self):
        """Number of people attending"""
        return int(self._event_dict['event_attending_count']['#text'])

    @property
    def responses_count(self):
        """Number of poeple invited"""
        return int(self._event_dict['event_responses_count']['#text'])

    @property
    def resource(self):
        """Type and ID for the event resource"""
        return (self._event_dict['resouce_type'],
                self._event_dict['resouce_id']['#text'])
