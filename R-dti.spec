%global packname  dti
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Analysis of diffusion weighted imaging (DWI) data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-adimpro R-fmri R-rgl R-gsl 


BuildRequires:    R-devel tex(latex) R-methods R-adimpro R-fmri R-rgl R-gsl



%description
Diffusion Weighted Imaging (DWI) is a Magnetic Resonance Imaging modality,
that measures diffusion of water in tissues like the human brain. The
package contains R-functions to process diffusion-weighted data. The
functionality includes diffusion tensor imaging (DTI), structural adaptive
smoothing in in case of (DTI) (K. Tabelow, J. Polzehl, V. Spokoiny, and
H.U. Voss, Diffusion Tensor Imaging: Structural Adaptive Smoothing,
Neuroimage 39(4), 1763-1773 (2008)), modeling for high angular resolution
diffusion weighted imaging (HARDI) using Q-ball-reconstruction and tensor
mixture models and a stremaline fiber tracking for tensor and tensor
mixture models. The package provides functionality to manipulate and
visualize results in 2D and 3D.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0.1-1
- initial package for Fedora