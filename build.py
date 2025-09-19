import os
import json

OUTPUT_FOLDER = 'output'

def build_story_index():
    """output 폴더를 스캔하여 모든 이야기의 메타데이터를 stories.json 파일로 생성합니다."""
    stories_details = []
    print(f"'{OUTPUT_FOLDER}' 폴더를 스캔하여 인덱스를 생성합니다...")

    if not os.path.exists(OUTPUT_FOLDER):
        print(f"'{OUTPUT_FOLDER}' 폴더를 찾을 수 없습니다. 먼저 동화를 생성해주세요.")
        return

    # output 폴더 내의 모든 하위 폴더(각 이야기)를 찾음
    story_folders = [d for d in os.listdir(OUTPUT_FOLDER) if os.path.isdir(os.path.join(OUTPUT_FOLDER, d))]
    story_folders.sort(reverse=True)  # 최신순 정렬

    for folder in story_folders:
        story_path = os.path.join(OUTPUT_FOLDER, folder)
        title_path = os.path.join(story_path, 'title.txt')
        
        # HTML에서 사용할 상대 경로 설정
        cover_image_relative_path = f"{folder}/cover_image.png"

        title = folder  # title.txt 파일이 없을 경우 폴더명을 기본 제목으로 사용
        if os.path.exists(title_path):
            with open(title_path, 'r', encoding='utf-8') as f:
                title = f.read().strip()
        
        stories_details.append({
            'id': folder,
            'title': title,
            'cover_image': cover_image_relative_path 
        })
    
    # 최종 데이터를 output 폴더 안에 stories.json으로 저장
    index_file_path = os.path.join(OUTPUT_FOLDER, 'stories.json')
    with open(index_file_path, 'w', encoding='utf-8') as f:
        json.dump(stories_details, f, ensure_ascii=False, indent=2)
        
    print(f"성공! '{index_file_path}' 파일이 생성되었습니다.")
    print(f"총 {len(stories_details)}개의 이야기를 찾았습니다.")

if __name__ == '__main__':
    build_story_index()