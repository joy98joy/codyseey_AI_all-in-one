# ' ' , _=_ 수정 ,들여쓰기 공백, Python의 coding style guide가이드를 준수
import json
def main(filename="mission_computer_main.log"):
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            #print(content)
    except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다. 파일이 현재 디렉터리에 있는지 확인해주세요.")
    except UnicodeDecodeError:
        print(f"오류: '{filename}' 파일을 읽는 중 디코딩 오류가 발생했습니다. 파일 인코딩이 'utf-8'이 아닐 수 있습니다.")
    except Exception as e:
        print(f"파일을 읽는 중 예상치 못한 오류가 발생했습니다: {e}")
    content = content.splitlines()

    lines = []
    Event = []
    TimeStamp = []
    Message = []

    for i in range(0,len(content)):
        lines += content[i].split(",")

    for i in range(0,len(lines),3):
        TimeStamp.append(lines[i])
        Event.append(lines[i+1])
        Message.append(lines[i+2])
    # print(TimeStamp)
    # print(Event)
    # print(Message)

    reverseTimeStamp = sorted(content,reverse = True)
    content.sort(reverse = True)
   
    # timestamp,event,message 같이 출력
    # print(dict(zip(range(1,(len(reverseTimeStamp))+1),reverseTimeStamp)))


    # timestamp,event,message 출력 x 
    # del reverseTimeStamp[0]
    # print(dict(zip(range(1,(len(reverseTimeStamp))+1),reverseTimeStamp)))
    
    Event = []
    TimeStamp = []
    Message = []
    lines = []
    for i in range(0,len(content)):
        lines += content[i].split(",")

    for i in range(0,len(lines),3):
        TimeStamp.append(lines[i])
        Event.append(lines[i+1])
        Message.append(lines[i+2])
    # print(TimeStamp)
    # print(Event)
    # print(Message)
    
    
    #객체 별로 dict 출력
    space = " "
    reverseTimeStampDict = dict(zip(range(0,(len(reverseTimeStamp))+1),TimeStamp))
    for i in range(0,len(reverseTimeStamp)):
       reverseTimeStampDict[i] += space + Event[i] + space + Message[i]
    # print(reverseTimeStampDict)

    del TimeStamp[0]
    TimeStampDict = {"TimeStamp":TimeStamp}
    # print(TimeStampDict)

    del Event[0]
    EnventDict = {"Event": Event}
    
    del Message[0] 
    MessageDict = {"Message": Message} 
    def save_dict_to_json(data_dict1,data_dict2,data_dict3, filename="mission_computer_main.json"):
   
      try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_dict1, file, ensure_ascii=False, indent=4)
            json.dump(data_dict2, file, ensure_ascii=False,indent=4)
            json.dump(data_dict3, file, ensure_ascii=False,indent=4)
        return print(f"'{filename}' 파일이 성공적으로 저장되었습니다.")
      except IOError as error:
        return print(f"파일 저장 중 오류가 발생했습니다: {error}")
      # except TypeError as error:
      #   return print(f"JSON 직렬화 오류: 지원되지 않는 타입이 딕셔너리에 포함되어 있습니다. {error}")
      except FileNotFoundError:
        print(f"오류: '{filename}' 파일을 찾을 수 없습니다. 새로운 파일로 저장합니다.")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data_dict1,data_dict2,data_dict3, f, ensure_ascii=False)
      except json.JSONDecodeError:
        print(f"오류: '{filename}' 파일이 유효한 JSON 형식이 아닙니다.")
      except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    return save_dict_to_json(TimeStampDict,EnventDict,MessageDict)

    # timestamp,event,message 출력 x 
    # del reverseTimeStampDict[0]
    # print(reverseTimeStampDict)
    
    #key가 timestamp,event,message
    # del TimeStamp[0]
    # del Event[0]
    # del Message[0]
    # key = ["timestamp","event","message"]
    # prev = {}
    # for i in range (0,len(TimeStamp)+1):
    #     if i+1 > len(Event):
    #         break
    #     if i+2 > len(Message):
    #         break
    #     prev[key[0]] += TimeStamp[i]
    #     prev[key[1]] += Event[i+1]
    #     prev[key[2]] += Message[i+2]

    # print(prev)


if __name__ == "__main__":
    main()
    
