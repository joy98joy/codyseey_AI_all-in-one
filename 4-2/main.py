# 파일명: csv_processing_no_pandas.py
import csv

def process_inventory_list(input_filename="Mars_Base_Inventory_List.csv", output_filename="Mars_Base_Inventory_danger.csv"):
    
    full_data = []
    
    try:
        print("--- CSV 파일 전체 내용 ---")
        with open(input_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  
            print(', '.join(header))
            
            for row in csv_reader:
                full_data.append(row)
                print(', '.join(row))


    
        try:
            # 정렬을 위해 float 타입으로 변환합니다.
            def get_flammability(row):
                try:
                    return float(row[4])
                except (ValueError, IndexError):
                    return row[4]
            # header를 제외한 본문 데이터를 인화성 지수 기준으로 내림차순 정렬
            sorted_data = sorted(full_data, key=get_flammability, reverse=True)
            
            print("--- 인화성 지수(Flammability) 내림차순 정렬 결과 ---")
            print(', '.join(header))
            for row in sorted_data:
                print(', '.join(row))

        except Exception as e:
            print(f"정렬 중 오류가 발생했습니다: {e}")
        

        filtered_data = []
        try:
            for row in sorted_data:
                if float(row[4]) >= 0.7:
                    filtered_data.append(row)
            
            print("--- 인화성 지수 0.7 이상인 항목만 필터링한 결과 ---")
            print(', '.join(header))
            for row in filtered_data:
                print(', '.join(row))

        except (ValueError, IndexError) as e:
            print(f"필터링 중 오류가 발생했습니다: {e}")

        print("\n" + "="*50 + "\n")

        # 4. 필터링된 결과를 새 CSV 파일로 저장
        try:
            with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
                csv_writer = csv.writer(outfile)
                csv_writer.writerow(header)
                csv_writer.writerows(filtered_data)
            print(f"필터링된 결과가 '{output_filename}' 파일로 저장되었습니다.")
        except Exception as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")

    except FileNotFoundError:
        print(f"오류: '{input_filename}' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")
    except UnicodeDecodeError:
        print(f"오류: '{input_filename}' 파일을 읽는 중 디코딩 오류가 발생했습니다. 파일 인코딩이 'utf-8'이 아닐 수 있습니다.")

if __name__ == "__main__":
    process_inventory_list()


    

    # try:
    #    df = pd.read_csv(filename)
    # #    print(df)
    # except FileNotFoundError:
    #     print(f"오류: '{filename}' 파일을 찾을 수 없습니다. 파일이 현재 디렉터리에 있는지 확인해주세요.")
    # except UnicodeDecodeError:
    #     print(f"오류: '{filename}' 파일을 읽는 중 디코딩 오류가 발생했습니다. 파일 인코딩이 'utf-8'이 아닐 수 있습니다.")
    # except Exception as e:
    #     print(f"파일을 읽는 중 예상치 못한 오류가 발생했습니다: {e}")
    
    # column_lists = {}
    # for column in df.columns:
    #     column_lists[column] = df[column].tolist()
    #     # print(f"'{column}': {column_lists[column]}")
    # df_sorted = df.sort_values(by='Flammability', ascending=False)
    # # print(df_sorted)
    # df_filtered = df_sorted[df_sorted['Flammability'] >= 0.7]
    # print(df_filtered)
    # output_filename = "Mars_Base_Inventory_danger.csv"
    # df_filtered.to_csv(output_filename, index=False, encoding='utf-8')
    # print(f"필터링된 결과가 '{output_filename}' 파일로 저장되었습니다.")
    Substance = []
    Weight = []
    SpecificGravity = []
    Strength = []
    Flammability = []
    lines = []

    # for i in range(0,len(df)):
    #     lines += df[i].split(",")

    # for i in range(0,len(lines),5):
    #     Substance.append(lines[i])
    #     Weight.append(lines[i+1])
    #     SpecificGravity.append(lines[i+2])
    #     Strength.append(lines[i+3])
    #     Flammability.append(lines[i+4])
    # print(Substance)





