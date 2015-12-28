(function() {
'use strict';

angular
    .module('app')
    .directive('candidatesList', candidatesList);

/* @ngInject */
function candidatesList() {
  return {
    restrict: 'E',
    templateUrl: 'app/candidatesList/candidatesList.tpl.html',
    scope: true,

    controller: function($scope, $mdDialog, $mdMedia, $http, $stateParams) {
      $scope.status = '  ';
      $scope.customFullscreen = $mdMedia('xs') || $mdMedia('sm');
        $scope.message = '';
        $scope.left  = function() {return 100 - $scope.message.length;};
        $scope.clear = function() {$scope.message = '';};
        $scope.save  = function() {alert($scope.message);};
        $http.get('/s').then(function(resp) {
        $scope.users = resp.data;
        console.log($scope.users);
    });
      $scope.remove = function(id) {
        $http.post('/remove_candidate', {'id': id}).then(function(resp) {
        console.log(resp);
        $http.get('/s').then(function(resp) {
        $scope.users = resp.data;
        console.log($scope.users);
        });
      });
    };
    }
  };
}
}());
