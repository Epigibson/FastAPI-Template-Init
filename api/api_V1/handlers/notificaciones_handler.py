from fastapi import HTTPException, APIRouter
from schemas.notificaciones_schema import NotificacionCreate
from services.notificaciones_services import NotificationService

notification_router = APIRouter()


@notification_router.post('/send_notification_email', summary="Send notification", tags=["Notification"])
async def send_notification_email(notification: NotificacionCreate):
    recipients = notification.recipients
    body = notification.message

    # Send email notification
    result = NotificationService.send_email_notification(recipients, "Notification", body)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to send email notification")

    return {"message": "Notification sent successfully"}


@notification_router.post('/send_notification_whatsapp', summary="Send notification", tags=["Notification"])
async def send_notification_whats(notification: NotificacionCreate):
    recipients = notification.recipients
    body = notification.message

    # Send email notification
    result = NotificationService.send_whatsapp_notification(recipients, body)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to send email notification")

    return {"message": "Notification sent successfully"}
