var app = angular.module('app', ['ngRoute', 'ngResource']);

app.controller('admin', function($scope, $resource){
    api = $resource('/:api',{api: '@api'});

    api.get({api: 'data'}, function(json){
        console.log(json)
    })

})