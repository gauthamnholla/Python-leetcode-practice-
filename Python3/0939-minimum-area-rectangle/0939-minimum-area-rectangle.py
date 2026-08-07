class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        hashmap = {} # Key => Integer | Value => Set

        for single_point in points: # Iterate through every single point & store the coordinates in map
            if single_point[0] not in hashmap: # Check if x coordinate of the single point already exisits as a Key in hasmap
                hashmap[single_point[0]] = set() # Insert a new Key (equal to x coordinate) in the hashmap with corresponding Value (equal to newly created empty HashSet)
            hashmap[single_point[0]].add(single_point[1]) # Insert y coordinate into Value (HashSet) corresponding to Key (equal to x coordinate)
			# Explanation : 
			#		single_point => refering to a single point [x,y]
			#		x-coordinate of a single point => single_point[0]
			#		y-coordinate of a single point => single_point[1]

			#		Key => x coordinate of a point 
			#			=> single_point[0]

			#		Value => HashSet of y coordinates 
			#			=> hashmap[Key]
			#			=> hashmap[x-coordinate of a single point]
			#			=> hashmap[single_point[0]]

			#		Insert y coordinate into corresponding Value (HashSet)
			#			=> Value.add(y-coordinate of a single point)
			#			=> hashmap[Key].add(y-coordinate of a single point)
			#			=> hashmap[x-coordinate of a single point].add(y-coordinate of a single point)
			#			=> hashmap[single_point[0]].add(single_point[1])

        minimum_area = inf # Vairable to store the minimum area

        for i in range(len(points)): # Iterator corresponding to different A points
            for j in range(len(points)): # Iterator corresponding to different B points

                x1, y1 = points[i][0], points[i][1] # Coordinates of Point A
                
                x2, y2 = points[j][0], points[j][1] # Coordinates of Point B

                if x1 != x2 and y1 != y2: # Point A & B must form a diagonal of the rectangle.
                    if (y2 in hashmap[x1] # Check if D exists in hashmap
                            and 
                    y1 in hashmap[x2]): # Check if C exists in hashmap
                    # Explanation :
                    #		Check existence of y2 in Value (HashSet) corresponding to x1 Key
					#			=> (y-coordinate of point B) in Value
					#			=> (y-coordinate of point B) in hashmap[Key]
					#			=> (y-coordinate of point B) in hashmap[x-coordinate of point A]
                    #			=> y2 in hashmap[x1] => Checks if point D exists in hashmap
					#		Check existence of y1 in Value (HashSet) corresponding to x2 Key
					#			=> (y-coordinate of point A) in Value
					#			=> (y-coordinate of point A) in hashmap[Key]
					#			=> (y-coordinate of point A) in hashmap[x-coordinate of point B]
                    #			=> y1 in hashmap[x2] => Checks if point C exists in hashmap
                        minimum_area = min(minimum_area, abs(x1-x2) * abs(y1-y2)) # Store the minimum area possible
        
        return minimum_area if minimum_area != inf else 0 # Return 0 if no rectangle exists