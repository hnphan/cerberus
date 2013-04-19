//JavaScript Document
$(document).ready(function(){
	
	var start = document.getElementById("start");
	var restart = document.getElementById("restart");
	var loadcount =0;
	//var restartMenu,menu;
	//showButton();	
	
	function showButton() {
	start.style.top = "30%";
	}
	
	var canvas = $('#snake')[0],
		ctx;
		
	//varibles of direction,food, score, and the array of the snake
	var di;
	var food;
	var score;
	var snake;
	var cell = 20;
	var w = $("#snake").width();
	var h = $("#snake").height();
	
			
	if(canvas.getContext){
		ctx= canvas.getContext("2d");
		$('#start').click(function(){
			startMenu();
			init();
		});
	
		
		
		function init(){
			menu.style.zIndex = "-1";
			restartMenu.style.zIndex = "-1";
			di= "right";
			createSnake();
			createFood();
			score=0;		
			scoreStyle.innerHTML = "Score:"+score;
			if(typeof game_loop!="undefined"){
				 clearInterval(game_loop);
				 showButton();
				}
			 game_loop = setInterval(paint,60);
			}
			
		
	
		function createSnake(){
			var length = 5; 
			snake = [ ]; 
			for(var i = length-1; i>=0; i--){			
				snake.push({x:i, y:0});
				}
			}
		
		function createFood() {
			food = {
				x: Math.round(Math.random()*(w-cell)/cell),
				y: Math.round(Math.random()*(h-cell)/cell),
				};
			}
			
		
		function paint(){
			
			ctx.fillStyle = "white";
			ctx.fillRect(0, 0, w, h);
			ctx.strokeStyle = "black";
			ctx.strokeRect(0, 0, w, h);
			
			
			
			var nx = snake[0].x;
			var ny = snake[0].y;
			
			if(di == "right") nx++;
			else if(di == "left") nx--;
			else if(di == "up") ny--;
			else if(di == "down") ny++;
			
		
			if(nx == -1 || ny == h/cell || nx == w/cell || ny == -1  || check_collision(nx, ny, snake)){
				clearInterval(game_loop);
				showButton();
				restartMenu.style.zIndex = "1";
				$('#restart').click(function(){
					init();
					});			
				return;
				}
			
			
			if(nx == food.x && ny == food.y){
				var tail = {x: nx, y: ny};
				score=score+5;
				createFood()
				}
				
			else{
				var tail = snake.pop(); 
				tail.x = nx; tail.y = ny;
				}
			
			snake.unshift(tail); 
			
			for(var i = 0; i < snake.length; i++){
				var c = snake[i];
				paint_cell(c.x, c.y);
				}
			
			paint_cell(food.x, food.y);
			
			}
		
		
		function paint_cell(x, y){
			ctx.fillStyle = "black";
			ctx.fillRect(x*cell, y*cell, cell, cell);
			}
		
		function check_collision(x, y, array){
		
			for(var i = 0; i < array.length; i++)
			{
				if(array[i].x == x && array[i].y == y)
				 return true;
			}
			return false;
			}
		
		//keyboard
		$(document).keydown(function(e){
			var key = e.which;
			if(key == "37" && di != "right") di = "left";
			else if(key == "38" && di != "down") di = "up";
			else if(key == "39" && di != "left") di = "right";
			else if(key == "40" && di != "up") di = "down";
		})
		
		function startMenu(){
		menu = document.getElementById("mainMenu");
		restartMenu = document.getElementById("restartMenu");
		scoreStyle = document.getElementById("score");
		restartMenu.style.zIndex = "-1";
		
		}
		
		
		
				
	}
	
	else{
		alert('Canvas is not supported in your browser.');
	}
	
})