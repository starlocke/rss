# -*- coding: utf-8 -*-
'''
Подготовка файлов перед выпуском новой версии
 
@file prepare-install.py
@author aleksey.hohryakov@gmail.com
'''

import os
import shutil

qtsdkAbsPath = 'c:\\QtSDK\\Desktop\\Qt\\4.8.0\\mingw'
quiterssSourceAbsPath = "e:\\Work\\_Useful\\QtProjects\\QuiteRSS"
quiterssReleaseAbsPath = "e:\\Work\\_Useful\\QtProjects\\QuiteRSS-build-desktop_Release\\release\\target"
prepareAbsPath  = "e:\\Work\\_Useful\\QtProjects\\QuiteRSS_prepare-install"

# Список файлов состоит из относительного пути папки, содержащей файл,
# и имени файла, который необходимо скопировать
idDir  = 0
idName = 1
filesFromSource = [
  ['\\sound', 'notification.wav'],
  ['', 'AUTHORS'],
  ['', 'COPYING'],
  ['', 'HISTORY_EN'],
  ['', 'HISTORY_RU'],
  ['', 'README'],
  ['', 'TODO']
]

filesFromQtSDKPlugins = [
  ['\\sqldrivers', 'qsqlite4.dll'],
  ['\\iconengines', 'qsvgicon4.dll'],
  ['\\imageformats', 'qgif4.dll'],
  ['\\imageformats', 'qico4.dll'],
  ['\\imageformats', 'qjpeg4.dll'],
  ['\\imageformats', 'qmng4.dll'],
  ['\\imageformats', 'qsvg4.dll'],
  ['\\imageformats', 'qtga4.dll'],
  ['\\imageformats', 'qtiff4.dll'],
  ['\\phonon_backend', 'phonon_ds94.dll']
]

filesFromQtSDKBin = [
  ['', 'libeay32.dll'],
  ['', 'libgcc_s_dw2-1.dll'],
  ['', 'libssl32.dll'],
  ['', 'mingwm10.dll'],
  ['', 'phonon4.dll'],
  ['', 'QtCore4.dll'],
  ['', 'QtGui4.dll'],
  ['', 'QtNetwork4.dll'],
  ['', 'QtSql4.dll'],
  ['', 'QtSvg4.dll'],
  ['', 'QtWebKit4.dll'],
  ['', 'QtXml4.dll'],
  ['', 'ssleay32.dll']
]


def preparePath(path):
  print "---- Preparing path: " + path
  if (os.path.exists(path)):
    print "Path exists. Remove it"
    shutil.rmtree(path)
  
  os.makedirs(path)
  print "Path created"
    
def copyLangFiles():
  print "---- Copying language files..."
  shutil.copytree(quiterssReleaseAbsPath + "\\lang", prepareAbsPath + "\\lang")
  print "Done"

def copyExeFile():
  print "---- Copying exe-file..."
  shutil.copy(quiterssReleaseAbsPath + "\\QuiteRSS.exe", prepareAbsPath + "\\QuiteRSS.exe")
  print "Done"

def copyFilesFromSource():
  print "---- Copying files from source..."
  
  # Перебираем список файлов
  for file in filesFromSource:
    print file[idDir] + '\\' + file[idName]
    
    # Если есть имя папки, то создаём её
    if file[idDir]:
      shutil.copytree(quiterssSourceAbsPath + file[idDir], prepareAbsPath + file[idDir])
      
    # Копируем файл
    shutil.copy(quiterssSourceAbsPath + file[idDir] + '\\' + file[idName], prepareAbsPath + file[idDir] + '\\' + file[idName])
    
  print "Done"

def copyFileList(fileList, src):
  '''
  Копирование файлов из списка fileList из папки src
  '''
  print "---- Copying files from " + src
  
  # Перебираем список файлов
  for file in fileList:
    print file[idDir] + '\\' + file[idName]
    
    # Если есть имя папки, то создаём её
    if file[idDir] and (not os.path.exists(prepareAbsPath + file[idDir])):
      shutil.copytree(src + file[idDir], prepareAbsPath + file[idDir])
      
    # Копируем файл, обрабатывая ошибки
    try:
      shutil.copy(src + file[idDir] + '\\' + file[idName], prepareAbsPath + file[idDir] + '\\' + file[idName])
    except (IOError, os.error), why:
      print str(why)
    
  print "Done"

def main():
  print "QuiteRSS prepare-install"
  preparePath(prepareAbsPath)
  copyLangFiles()
  copyExeFile()
  copyFilesFromSource()
  copyFileList(filesFromQtSDKPlugins, qtsdkAbsPath + '\\plugins')
  copyFileList(filesFromQtSDKBin, qtsdkAbsPath + '\\bin')

if __name__ == '__main__':
  main()