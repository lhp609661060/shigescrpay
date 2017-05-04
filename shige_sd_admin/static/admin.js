var app = angular.module('app', ['ngRoute', 'ngResource']);

app.controller('admin', function($scope, $resource){
    api = $resource('/:api',{api: '@api'});

    $scope.search = function(){
        console.log($scope.kw);
        api.get({api: 'search', kw: JSON.stringify({kw: $scope.kw})}, function(json){
            console.log(json)
        })
    }
    
    $scope.keypress = function ($event) {
        if($event.keyCode==13){//回车
            $scope.search();
        }
    }

    $scope.search();

})
