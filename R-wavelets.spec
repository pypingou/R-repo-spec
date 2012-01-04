%global packname  wavelets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          A package of funtions for computing wavelet filters, wavelet transforms and multiresolution analyses

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package contains functions for computing and plotting discrete
wavelet transforms (DWT) and maximal overlap discrete wavelet transforms
(MODWT), as well as their inverses. Additionally, it contains
functionality for computing and plotting wavelet transform filters that
are used in the above decompositions as well as multiresolution analyses.

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
%doc %{rlibdir}/wavelets/html
%doc %{rlibdir}/wavelets/DESCRIPTION
%{rlibdir}/wavelets/data
%{rlibdir}/wavelets/libs
%{rlibdir}/wavelets/R
%{rlibdir}/wavelets/Meta
%{rlibdir}/wavelets/NAMESPACE
%{rlibdir}/wavelets/help
%{rlibdir}/wavelets/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora