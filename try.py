# # from faker import Faker
# # import random
# #
# # fake = Faker('en_IN')  # 'en_IN' for Indian English locale
# #
# #
# # def generate_job_seekers(num_records):
# #     job_seekers = []
# #     for _ in range(num_records):
# #         full_name = fake.name()
# #         email_id = fake.email()
# #         contact = fake.phone_number()
# #         city = fake.city()
# #         address = fake.address()
# #
# #         # Ensure that the city is in Maharashtra
# #         while not city or city.lower() not in ['mumbai', 'pune', 'nagpur', 'nashik', 'aurangabad', 'solapur', 'amravati', 'kolhapur', 'thane']:
# #             city = fake.city()
# #
# #         job_seekers.append({
# #             'full_name': full_name,
# #             'email_id': email_id,
# #             'contact': contact,
# #             'city': city,
# #             'address': address
# #         })
# #
# #     return job_seekers
# #
# #
# # if __name__ == '__main__':
# #     num_records = 10
# #     job_seekers = generate_job_seekers(num_records)
# #
# #     # Print the generated job seekers
# #     for idx, job_seeker in enumerate(job_seekers, start=1):
# #         print(f"Job Seeker {idx}:")
# #         print(f"Full Name: {job_seeker['full_name']}")
# #         print(f"Email ID: {job_seeker['email_id']}")
# #         print(f"Contact: {job_seeker['contact']}")
# #         print(f"City: {job_seeker['city']}")
# #         print(f"Address: {job_seeker['address']}")
# #         print()
#
#
# <div class="rectangle-container">
#         <div class="frame-inner"></div>
#         <div class="srno-wrapper">
#           <div class="srno">Id</div>
#         </div>
#         <div class="name-wrapper">
#           <div class="name">Name</div>
#         </div>
#         <div class="contact-wrapper">
#           <div class="contact">Contact</div>
#         </div>
#         <div class="email-id-wrapper">
#           <div class="email-id">Email ID</div>
#         </div>
#         <div class="gender-wrapper shifted1">
#           <div class="gender">Gender</div>
#         </div>
#         <div class="image-parent">
#           <div class="image">Image</div>
#           <div class="action-wrapper shifted">
#             <div class="action">Action</div>
#           </div>
#         </div>
#       </div>
#
# {% for job_seeker in job_seekers %}
#             <main class="frame-main">
#               <div class="rectangle-div"></div>
#               <section class="frame-section">
#                 <div class="rectangle-parent1">
#                   <div class="frame-child1"></div>
#                   <div class="frame-wrapper1">
#                     <div class="parent">
#                       <div class="div">{{ job_seeker.id }}</div>
#                       <div class="dushyant-bhagwat-wrapper">
#                         <div class="dushyant-bhagwat">{{ job_seeker.full_name }}</div>
#                       </div>
#                       <div class="wrapper">
#                         <div class="div1">{{ job_seeker.mobile_no }}</div>
#                       </div>
#                       <div class="dushyantdbhagwatgmailcom">
#                         {{ job_seeker.email_id }}
#                       </div>
#                     </div>
#                   </div>
#                   <div class="male-wrapper">
#                     <div class="male">male</div>
#                   </div>
#                   <div class="vector-parent">
#                     {% if job_seeker.image %}
#                         <img
#                         id="image1"
#                           class="ellipse-icon"
#                           loading="lazy"
#                           alt=""
#                           src="{{ job_seeker.image.url }}"
#                         />
#                     {% else %}
#                         <img
#                         id="image2"
#                           class="ellipse-icon"
#                           loading="lazy"
#                           alt=""
#                           src="{% static 'images/profile pic.jpg' %}"
#                         />
#                     {% endif %}
#
#                     <div class="delete-wrapper">
#                         <button class="delete" data-user-id="{{ job_seeker.id }}" onclick="return confirm('Are you sure you want to delete this user?')">
#                             delete
#                         </button>
#                     </div>
#
#                     <script>
#                         // Add event listener to delete buttons
#                         document.querySelectorAll('.delete').forEach(button => {
#                             button.addEventListener('click', function() {
#                                 const userId = this.getAttribute('data-user-id');
#                                 // Send AJAX request to delete user
#                                 fetch(`/delete_job_seeker/${userId}`, {
#                                     method: 'DELETE',
#                                     headers: {
#                                         'X-CSRFToken': '{{ csrf_token }}'
#                                     }
#                                 })
#                                 .then(response => {
#                                     if (response.ok) {
#                                         // Remove the deleted user row from the UI
#                                         this.closest('.rectangle-parent').remove();
#                                         // Redirect to the same page after deleting
#                                         location.reload();
#                                     }
#                                 })
#                                 .catch(error => {
#                                     console.error(error);
#                                 });
#                             });
#                         });
#                     </script>
#
#
#                   </div>
#                 </div>
#               </section>
#             </main>
#       {% endfor %}