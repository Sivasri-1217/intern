def route_request(req_data):
     if req_data['type'] == 'Leave':
        return "Direct Manager"
     elif req_data['priority'] == 'High':
        return "Senior Manager"
     elif req_data['type'] == 'Training' and req_data['department'] == 'HR':
        return "HR Head"
     else:
        return "Department Head"
    
     """
    Function to determine the approver based on request data.

    Parameters:
    - req_data (dict): A dictionary containing the following keys:
        - 'type' (str): The type of request (e.g., 'Leave', 'Training').
        - 'priority' (str): The priority level of the request (e.g., 'High', 'Medium', 'Low').
        - 'department' (str): The department of the requester (e.g., 'IT', 'HR').

    Returns:
    - str: The assigned approver based on the routing logic.
        - Example: 'Direct Manager', 'Senior Manager', 'HR Head', or 'Department Head'.

    Example:
        Input:
            req_data = {
                "type": "Leave",
                "priority": "High",
                "department": "IT"
            }
        Output:
            "Direct Manager"
    """
   
