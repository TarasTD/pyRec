(function() {
'use strict';

angular
    .module('candidateView')
    .controller('candidateView', candidateView);

/* @ngInject */
function candidateView($scope, $stateParams, $http) {
    // console.log($stateParams.id);
    $http.get('/get_candidate/' + $stateParams.id).then(function(resp){
        $scope.candidate = resp.data
        console.log($scope.candidate)
        })

}
}());
