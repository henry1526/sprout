'use strict';

/* Controllers */

angular.module('sproutApp.controllers', [])
    .controller('BaseController', ['$scope', '$window', 'brand', 'SessionService', function($scope, $window, brand, SessionService) {
        $scope.brand = brand;

        $scope.doLogout = function() {
            SessionService.removeSession();
            $window.location = '/';
        };
    }])
    .controller('HomeController', ['$scope', 'SessionService', function($scope, SessionService) {
        $scope.session = SessionService.getSession();

        $scope.user = {};

        $scope.$on('event:login-confirmed', function() {
            console.log('event has been broadcast to Home Controller');
            $scope.session = SessionService.getSession();
        });
    }])
    .controller('ItemsController', function($scope, SessionService, Restangular) {
        $scope.session = SessionService.getSession();

        var item1 = {
                name: "Item one",
                number: "12"
        };

        var item2 = {
                name: "Item two",
                number: "24"
        };

//        $scope.items = [item1, item2];

        Restangular.all('items').getList().then(function (data) {
            $scope.items = data;
        });
    });