var ChatApp = angular.module('ChatApp', [
    'SwampDragonServices',
    'ChatControllers'
]);

swampdragon.ready(function () {
    subscribe();
});


function subscribe () {
    swampdragon.subscribe('chat', 'local-channel', null, 
        function (context, data) {
    }, function (context, data) {
    });
}

