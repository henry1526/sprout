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
    .controller('AddRecipeController', function($scope, SessionService, Restangular) {
        $scope.recipe = { ingredients: [], tags: [] };
        $scope.status = null;
        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }];

        Restangular.all('ingredients').getList().then(function(ingredients) {
            $scope.ingredients = ingredients

            for (var i = 0; i < $scope.ingredients.legth; i++) {
                $scope.ingredients[ingredientIndex].active = true;
            }
        });

        Restangular.all('tags').getList().then(function(tags) {
            $scope.tags = tags;
        });

        $scope.tagObjectsToIds = function() {
                for (var i = 0; i < $scope.recipe.tags.length; i++) {
                    var tag = $scope.recipe.tags[i];
                    $scope.recipe.tags[i] = tag.id;
                }
        }

        $scope.ingredientObjectsToIds = function() {
                for (var i = 0; i < $scope.recipe.ingredients.length; i++) {
                    var ingredient = $scope.recipe.ingredients[i];
                    $scope.recipe.ingredients[i] = ingredient.id;
                }
        }


        $scope.saveNewRecipe = function() {

            $scope.tagObjectsToIds()
            $scope.ingredientObjectsToIds();

            Restangular.all('create-recipe').customPOST($scope.recipe).then(function() {

                $scope.status = "The recipe was successfully created!";
                $scope.recipe = { ingredients: [], tags: [] };
            }, function() {
                $scope.status = "The recipe couldn't be saved";
            });
        };


        $scope.addIngredient = function(ingredientId) {
            if ($scope.recipe.ingredients.indexOf(ingredientId) == -1) {
                $scope.recipe.ingredients.push(ingredientId);

                for (var ingredientIndex in $scope.ingredients) {
                    var ingredient = $scope.ingredients[ingredientIndex];
                    if (ingredient.id == ingredientId) {
                        $scope.ingredients[ingredientIndex].active = false;
                    }
                }

            }
        };

        $scope.getIngredientName = function(ingredientId) {
            for (var ingredientIndex in $scope.ingredients) {
                var ingredient = $scope.ingredients[ingredientIndex];
                if (ingredient.id == ingredientId) {
                    return ingredient.name;
                }
            }
        };

        $scope.getTagName = function(TagtId) {
            for (var tagIndex in $scope.tags) {
                var tag = $scope.tags[tagtIndex];
                if (tagt.id == tagId) {
                    return tagt.name;
                }
            }
        };

        var getTagFromName = function(tagName){
            for (var tagIndex = 0; tagIndex < $scope.tags.length; tagIndex++) {
                var tag = $scope.tags[tagIndex];
                if (tag.name == tagName) {
                    return tag;
                }
            }
            return null;
        };

        var addTagToRecipe = function(tag) {
            if ($scope.recipe.tags.indexOf(tag) == -1) {
                $scope.recipe.tags.push(tag);
            }
        };

        $scope.saveTag = function (tagName) {
            var tag = getTagFromName(tagName);
            if (tag == null) {
                createTag(tagName);
            }
            else {
                addTagToRecipe(tag);
            }
            $scope.tagName = "";
        };

        var createTag = function (tagName) {

            var tag = {name: tagName};
            Restangular.all('tags').customPOST(tag).then(function (tag) {
                tag.justAdded = true;
                $scope.tags.push(tag);
                addTagToRecipe(tag);
            })
        };

        var getTagFromName = function(tagName) {
            for (var i = 0; i < $scope.tags.length; i++) {
                var tag = $scope.tags[i];
                if (tag.name == tagName) {
                    return tag;
                };
            }
        }

        // Functions to save ingredients.
        $scope.saveIngredient = function (ingredientName) {
            console.log('Add ingredient button clicked.' +
                'User typed ' + ingredientName);

            //Get the ingredient if it already exists.
            var ingredient = getIngredientFromName(ingredientName);

            //Create the ingredient if it doesn't already exist.
            if (ingredient == null) {
                createIngredient(ingredientName);
                console.log("You typed a new ingredient!");
            }
            //Add the newly found ingredient to the recipe.
            else {
                addIngredientToRecipe(ingredient);
                console.log("That ingredient already exists!");
            }
            //Clear the input box.
            $scope.ingredientName = '';
        }

        var addIngredientToRecipe = function (ingredient) {
            if ($scope.recipe.ingredients.indexOf(ingredient) == -1) {
                $scope.recipe.ingredients.push(ingredient);
            }
        };

        var createIngredient = function (name) {
            var ingredient = { name: name, glycemic_index: $scope.glycemicIndex};

            Restangular.all('ingredients').customPOST(ingredient).then(function (data) {
                addIngredientToRecipe(data);
            })
        }

        var getIngredientFromName = function (name) {
            for (var i = 0; i < $scope.ingredients.length; i++) {
                var ingredient = $scope.ingredients[i];
                if (ingredient.name == name) {
                    return ingredient;
                }
            }

            return null;
        }
    })

    .controller('EditRecipeController', function($scope, SessionService, Restangular, $routeParams, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        })

        $scope.methods = [
            { printed_name: 'Bake', stored_name: 'bake' },
            { printed_name: 'Microwave', stored_name: 'microwave' },
            { printed_name: 'Fry', stored_name: 'fry' },
            { printed_name: 'Dutch Oven', stored_name: 'dutch_oven' }];

        $scope.editRecipe = function() {
            Restangular.one('recipes', $scope.recipeId).customPUT($scope.recipe).then(function (data) {
                $scope.status = "The recipe was successfully edited!";
                $scope.recipe = data;
                $location.path('/recipes');
            }, function() {
                $scope.status = "The recipe couldn't be saved.";
            });
        }

        $scope.deleteRecipe = function() {
            Restangular.one('recipes', $scope.recipeId).customDELETE().then(function (data) {
                $location.path('/recipes');
            }, function() {
                $scope.status = "The recipe couldn't be deleted.";
            });
        }
    })

    .controller('RecipeDetailsController', function($scope, SessionService, Restangular, $routeParams) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).get({nested: 'true'}).then(function (data) {
            $scope.recipe = data;
        })
    })

    .controller('FavoritesController', function($scope, Sessionservice, Restangular) {

    })

    .controller('RecipeController', function($scope, SessionService, Restangular) {

        $scope.session = SessionService.getSession()

        Restangular.one('getuserid', $scope.session).customGET().then(function(data) {
            $scope.userId = data;
        })

        Restangular.all('recipes').getList().then(function (data) {
            $scope.recipes = data; // Put the server's response into $scope.recipes.
        });

        $scope.ifFavorited = function (recipe) {
            for (var i = 0; i < recipe.favorited_by.length; i++) {
                if ($scope.userId == recipe.favorited_by[i]) {
                    return true;
                }
            }
            return false;
        }

        $scope.unfavorite = function (recipe) {
            var index_of_favorite = recipe.favorited_by.indexOf($scope.userId);
            recipe.favorited_by.splice(index_of_favorite, 1);

            Restangular.one('recipes', recipe.id).customPUT(recipe);

        }

        $scope.favorite = function (recipe) {
            recipe.favorited_by.push($scope.userId);
            Restangular.one('recipes', recipe.id).customPUT(recipe);
        }

        $scope.filterFavorites = function() {
            if ($scope.favorites == 'soup') {
                $scope.favorites = '';
            }
            else {
                $scope.favorites = 'soup';
            }
        }

    });