%global packname  sva
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.0.0
Release:          1%{?dist}
Summary:          Surrogate Variable Analysis

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-corpcor R-mgcv 

BuildRequires:    R-devel tex(latex) R-corpcor R-mgcv 

%description
The sva package contains functions for removing batch effects and other
unwanted variation in high-throughput experiment. Specifically, the sva
package contains functions for the identifying and building surrogate
variables for high-dimensional data sets. Surrogate variables are
covariates constructed directly from high-dimensional data (like gene
expression/RNA sequencing/methylation/brain imaging data) that can be used
in subsequent analyses to adjust for unknown, unmodeled, or latent sources
of noise. The sva package can be used to remove artifacts in two ways: (1)
identifying and estimating surrogate variables for unknown sources of
variation in high-throughput experiments (Leek and Storey 2007 PLoS
Genetics,2008 PNAS) and (2) directly removing known batch effects using
ComBat (Johnson et al. 2007 Biostatistics). Removing batch effects and
using surrogate variables in differential expression analysis have been
shown to reduce dependence, stabilize error rate estimates, and improve
reproducibility, see (Leek and Storey 2007 PLoS Genetics, 2008 PNAS or
Leek et al. 2011 Nat. Reviews Genetics). Surrogate variable analysis and
ComBat were developed in the context of microarray experiments, but may be
used as a general tool for high throughput data sets where dependence may
be involved.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0.0-1
- initial package for Fedora