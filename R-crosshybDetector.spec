%global packname  crosshybDetector
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Detection of cross-hybridization events in microarray experiments

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-marray R-methods 

BuildRequires:    R-devel tex(latex) R-marray R-methods 

%description
Functions for identification of probes potentially affected by
cross-hybridizations in microarray experiments. Includes functions for
diagnostic plots. The package contains code from the dismissed pairseqsim
package (removed in BioConductor > 1.9 ), created by Witold Wolski
<witek96@users.sourceforge.net> and released under GNU LGPL license

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
* Wed Nov 23 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora