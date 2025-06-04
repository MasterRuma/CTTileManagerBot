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
    try:
        response = utils.service.complete(tiles, ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="전체조회", description="점령한 영토들을 조회할 수 있습니다.")
async def 전체조회(ctx: discord.ApplicationContext):
    await ctx.respond(os.getenv("URL"), ephemeral=True)


@bot.slash_command(name="all", description="점령한 영토들을 조회할 수 있습니다.")
async def all(ctx: discord.ApplicationContext):
    await ctx.respond(os.getenv("URL"), ephemeral=True)


@bot.slash_command(name="삭제", description="잘못 기재된 정보들을 삭제할 수 있습니다.")
async def 삭제(
    ctx: discord.ApplicationContext,
    tiles: discord.Option(str, autocomplete=tile_autocomplete),
):
    await ctx.defer(ephemeral=True)
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
    try:
        response = utils.service.status(tiles)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send(f"오류가 발생했습니다: {str(e)}", ephemeral=True)


@bot.slash_command(name="정보", description="해당 유저의 영토 점령 정보를 확인합니다.")
async def 정보(ctx: discord.ApplicationContext, player: discord.Member):
    await ctx.defer(ephemeral=True)
    try:
        await ctx.followup.send(f"{os.getenv('URL')}{str(player.id)}", ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(name="view", description="해당 유저의 영토 점령 정보를 확인합니다.")
async def view(ctx: discord.ApplicationContext, player: discord.Member):
    await ctx.defer(ephemeral=True)
    try:
        await ctx.followup.send(f"{os.getenv('URL')}{str(player.id)}", ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


@bot.slash_command(
    name="전체지우기", description="[관리자 명령어] 모든 타일의 정보를 삭제합니다."
)
async def 전체지우기(ctx: discord.ApplicationContext):
    await ctx.defer(ephemeral=True)
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
    try:
        response = utils.service.connectTest(ctx.author.id)
        await ctx.followup.send(response, ephemeral=True)
    except Exception as e:
        await ctx.followup.send("해당하는 유저는 없습니다!", ephemeral=True)


def start():
    bot.run(os.getenv("TOKEN"))
