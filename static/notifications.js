
notifications.onNotification(addNotification);

notifications.enableDesktopNotifications();

function addNotification(notification) {
    var li = document.createElement("li");
    li.innerHTML = notification.name + ' - ' + notification.timestamp;
    var notificationsList = document.getElementById("notifications");
    notificationsList.insertBefore(li, notificationsList.firstChild);

    notifications.desktopNotification('New foo', {body: notification.name, icon: notification.icon, tag: 'foo'});
}