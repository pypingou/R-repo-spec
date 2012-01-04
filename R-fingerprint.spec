%global packname  fingerprint
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.4.5
Release:          1%{?dist}
Summary:          Functions to operate on binary fingerprint data

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This package contains functions to manipulate binary fingerprints of
arbitrary length. A fingerprint is represented by an object of S4 class
'fingerprint' which is internally represented a vector of integers, such
that each element represents the position in the fingerprint that is set
to 1. The bitwise logical functions in R are overridden so that they can
be used directly with 'fingerprint' objects. A number of distance metrics
are also available (many contributed by Michael Fadock). Fingerprints can
be converted to Euclidean vectors (i.e., points on the unit hypersphere)
and can also be folded using OR.  Arbitrary fingerprint formats can be
handled via line handlers. Currently handlers are provided for CDK, MOE
and BCI fingerprint data.

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
%doc %{rlibdir}/fingerprint/DESCRIPTION
%doc %{rlibdir}/fingerprint/html
%{rlibdir}/fingerprint/libs
%{rlibdir}/fingerprint/NAMESPACE
%{rlibdir}/fingerprint/Meta
%{rlibdir}/fingerprint/INDEX
%{rlibdir}/fingerprint/help
%{rlibdir}/fingerprint/R
%{rlibdir}/fingerprint/unitTests

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.4.5-1
- initial package for Fedora