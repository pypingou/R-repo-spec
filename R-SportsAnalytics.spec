%global packname  SportsAnalytics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Infrastructure for Sports Analytics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
The aim of this package is to provide infrastructure for sports analysis.
Anyway, currently it is a selection of data sets, functions to fetch
sports data, examples, and demos -- with the ambition to develop bit by
bit a set of classes to represent general concepts of sports analysis.

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
%doc %{rlibdir}/SportsAnalytics/html
%doc %{rlibdir}/SportsAnalytics/NEWS
%doc %{rlibdir}/SportsAnalytics/DESCRIPTION
%{rlibdir}/SportsAnalytics/NAMESPACE
%{rlibdir}/SportsAnalytics/help
%{rlibdir}/SportsAnalytics/data
%{rlibdir}/SportsAnalytics/Meta
%{rlibdir}/SportsAnalytics/INDEX
%{rlibdir}/SportsAnalytics/demo
%{rlibdir}/SportsAnalytics/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora