# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(["'legal_drafting.py'"],
             pathex=['C:\\Users\\Riley\\Documents\\College\\2021-1 Winter\\CSE 111\\project'],
             binaries=[],
             datas=[],
             hiddenimports=["'pyautogui'"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=''legal_drafting',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
