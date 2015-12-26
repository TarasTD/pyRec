/**
 * @ngdoc overview
 * @name app.dashboard
 * @description < description placeholder >
 */

(function(){
'use strict';

angular
    .module('candidateView', ['ui.router'])
    .config(configuration);

/* @ngInject */
function configuration($stateProvider){
  //add your state mappings here
  $stateProvider.state('candidateView', {
    url: '/candidate/:id',
    templateUrl: 'app/candidateView/candidateView.tpl.html',
    controller: 'candidateView',
    title: 'candidateView',
  });
}

}());
