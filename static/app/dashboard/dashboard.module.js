/**
 * @ngdoc overview
 * @name app.dashboard
 * @description < description placeholder >
 */

(function(){
'use strict';

angular
    .module('app.dashboard', ['ui.router'])
    .config(configuration);

/* @ngInject */
function configuration($stateProvider){
  //add your state mappings here
  $stateProvider.state('dashboard', {
    url: '/dash',
    templateUrl: 'app/dashboard/index.html',
    controller: 'dashboard',
    title: 'LANG_DASHBOARD',
  });
}

}());
