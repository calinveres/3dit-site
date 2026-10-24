# One source for the privacy policy and support text: writes the web pages and the app's bundled JSON.
import json, html, sys
APP = sys.argv[1] if len(sys.argv) > 1 else None
EMAIL = "calinveres1@gmail.com"
UPDATED = "October 24, 2026"

privacy = [
 ("The short version", "3Dit has no account, no ads, no tracking and no analytics. Your scans, photos and measurements stay on your device. The developer never receives them, and the app has no server of its own."),
 ("What the app saves on your device", "When you scan, 3Dit uses the camera and LiDAR to save room geometry, reference photos, a walkthrough video, depth frames and camera positions. It also saves what you add: project and room names, addresses, notes, inventory, laser measurements, plans you import, cable runs and design options. Technical details about each scan (device model, tracking quality, memory and temperature warnings) are saved with it so problems can be diagnosed. Photos and room geometry can show private details of your surroundings."),
 ("People in photos", "To keep people out of models and renders, 3Dit looks for people, faces, hands and bodies in your scan photos and masks them out. This runs entirely on your device with Apple’s Vision framework. Nothing is uploaded, and the app doesn’t identify anyone."),
 ("Camera", "Camera access is requested when you start a scan. You can turn it off in Settings. Viewing, importing and sharing existing scans doesn’t need it."),
 ("Location", "Location is used only when you tap Use my location to fill in an address. Your position is sent to Apple’s Maps services to look up the street address and nearby places, and 3Dit saves only the address you keep. The Sites map also uses Apple Maps. Apple’s handling of this is covered by Apple’s privacy policy."),
 ("Photos library", "3Dit asks to add to your Photos library only when you choose to save something there, such as a walkthrough video or design image. It never reads your library."),
 ("Sharing", "Nothing is shared automatically. When you share a room, export for CAD or send a design, iOS sends the file to the app, person or device you pick. Exports can contain photos, video, measurements and scan diagnostics, so check the destination first. Copies you share are controlled by whoever receives them."),
 ("Purchases", "If you buy 3Dit Pro, Apple handles the payment. 3Dit only learns whether Pro is unlocked on your Apple Account and never sees your payment details."),
 ("Storage, backups and deletion", "Scans are stored in the app’s Documents folder, which you can also reach through the Files app. Your device backups may include them. Deleted rooms go to Recently Deleted until you restore them or delete them permanently. Deleting a project removes its scans from the device. Backups and copies you’ve shared have to be removed separately."),
 ("Children", "3Dit is a measuring tool for general audiences and doesn’t knowingly collect information from children."),
 ("Changes and contact", f"If 3Dit’s data practices change, this policy will be updated and the date above will change. Questions? Email {EMAIL}."),
]
support = [
 ("Get in touch", f"Email {EMAIL}. Include your device model, iOS version, the 3Dit version (in Help & privacy), and what you tapped before the problem. Please don’t attach private room photos or scan exports unless you want to share them. When testing through TestFlight, you can also take a screenshot and tap Share Beta Feedback."),
 ("Supported devices", "Scanning needs an iPhone Pro or iPad Pro with LiDAR, on iOS 17 or later. Other iPhones and iPads can open, view and share scans that were made on a LiDAR device."),
 ("Scanning a room", "Create a project, tap Scan a room and name it. Move slowly in good light and keep walls and furniture in view; the guide tells you what’s left to cover. Finish when you’re happy, then open the room for the 3D model, measurements, inventory and the walkthrough video. Check critical measurements with a tape or laser before ordering or building."),
 ("Hiding and moving items", "In the 3D view, tap an item to move, turn or hide it. The eye button on the right lists every item: show or hide them one at a time, or use Show all and Hide all. Hidden items stay hidden in every view."),
 ("Redesign", "Open a room and tap Redesign in 3D. Tap a wall, the floor or an item to change it: paint, finishes, furniture and new walls. Keep several options, compare with Before, and share an image or the CAD files."),
 ("Exporting for CAD", "Export for CAD creates a floor plan (DXF) for Vectorworks, AutoCAD and others, plus 3D models for SketchUp. Laser-corrected walls are marked (L)."),
 ("Camera access is off", "Open Help & privacy, then Open app settings, and turn on Camera. If it can’t be turned on, Screen Time or a device-management profile may be blocking it."),
 ("Importing a shared room", "Save the 3Dit ZIP to Files and tap it to unzip. In 3Dit, tap the import button at the top left and pick the folder that contains manifest.json."),
 ("Recovering a deleted room", "Deleted rooms go to Recently Deleted, below the project’s room list. Restore them from there or delete them permanently."),
]

def page(title, sections, lead=""):
    secs = "\n".join(f"<section><h2>{html.escape(t)}</h2><p>{html.escape(b).replace(html.escape(EMAIL), f'<a href=\"mailto:{EMAIL}\">{EMAIL}</a>')}</p></section>" for t, b in sections)
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · 3Dit</title><link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png"></head>
<body><main>
<header><img src="icon.png" alt=""><a href="./">3Dit</a><nav><a href="privacy.html">Privacy</a><a href="support.html">Support</a></nav></header>
<h1>{html.escape(title)}</h1><p class="updated">Updated {UPDATED}</p>
{lead_html}
{secs}
<footer>3Dit · scan, measure and redesign spaces with LiDAR</footer>
</main></body></html>
"""

open("privacy.html", "w").write(page("Privacy policy", privacy))
open("support.html", "w").write(page("Help & support", support))
open("index.html", "w").write(page("3Dit", [
 ("Scan any space", "Scan rooms, houses, AV installs and construction sites with your iPhone’s LiDAR. 3Dit builds a clean 3D model, measurements, an inventory and a walkthrough video."),
 ("Plan and redesign", "Redesign rooms in 3D, line scans up on building plans, map cable runs, and export to SketchUp, Vectorworks and other CAD tools."),
 ("Private by design", "No account and no tracking. Your scans stay on your device.")],
 lead="Scan, measure and redesign spaces with LiDAR.").replace('<p class="updated">Updated ' + UPDATED + '</p>', ''))
if APP:
    for name, title, secs in [("PrivacyPolicy.json", "Privacy policy", privacy), ("Support.json", "Help & support", support)]:
        json.dump({"title": title, "updated": UPDATED, "sections": [{"title": t, "body": b} for t, b in secs]},
                  open(f"{APP}/{name}", "w"), ensure_ascii=False, indent=2)
print("ok")
