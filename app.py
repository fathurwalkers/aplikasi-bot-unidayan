import os
import tempfile
import telegram.ext
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""
    Selamat Datang {update.effective_user.first_name}, di Bot Sistem Informasi Informatika Unidayan!
    Silahkan gunakan perintah " /help " untuk melihat apa saja Command (perintah) yang tersedia pada Bot ini untuk melihat beberapa informasi terkait informasi dan data akademik pada Fakultas Teknik Informatika Universitas Dayanu Ikhsanuddin.""")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
    """
    /start      -> Displaying welcome message. 
    ..
    /help       -> Get information of basic usage of this bot.
    .. 
    /jadwalmatkul   -> Mengambil informasi terkait matakuliah. 
    ..
    /transkip   -> Mengambil data Transkip nilai sesuai dengan NIM yang di request. 
    ex : /transkip 2020 20650001
    ..
    /khs        -> Mengambil data Kartu Hasil Studi sesuai dengan NIM yang di request. 
    ex : /khs 2020 20650001
    ..
    /krs        -> Mengambil data KRS pada semester yang aktif. 
    ex : /krs 
    ..
    """)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"""Instagram : sir.n3wt0n_ Current User : {update.effective_user.id} 
    User Name : {update.effective_user.full_name}""")
    
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    params = "".join(context.args)
    await update.message.reply_text(f"""Instagram : sir.n3wt0n_ Current User : {update.effective_user.id} 
    User Name : {update.effective_user.full_name}, params : {params}""")

async def sendfile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    params = " ".join(context.args)
    tmp_filename = 'ex_doc/' + params + '.pdf'
    document = open(tmp_filename, 'rb')
    await update.message.reply_document(document=document)

async def transkip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    params = "/".join(context.args)
    tmp_filename = 'ex_doc/Transkip Nilai/' + params + 'TR.pdf'
    document = open(tmp_filename, 'rb')
    await update.message.reply_document(document=document)
    
async def khs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    params = "/".join(context.args)
    tmp_filename = 'ex_doc/Kartu Hasil Studi/' + params + '.pdf'
    document = open(tmp_filename, 'rb')
    await update.message.reply_document(document=document)
    
async def krs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    tmp_filename = 'ex_doc/Kartu Rencana Studi/KRS MBKM SMT GENAP.pdf'
    document = open(tmp_filename, 'rb')
    await update.message.reply_document(document=document)
    
async def jadwalmatkul(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
    tmp_filename = 'ex_doc/jadwal-matkul/JADWAL PERKULIAHAN SEMESTER GENAP TAHUN AKADEMIK 2022 2023.pdf'
    document = open(tmp_filename, 'rb')
    await update.message.reply_document(document=document)

# app = ApplicationBuilder().token("6320416802:AAEFPX1kePXFNt8o-ohSvtzINdsFaNrpOps").build() # FATHUR BOT  
app = ApplicationBuilder().token("6544544911:AAFYAqDxGq-rdbmZAZMzmnIL-iwR8clV8ak").read_timeout(30).write_timeout(30).build() # SISFO UNIDAYAN BOT 

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("sendfile", sendfile))
app.add_handler(CommandHandler("transkip", transkip))
app.add_handler(CommandHandler("khs", khs))
app.add_handler(CommandHandler("krs", krs))
app.add_handler(CommandHandler("jadwalmatkul", jadwalmatkul))
app.add_handler(CommandHandler("test", test))

app.run_polling()