/**
	simulate.cpp

	Purpose: implements a Simulation class which
	simulates a robot living in a 2D world. Relies 
	on localization code from localizer.py 

	This file is incomplete! Your job is to make 
	this code work. 
*/

#include <algorithm>
#include "simulate.h"
#include "localizer.cpp"

/**
Constructor for the Simulation class.
*/
Simulation::Simulation(vector < vector <char> > map, 
	float blurring,
	float hit_prob, 
	std::vector<int> start_pos
	) 
{
	height = map.size();
	width = map[0].size();
	grid = map;
	blur = blurring;
	p_hit = hit_prob;
	p_miss = 1.0 - p_hit;
	beliefs = initialize_beliefs(map);
	incorrect_sense_prob = p_miss / (p_hit + p_miss);
	true_pose = start_pos;
	prev_pose = true_pose;
	colors = get_colors();
}

/**
 * 
 */
void Simulation:: run(int numsteps) {
	while (numsteps--) {
		char color = get_observed_color();
		//cout << "color = " << color << endl;
		beliefs = sense(color, grid, beliefs, p_hit, p_miss);
		//show_grid(beliefs);
		vector<int> d = get_random_move();
		beliefs = move(d[0], d[1], beliefs, blur);
		prev_pose = true_pose;
		cout << true_pose.size() << endl;
		true_pose[0] = (true_pose[0] + d[0] + height) % height;
		true_pose[1] = (true_pose[1] + d[1] + width) % width;
	}
}
/**
Grabs colors from the grid map.
*/
vector <char> Simulation::get_colors() {
	vector <char> all_colors;
	char color;
	int i,j;
	for (i=0; i<height; i++) {
		for (j=0; j<width; j++) {
			color = grid[i][j];
			if(std::find(all_colors.begin(), all_colors.end(), color) != all_colors.end()) {
				/* v contains x */
			} else {
				all_colors.push_back(color);
				cout << "adding color " << color << endl;
				/* v does not contain x */
			}
		}
	}
	colors = all_colors;
	num_colors = colors.size();
	return colors;
}

/**
 * Get the color at current position
 */
char Simulation::get_observed_color() {
	char true_color = grid[true_pose[0]][true_pose[1]];
	if (rand() < RAND_MAX * incorrect_sense_prob) {
		vector<char> options;
		for (auto c : colors) {
			if (c == true_color) {
				continue;
			}
			options.push_back(c);
		}
		return options[rand() % options.size()];
	} 
	else {
		return true_color;
	}
}

/**
 * Move the robot randomly to adjacent cells
 */
vector<int> Simulation::get_random_move() {
	vector<int> res(2);
	res[0] = rand() % 3 - 1;
	res[1] = rand() % 3 - 1;
	return res;
}

/**
You can test your code by running this function. 

Do that by first compiling this file and then 
running the output.
*/
int main() {
	
	vector < vector <char> > map;
	vector <char> mapRow;
	int i, j, randInt;
	char color;
	std::vector<int> pose;
	pose.push_back(0);
	pose.push_back(0);
	cout << pose.size() << endl;
	for (i = 0; i < 4; i++)
	{
		mapRow.clear();
		for (j=0; j< 4; j++)
		{
			randInt = rand() % 2;
			if (randInt == 0 ) {
				color = 'r';
			} 
			else {
				color = 'g';
			}
			mapRow.push_back(color);
		}
		map.push_back(mapRow);
	}
	cout << "map is\n";
	Simulation simulation (map, 0.1, 0.9, pose);
	cout << "initialization success!\n";
	show_grid(map);

	cout << "x, y = (" << simulation.true_pose[0] << ", " << simulation.true_pose[1] << ")" << endl;

	while(cin.get() == '\n') {
		simulation.run(1);
		show_grid(simulation.beliefs);
		cout << "x, y = (" << simulation.true_pose[0] << ", " << simulation.true_pose[1] << ")" << endl;
	}
	return 0;
}
