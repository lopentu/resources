# https://github.com/lopentu/keke/blob/master/dialogue/chatai/bin/download_data.py
class Drive():

    def __init__(self, service):
        self.service = service
        self.folders = {}  # {id: {id, name, parents} }
        self.file_content = {}  # {id: content}


    # Get LOPE_INDEX.md
    def list_all_docs(self):
        query_string = f"name='LOPE_INDEX.md' and trashed=false"
        resp = self.service.files().list(q=query_string,
                                    spaces='drive',
                                    corpora='allDrives',
                                    fields='nextPageToken, files(id, name, mimeType, parents)',
                                    includeItemsFromAllDrives=True,
                                    supportsAllDrives=True).execute()
        return resp.get('files', [])
    

    def get_full_path(self, file_id):
        file = self.get_file_meta(file_id)
        is_root = False if 'parents' in file else True

        drive_path = []
        while not is_root:
            file_id = file['parents'][0]
            file = self.get_file_meta(file_id)
            drive_path.append( (file['name'], file_id) )
            is_root = False if 'parents' in file else True

        drive_path.reverse()
        return drive_path


    def get_file_meta(self, file_id):

        if file_id in self.folders:
            return self.folders[file_id]
        else:
            file = self.service.files().get(
                fileId=file_id,
                fields='id, name, mimeType, parents',
                supportsTeamDrives=True).execute()
            
            # update cache
            self.folders[file['id']] = file

            return file
    

    def get_file_content(self, file_id):
        if file_id not in self.file_content:
            self.file_content[file_id] = self.service.files().get_media(
                fileId=file_id).execute().decode('UTF-8')
        
        return self.file_content[file_id]


    def get_file_content_by_folderid(self, folder_id):
        for fid, fmeta in self.folders.items():
            if ('parents' in fmeta) and (fmeta['parents'][0] == folder_id):
                return self.get_file_content(fid)
        
        return None