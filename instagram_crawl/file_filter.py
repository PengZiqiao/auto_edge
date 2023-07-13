from pathlib import Path

path = Path(r'F:\desktop\10_sawayaka')
keywords = ['multiple boys', 'multiple girls', '1boy']

for i, caption_file in enumerate(path.glob('*.caption')):
    print(f'>>> {i} - {caption_file.stem}')

    content = caption_file.read_text()
    print(f"""
    --------------------------------
    {content}
    --------------------------------
    """)

    delete_flag = False
    for keyword in keywords:
        if keyword in content:
            delete_flag = True
    if delete_flag:
        print(f">>> deleting...")
        caption_file.unlink()
        caption_file.with_suffix('.jpg').unlink()


# for i, jpg_file in enumerate(path.glob('*.jpg')):
#     print(f'>>> {i} - {jpg_file.stem}')

#     if not jpg_file.with_suffix('.caption').exists():
#         jpg_file.unlink()

    
