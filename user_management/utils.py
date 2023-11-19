from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_order_cancellation_notification(user_email, user_first_name, order_id, total_amount):
    subject = 'Order Cancellation Notification'
    html_message = render_to_string('order_cancellation_email.html', {
        'customer_name': user_first_name,
        'order_id': order_id,
        'total_amount': total_amount,     
    })
    # Create an EmailMessage object with HTML content
    email = EmailMessage(subject, html_message, 'helpa077637@gmail.com', [user_email])
    email.content_subtype = 'html'  
    email.send()
    
def send_order_assignment_notification(user_email, agent_email, agent_phone, order_details):
    subject = 'Order Assignment Notification'
    html_message = render_to_string('order_assignment_email.html', {
        'user_email': user_email,
        'agent_email': agent_email,
        'agent_phone': agent_phone,
    })
    send_mail(subject, '', 'helpa077637@gmail.com', [user_email], html_message=html_message)