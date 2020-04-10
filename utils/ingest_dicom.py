## Script to ingest dicom from local FS and write into a postgreSQL database
#!/usr/bin/env python3
## Currently takes parameters such as PostgreSQL server config vars and local FS path as cmd-line input.
## Future versions should include parsing such information from a YAML config file.

import os
import pydicom as pdicom

# Set a default value for input folder
def load_dcm(path):
    dicomImgLst = []
    for dirName, subdirList, fileList in os.walk(path):
        for filename in fileList:
            if '.dcm' in filename.lower():
                dicomImgLst.append(os.path.join(dirName, filename))
    return dicomImgLst


if __name__ == '__main__':
    INPUT_FOLDER = input('Enter the fullpath to the local FS: ')
    dicomImgLst = load_dcm(INPUT_FOLDER)

    sampleDicomFile = dicomImgLst[0]
    # print(pdicom.filereader.dcmread(dicomImgLst[0]))
    

    