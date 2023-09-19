import os
import tempfile
import telegram.ext
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    /start      -> Displaying welcome message. 
    /help       -> Get information of basic usage of this bot. 
    /contact    -> Contact information.""")

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

# app = ApplicationBuilder().token("6320416802:AAEFPX1kePXFNt8o-ohSvtzINdsFaNrpOps").build() # FATHUR BOT  
app = ApplicationBuilder().token("6544544911:AAFYAqDxGq-rdbmZAZMzmnIL-iwR8clV8ak").build() # SISFO UNIDAYAN BOT 

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("sendfile", sendfile))
app.add_handler(CommandHandler("transkip", transkip))
app.add_handler(CommandHandler("khs", khs))
app.add_handler(CommandHandler("krs", krs))
app.add_handler(CommandHandler("test", test))

app.run_polling()