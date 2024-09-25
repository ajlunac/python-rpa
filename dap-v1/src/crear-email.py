import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

emailOutlook = outlook.CreateItem(0)
emailOutlook.To = 'recipient@email.com'
emailOutlook.Subject = 'Feliz Aniversario!'
emailOutlook.HtmlBody = '''
<>En hora buena!, Ana!<br>
'''