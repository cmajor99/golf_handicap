function handicap()
        {
            var player = document.getElementById('players').value;
            var inputVal = "";
            if (player) 
            {
                input_player = player.value;
            }
            console.log(player);
            var course = document.getElementById('courses').value;
            if (course) 
            {
                input_course = course.value;
            }
            console.log(course);
            var tee = document.getElementById('tees').value;
            if (tee) 
            {
                input_tee = tee.value;
            }
            console.log(tee); 
            var score = document.getElementById('myscore').value;
            if (score) 
            {
                input_score = score.value;
            }
            console.log(score); 
        }
