from bucketlist.models import BucketList


def paginate_data(query, limit, offset, url):
    links = {}
    pages = query.paginate(offset, limit, error_out=False)
    links["first"] = "{}/offset={}&limit={}".format(
        url, 1, limit)

    if pages.has_prev:
        prev_page = "{}/offset={}&limit={}".format(
            url, pages.prev_num, limit)
        links["prev"] = prev_page
    links["current"] = "{}/offset={}&limit={}".format(
        url, offset, limit)
    if pages.has_next:
        next_page = "{}?offset={}&limit={}".format(
            url, pages.next_num, limit)
        links["next"] = next_page

    links['last'] = "{}/offset={}&limit={}".format(
        url, pages.pages, limit)

    info = {}
    info['offset'] = offset
    info['limit'] = limit
    info['total'] = pages.total
    headers = {"links": links}
    return pages.items, info, headers
