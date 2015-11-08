# -*- coding: utf-8 -*-

from malfeeds.engines import MalFeedEngine
from malfeeds.library import get_item_type

class MalRSSFeed(MalFeedEngine):
    def __init__(self, feedurl, feedtype, input_type, **kwargs):
        super(MalRSSFeed, self).__init__(feedurl, feedtype, input_type, **kwargs)

    def _iter_entry(self):
        for feeditem in self._feed_stream.entries:
            _itype = get_item_type(feeditem.link)
            if _itype is None:
                _itype = self._feed_entry_type

            _item = self._struct_entry
#            _item[self._feed_entry_type] = feeditem.link
            _item[_itype] = feeditem.link
            _item['last_update'] = self._feed_header['last_update']
            _item['description'] = feeditem.get('description', '')
            _item['type'] = _itype
            yield _item
