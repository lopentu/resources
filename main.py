#%%
MD_FOLDER = 'docs'
SIDEBAR_PATH = f'{MD_FOLDER}/_sidebar.md'


def main():

    import os
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from traverse_files import Drive

    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = './lope-drive-token.json'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=credentials)

    # Get all LOPE_INDEX.md
    drive = Drive(drive_service)
    docs = []
    for file in drive.list_all_docs():
        docs.append({
            'id': file['id'],
            'path': drive.get_full_path(file_id=file['id']),
            'content': drive.get_file_content(file_id=file['id'])
        })

    #%%
    # Classify content based on Drive location
    docs_classified = {} # {id: []}
    for doc in docs:
        doc_class = get_category(doc)
        if doc_class not in docs_classified:
            docs_classified[doc_class] = [ f'# {doc_class}\n\n' ]
            docs_classified[doc_class].append( content_writer(doc) )
        else:
            docs_classified[doc_class].append( content_writer(doc) )

    # Write to md
    sidebar = []
    for doc_class, doc in docs_classified.items():
        # write doc content
        fname = f"{doc_class.replace('/', '_').strip('_')}.md"
        doc = '\n'.join(doc)
        with open(f"{MD_FOLDER}/{fname}", 'w', encoding='utf-8') as f:
            f.write(doc)
        sidebar.append( (doc_class, fname) )

    # write sidebar to _sidebar.md
    sidebar.sort()
    with open(SIDEBAR_PATH, 'w', encoding='utf-8') as f:
        f.write('<!-- docs/_sidebar.md -->\n\n')
        for doc_class, fname in sidebar:
            f.write(f'- [{doc_class}]({fname})\n')


def content_writer(doc):
    url = f"https://drive.google.com/drive/folders/{doc['path'][-1][1]}"
    drive_path = '/' + '/'.join(x for x, y in doc['path'][1:])

    return f"<a href='{url}' target='_blank' class='drive-location'><code>{drive_path}</code></a>\n\n{doc['content']}"
    

def get_category(doc):
    return '/' + '/'.join(x for x, y in doc['path'][1:-1])


if __name__ == "__main__":
    main()