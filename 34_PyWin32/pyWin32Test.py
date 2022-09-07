import win32com.client

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'vikram7sarun@gmail.com'
# mail.CC = 'teste@teste.com;teste3@teste.com'
mail.Subject = 'Teste - 2'
# Attachments=("c://Users/lucas/Downloads/USIM5.xlsx")

# mail.Attachments.Add(Attachments)

pathToIMage = "c://Users/AppData/Roaming/Microsoft/Signaturesa/Teste.png"
# attachment = mail.Attachments.Add(pathToIMage)
#
# attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId1")

mail.HTMLBody = '<p>Hi<p>' \
                '<p>Thats the code :))<p>' \
                '<p> <figure><img src=""cid:MyId1""</figure>'
mail.display()
mail.Send()