import json
from . import redisConnect

def reserve(tiles, userId):
    try:
        data = redisConnect.validation(tiles)
        if data is None:
            body = {"status": "예약중", "player": userId}
            redisConnect.save(tiles, body)
            return "예약이 완료 되었습니다."

        json_object = json.loads(data)
        player = json_object.get('player', '알 수 없는 사용자')
        status = json_object.get('status', '알 수 없는 상태')

        if status == "예약중":
            return f"{player} 님이 이미 예약을 하셨습니다."
        elif status == "시작중":
            return f"{player} 님이 이미 시작하셨습니다."
        elif status == "완료":
            body = {"status": "예약중", "player": userId}
            redisConnect.save(tiles, body)
            return "예약이 완료 되었습니다."
            
    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"예약 처리 중 오류가 발생했습니다: {str(e)}"


def start(tiles, userId):
    try:
        data = redisConnect.validation(tiles)
        if data is None:
            body = {"status": "시작중", "player": userId}
            redisConnect.save(tiles, body)
            return "시작 마크를 표시했습니다. 이제 점령 하셔도 됩니다."

        json_object = json.loads(data)
        player = json_object.get('player', '알 수 없는 사용자')
        status = json_object.get('status', '알 수 없는 상태')

        if status == "예약중":
            if player == userId:  # Ensure we're comparing strings
                body = {"status": "시작중", "player": userId}
                redisConnect.remove(tiles)
                redisConnect.save(tiles, body)
                return "시작 마크를 표시했습니다. 이제 점령 하셔도 됩니다."
            else:
                return f"해당 영토는 {player} 님이 예약하신 영토입니다."
        elif status == "시작중":
            return f"해당 영토는 {player} 님이 이미 시작하신 영토입니다."
        else:
            return f"처리할 수 없는 상태입니다. 상태: {status}"
            
    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"
    
def complete(tiles, userId):
    try:
        data = redisConnect.validation(tiles)
        
        if data is None:
            return f"아무것도 표시가 안된 타일입니다. `/시작 tiles:{tiles}` 명령어를 실행해주세요."
        
        json_object = json.loads(data)
        player = json_object.get('player', '알 수 없는 사용자')
        status = json_object.get('status', '알 수 없는 상태')
        
        if status == "시작중":
            if player == userId:  # Ensure we're comparing strings
                body = {"status": "완료", "player": userId}
                redisConnect.remove(tiles)
                redisConnect.save(tiles, body)
                return "성공적으로 완료 처리되었습니다. 수고하셨습니다!"
            else:
                return f"다른 사람({player})의 영토는 완료 처리할 수 없습니다."
        elif status == "예약중":
            return f"이 타일은 아직 시작 전 상태입니다. 먼저 시작해주세요."
        elif status == "완료":
            return "이미 완료 처리된 타일입니다."
        else:
            return f"처리할 수 없는 상태입니다. 상태: {status}"
            
    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"