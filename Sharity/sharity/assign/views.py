from django.http import HttpResponse
from django.shortcuts import redirect, render
from Sharity.sharity.apply.models import Application
from Sharity.sharity.assign.models import Assignment

from Sharity.sharity.offers.models import Offer

# This is for listing assingments for the services
# Login is required to see details of services 

#@login_required(login_url='login')
def assigning(request, ofnum):
    offer = Offer.objects.get(serviceID=ofnum)
    application = Application.objects.filter(serviceID=ofnum)
    allAccepted = Application.objects.filter(status='Accepted').filter(serviceID=offer).count()
    
    # Remaning capacity is sent to frontend to avoid more assignments than capacity
    remainingCapacity = offer.capacity - allAccepted

    context = {'offers':offer, 'applications':application, "remainingCapacity":remainingCapacity}
    
    #This needs to be updated based on assignment Front-end
    return render(request, 'landing/assignment.html', context)

# This is for accepting requests and assinging users for the services
# Login is required to see details of services

#@login_required(login_url='login')
def assignService(request,sID, rID, uID, sType):

    # Information application to be assigned is retrieved
    myRequest = Application.objects.get(requestID=rID)

    # Application is processed if it's still in 'Inprocess' state
    # New assignment object is created for this application
    if myRequest.status == 'Inprocess':
        newassignment = Assignment.objects.create(
                requestID=myRequest, 
                approverID=request.user, 
                requesterID=myRequest.requesterID, 
                serviceType=myRequest.serviceID.serviceType, 
                status="Open"
            )    
       
        # When assignment is done status for service is updated as 'Assigned', and application status is updated as 'Accepted'
        if newassignment:

            newassignment.requestID.serviceID.status = 'Assigned'
            newassignment.save()
            
            myRequest.status = 'Accepted'
            myRequest.save()

            # Remaining capacity is calculated by deducting all accepted request.

            allAccepted = Application.objects.filter(status='Accepted').filter(serviceID=myRequest.serviceID).count()
            remainingCapacity = newassignment.requestID.serviceID.capacity - allAccepted

            # New notification is created for requesters to inform that the application is accepted, and request is approved
 #           newnote = Notification.objects.create(
 #                   serviceID=myRequest.serviceID, 
 #                   receiverID=myRequest.requesterID, 
 #                   noteContent=request.user.username
 #                               +' approved your request for '
 #                               + myRequest.serviceID.keywords, 
 #                   status='Unread'
 #              )
 #           if newnote:

                # After the assignment, if there is no availbe capacility, all 'Inprocess' applications' status are updated as 'Rejected'
                # Credits for these applications are released back
                # A notification is sent to requester to inform than application is rejected due to capacity constraint

 #               if remainingCapacity == 0:
 #                   openRequests = Requestservice.objects.filter(status='Inprocess').filter(serviceID=myRequest.serviceID)
 #                   
 #                   for openRqst in openRequests:
 #                       openRqst.status = 'Rejected'
 #                       openRqst.save()

 #                       # Credits given back
 #                       creditNeeded = 0
 #                       if openRqst.serviceID.serviceType == "Offering":
 #                           creditNeeded = openRqst.serviceID.duration
 #                       blkQnt= creditNeeded
 #                       openRqst.requesterID.profile.blockCredit(+blkQnt)
 #                       openRqst.requesterID.profile.save()
                        
                        # Notification for rejection
 #                       newnote = Notification.objects.create(
 #                               serviceID=openRqst.serviceID, 
 #                               receiverID=openRqst.requesterID, 
 #                               noteContent=request.user.username
 #                                           +' could not acceept your request for '
 #                                           + myRequest.serviceID.keywords
 #                                           +' due to capacity constraints',
 #                               status='Unread'
 #                           )
                
                # User is sent back to assignment page to see updates.
            application = Application.objects.filter(serviceID=myRequest.serviceID)
            context = {'offers':myRequest.serviceID, "applications":application, "remainingCapacity":remainingCapacity}
            return render(request, 'landing/assignment.html', context)
        else:
            return HttpResponse("A problem occured. Please try again later")
    else:
        return redirect('home')