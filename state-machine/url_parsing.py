
SCHEMA = 1
AUTHORITY = 2
RESOURCE = 3
ERROR = 4

SCHEMA_SEPARATION = 5
SCHEMA_NUM_SEPARATORS = 2



SCHEMA_SEPARATOR = ':'

RESOURCE_SEPARATOR = '/'

def disect_url(url: str) -> None:
    state = SCHEMA
    schema = ''
    auth = ''
    resource = ''
    schema_sep_left = SCHEMA_NUM_SEPARATORS

    for char in url:
        if state == SCHEMA:
            if char == SCHEMA_SEPARATOR:
                state = SCHEMA_SEPARATION
            else:
                schema += char
            continue

        if state == SCHEMA_SEPARATION:
            if char == RESOURCE_SEPARATOR and schema_sep_left > 1:
                schema_sep_left -= 1
            elif schema_sep_left  == 1:
                state = AUTHORITY
            else:
                state = ERROR

            continue

        if state == AUTHORITY:
            if char == RESOURCE_SEPARATOR:
                state = RESOURCE
                resource += char
            else:
                auth += char
            continue
        
        if state == RESOURCE:
            resource += char
            continue

        if ERROR:
            print('Could not parse url.')
            return

    show_disection(url, schema, auth, resource)
        

def show_disection(url: str, schema: str, auth: str, resource: str) -> None:
    print(f''' 
    URL : {url}
    SCHEMA: {schema}
    AUTHORITY: {auth}
    RESOURCE: {resource}
    ''')
