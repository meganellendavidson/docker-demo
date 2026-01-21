## Docker Explained - Wheatbag Theory

### Base Materials = Base Images

Before you make a Wheat bag, you need basic materials like fabric, wheat and thread. In Docker base images (Ubuntu/Alpine) provide the foundational layers for your applications and will be specified in your sewing pattern (Dockerfile).

### Sewing Pattern = Dockerfile

A pattern tells you how to prepare a wheatbag from scratch, similarly a Dockerfile contains the instructions for building an image.
If you share the sewing pattern others can make their own wheatbag.

### Wheatbag = Docker Image

A wheatbag is fully prepared, packaged, and ready to heat. It's static and doesn't change, you can store or share it with others. Similarly a Docker image is a complete, read-only package with everything your app needs. You can share the image via Docker Hub so others can 'heat' it without making it from scratch using the pattern.

### Heated Wheatbag = Docker Container

When you heat the wheatbag it becomes active and ready to use. You can heat multiple wheatbags at the same time and you can reuse the wheatbag whenever it is required. Similarly a Docker container is a running instance of the image.

### Microwave = Host

The microwave is where you heat the wheatbag, different microwaves can heat the same wheatbag and get the same result. Different computers can run the same docker image and create identical containers.

### Orchestration

Docker lets you prepare and heat individual wheatbags but what if you're running a busy hotel that provides guests with wheatbags during turndown service? You need a system to manage hundreds of wheatbags efficiently. That's where orchestration comes in.

Container orchestration (Kubernetes) acts as the hotel manager:
- Scaling: if 50 guests arrive, the hotel manager heats 50 heated wheatbags automatically (creates containers)
- Load balancing: the hotel manager decides which microwave (node/server) heats which wheatbag for efficiency. 
- Health Checks: If a microwave breaks, it moves wheatbags to another one (reschedules containers).
- Inventory: Ensures enough wheatbags (images) are available.