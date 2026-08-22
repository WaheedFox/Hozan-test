def test_foundation_imports():
    import hozan
    from hozan.core.lifecycle.runtime import Lifecycle
    from hozan.features.registry import FeatureRegistry

    assert hozan is not None
    assert Lifecycle is not None
    assert FeatureRegistry is not None
