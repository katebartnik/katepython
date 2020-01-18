import sys
sys.path.insert(1, '../repository')

import CoachRepository
# import CategoryRepository

CoachRepository = CoachRepository.CoachRepository()
# CategoryRepository = CategoryRepository.CategoryRepository()

coaches = CoachRepository.findOneById(5)
print(coaches)
