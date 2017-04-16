var app = angular.module('todo', ['ngResource', 'ui.bootstrap', 'todoCtrls', 'todoServices', 'todoDirectives']);

app.config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);