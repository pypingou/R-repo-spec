%global packname  timeDate
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2131.00
Release:          1%{?dist}
Summary:          Rmetrics - Chronological and Calendarical Objects

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-utils R-stats R-methods 

BuildRequires:    R-devel tex(latex) R-graphics R-utils R-stats R-methods 

%description
Environment for teaching "Financial Engineering and Computational Finance"

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
%doc %{rlibdir}/timeDate/html
%doc %{rlibdir}/timeDate/DESCRIPTION
%{rlibdir}/timeDate/unitTests
%{rlibdir}/timeDate/R
%{rlibdir}/timeDate/NAMESPACE
%{rlibdir}/timeDate/INDEX
%{rlibdir}/timeDate/COPYRIGHT.html
%{rlibdir}/timeDate/help
%{rlibdir}/timeDate/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2131.00-1
- initial package for Fedora