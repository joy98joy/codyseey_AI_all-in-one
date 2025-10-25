# 파일명: main.py
import numpy as np
import os
import csv


def process_and_save_parts(input_filename, output_file):
    """
    여러 CSV 파일을 읽어 항목별 평균 강도를 계산하고, 특정 조건에 따라 필터링하여 새로운 CSV로 저장합니다.

    Args:
        input_files (list): 처리할 CSV 파일명 리스트.
        output_file (str): 결과를 저장할 CSV 파일명.
    """
    all_data = []
    full_data = []

    
    # 1. 세 개의 CSV 파일을 읽어 데이터 병합
    print("--- 파일 읽기 및 데이터 병합 ---")
    with open(input_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  
            
            for row in csv_reader:
                full_data.append(row)
                print(', '.join(row))
    for filename in input_filename:
        try:
            # np.genfromtxt를 사용하여 헤더와 혼합된 데이터 타입을 처리
            data = np.genfromtxt(filename, delimiter=',', names=True, dtype=None, encoding='utf-8')
            all_data.append(data)
            print(f"'{filename}' 파일을 성공적으로 읽었습니다.")
        except FileNotFoundError:
            print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
            return
        except Exception as e:
            print(f"파일을 읽는 중 예상치 못한 오류가 발생했습니다: {e}")
            return

    if not all_data:
        print("읽어온 데이터가 없습니다. 프로그램을 종료합니다.")
        return

    # 2. 모든 데이터를 하나의 구조화된 배열로 병합
    try:
        combined_data = np.concatenate(all_data)
        print("\n모든 데이터가 성공적으로 병합되었습니다.")
        # print("병합된 데이터의 형태:", combined_data.shape)
    except Exception as e:
        print(f"\n데이터 병합 중 오류가 발생했습니다: {e}")
        return

    # 3. 항목별 평균값 계산
    print("\n--- 항목별 평균 강도 계산 ---")
    # 고유한 부품 이름(parts)을 추출
    unique_parts = np.unique(combined_data['parts'])
    average_strengths = {}

    for part_name in unique_parts:
        # 각 부품에 해당하는 강도 값들을 필터링
        strengths = combined_data[combined_data['parts'] == part_name]['strength']
        # 평균 계산
        if strengths.size > 0:
            average_strengths[part_name] = np.mean(strengths)
    
    print("항목별 평균 강도:", average_strengths)

    # 4. 평균 강도가 50보다 작은 항목만 필터링
    print("\n--- 평균 강도가 50보다 작은 항목 필터링 ---")
    filtered_items = {k: v for k, v in average_strengths.items() if v < 50}

    if not filtered_items:
        print("평균 강도가 50보다 작은 항목이 없습니다.")
        return
    
    # 필터링된 결과 출력
    for item, avg_strength in filtered_items.items():
        print(f"항목: {item}, 평균 강도: {avg_strength:.2f}")

    # 5. 필터링된 결과를 CSV 파일로 저장
    try:
        output_dir = os.path.dirname(output_file)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 저장할 데이터를 리스트 형태로 변환
        output_data = [[item, avg] for item, avg in filtered_items.items()]
        
        # 파일 헤더
        header = "part,average_strength"

        # np.savetxt를 사용하여 CSV로 저장
        np.savetxt(output_file, output_data, delimiter=',', fmt='%s,%.2f', header=header, comments='')
        print(f"\n필터링된 결과가 '{output_file}' 파일로 성공적으로 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    # 처리할 파일 리스트
    input_filename= [
        "mars_base_main_parts-001.csv",
        "mars_base_main_parts-002.csv",
        "mars_base_main_parts-003.csv"
    ]
    # 결과 저장 파일
    output_filename = "parts_to_work_on.csv"
    
    process_and_save_parts(input_filename, output_filename)
