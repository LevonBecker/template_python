from invoke import task


@task(name="pytest")
def run_pytest(context):
    """Run Pytest Unit Test Suite"""
    print("\n------------")
    print("Pytest")
    print("------------\n")
    context.run("pytest")
