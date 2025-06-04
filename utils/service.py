import json
from . import redisConnect
from dotenv import load_dotenv
import os

load_dotenv()


def uppercase(tiles):
    return str(tiles).upper().replace(" ", "")


def tilesValidation(tile):
    tiles = [
        "MRX",
        "DAG",
        "DAF",
        "DAE",
        "DAD",
        "DAC",
        "DAB",
        "DAA",
        "AAG",
        "AAF",
        "AAE",
        "AAD",
        "AAC",
        "AAB",
        "AAA",
        "CAG",
        "CBF",
        "DCE",
        "DCD",
        "DCC",
        "DCB",
        "DCA",
        "BAG",
        "ABF",
        "ABE",
        "ABD",
        "ABC",
        "ABB",
        "ABA",
        "BBF",
        "CAF",
        "CBE",
        "CDD",
        "DEC",
        "DEB",
        "DEA",
        "BAF",
        "BCE",
        "ADD",
        "ADC",
        "ADB",
        "ADA",
        "CCE",
        "CAE",
        "CBD",
        "CDC",
        "CFB",
        "DGA",
        "BBE",
        "BAE",
        "BCD",
        "BEC",
        "AFB",
        "AFA",
        "BDD",
        "CCD",
        "CAD",
        "CBC",
        "CDB",
        "CFA",
        "BBD",
        "BAD",
        "BCC",
        "BEB",
        "BGA",
        "CEC",
        "CCC",
        "CAC",
        "CBB",
        "CDA",
        "BDC",
        "BBC",
        "BAC",
        "BCB",
        "BEA",
        "BFB",
        "CEB",
        "CCB",
        "CAB",
        "CBA",
        "BDB",
        "BBB",
        "BAB",
        "BCA",
        "CGA",
        "CEA",
        "CCA",
        "CAA",
        "BFA",
        "BDA",
        "BBA",
        "BAA",
        "EAG",
        "DBF",
        "DBE",
        "DBD",
        "DBC",
        "DBB",
        "DBA",
        "FAH",
        "FBF",
        "ACE",
        "ACD",
        "ACC",
        "ACB",
        "ACA",
        "EBF",
        "EAF",
        "ECE",
        "DDD",
        "DDC",
        "DDB",
        "DDA",
        "FAF",
        "FBE",
        "FDD",
        "AEC",
        "AEB",
        "AEA",
        "EBE",
        "EAE",
        "ECD",
        "EEC",
        "DFB",
        "DFA",
        "FCE",
        "FAE",
        "FBD",
        "FDC",
        "FFB",
        "AGA",
        "EDD",
        "EBD",
        "EAD",
        "ECC",
        "EEB",
        "EGA",
        "FCD",
        "FAD",
        "FBC",
        "FDB",
        "FFA",
        "EDC",
        "EBC",
        "EAC",
        "ECB",
        "EEA",
        "FEC",
        "FCC",
        "FAC",
        "FBB",
        "FDA",
        "EFB",
        "EDB",
        "EBB",
        "EAB",
        "ECA",
        "FEB",
        "FCB",
        "FAB",
        "FBA",
        "EFA",
        "EDA",
        "EBA",
        "EAA",
        "FGA",
        "FEA",
        "FCA",
        "FAA",
    ]
    tilesSet = set(tiles)
    return tile in tilesSet


def reserve(tiles, userId):
    try:
        tiles = uppercase(tiles)
        if tilesValidation(tiles) == False:
            return f"{tiles} 영토는 없는 영토입니다."
        data = redisConnect.validation(tiles)
        if data is None:
            body = {"status": "예약중", "player": userId}
            redisConnect.save(tiles, body)
            return f"{tiles} 점령 예약이 완료 되었습니다."

        json_object = json.loads(data)
        player = json_object.get("player", "알 수 없는 사용자")
        status = json_object.get("status", "알 수 없는 상태")

        if status == "예약중":
            return f"<@{player}> 님이 {tiles} 점령을 이미 예약을 하셨습니다."
        elif status == "시작중":
            return f"<@{player}> 님이 {tiles} 점령을 이미 시작하셨습니다."
        elif status == "완료":
            body = {"status": "예약중", "player": userId}
            redisConnect.save(tiles, body)
            return f"{tiles} 점령 예약이 완료 되었습니다."

    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"예약 처리 중 오류가 발생했습니다: {str(e)}"


