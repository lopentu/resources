import re
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from traverse_files import Drive

#%%
MD_FOLDER = 'docs'
SIDEBAR_PATH = f'{MD_FOLDER}/_sidebar.md'
# https://drive.google.com/drive/folders/19DIiWLKiXg9ImUjYs1P1oFee6ZC1mB8Z
PAT_folderid = re.compile(r'/folders/([0-9a-zA-Z_-]+)')
# https://drive.google.com/file/d/1FoXwe12oZEMcRAR_Mg44ULD9YxOi14Ml/view?usp=sharing
PAT_fileid = re.compile(r'/file/d/([0-9a-zA-Z_-]+)')



def main():

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

    # Classify content based on Drive location
    docs_classified = {} # {id: []}
    for doc in docs:
        doc_class = get_category(doc)
        if doc_class not in docs_classified:
            docs_classified[doc_class] = [ f'# {doc_class}\n\n' ]
            docs_classified[doc_class].append( content_writer(doc, drive) )
        else:
            docs_classified[doc_class].append( content_writer(doc, drive) )

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


def content_writer(doc, drive):
    url = f"https://drive.google.com/drive/folders/{doc['path'][-1][1]}"
    drive_path = '/' + '/'.join(x for x, y in doc['path'][1:])

    # link to other folder/file
    if doc['content'].strip().startswith('https://drive.google.com/'):
        id_, isfile = get_id_from_url(doc['content'].strip())
        if isfile: 
            fname, path_str = get_file_rel_path(id_, drive)
        else: 
            fname, path_str = get_folder_rel_path(id_, drive)
        if fname:
            doc['content'] = f"## Please refer to [{path_str}]({fname})\n\n"
        else:
            doc['content'] = 'Cannot find referenced URL\n\n' + doc['content']

    return f"<a href='{url}' target='_blank' class='drive-location'><code>{drive_path}</code></a>\n\n{doc['content']}"
    

def get_category(doc):
    return '/' + '/'.join(x for x, y in doc['path'][1:-1])


def get_id_from_url(url):
    if PAT_fileid.search(url):
        return PAT_fileid.search(url)[1], True
    elif PAT_folderid.search(url):
        return PAT_folderid.search(url)[1], False
    else:
        print('invalid GD URL')
        print(url)
        return '', False
        #raise Exception('invalid GD URL')


def get_file_rel_path(fid, drive):
    full_path = drive.get_full_path(fid)
    if full_path:
        full_path_str = '/' + '/'.join(x for x, y in full_path[1:-1])
        fname = full_path_str.replace('/', '_').strip('_') + '.md'
        return fname, full_path_str
    return None, None


def get_folder_rel_path(folder_id, drive):
    full_path = drive.get_full_path(folder_id)
    if full_path:
        full_path_str = '/' + '/'.join(x for x, y in full_path[1:])
        fname = full_path_str.replace('/', '_').strip('_') + '.md'
        return fname, full_path_str
    return None, None

if __name__ == "__main__":
    main()