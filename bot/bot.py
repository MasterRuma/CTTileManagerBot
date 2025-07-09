from dis import disco
from pydoc import describe
from re import T
import discord
from discord.ext import tasks
import utils.service
from dotenv import load_dotenv
import os

bot = discord.Bot()

load_dotenv()

SETUP_MESSAGE_ID = 0

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


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


async def tile_autocomplete(ctx: discord.AutocompleteContext):
    user_input = ctx.value.lower() if ctx.value else ""
    filtered = [tile for tile in tiles if user_input in tile.lower()]
    return filtered[:25]


@bot.slash_command(name="예약", description="타일 예약을 지정합니다.")
async def 예약(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.reserve(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="r", description="타일 예약을 지정합니다.")
async def r(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.reserve(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="시작", description="타일 시작을 지정합니다.")
async def 시작(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.start(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="s", description="타일 시작을 지정합니다.")
async def s(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.start(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="완료", description="점령 완료 타일을 지정합니다.")
async def 완료(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.complete(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="c", description="점령 완료 타일을 지정합니다.")
async def c(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    # Defer the response first
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.complete(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="전체조회", description="점령한 영토들을 조회할 수 있습니다.")
async def 전체조회(ctx: discord.ApplicationContext):
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.respond(f"해당 권한이 없습니다.", ephemeral=True)
        return
    await ctx.respond(os.getenv("URL"), ephemeral=True)


@bot.slash_command(name="all", description="점령한 영토들을 조회할 수 있습니다.")
async def all(ctx: discord.ApplicationContext):
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.respond(f"해당 권한이 없습니다.", ephemeral=True)
        return
    await ctx.respond(os.getenv("URL"), ephemeral=True)


@bot.slash_command(name="삭제", description="잘못 기재된 정보들을 삭제할 수 있습니다.")
async def 삭제(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.remove(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(
    name="remove", description="잘못 기재된 정보들을 삭제할 수 있습니다."
)
async def remove(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.remove(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="상태", description="해당 영토의 점령 여부를 확인합니다.")
async def 상태(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.status(tiles)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="status", description="해당 영토의 점령 여부를 확인합니다.")
async def status(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.status(tiles)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="정보", description="해당 유저의 영토 점령 정보를 확인합니다.")
async def 정보(ctx: discord.ApplicationContext, player: discord.Member):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        await ctx.followup.send(f"{os.getenv('URL')}{str(player.id)}", ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(name="view", description="해당 유저의 영토 점령 정보를 확인합니다.")
async def view(ctx: discord.ApplicationContext, player: discord.Member):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        await ctx.followup.send(f"{os.getenv('URL')}{str(player.id)}", ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(
    name="전체지우기", description="[관리자 명령어] 모든 타일의 정보를 삭제합니다."
)
async def 전체지우기(ctx: discord.ApplicationContext):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.allRemove(ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(
    name="연결테스트",
    description="[관리자 명령어] Redis와 클라이언트의 연결을 테스트 합니다.",
)
async def 연결테스트(ctx: discord.ApplicationContext):
    await ctx.defer(ephemeral=True)
    if not utils.service.vaildRole(ctx.author.roles):
        await ctx.followup.send(f"해당 권한이 없습니다.", ephemeral=True)
        return
    try:
        response = utils.service.connectTest(ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(
    name="setup", description="[관리자 전용] 역할 지급 메시지를 생성합니다."
)
@discord.default_permissions(administrator=True)
async def setup(ctx: discord.ApplicationContext):
    """
    역할 지급을 위한 메시지를 보내고 반응 이모지를 추가합니다.
    이 메시지에 반응하는 유저는 INFO_ROLE_ID에 지정된 역할을 받게 됩니다.
    """
    global SETUP_MESSAGE_ID
    admin_id = os.getenv("ADMIN_ID")
    if not admin_id or str(ctx.author.id) != admin_id:
        await ctx.respond("이 명령어를 사용할 권한이 없습니다. (관리자만 가능)", ephemeral=True)
        return

    if not os.getenv("INFO_ROLE_ID"):
        await ctx.respond(
            "환경변수(.env)에 `INFO_ROLE_ID`가 설정되지 않았습니다.", ephemeral=True
        )
        return

    message_content = """
## 이 서버에 가입하신 목적이 영토전 가입 이시라면 이 메세지를 꼭 읽어주시길 바랍니다!

### 가입 절차 (신규)
> 제공된 팀 코드를 복붙하여 가입한다.
> 가입 후 해당 이모지에 체크를 한다.
> <#1245601540958326826> 에 들어가 포스트를 만든다.
> 가입 완료 사진과 함께 본인 풍타디 닉네임을 기입한다.

### 가입 절차 (기존)
> 제공된 팀 코드를 복붙하여 기입한다.
> 가입 후 해당 이모지에 체크를 한다.
"""
    await ctx.respond("역할 지급 메시지를 현재 채널에 보냅니다.", ephemeral=True)
    message = await ctx.send(message_content)
    await message.add_reaction("✅")

    # 메시지 ID를 저장하여 반응 이벤트에서 어떤 메시지에 대한 반응인지 식별합니다.
    # 실제 운영 환경에서는 봇이 재시작되어도 ID를 기억하도록 데이터베이스나 파일에 저장하는 것이 좋습니다.
    SETUP_MESSAGE_ID = message.id


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    """유저가 이모지 반응을 추가했을 때 역할을 지급합니다."""
    info_message_id_str = os.getenv("INFO_MESSAGE_ID")
    if not info_message_id_str:
        return

    try:
        info_message_id = int(info_message_id_str)
    except ValueError:
        print(f"오류: INFO_MESSAGE_ID ('{info_message_id_str}')가 올바른 숫자 형식이 아닙니다.")
        return

    if payload.message_id != info_message_id or payload.user_id == bot.user.id:
        return

    if str(payload.emoji) == "✅":
        guild = bot.get_guild(payload.guild_id)
        if not guild:
            return

        role_id_str = os.getenv("INFO_ROLE_ID")
        if not role_id_str:
            print("오류: .env 파일에 INFO_ROLE_ID가 설정되지 않았습니다.")
            return

        try:
            role_id = int(role_id_str)
            role = guild.get_role(role_id)
            if not role:
                print(f"오류: 역할(ID: {role_id})을 찾을 수 없습니다.")
                return

            member = await guild.fetch_member(payload.user_id)
            if not member:
                return

            await member.add_roles(role)
            print(f"{member.name}에게 {role.name} 역할을 부여했습니다.")
        except ValueError:
            print(f"오류: INFO_ROLE_ID ('{role_id_str}')가 올바른 숫자 형식이 아닙니다.")
        except discord.NotFound:
            print(f"오류: 멤버(ID: {payload.user_id})를 찾을 수 없습니다.")
        except discord.Forbidden:
            print(f"오류: 역할을 부여할 권한이 없습니다.")
        except Exception as e:
            print(f"역할 부여 중 오류 발생: {e}")


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    """유저가 이모지 반응을 제거했을 때 역할을 회수합니다."""
    info_message_id_str = os.getenv("INFO_MESSAGE_ID")
    if not info_message_id_str:
        return

    try:
        info_message_id = int(info_message_id_str)
    except ValueError:
        print(f"오류: INFO_MESSAGE_ID ('{info_message_id_str}')가 올바른 숫자 형식이 아닙니다.")
        return

    if payload.message_id != info_message_id or payload.user_id == bot.user.id:
        return

    if str(payload.emoji) == "✅":
        guild = bot.get_guild(payload.guild_id)
        if not guild:
            return

        role_id_str = os.getenv("INFO_ROLE_ID")
        if not role_id_str:
            print("오류: .env 파일에 INFO_ROLE_ID가 설정되지 않았습니다.")
            return

        try:
            role_id = int(role_id_str)
            role = guild.get_role(role_id)
            if not role:
                print(f"오류: 역할(ID: {role_id})을 찾을 수 없습니다.")
                return

            member = await guild.fetch_member(payload.user_id)
            if not member:
                return

            await member.remove_roles(role)
            print(f"{member.name}에게서 {role.name} 역할을 제거했습니다.")
        except ValueError:
            print(f"오류: INFO_ROLE_ID ('{role_id_str}')가 올바른 숫자 형식이 아닙니다.")
        except discord.NotFound:
            print(f"오류: 멤버(ID: {payload.user_id})를 찾을 수 없습니다.")
        except discord.Forbidden:
            print(f"오류: 역할을 제거할 권한이 없습니다.")
        except Exception as e:
            print(f"역할 제거 중 오류 발생: {e}")


@bot.slash_command(name="new", description="[관리자 전용] 새로운 팀 코드를 공지합니다.")
async def new(
    ctx: discord.ApplicationContext,
    teamcode: discord.Option(str, "팀 코드를 입력하세요."),
):
    """
    새로운 팀 코드를 역할 맨션과 함께 공지합니다.
    """
    admin_id = os.getenv("ADMIN_ID")
    if not admin_id or str(ctx.author.id) != admin_id:
        await ctx.respond("이 명령어를 사용할 권한이 없습니다. (관리자만 가능)", ephemeral=True)
        return

    info_role_id = os.getenv("INFO_ROLE_ID")
    if not info_role_id:
        await ctx.respond("환경변수(.env)에 `INFO_ROLE_ID`가 설정되지 않았습니다.", ephemeral=True)
        return

    try:
        # 1. 역할 맨션과 함께 팀 코드 보내기
        await ctx.send(f"## <@&{info_role_id}> **새로운 팀 코드**")
        
        # 2. 팀 코드만 따로 보내기 (복사하기 쉽도록)
        await ctx.send(teamcode)

        await ctx.respond("팀 코드 메시지를 성공적으로 보냈습니다.", ephemeral=True)

    except Exception as e:
        await ctx.respond(f"메시지 전송 중 오류가 발생했습니다: {e}", ephemeral=True)

def start():
    bot.run(os.getenv("TOKEN"))
