var ChatControllers = angular.module('ChatControllers', []);

ChatControllers.controller('ChatCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.channel = 'chat';
    $scope.messages = [];
    
    /// Subscribe to the chat router
    $dragon.onReady(function () {
        $dragon.subscribe('chat', $scope.channel, {chat__id: $scope.chatid}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
        });

        $dragon.getSingle('message', {id: $scope.chatid}).then(function(response) {
            $scope.chat = response.data;
        });

        $dragon.getList('message', {chat_id: $scope.chatid}).then(function(response) {
            $scope.messages = response.data;
        });
    });

    $dragon.onChannelMessage(function (channels, message) {
        console.log('came');
        addMessage(data.data.author.username, data.data.text);
    });

    $scope.sendMessage = function () {
        $scope.errors = null;
        $dragon.callRouter('chat', 'chat', {message: this.message})
            .then(function (response) {
                $scope.message = '';
            })
            ["catch"](function (response) {
            $scope.errors = response.errors;
        });
    }


    swampdragon.onChannelMessage(function (chanel, data) {
        console.log('came');
        addMessage(data.data.author.username, data.data.text);
    });

    document.getElementById("send-message-button").addEventListener("click", function () {
        var message = document.getElementById("message").value;
        sendMessage(message);
        console.log('sent');
    });


    function addMessage(name, msg) {
        var messages = document.getElementById("messages");
        messages.innerHTML += '<li>' + name + ' : ' + msg +  '</li>';
        console.log(name);

    }


    function sendMessage(message) {
        // Reset error messages
        document.getElementById('error-name').innerHTML = "";
        document.getElementById('error-message').innerHTML = "";
        console.log(message);
        // Send message
        swampdragon.callRouter('chat', 'chat', {message: message, chat_id: $scope.chatid}, null, function (e, error) {
            console.log('error');
        });
    }
    
}]);