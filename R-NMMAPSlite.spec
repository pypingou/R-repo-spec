%global packname  NMMAPSlite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          NMMAPS Data Lite

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stashR 


BuildRequires:    R-devel tex(latex) R-stashR



%description
Provides remote access to daily mortality, weather, and air pollution data
from the National Morbidity, Mortality, and Air Pollution Study for 108
U.S. cities (1987--2000); data are obtained from the Internet-based Health
and Air Pollution Surveillance System (iHAPSS)

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
%doc %{rlibdir}/NMMAPSlite/COPYING
%doc %{rlibdir}/NMMAPSlite/html
%doc %{rlibdir}/NMMAPSlite/doc
%doc %{rlibdir}/NMMAPSlite/DESCRIPTION
%doc %{rlibdir}/NMMAPSlite/CITATION
%{rlibdir}/NMMAPSlite/NAMESPACE
%{rlibdir}/NMMAPSlite/Meta
%{rlibdir}/NMMAPSlite/help
%{rlibdir}/NMMAPSlite/code
%{rlibdir}/NMMAPSlite/R
%{rlibdir}/NMMAPSlite/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.2-1
- initial package for Fedora