def start(tiles, userId):
    try:
        tiles = uppercase(tiles)
        if tilesValidation(tiles) == False:
            return f"{tiles} 영토는 없는 영토입니다."
        data = redisConnect.validation(tiles)
        if data is None:
            body = {"status": "시작중", "player": userId}
            redisConnect.save(tiles, body)
            return f"{tiles} 타일의 시작 마크를 표시했습니다. 이제 점령 하셔도 됩니다."

        json_object = json.loads(data)
        player = json_object.get("player", "알 수 없는 사용자")
        status = json_object.get("status", "알 수 없는 상태")

        if status == "예약중":
            if player == userId:  # Ensure we're comparing strings
                body = {"status": "시작중", "player": userId}
                redisConnect.remove(tiles)
                redisConnect.save(tiles, body)
                return (
                    f"{tiles} 타일의 시작 마크를 표시했습니다. 이제 점령 하셔도 됩니다."
                )
            else:
                return f"{tiles} 영토는 <@{player}> 님이 예약하신 영토입니다."
        elif status == "시작중":
            return f"{tiles} 영토는 <@{player}> 님이 이미 시작하신 영토입니다."
        else:
            return f"처리할 수 없는 상태입니다. 상태: {status}"

    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"


def complete(tiles, userId):
    try:
        tiles = uppercase(tiles)
        if tilesValidation(tiles) == False:
            return f"{tiles} 영토는 없는 영토입니다."
        data = redisConnect.validation(tiles)

        if data is None:
            return f"아무것도 표시가 안된 영토입니다. `/시작 tiles:{tiles}` 명령어를 실행해주세요."

        json_object = json.loads(data)
        player = json_object.get("player", "알 수 없는 사용자")
        status = json_object.get("status", "알 수 없는 상태")

        if status == "시작중":
            if player == userId:  # Ensure we're comparing strings
                body = {"status": "완료", "player": userId}
                redisConnect.remove(tiles)
                redisConnect.save(tiles, body)
                return f"성공적으로 {tiles} 점령 처리 완료되었습니다. 수고하셨습니다!"
            else:
                return (
                    f"다른 사람(<@{player}>)의 {tiles} 영토는 완료 처리할 수 없습니다."
                )
        elif status == "예약중":
            return f"{tiles} 영토는 아직 시작 전 상태입니다. 먼저 시작해주세요."
        elif status == "완료":
            return f"이미 완료 처리된 {tiles} 영토입니다."
        else:
            return f"처리할 수 없는 상태입니다. 상태: {status}"

    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"


def remove(tiles, userId):
    try:
        tiles = uppercase(tiles)
        if tilesValidation(tiles) == False:
            return f"{tiles} 영토는 없는 영토입니다."
        data = redisConnect.validation(tiles)

        if data is None:
            return f"아무것도 표시가 안된 영토입니다."

        json_object = json.loads(data)
        player = json_object.get("player", "알 수 없는 사용자")

        if player == userId:
            redisConnect.remove(tiles)
            return f"{tiles} 영토의 삭제가 완료되었습니다."
        else:
            return f"{tiles} 영토 삭제에 실패했습니다. <@{player}> 에게 문의해주세요."

    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"


def status(tiles):
    try:
        tiles = uppercase(tiles)
        if tilesValidation(tiles) == False:
            return f"{tiles} 영토는 없는 영토입니다."
        data = redisConnect.validation(tiles)

        if data is None:
            return f"아무것도 표시가 안된 영토입니다."

        json_object = json.loads(data)
        player = json_object.get("player", "알 수 없는 사용자")
        status = json_object.get("status", "알 수 없는 상태")

        return f"## {tiles}\n상태 : {status}\n플레이어 : <@{player}>"

    except json.JSONDecodeError:
        return "데이터 처리 중 오류가 발생했습니다. 관리자에게 문의해주세요."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다: {str(e)}"


def allRemove(playerId):
    try:
        if playerId == int(os.getenv("ADMIN_ID")):
            keys = redisConnect.scan_keys()
            for key in keys:
                redisConnect.remove(key)
            return f"모든 영토의 정보가 삭제되었습니다."
        else:
            return f"해당 명령어를 사용할 권한이 없습니다."
    except Exception as e:
        return f"처리 중 오류가 발생했습니다 : {str(e)}"


def connectTest(playerId):
    try:
        if playerId == int(os.getenv("ADMIN_ID")):
            redisConnect.save("test", {"status": "test", "player": "test"})
            if (
                redisConnect.validation("test")
                != '{"status": "test", "player": "test"}'
            ):
                return "데이터 테스트 중 잘못된 값을 전송했습니다."
            redisConnect.remove("test")
            return "Redis 테스트 완료."
        else:
            return "해당 명령어를 사용할 권한이 없습니다."
    except Exception as e:
        return f"Redis 연결 중 오류가 발생했습니다: {str(e)}"
