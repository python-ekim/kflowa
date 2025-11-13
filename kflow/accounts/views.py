from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def otp_status(request):
    # OTPMiddleware wraps request.user and adds .is_verified()
    try:
        verified = request.user.is_verified()  # method, not a simple attribute
    except Exception:
        verified = False
    return HttpResponse(f"Logged in as {request.user.username}. OTP verified: {verified}")

@login_required
def profile(request):
    return HttpResponse("Profile OK")

