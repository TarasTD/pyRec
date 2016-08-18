(function() {
'use strict';

angular
    .module('app')
    .directive('navBar', navBar);

/* @ngInject */
function navBar() {
  return {
    restrict: 'E',
    templateUrl: 'app/navBar/navBar.tpl.html',
    scope: true,

    controller: function($scope) {
    }
  };
}
}());
